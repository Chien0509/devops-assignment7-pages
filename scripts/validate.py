#!/usr/bin/env python3
"""Fail closed if required site source or generated output is missing."""
import argparse
from pathlib import Path
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--site")
args = parser.parse_args()
readme = Path("README.md").read_text(encoding="utf-8")
index = Path("index.md").read_text(encoding="utf-8")
errors = []
start = "<!--START_SECTION:activity-->"
end = "<!--END_SECTION:activity-->"
if readme.count(start) != 1 or readme.count(end) != 1:
    errors.append("Activity markers must occur exactly once")
if readme.find(start) >= readme.find(end):
    errors.append("Activity marker order is invalid")
if "{% include_relative README.md %}" not in index:
    errors.append("Missing Jekyll README include")
if not index.lstrip().startswith("---"):
    errors.append("Missing Jekyll front matter")
for url in re.findall(r"\]\((https?://[^)]+)\)", readme):
    if not url.startswith("https://github.com/"):
        errors.append("Unexpected external URL: " + url)
if args.site:
    html = Path(args.site) / "index.html"
    if not html.is_file():
        errors.append("Built index.html missing")
    else:
        body = html.read_text(encoding="utf-8")
        for phrase in ("Recent activity", "Release safety"):
            if phrase not in body:
                errors.append("Built HTML missing " + phrase)
if errors:
    print("VALIDATION FAILED:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print("VALIDATION PASSED")
