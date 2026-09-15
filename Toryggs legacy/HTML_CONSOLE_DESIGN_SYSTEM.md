# FROGS 5 HTML CONSOLE DESIGN SYSTEM & TEMPLATES
*Authoritative Design Specification for Interactive GM Run-Sheets and Player Character Consoles*

---

## I. PURPOSE & PHILOSOPHY

The HTML Console format provides a zero-dependency, standalone, offline-ready interface optimized for live tabletop GMing and player reference.

### Core Tenets:
1. **Self-Contained & Instant:** Single `.html` file with all CSS, layout, and vanilla JavaScript inline. No external CDNs, no npm dependencies, works out of the box in any browser (desktop, tablet, mobile).
2. **Glanceable Visual Hierarchy:** The GM never hunts for what to say or adjudicate. Read-aloud is high-contrast blue, GM-only guidance is maroon/amber, mechanics are monospace, and danger is crimson.
3. **Integrated Table Tools:** Built-in interactive d20 roll-under widgets, boss phase health trackers, and clickable doom clock pips eliminate mental overhead during intense rounds.
4. **Strict FROGS 5 Mechanics:** Always uses roll-under stat Target Numbers, Difficulty Modifiers (+/- to player TN), 0-cost off-turn Bonus Actions, and Formula of Pain damage stacking.

---

## II. THE VISUAL & COLOR PALETTE

```css
:root {
  /* DARK SLATE & OBSIDIAN FOUNDATION */
  --bg-dark: #0d1117;
  --bg-card: #161b22;
  --bg-surface: #1f242c;
  --bg-highlight: #222d3d;
  --border: #30363d;
  --border-accent: #8b263e;
  
  /* TYPOGRAPHY COLORS */
  --text-main: #e6edf3;
  --text-muted: #8b949e;
  --text-secondary: #94a3b8;
  
  /* READ-ALOUD BLUE (Spoken Cold at Table) */
  --blue-read: #58a6ff;
  --blue-bg: #0d1e36;
  --blue-border: #1f4273;
  
  /* GM MAROON & COMBAT RED */
  --maroon: #e55368;
  --maroon-dark: #7a1d2e;
  --red-danger: #f85149;
  --red-bg: #2d1217;
  --dagon-red: #f43f5e;
  
  /* GOLD & ANCIENT AMBER */
  --gold: #d29922;
  --gold-bright: #f0883e;
  
  /* VIRULENT / VITAL GREEN */
  --green-accent: #3fb950;
  --toxic-green: #4ade80;
  
  /* DAEDRIC / SPECIAL THEMES */
  --namira-purple: #a855f7;
  --peryite-cyan: #38bdf8;
  
  /* FONTS */
  --font-serif: "Iowan Old Style", "Sitka Text", Palatino, "Palatino Linotype", Georgia, serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "Cascadia Code", Consolas, monospace;
}
```

---

## III. CORE COMPONENT TAXONOMY

### 1. Read-Aloud Block (`.read-aloud`)
- **Purpose:** Spoken cold aloud to the table.
- **Style:** Deep navy background (`--blue-bg`), blue border (`--blue-border`), serif font, italicized body text.
- **Rule:** Max detail, zero filler, chronological syntax, no narrating PC emotions or conclusions.

### 2. GM Note Block (`.gm-note`)
- **Purpose:** Adjudication rules, background truth, and gating instructions.
- **Style:** Bordered card with a bold maroon/amber `[GM:]` tag. Explains *what this establishes* without polluting read-aloud prose.

### 3. Spoken NPC Dialogue (`.spoken-block`)
- **Purpose:** In-character NPC lines designed for live spoken delivery.
- **Style:** Speaker tag in bold gold/maroon, dialogue in quotes with clear stage directions. Follows Writing Guide Section IX rules.

### 4. Interactive Dice Roller (`.roller-widget`)
- **Purpose:** One-click rolling against custom character TNs or table difficulty modifiers.
- **Features:** Auto-detects Nat 1 (Lethal Critical $\times 2$ Damage) and Nat 20 (Critical Failure), calculates margin of success/failure.

### 5. Clickable Doom Clock Pips (`.pip-container`)
- **Purpose:** Tracking stages of corruption, rust, notice clocks, or boss phases.
- **Features:** Clickable pips that dynamically update stage names and visual state.

---

## IV. ARCHETYPE A: GM SESSION RUN-SHEET TEMPLATE

