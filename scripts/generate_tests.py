#!/usr/bin/env python3
"""Scan esphome/packages/component and esphome/packages/device and generate
test stubs under tests/component/ and tests/device/.

Naming: for a package at  esphome/packages/component/sensor/i2c/scd4x.yaml
        the test dir is    tests/component/sensor-i2c-scd4x/config.yaml

Includes use short paths (e.g. packages/base/api.yaml) because the justfile
mounts esphome/packages and esphome/clusters into /config.
Existing test files are never overwritten.
"""

from pathlib import Path


PACKAGE_DIRS = ["component", "device"]


def test_dir_name_from_package(rel_path: Path) -> str:
    """Convert a relative package path like sensor/i2c/scd4x.yaml to sensor-i2c-scd4x."""
    parts = list(rel_path.parts)
    stem = Path(parts[-1]).stem
    folders = parts[:-1]
    return "-".join(folders + [stem]) if folders else stem


def generate_stub(package_name: str, pkg_dir_name: str, rel_posix: str) -> str:
    """Generate a minimal test YAML stub."""
    lines = [
        f"# Test stub for {package_name}",
        "substitutions:",
        "  <<: !include clusters/test_api_static.yaml",
        "packages:",
        "  base: !include packages/base/api.yaml",
        "  wifi: !include packages/network/wifi/static.yaml",
        "  device: !include packages/device/generic/esp32.yaml",
        f"  test: !include packages/{pkg_dir_name}/{rel_posix}",
        "",
    ]
    return "\n".join(lines)


def main():
    root = Path(__file__).resolve().parent.parent
    esphome_packages = root / "esphome" / "packages"
    tests_dir = root / "tests"

    created = 0
    skipped = 0

    for pkg_dir_name in PACKAGE_DIRS:
        pkg_dir = esphome_packages / pkg_dir_name
        if not pkg_dir.exists():
            print(f"Skipping {pkg_dir} (not found)")
            continue

        out_dir = tests_dir / pkg_dir_name

        for yaml_file in sorted(pkg_dir.rglob("*.yaml")):
            rel = yaml_file.relative_to(pkg_dir)
            dir_name = test_dir_name_from_package(rel)
            test_dir = out_dir / dir_name
            test_file = test_dir / "config.yaml"

            if test_file.exists():
                skipped += 1
                continue

            test_dir.mkdir(parents=True, exist_ok=True)
            stub = generate_stub(
                f"{pkg_dir_name}/{rel.as_posix()}",
                pkg_dir_name,
                rel.as_posix(),
            )
            test_file.write_text(stub, encoding="utf-8")
            created += 1
            print(f"  Created {test_file.relative_to(root)}")

    print(f"Done: {created} created, {skipped} skipped (already exist)")


if __name__ == "__main__":
    main()
