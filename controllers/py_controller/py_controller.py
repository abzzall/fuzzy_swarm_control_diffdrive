from controller import Robot, Keyboard

TIME_STEP = 32
SPEED_UNIT = 6.28  # Approx conversion from m/s to motor velocity

robot = Robot()
keyboard = Keyboard()
keyboard.enable(TIME_STEP)

# Motors
left_motor = robot.getDevice('left wheel')
right_motor = robot.getDevice('right wheel')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0)
right_motor.setVelocity(0)

# Distance sensors
sensor_names = [f"so{i}" for i in range(16)]
sensors = [robot.getDevice(name) for name in sensor_names]
sensors_enabled = False

# LEDs (to indicate observer role)
led_names = ["red led 1", "red led 2", "red led 3"]
leds = [robot.getDevice(name) for name in led_names]

# yellow led
yellow_led=robot.getDevice('green led')
# Initial state
base_speed = 0.0
print("Controller started. Use W/A/S/D/X to move, L to enable sensors + LEDs, K to disable both.")

while robot.step(TIME_STEP) != -1:
    key = keyboard.getKey()

    if key == ord('W'):
        base_speed = 1.0
        left_motor.setVelocity(base_speed * SPEED_UNIT)
        right_motor.setVelocity(base_speed * SPEED_UNIT)

    elif key == ord('A'):
        left_motor.setVelocity(1.2 * SPEED_UNIT)
        right_motor.setVelocity(base_speed * SPEED_UNIT)

    elif key == ord('D'):
        left_motor.setVelocity(base_speed * SPEED_UNIT)
        right_motor.setVelocity(1.2 * SPEED_UNIT)

    elif key == ord('X'):
        base_speed = -1.0
        left_motor.setVelocity(base_speed * SPEED_UNIT)
        right_motor.setVelocity(base_speed * SPEED_UNIT)

    elif key == ord('S'):
        base_speed = 0.0
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)

    elif key == ord('L') and not sensors_enabled:
        for sensor in sensors:
            sensor.enable(TIME_STEP)
        for led in leds:
            led.set(1)
        yellow_led.set(1)
        sensors_enabled = True
        print("Distance sensors and LEDs enabled.")

    elif key == ord('K') and sensors_enabled:
        for sensor in sensors:
            sensor.disable()
        for led in leds:
            led.set(0)
        yellow_led.set(0)
        sensors_enabled = False
        print("Distance sensors and LEDs disabled.")
