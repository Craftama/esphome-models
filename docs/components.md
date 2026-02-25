# ESPHome Component Packages

Auto-generated documentation for `esphome/packages/component/`.

## General

### [1wire](https://esphome.io/components/one_wire)

File: `esphome/packages/component/1wire.yaml`

| Variable | Default |
|----------|---------|
| `one_wire_id` | `one_wire_0` |
| `one_wire_pin` | `GPIO04` |

### [deep-sleep](https://esphome.io/components/deep_sleep.html)

File: `esphome/packages/component/deep-sleep.yaml`

| Variable | Default |
|----------|---------|
| `id` | `deep_sleep_0` |
| `run_duration` | `` |
| `sleep_duration` | `30min` |

### [i2c](https://esphome.io/components/i2c.html)

File: `esphome/packages/component/i2c.yaml`

| Variable | Default |
|----------|---------|
| `id` | `i2c_0` |
| `sda_pin` | `GPIO21` |
| `scl_pin` | `GPIO22` |
| `frequency` | `50kHz` |

### [logger](https://esphome.io/components/logger.html)

File: `esphome/packages/component/logger.yaml`

| Variable | Default |
|----------|---------|
| `log_level` | `INFO` |

### pca9685

File: `esphome/packages/component/pca9685.yaml`

| Variable | Default |
|----------|---------|
| `id` | `pca9685_0` |
| `address` | `GPIO22` |
| `frequency` | `500` |

### ping-esp32

File: `esphome/packages/component/ping-esp32.yaml`

### ping-esp8266

File: `esphome/packages/component/ping-esp8266.yaml`

### [spi](https://esphome.io/components/spi.html)

File: `esphome/packages/component/spi.yaml`

| Variable | Default |
|----------|---------|
| `id` | `spi_1` |
| `clk_pin` | `GPIO18` |
| `mosi_pin` | `GPIO23` |
| `miso_pin` | `GPIO19` |
| `interface` | `hardware` |

## Binary Sensor

### binary-sensor/gpio

File: `esphome/packages/component/binary-sensor/gpio.yaml`

| Variable | Default |
|----------|---------|
| `sensor_id` | `button` |
| `sensor_name` | `${name_prefix} button` |
| `sensor_pin` | `GPIO0` |

### [binary-sensor/status](https://esphome.io/components/binary_sensor/status.html)

File: `esphome/packages/component/binary-sensor/status.yaml`

## Button

### [button/restart](https://esphome.io/components/button/restart.html)

File: `esphome/packages/component/button/restart.yaml`

## Camera

### [camera/amg8833](https://github.com/TheRealWaldo/AMG8833-ESPHOME)

File: `esphome/packages/component/camera/amg8833.yaml`

## Fan

### [fan/gpio](https://esphome.io/components/fan/binary.html)

File: `esphome/packages/component/fan/gpio.yaml`

| Variable | Default |
|----------|---------|
| `fan_id` | `fan_id` |
| `fan_name` | `${name_prefix} fan` |
| `fan_pin` | `GPIO12` |
| `fan_icon` | `mdi:fan` |
| `fan_inverted` | `false` |

## Light

### light/esp8266-pwm

File: `esphome/packages/component/light/esp8266-pwm.yaml`

| Variable | Default |
|----------|---------|
| `light_id` | `light_id` |
| `light_name` | `${name_prefix} light` |
| `light_pin` | `GPIO4` |
| `light_inverted` | `true` |
| `light_category` | `` |

### [light/gpio](https://esphome.io/components/light/binary)

File: `esphome/packages/component/light/gpio.yaml`

| Variable | Default |
|----------|---------|
| `light_id` | `light_id` |
| `light_name` | `${name_prefix} light` |
| `light_pin` | `GPIO12` |
| `light_icon` | `mdi:lightbulb` |
| `light_inverted` | `false` |

### [light/ledc](https://esphome.io/components/output/ledc.html)

File: `esphome/packages/component/light/ledc.yaml`

| Variable | Default |
|----------|---------|
| `light_id` | `light_id` |
| `light_name` | `${name_prefix} light` |
| `light_pin` | `GPIO4` |
| `light_channel` | `2` |

### [light/status_led](https://esphome.io/components/light/status_led)

File: `esphome/packages/component/light/status_led.yaml`

| Variable | Default |
|----------|---------|
| `light_pin` | `GPIO12` |
| `light_inverted` | `true` |

