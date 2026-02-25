# ESPHome Models

Reusable ESPHome packages for components, devices, and network configurations.

## Project Structure

```
esphome/
├── clusters/          # Shared substitution presets (test configs)
├── components/        # External ESPHome components (via vendir)
├── fonts/             # Font files for displays
├── images/            # Image assets
├── includes/          # External includes (via vendir)
└── packages/
    ├── base/          # Base configs (API, MQTT)
    ├── component/     # Reusable component packages
    ├── device/        # Device board definitions
    └── network/       # Network configurations
scripts/               # Code generation scripts
tests/                 # Auto-generated test stubs
docs/                  # Auto-generated documentation
```

## Components

| Category | Package | Description |
|----------|---------|-------------|
| **Binary Sensor** | `binary-sensor/gpio` | GPIO binary sensor |
| | `binary-sensor/status` | Connection status |
| **Button** | `button/restart` | Restart button |
| **Camera** | `camera/amg8833` | AMG8833 thermal camera |
| **Fan** | `fan/gpio` | GPIO fan control |
| **Light** | `light/esp8266-pwm` | ESP8266 PWM light |
| | `light/gpio` | GPIO on/off light |
| | `light/ledc` | LEDC PWM light |
| | `light/status_led` | Status LED |
| **Motor** | `motor/l293d` | L293D motor driver |
| **RTTTL** | `rtttl/esp8266-pwm` | Buzzer (ESP8266 PWM) |
| | `rtttl/ledc` | Buzzer (LEDC) |
| **Sensor** | `sensor/absolute-humidity` | Absolute humidity calc |
| | `sensor/dew-point` | Dew point calc |
| | `sensor/ping` | Network ping |
| | `sensor/uptime` | Uptime sensor |
| | `sensor/wifi-signal` | WiFi signal strength |
| **Sensor / 1-Wire** | `sensor/1wire/dallas_temp` | Dallas temperature |
| | `sensor/1wire/dallas_temp_single` | Dallas single sensor |
| **Sensor / ADC** | `sensor/adc/battery` | ADC battery voltage |
| | `sensor/adc/battery.esp32` | ADC battery (ESP32) |
| | `sensor/adc/illuminance.esp32` | ADC illuminance (ESP32) |
| **Sensor / BLE** | `sensor/ble/miflora` | Xiaomi MiFlora |
| | `sensor/ble/rssi` | BLE RSSI |
| | `sensor/ble/vegtrug` | VegTrug sensor |
| **Sensor / I²C** | `sensor/i2c/bh1750` | BH1750 light sensor |
| | `sensor/i2c/scd4x` | SCD4x CO₂/temp/humidity |
| | `sensor/i2c/sht3x` | SHT3x temp/humidity |
| | `sensor/i2c/stemma-soil-sensor` | Stemma soil moisture |
| | `sensor/i2c/tsl2561` | TSL2561 light sensor |
| **Sensor / SPI** | `sensor/spi/max31855` | MAX31855 thermocouple |
| | `sensor/spi/max31865` | MAX31865 RTD |
| | `sensor/spi/max6675` | MAX6675 thermocouple |
| **Sensor / UART** | `sensor/uart/pm1006` | PM1006 particulate |
| **Servo** | `servo/esp8266-pwm` | Servo (ESP8266 PWM) |
| | `servo/ledc` | Servo (LEDC) |
| | `servo/pca9685` | Servo (PCA9685) |
| **Stepper** | `stepper/uln2003` | ULN2003 stepper |
| **Switch** | `switch/gpio` | GPIO switch |
| **Text Sensor** | `text-sensor/ethernet-info` | Ethernet info |
| | `text-sensor/version` | ESPHome version |
| | `text-sensor/wifi-info` | WiFi info |
| **Bus / General** | `1wire` | 1-Wire bus |
| | `deep-sleep` | Deep sleep mode |
| | `i2c` | I²C bus |
| | `logger` | Logger |
| | `pca9685` | PCA9685 PWM driver |
| | `ping-esp32` | Ping (ESP32) |
| | `ping-esp8266` | Ping (ESP8266) |
| | `spi` | SPI bus |
| | `time/homeassistant` | HA time sync |
| | `time/sntp` | SNTP time sync |
| | `web/web-server` | Web server |

## Devices

| Manufacturer | Board | Package |
|-------------|-------|---------|
| **AI-Thinker** | ESP32-CAM | `ai-thinker/esp32-cam` |
| **Athom** | PS01 Presence Sensor | `athom/ps01` |
| **Generic** | ESP32 | `generic/esp32` |
| | ESP8266 | `generic/esp8266` |
| **LaskaKit** | ESPlan (Ethernet) | `laskakit/esplan` |
| | Vindriktning | `laskakit/vindriktning` |
| | Vindriktning + LEDs | `laskakit/vindriktning-leds` |
| **M5Stack** | AtomS3 | `m5stack/atoms3` |
| **Shelly** | Shelly 1 | `shelly/shelly-1` |
| **Sonoff** | 4CH Pro (base) | `sonoff/4ch-pro-base` |
| | 4CH Pro | `sonoff/4ch-pro` |
| | 4CH Pro R2 (base) | `sonoff/4ch-pro-r2-base` |
| | 4CH Pro R2 | `sonoff/4ch-pro-r2` |
| | Mini (base) | `sonoff/mini-base` |
| | Mini | `sonoff/mini` |
| | NSPanel | `sonoff/nspanel` |
| | NSPanel Advanced | `sonoff/nspanel-advanced` |
| | NSPanel TFT Upload | `sonoff/nspanel-tft-upload` |
| | S20 | `sonoff/s20` |
| **Ulanzi** | TC001 Pixel Clock | `ulanzi/tc001` |
| **Weber** | iGrill v2 | `weber/igrill-v2` |
| **Wemos** | D1 Mini | `wemos/d1-mini` |

## Network Configurations

| Type | Package | Description |
|------|---------|-------------|
| **WiFi** | `network/wifi/static` | Static IP WiFi |
| | `network/wifi/dhcp` | DHCP WiFi |
| | `network/wifi/multi` | Multi-network WiFi |
| | `network/wifi/dns` | DNS settings |
| | `network/wifi/ap` | Access point fallback |
| **Ethernet** | `network/ethernet/static` | Static IP Ethernet |
| | `network/ethernet/dns` | Ethernet DNS |
| **Bluetooth** | `network/bluetooth/proxy` | BLE proxy |
| | `network/bluetooth/tracker` | BLE tracker |

## Base Configurations

| Package | Description |
|---------|-------------|
| `base/api` | Home Assistant API + OTA + web server |
| `base/mqtt` | MQTT + OTA + web server |

## Test Clusters

| Cluster | Description |
|---------|-------------|
| `clusters/test_api_static` | API mode, static WiFi IP |
| `clusters/test_api_dhcp` | API mode, DHCP WiFi |
| `clusters/test_mqtt` | MQTT mode |

## Scripts

| Command | Description |
|---------|-------------|
| `just generate-tests` | Generate test stubs for all packages |
| `just generate-library-docs` | Generate library docs from `vendir.yml` |
| `just generate-package-docs` | Generate component/device docs |
| `just test-config <DIR>` | Compile a single test config via Docker |
| `just test-all-configs` | Compile all test configs |
