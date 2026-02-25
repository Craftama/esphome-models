#!/usr/bin/env python3
"""Scan esphome/packages/component and esphome/packages/device and generate
docs/components.md and docs/devices.md.

Extracts:
- Package path (relative to component/device root)
- Link comment from the first line (if present, e.g. # https://...)
- Substitution variables with their default values
"""

import re
from pathlib import Path


def extract_link_comment(filepath: Path) -> str | None:
    """Extract a URL from a comment on the first line of the YAML file."""
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Match lines like: # https://esphome.io/...  or  # https://github.com/...
            m = re.match(r"^#\s*(https?://\S+)", line)
            if m:
                return m.group(1)
            # Also handle multi-line comment blocks like NSPanel
            if line.startswith("#"):
                url = re.search(r"(https?://\S+)", line)
                if url:
                    return url.group(1)
            break
    return None


def extract_substitutions(filepath: Path) -> dict[str, str]:
    """Extract substitution variables and their defaults from a YAML file."""
    subs = {}
    in_substitutions = False
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            stripped = line.rstrip()
            # Detect the start of the substitutions block
            if stripped == "substitutions:":
                in_substitutions = True
                continue
            if in_substitutions:
                # End of substitutions block (non-indented line or empty)
                if stripped and not stripped.startswith(" ") and not stripped.startswith("#"):
                    break
                # Parse key: value pairs
                m = re.match(r"^\s{2}(\w+):\s*(.*)", stripped)
                if m:
                    key = m.group(1)
                    value = m.group(2).strip().strip("'\"")
                    subs[key] = value
    return subs


def generate_doc(pkg_type: str, pkg_dir: Path) -> list[str]:
    """Generate markdown lines for a package directory (component or device)."""
    lines = [
        f"# ESPHome {pkg_type.title()} Packages",
        "",
        f"Auto-generated documentation for `esphome/packages/{pkg_type}/`.",
        "",
    ]

    # Group files by top-level subdirectory
    groups: dict[str, list[Path]] = {}
    for yaml_file in sorted(pkg_dir.rglob("*.yaml")):
        rel = yaml_file.relative_to(pkg_dir)
        parts = rel.parts
        group = parts[0] if len(parts) > 1 else "_root"
        groups.setdefault(group, []).append(yaml_file)

    # Root-level files first
    if "_root" in groups:
        lines.append("## General")
        lines.append("")
        lines.extend(_format_group(groups.pop("_root"), pkg_dir))

    # Then subdirectories
    for group_name in sorted(groups.keys()):
        lines.append(f"## {group_name.replace('-', ' ').title()}")
        lines.append("")
        lines.extend(_format_group(groups[group_name], pkg_dir))

    return lines


def _format_group(files: list[Path], pkg_dir: Path) -> list[str]:
    """Format a group of files into markdown."""
    lines = []

    for yaml_file in sorted(files):
        rel = yaml_file.relative_to(pkg_dir)
        name = rel.as_posix().replace(".yaml", "")
        link = extract_link_comment(yaml_file)
        subs = extract_substitutions(yaml_file)

        # Header
        if link:
            lines.append(f"### [{name}]({link})")
        else:
            lines.append(f"### {name}")

        lines.append("")
        lines.append(f"File: `esphome/packages/{pkg_dir.name}/{rel.as_posix()}`")
        lines.append("")

        # Substitutions table
        if subs:
            lines.append("| Variable | Default |")
            lines.append("|----------|---------|")
            for key, value in subs.items():
                lines.append(f"| `{key}` | `{value}` |")
            lines.append("")

    return lines


def main():
    root = Path(__file__).resolve().parent.parent
    esphome_packages = root / "esphome" / "packages"
    docs_dir = root / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    for pkg_type in ["component", "device"]:
        pkg_dir = esphome_packages / pkg_type
        if not pkg_dir.exists():
            print(f"Skipping {pkg_dir} (not found)")
            continue

        doc_lines = generate_doc(pkg_type, pkg_dir)
        out_file = docs_dir / f"{pkg_type}s.md"
        out_file.write_text("\n".join(doc_lines), encoding="utf-8")
        print(f"Generated {out_file.relative_to(root)}")


if __name__ == "__main__":
    main()
