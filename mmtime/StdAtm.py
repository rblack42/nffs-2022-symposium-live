import pint
u = pint.UnitRegistry()

from fluids import ATMOSPHERE_1976 as StdAtm

def get_air_properties(altitude):
    h = altitude.to_base_units()
    sa = StdAtm(h.magnitude) # strip off units for call
    result = {
        'T': sa.T * u.kelvin,
        'P': sa.P * u.pascals,
        'rho': sa.rho * u.kg / u.m ** 3,
        'mu': sa.mu * u.pascals * u.second
    }
    return result
