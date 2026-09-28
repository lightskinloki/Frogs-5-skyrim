"""Live Parakeet table ear for the existing transcript bridge.

This uses the installed table-ear Parakeet TDT v3 ONNX model for each detected
utterance, then posts the same payload consumed by the existing bridge server.
It intentionally does not load Whisper or NVIDIA NeMo. Speaker attribution is
kept as a configurable label for now; the after-session Parakeet + Nemotron
diarized path remains the accurate speaker-labeling path.
"""

from __future__ import annotations

import argparse
import json
import queue
import time
import urllib.request

import numpy as np
import sherpa_onnx
import sounddevice as sd


BRIDGE_URL = "http://127.0.0.1:3111/api/transcript"
SAMPLE_RATE = 16000
CHANNELS = 1
MODELS = r"C:\Users\fbrown\Projects\table-ear\models"
PARAKEET = f"{MODELS}/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8"


def post_transcript(text: str, speaker: str):
    payload = json.dumps({
        "text": text.strip(),
        "speaker": speaker,
        "sender": speaker,
        "source": "parakeet-live",
        "timestamp": time.strftime("%H:%M:%S"),
    }).encode("utf-8")
    request = urllib.request.Request(
        BRIDGE_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=3):
        pass


def make_recognizer(threads: int):
    return sherpa_onnx.OfflineRecognizer.from_transducer(
        encoder=f"{PARAKEET}/encoder.int8.onnx",
        decoder=f"{PARAKEET}/decoder.int8.onnx",
        joiner=f"{PARAKEET}/joiner.int8.onnx",
        tokens=f"{PARAKEET}/tokens.txt",
        num_threads=threads,
        model_type="nemo_transducer",
    )


def transcribe(recognizer, audio: np.ndarray) -> str:
    stream = recognizer.create_stream()
    stream.accept_waveform(SAMPLE_RATE, audio.astype(np.float32))
    recognizer.decode_stream(stream)
    return stream.result.text.strip()


def run(device, threshold: float, speaker: str, threads: int):
    recognizer = make_recognizer(threads)
    audio_queue: queue.Queue[np.ndarray] = queue.Queue()
    block_duration = 0.05
    block_samples = int(SAMPLE_RATE * block_duration)
    silence_blocks = int(0.8 / block_duration)
    minimum_blocks = int(0.3 / block_duration)
    buffer: list[np.ndarray] = []
    speaking = False
    quiet = 0

    def callback(indata, frames, time_info, status):
        if status:
            print(f"[audio] {status}")
        audio_queue.put(indata[:, 0].copy())

    print("=" * 68)
    print("FROGS 5 LIVE EAR — PARAKEET TDT v3")
    print(f"Model: {PARAKEET}")
    print(f"Posting to: {BRIDGE_URL}")
    print(f"Speaker label: {speaker} (after-session Nemotron diarization remains available)")
    print("=" * 68)

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        blocksize=block_samples,
        device=device,
        callback=callback,
    ):
        while True:
            chunk = audio_queue.get()
            rms = float(np.sqrt(np.mean(chunk ** 2)))
            if rms >= threshold:
                if not speaking:
                    speaking = True
                    buffer = []
                buffer.append(chunk)
                quiet = 0
                print("\r🎙️ listening...", end="", flush=True)
            elif speaking:
                buffer.append(chunk)
                quiet += 1
                if quiet >= silence_blocks:
                    speaking = False
                    quiet = 0
                    if len(buffer) >= minimum_blocks:
                        audio = np.concatenate(buffer)
                        print("\r⚡ Parakeet transcribing...", end="", flush=True)
                        text = transcribe(recognizer, audio)
                        if text:
                            print(f"\r>> [{time.strftime('%H:%M:%S')}] {speaker}: {text}")
                            try:
                                post_transcript(text, speaker)
                            except Exception as exc:
                                print(f"[bridge] {exc}")
                        else:
                            print("\r[Parakeet] no text" + " " * 30)
                    buffer = []
            else:
                print("\ridle...", end="", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", type=int, default=None)
    parser.add_argument("--threshold", type=float, default=0.015)
    parser.add_argument("--speaker", default="Table")
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--list-devices", action="store_true")
    args = parser.parse_args()
    if args.list_devices:
        print(sd.query_devices())
        return
    try:
        run(args.device, args.threshold, args.speaker, args.threads)
    except KeyboardInterrupt:
        print("\n[Stopped]")


if __name__ == "__main__":
    main()
