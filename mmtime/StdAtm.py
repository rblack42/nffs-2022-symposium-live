from fluids import ATMOSPHERE_1976 as StdAtm

class Air(object):

    def __init__(self, ureg):
        self.ureg = ureg

    def get_properties(self,altitude):
        sa = StdAtm(altitude)
        u = self.ureg
        result = {
            'T': sa.T * u.kelvin,
            'P': sa.P * u.pascals,
            'rho': sa.rho * u.kg / u.m ** 3,
            'mu': sa.mu * u.pascals * u.second
        }
        return result

if __name__ == '__main__':
    import pint
    u = pint.UnitRegistry()
    s = Air(u)
    p = s.get_properties(864)
    print(p)
