import math
import pint
u = pint.UnitRegistry()

winds = 3660
Wr = 0.86 * u.grams
Q0 = 0.31 * u.inch * u.ounce
Qh = Q0 / 6
He = 900 * u.meters
flight_time = 818 * u.seconds
n_h = winds/flight_time
Time = He * Wr / (2.8 * math.pi * Qh *n_h)

