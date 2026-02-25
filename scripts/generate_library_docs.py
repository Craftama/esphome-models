#!/usr/bin/env python3
"""Parse vendir.yml and generate docs/libraries.md."""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")


def parse_url(url: str) -> dict:
    """Extract repo URL, version, and source type from a vendir HTTP URL."""
    info = {"url": url, "version": None, "repo": None, "source": "http"}

    # GitHub archive tag: /archive/refs/tags/<version>.zip
    m = re.search(r"github\.com/([^/]+/[^/]+)/archive/refs/tags/v?(.+?)\.zip", url)
    if m:
        info["repo"] = f"https://github.com/{m.group(1)}"
        info["version"] = m.group(2)
        return info

    # GitHub archive branch: /archive/refs/heads/<branch>.zip
    m = re.search(r"github\.com/([^/]+/[^/]+)/archive/refs/heads/(.+?)\.zip", url)
    if m:
        info["repo"] = f"https://github.com/{m.group(1)}"
        info["version"] = f"{m.group(2)} (branch)"
        return info

    # GitHub release asset: /releases/download/<version>/<file>
    m = re.search(r"github\.com/([^/]+/[^/]+)/releases/download/v?([^/]+)/", url)
    if m:
        info["repo"] = f"https://github.com/{m.group(1)}"
        info["version"] = m.group(2)
        return info

    # GitHub gist
    m = re.search(r"gist\.github\.com/([^/]+/[^/]+)/", url)
    if m:
        info["repo"] = f"https://gist.github.com/{m.group(1)}"
        info["version"] = "latest"
        return info

    # Fallback: try to get github repo
    m = re.search(r"github\.com/([^/]+/[^/]+)", url)
    if m:
        info["repo"] = f"https://github.com/{m.group(1)}"

    return info


def generate_docs(vendir_path: str, output_path: str) -> None:
    """Generate libraries.md from vendir.yml."""
    vendir_file = Path(vendir_path)
    if not vendir_file.exists():
        sys.exit(f"File not found: {vendir_file}")

    with open(vendir_file) as f:
        config = yaml.safe_load(f)

    lines = [
        "# External Libraries",
        "",
        f"Auto-generated from [`vendir.yml`](../vendir.yml).",
        "",
    ]

    for directory in config.get("directories", []):
        dir_path = directory.get("path", "unknown")
        contents = directory.get("contents", [])
        if not contents:
            continue

        lines.append(f"## {dir_path}")
        lines.append("")
        lines.append("| Name | Version | Source |")
        lines.append("|------|---------|--------|")

        for item in contents:
            name = item.get("path", "unknown")
            url = item.get("http", {}).get("url", "")
            info = parse_url(url)

            version = info["version"] or "—"
            repo = info["repo"] or url
            link = f"[{name}]({repo})"

            lines.append(f"| {link} | {version} | {repo} |")

        lines.append("")

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {out}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    vendir = sys.argv[1] if len(sys.argv) > 1 else str(root / "vendir.yml")
    output = sys.argv[2] if len(sys.argv) > 2 else str(root / "docs" / "libraries.md")
    generate_docs(vendir, output)