Use this boilerplate for full multi-scene adventure modules.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FROGS 5 — [MODULE NAME] (Session Sheet)</title>
<style>
  :root {
    --bg-dark: #0d1117; --bg-card: #161b22; --bg-surface: #1f242c;
    --border: #30363d; --border-accent: #8b263e;
    --text-main: #e6edf3; --text-muted: #8b949e;
    --maroon: #e55368; --gold: #d29922; --blue-read: #58a6ff;
    --blue-bg: #0d1e36; --blue-border: #1f4273; --red-danger: #f85149;
    --font-serif: "Iowan Old Style", Palatino, Georgia, serif;
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --font-mono: ui-monospace, "SF Mono", Consolas, monospace;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg-dark); color: var(--text-main); font-family: var(--font-sans); display: flex; min-height: 100vh; }
  
  /* SIDEBAR */
  #sidebar { width: 280px; background: var(--bg-card); border-right: 1px solid var(--border); position: fixed; top: 0; bottom: 0; left: 0; overflow-y: auto; padding: 1.5rem 1rem; display: flex; flex-direction: column; gap: 1rem; }
  #sidebar h2 { font-family: var(--font-serif); font-size: 1.1rem; color: var(--gold); text-transform: uppercase; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }
  .nav-item { display: block; padding: 0.5rem 0.75rem; border-radius: 6px; color: var(--text-muted); text-decoration: none; font-size: 0.85rem; border-left: 3px solid transparent; }
  .nav-item:hover, .nav-item.active { background: var(--bg-surface); color: var(--gold); border-left-color: var(--gold); }
  
  /* MAIN CONTENT */
  #main-content { margin-left: 280px; flex: 1; padding: 2rem 2.5rem; max-width: 1050px; display: flex; flex-direction: column; gap: 2rem; }
  .scene-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 8px; padding: 1.75rem; }
  .scene-number { color: var(--maroon); font-size: 0.85rem; font-weight: 700; text-transform: uppercase; font-family: var(--font-mono); }
  .scene-title { font-family: var(--font-serif); font-size: 1.6rem; color: #fff; margin-bottom: 0.25rem; }
  .scene-subtitle { font-size: 0.9rem; color: var(--text-muted); font-style: italic; margin-bottom: 1rem; }
  
  /* READ ALOUD & GM NOTES */
  .read-aloud { background: var(--blue-bg); border: 1px solid var(--blue-border); border-left: 4px solid var(--blue-read); border-radius: 6px; padding: 1.25rem; margin: 1rem 0; font-family: var(--font-serif); font-style: italic; color: #dbeafe; line-height: 1.6; }
  .read-aloud-tag { font-family: var(--font-sans); font-size: 0.75rem; font-weight: 700; color: var(--blue-read); text-transform: uppercase; font-style: normal; margin-bottom: 0.5rem; }
  .gm-note { background: var(--bg-surface); border: 1px solid var(--border); border-left: 3px solid var(--maroon); border-radius: 6px; padding: 0.85rem 1.1rem; font-size: 0.88rem; color: #cbd5e1; margin: 0.75rem 0; }
  .gm-tag { color: var(--maroon); font-weight: 700; font-family: var(--font-mono); }
  
  /* WIDGETS */
  .quick-roller { background: var(--bg-surface); border: 1px solid var(--border); border-radius: 6px; padding: 0.75rem 1rem; text-align: center; }
  .roll-btn { background: var(--maroon-dark); color: #fff; border: 1px solid var(--maroon); padding: 0.35rem 0.75rem; border-radius: 4px; cursor: pointer; font-size: 0.8rem; font-weight: 600; }
</style>
</head>
<body>

<nav id="sidebar">
  <h2>Module Navigation</h2>
  <div class="quick-roller">
    <button class="roll-btn" onclick="rollD20()">Roll Quick d20</button>
    <div id="quick-roll-result" style="font-family:var(--font-mono); font-size:0.85rem; margin-top:0.4rem; color:var(--gold);">Ready</div>
  </div>
  <a href="#scene-1" class="nav-item">Scene 1: Opening Beat</a>
  <a href="#scene-2" class="nav-item">Scene 2: Combat Threshold</a>
</nav>

<main id="main-content">
  <section id="scene-1" class="scene-card">
    <div class="scene-number">Scene 01</div>
    <h2 class="scene-title">The High Ridge</h2>
    <p class="scene-subtitle">Stakes, bitter weather, and the first descent</p>
    
    <div class="read-aloud">
      <div class="read-aloud-tag">&gt;&gt; READ ALOUD</div>
      <p>The wind comes off the peak in sheets, carrying the dry rattle of loose shale...</p>
    </div>
    
    <div class="gm-note">
      <span class="gm-tag">GM:</span> Adjudicate cold exposure or perception rolls here.
    </div>
  </section>
</main>

<script>
  function rollD20() {
    const roll = Math.floor(Math.random() * 20) + 1;
    const res = document.getElementById('quick-roll-result');
    res.innerHTML = `Rolled: <strong>${roll}</strong>`;
    if (roll === 1) res.innerHTML += ' <span style="color:#4ade80;">(NAT 1 CRIT!)</span>';
    if (roll === 20) res.innerHTML += ' <span style="color:#f85149;">(NAT 20!)</span>';
  }
</script>
</body>
</html>
```

---

## V. ARCHETYPE B: PLAYER / NPC COMBAT SHEET TEMPLATE

Use this boilerplate for character sheets, special forms, and boss stat cards.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[CHARACTER NAME] — FROGS 5 Combat Sheet</title>
<style>
  :root {
    --bg-main: #0a0d12; --bg-card: #121820; --bg-surface: #1a222d;
    --border: #283344; --text-primary: #e6edf3; --text-secondary: #94a3b8;
    --gold: #fbbf24; --red: #f43f5e; --green: #4ade80; --blue: #38bdf8;
    --font-serif: "Iowan Old Style", Palatino, Georgia, serif;
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    --font-mono: ui-monospace, "SF Mono", Consolas, monospace;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg-main); color: var(--text-primary); font-family: var(--font-sans); padding: 2rem 1rem; display: flex; justify-content: center; }
  .sheet-container { max-width: 900px; width: 100%; display: flex; flex-direction: column; gap: 1.5rem; }
  
  /* HEADER */
  .header-card { background: var(--bg-card); border: 1px solid var(--border); border-top: 4px solid var(--gold); border-radius: 10px; padding: 1.75rem; }
  .char-title { font-family: var(--font-serif); font-size: 2rem; color: #fff; }
  .char-sub { color: var(--text-secondary); font-style: italic; margin-bottom: 0.75rem; font-size: 0.95rem; }
  
  /* STAT GRID */
  .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.75rem; }
  .stat-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; text-align: center; cursor: pointer; transition: transform 0.15s; }
  .stat-card:hover { transform: translateY(-2px); border-color: var(--gold); }
  .stat-label { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-secondary); }
  .stat-val { font-size: 2rem; font-family: var(--font-mono); font-weight: 800; color: #fff; }
  
  /* ACTIONS */
  .action-card { background: var(--bg-card); border: 1px solid var(--border); border-left: 4px solid var(--border); border-radius: 8px; padding: 1.25rem; margin-bottom: 0.75rem; }
  .action-card.major { border-left-color: var(--red); }
  .action-card.bonus { border-left-color: var(--green); }
  .action-card.reaction { border-left-color: var(--blue); }
  .action-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.4rem; }
  .action-title { font-family: var(--font-serif); font-size: 1.1rem; color: #fff; font-weight: 700; }
  .cost-badge { font-family: var(--font-mono); font-size: 0.75rem; background: rgba(244, 63, 94, 0.15); color: var(--red); padding: 0.15rem 0.5rem; border-radius: 4px; }
  .damage-pill { font-family: var(--font-mono); font-weight: 700; color: #fca5a5; background: rgba(239, 68, 68, 0.15); padding: 0.1rem 0.35rem; border-radius: 3px; }
</style>
</head>
<body>

<div class="sheet-container">
  <header class="header-card">
    <h1 class="char-title">[CHARACTER / ENTITY NAME]</h1>
    <div class="char-sub">[Title / Archetype / Allegiance]</div>
  </header>

  <div class="stats-grid">
    <div class="stat-card" onclick="rollStat('Might', 16)">
      <div class="stat-label">Might</div>
      <div class="stat-val">16</div>
    </div>
    <div class="stat-card" onclick="rollStat('Agility', 14)">
      <div class="stat-label">Agility</div>
      <div class="stat-val">14</div>
    </div>
    <div class="stat-card" onclick="rollStat('Magic', 19)">
      <div class="stat-label">Magic</div>
      <div class="stat-val">19</div>
    </div>
    <div class="stat-card" onclick="rollStat('Guile', 12)">
      <div class="stat-label">Guile</div>
      <div class="stat-val">12</div>
    </div>
  </div>

  <section>
    <div class="action-card major">
      <div class="action-header">
        <span class="action-title">Primary Strike</span>
        <span class="cost-badge">0 FP &bull; Major</span>
      </div>
      <p style="font-size:0.9rem; color:#cbd5e1;">Roll Might (TN 16). Deals <span class="damage-pill">14 Physical Damage</span>. On Natural 1 (Crit): <span class="damage-pill">28 Damage</span>.</p>
    </div>
  </section>
</div>

</body>
</html>
```

---

## VI. CHECKLIST BEFORE EXPORTING HTML

1. **Self-Contained:** Zero external style links or scripts.
2. **Formula of Pain Enforced:** All flat bonuses add first; all multipliers multiply together.
3. **No Target Numbers for Players:** Player roll buttons test against their *own* stat; difficulty modifiers adjust the roll target.
4. **Tested in Standard Browsers:** Verify that layout renders cleanly on both wide monitor and mobile viewports.