## Motor

### motor/l293d

File: `esphome/packages/component/motor/l293d.yaml`

| Variable | Default |
|----------|---------|
| `motor_id` | `motor` |
| `motor_name` | `${name_prefix} motor` |
| `power_pin` | `GPIO4` |
| `cw_pin` | `GPIO5` |
| `acw_pin` | `GPIO6` |

## Rtttl

### [rtttl/esp8266-pwm](https://esphome.io/components/rtttl.html)

File: `esphome/packages/component/rtttl/esp8266-pwm.yaml`

| Variable | Default |
|----------|---------|
| `rtttl_pin` | `GPIO16` |
| `rtttl_id` | `buzzer` |
| `rtttl_name` | `${name_prefix} buzzer` |

### [rtttl/ledc](https://esphome.io/components/rtttl.html)

File: `esphome/packages/component/rtttl/ledc.yaml`

| Variable | Default |
|----------|---------|
| `rtttl_pin` | `GPIO16` |
| `rtttl_id` | `buzzer` |
| `rtttl_name` | `${name_prefix} buzzer` |

## Sensor

### [sensor/1wire/dallas_temp](https://esphome.io/components/sensor/dallas_temp.html)

File: `esphome/packages/component/sensor/1wire/dallas_temp.yaml`

| Variable | Default |
|----------|---------|
| `temperature_id` | `temperature` |
| `temperature_name` | `${name_prefix} temperature` |
| `update_interval` | `10s` |

### [sensor/1wire/dallas_temp_single](https://esphome.io/components/sensor/dallas_temp.html)

File: `esphome/packages/component/sensor/1wire/dallas_temp_single.yaml`

| Variable | Default |
|----------|---------|
| `temperature_id` | `temperature` |
| `temperature_name` | `${name_prefix} temperature` |
| `update_interval` | `10s` |

### [sensor/absolute-humidity](https://esphome.io/components/sensor/absolute_humidity.html)

File: `esphome/packages/component/sensor/absolute-humidity.yaml`

| Variable | Default |
|----------|---------|
| `absolute_humidity_id` | `abs_humidity` |
| `absolute_humidity_name` | `${name_prefix} Absolute humidity` |
| `temperature_id` | `temperature` |
| `humidity_id` | `humidity` |

### sensor/adc/battery.esp32

File: `esphome/packages/component/sensor/adc/battery.esp32.yaml`

| Variable | Default |
|----------|---------|
| `pin` | `GPIO36` |
| `update_interval` | `10s` |
| `battery_level_id` | `battery_level` |
| `battery_level_name` | `${device_name} battery level` |

### sensor/adc/battery

File: `esphome/packages/component/sensor/adc/battery.yaml`

| Variable | Default |
|----------|---------|
| `pin` | `A0` |
| `battery_level_id` | `battery_level` |
| `battery_level_name` | `${device_name} battery level` |
| `update_interval` | `10s` |

### sensor/adc/illuminance.esp32

File: `esphome/packages/component/sensor/adc/illuminance.esp32.yaml`

| Variable | Default |
|----------|---------|
| `illuminance_id` | `illuminance_id` |
| `illuminance_name` | `${name_prefix} illuminance` |
| `illuminance_pin` | `GPIO12` |

### sensor/ble/miflora

File: `esphome/packages/component/sensor/ble/miflora.yaml`

| Variable | Default |
|----------|---------|
| `device_mac` | `aa:bb:cc:dd:ee:ff` |
| `device_name` | `MiFlora` |
| `temperature_name` | `${device_name} temperature` |
| `moisture_name` | `${device_name} moisture` |
| `illuminance_name` | `${device_name} illuminance` |
| `conductivity_name` | `${device_name} conductivity` |
| `battery_level_name` | `${device_name} battery level` |

### [sensor/ble/rssi](https://esphome.io/components/sensor/ble_rssi.html)

File: `esphome/packages/component/sensor/ble/rssi.yaml`

### sensor/ble/vegtrug

File: `esphome/packages/component/sensor/ble/vegtrug.yaml`

| Variable | Default |
|----------|---------|
| `device_mac` | `aa:bb:cc:dd:ee:ff` |
| `device_name` | `VegTrug` |
| `temperature_name` | `${device_name} temperature` |
| `moisture_name` | `${device_name} moisture` |
| `illuminance_name` | `${device_name} illuminance` |
| `conductivity_name` | `${device_name} conductivity` |

