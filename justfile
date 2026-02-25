#!/usr/bin/env just --justfile

esphome_image := "ghcr.io/esphome/esphome"

[doc('Show available just recipes.')]
default:
    @just --list

[doc('Generate test stubs for all packages.')]
[group('tests')]
generate-tests:
    @python3 scripts/generate_tests.py

[doc('Generate library docs from vendir.yml.')]
[group('docs')]
generate-library-docs:
    @python3 scripts/generate_library_docs.py

[doc('Generate component and device package docs.')]
[group('docs')]
generate-package-docs:
    @python3 scripts/generate_package_docs.py

[doc('Compile a single ESPHome test config by test dir path (e.g. tests/component/sensor-i2c-scd4x).')]
[group('tests')]
test-config DIR:
    docker run --rm \
        -v "$(pwd)/{{DIR}}":/config \
        -v "$(pwd)/esphome/packages":/config/packages \
        -v "$(pwd)/esphome/components":/config/components \
        -v "$(pwd)/esphome/fonts":/config/fonts \
        -v "$(pwd)/esphome/images":/config/images \
        -v "$(pwd)/esphome/includes":/config/includes \
        -v "$(pwd)/esphome/clusters":/config/clusters \
        {{esphome_image}} compile /config/config.yaml

[doc('Compile all ESPHome test configs.')]
[group('tests')]
test-all-configs:
    #!/usr/bin/env bash
    set -euo pipefail
    for dir in $(find tests -name 'config.yaml' -exec dirname {} \; | sort); do
        echo "=== Testing $dir ==="
        just test-config "$dir"
    done
