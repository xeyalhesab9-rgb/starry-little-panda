"""Offline, deterministic entry for make.fun's cutest-picture bounty."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
OUTPUT = Path('/output')
OUTPUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(ROOT / 'entry.png', OUTPUT / 'entry.png')