### [sensor/dew-point](https://esphome.io/cookbook/bme280_environment.html)

File: `esphome/packages/component/sensor/dew-point.yaml`

| Variable | Default |
|----------|---------|
| `dew_point_id` | `dew_point` |
| `dew_point_name` | `${name_prefix} Dew point` |
| `temperature_id` | `temperature` |
| `humidity_id` | `humidity` |

### [sensor/i2c/bh1750](https://esphome.io/components/sensor/bh1750)

File: `esphome/packages/component/sensor/i2c/bh1750.yaml`

| Variable | Default |
|----------|---------|
| `illuminance_id` | `illuminance` |
| `illuminance_name` | `${name_prefix} illuminance` |
| `update_interval` | `10s` |

### [sensor/i2c/scd4x](https://esphome.io/components/sensor/scd4x.html)

File: `esphome/packages/component/sensor/i2c/scd4x.yaml`

| Variable | Default |
|----------|---------|
| `co2_id` | `co2` |
| `co2_name` | `${name_prefix} CO2` |
| `temperature_id` | `temperature` |
| `temperature_name` | `${name_prefix} temperature` |
| `humidity_id` | `humidity` |
| `humidity_name` | `${name_prefix} humidity` |
| `update_interval` | `10s` |

### sensor/i2c/sht3x

File: `esphome/packages/component/sensor/i2c/sht3x.yaml`

| Variable | Default |
|----------|---------|
| `temperature_id` | `temperature` |
| `temperature_name` | `${name_prefix} temperature` |
| `humidity_id` | `humidity` |
| `humidity_name` | `${name_prefix} humidity` |
| `update_interval` | `10s` |

### [sensor/i2c/stemma-soil-sensor](https://randombytes.substack.com/p/using-the-adafruit-stemma-soil-sensor)

File: `esphome/packages/component/sensor/i2c/stemma-soil-sensor.yaml`

| Variable | Default |
|----------|---------|
| `device_name` | `Stemma Soil Sensor` |
| `temperature_name` | `${name_prefix} temperature` |
| `moisture_name` | `${name_prefix} moisture` |

### [sensor/i2c/tsl2561](https://esphome.io/components/sensor/tsl2561)

File: `esphome/packages/component/sensor/i2c/tsl2561.yaml`

| Variable | Default |
|----------|---------|
| `illuminance_id` | `illuminance` |
| `illuminance_name` | `${name_prefix} illuminance` |
| `illuminance_address` | `0x39` |
| `update_interval` | `10s` |

### [sensor/ping](https://github.com/trombik/esphome-component-ping)

File: `esphome/packages/component/sensor/ping.yaml`

| Variable | Default |
|----------|---------|
| `ping_name` | `ping probe` |
| `ip_address` | `1.1.1.1` |
| `num_attempts` | `10` |
| `timeout` | `1sec` |
| `update_interval` | `10s` |

### [sensor/spi/max31855](https://esphome.io/components/sensor/max31855.html)

File: `esphome/packages/component/sensor/spi/max31855.yaml`

| Variable | Default |
|----------|---------|
| `temperature_id` | `temperature` |
| `temperature_name` | `${name_prefix} temperature` |
| `cs_pin` | `` |
| `update_interval` | `10s` |

### [sensor/spi/max31865](https://esphome.io/components/sensor/max31865.html)

File: `esphome/packages/component/sensor/spi/max31865.yaml`

| Variable | Default |
|----------|---------|
| `update_interval` | `10s` |
| `temperature_id` | `temperature` |
| `temperature_name` | `${name_prefix} temperature` |
| `cs_pin` | `` |
| `reference_resistance` | `430 Ω` |
| `rtd_nominal_resistance` | `100 Ω` |

### [sensor/spi/max6675](https://esphome.io/components/sensor/max6675)

File: `esphome/packages/component/sensor/spi/max6675.yaml`

| Variable | Default |
|----------|---------|
| `temperature_id` | `temperature` |
| `temperature_name` | `${name_prefix} temperature` |
| `cs_pin` | `` |
| `update_interval` | `10s` |

### [sensor/uart/pm1006](https://esphome.io/components/sensor/pm1006.html)

File: `esphome/packages/component/sensor/uart/pm1006.yaml`

