# Simple script to sanity-check motor/sensor ports on the hub.
from pybricks.parameters import Port
from pybricks.pupdevices import Motor


def try_motor(p):
    try:
        m = Motor(getattr(Port, p) if isinstance(p, str) else p)
        m.run_angle(180, 90)
        m.run_angle(-180, 90)
        return True
    except Exception:
        return False

try_motor("A")
try_motor("B")
try_motor("C")
try_motor("D")
try_motor("E")
try_motor("F")

print("Port tester complete. Adjust ports and run on-hub.")
