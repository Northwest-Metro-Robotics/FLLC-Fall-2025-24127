from pybricks.parameters import Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import StopWatch, wait

from src.constants import MOTOR_ONE, MOTOR_TWO


def home_motor(
    motor,
    speed=-200,            # Direction & speed toward the expected hard stop
    duty_limit=30,         # Keep torque gentle to protect gears
    stall_window_ms=300,   # How long with near-zero movement = stall
    sweep_limit_deg=1080,  # Max travel while searching for a stop (3 turns)
    park_angle=0           # Angle to hold after homing
):
    """
    Homes a motor with a hard-stop if present; otherwise performs a soft home.
    After homing, moves to park_angle and holds.
    """

    watch = StopWatch()
    motor.reset_angle(motor.angle())  # normalize relative movement tracking
    start_angle = motor.angle() or 0

    # Start moving toward the expected hard stop
    motor.run(speed)

    # Stall detection via "no meaningful movement" over a time window
    last_move_time = watch.time() or 0
    prev_angle = start_angle or 0

    while True:
        wait(10)  # 10 ms tick

        ang = motor.angle() or 0
        # If angle barely changed, consider that "not moving"
        if abs(ang - prev_angle) < 1:  # ~1° tolerance
            if (watch.time() or 0) - last_move_time >= stall_window_ms:
                # HARD-STOP FOUND: stall detected
                motor.stop()                 # freewheel stop
                motor.hold()                 # stabilize
                motor.reset_angle(0)         # define this as zero
                break
        else:
            # Movement observed -> refresh timers/angle
            last_move_time = watch.time()
            prev_angle = ang

        # Safety: don't sweep forever if there is no hard stop
        if abs(ang - start_angle) >= sweep_limit_deg:
            # NO HARD-STOP: soft home at current spot
            motor.stop()
            motor.hold()
            motor.reset_angle(0)
            break

    # Move to the parked/home angle and hold
    motor.run_target(abs(speed), park_angle, then=Stop.HOLD)

def home_all():
    # Example: C homes backward to a stop; D homes forward (flip speed sign)
    home_motor(MOTOR_ONE, speed=-200, duty_limit=30, stall_window_ms=300, sweep_limit_deg=1080, park_angle=0)
    home_motor(MOTOR_TWO, speed=+200, duty_limit=30, stall_window_ms=300, sweep_limit_deg=1080, park_angle=0)


def log(msg: str):
    try:
        print(msg)
    except Exception:
        pass