| Variable | Default |
|----------|---------|
| `pm_2_5_id` | `pm_2_5` |
| `pm_2_5_name` | `${name_prefix} PM2.5` |
| `update_interval` | `10s` |

### [sensor/uptime](https://esphome.io/components/sensor/uptime.html)

File: `esphome/packages/component/sensor/uptime.yaml`

| Variable | Default |
|----------|---------|
| `update_interval` | `10s` |
| `sensor_name` | `${device_name} Uptime` |

### [sensor/wifi-signal](https://esphome.io/components/sensor/wifi_signal.html)

File: `esphome/packages/component/sensor/wifi-signal.yaml`

| Variable | Default |
|----------|---------|
| `update_interval` | `10s` |
| `sensor_name` | `${device_name} RSSI` |

## Servo

### [servo/esp8266-pwm](https://esphome.io/components/servo.html)

File: `esphome/packages/component/servo/esp8266-pwm.yaml`

| Variable | Default |
|----------|---------|
| `servo_pin` | `GPIO4` |
| `servo_id` | `servo_id` |
| `servo_name` | `servo` |
| `servo_category` | `` |

### [servo/ledc](https://esphome.io/components/servo.html)

File: `esphome/packages/component/servo/ledc.yaml`

| Variable | Default |
|----------|---------|
| `servo_pin` | `GPIO4` |
| `servo_id` | `servo_id` |
| `servo_name` | `servo` |
| `servo_category` | `` |

### [servo/pca9685](https://esphome.io/components/servo.html)

File: `esphome/packages/component/servo/pca9685.yaml`

| Variable | Default |
|----------|---------|
| `servo_channel` | `0` |
| `servo_id` | `servo_id` |
| `servo_name` | `servo` |
| `servo_category` | `` |

## Stepper

### [stepper/uln2003](https://esphome.io/components/stepper/index.html#uln2003-component)

File: `esphome/packages/component/stepper/uln2003.yaml`

| Variable | Default |
|----------|---------|
| `stepper_id` | `uln2003_stepper` |
| `max_speed` | `250 steps/s` |
| `pin_a` | `D1` |
| `pin_b` | `D2` |
| `pin_c` | `D5` |
| `pin_d` | `D6` |

## Switch

### [switch/gpio](https://esphome.io/components/switch/gpio)

File: `esphome/packages/component/switch/gpio.yaml`

| Variable | Default |
|----------|---------|
| `switch_id` | `switch_1` |
| `switch_name` | `${name_prefix} switch` |
| `switch_pin` | `GPIO12` |
| `switch_icon` | `mdi:toggle-switch` |
| `switch_device_class` | `switch` |
| `switch_inverted` | `false` |

## Text Sensor

### [text-sensor/ethernet-info](https://esphome.io/components/text_sensor/ethernet_info)

File: `esphome/packages/component/text-sensor/ethernet-info.yaml`

### [text-sensor/version](https://esphome.io/components/text_sensor/version.html)

File: `esphome/packages/component/text-sensor/version.yaml`

### [text-sensor/wifi-info](https://esphome.io/components/text_sensor/wifi_info)

File: `esphome/packages/component/text-sensor/wifi-info.yaml`

## Time

### [time/ds1307](https://esphome.io/components/time/ds1307)

File: `esphome/packages/component/time/ds1307.yaml`

| Variable | Default |
|----------|---------|
| `time_id` | `time_0` |

### [time/gps](https://esphome.io/components/time/gps)

File: `esphome/packages/component/time/gps.yaml`

| Variable | Default |
|----------|---------|
| `time_id` | `time_0` |

### [time/homeassistant](https://esphome.io/components/time/homeassistant)

File: `esphome/packages/component/time/homeassistant.yaml`

| Variable | Default |
|----------|---------|
| `time_id` | `time_0` |

### [time/pcf8563](https://esphome.io/components/time/pcf8563)

File: `esphome/packages/component/time/pcf8563.yaml`

| Variable | Default |
|----------|---------|
| `time_id` | `time_0` |

### [time/sntp](https://esphome.io/components/time/sntp)

File: `esphome/packages/component/time/sntp.yaml`

| Variable | Default |
|----------|---------|
| `time_id` | `time_0` |
| `timezone` | `Europe/Prague` |
| `server` | `0.pool.ntp.org` |

## Web

### [web/mjpeg-server](https://esphome.io/components/esp32_camera_web_server.html)

File: `esphome/packages/component/web/mjpeg-server.yaml`
