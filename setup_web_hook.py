# -*- coding: utf-8 -*-
"""OPT-IN: installs a git pre-commit hook that rebuilds THE WEB on every
commit, so web.json/web.html always match the corpus. Run once:
    python setup_web_hook.py
Remove anytime by deleting .git/hooks/pre-commit.
"""
import os, stat

HOOK = """#!/bin/sh
# THE WEB self-maintenance (installed by setup_web_hook.py)
python _build_web.py >/dev/null 2>&1 || exit 0
git add web/web.json web/web.html 2>/dev/null
exit 0
"""

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".git", "hooks", "pre-commit")
if os.path.exists(path):
    print("pre-commit hook already exists - not overwriting. Inspect it at:", path)
else:
    with open(path, "w", newline="\n") as f:
        f.write(HOOK)
    os.chmod(path, os.stat(path).st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    print("installed:", path)
    print("THE WEB will now rebuild itself on every commit.")
