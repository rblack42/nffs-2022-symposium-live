import pint
import math


class Wart(object):

    def __init__(self, u):
        self.name = 'wart-a6'
        self.weights = {
            'motor_stick': 0.22*u.grams,
            'tail_boom': 0.08*u.grams,
            'stab': 0.25*u.grams,
            'wing': 0.42*u.grams,
            'prop': 0.23*u.grams,
            'rubber': 0.86*u.grams
        }
        self.cg_arms = {
            'prop': (0*u.inch,-0.125*u.inch),
            'wing': (2.25*u.inch, (7/8)*u.inch),
            'stab': ((6+8.5-1)*u.inch,0.125*u.inch),
            'motor_stick': (3*u.inch,0.0625*u.inch),
            'tail_boom': (10.0*u.inch,0.125*u.inch),
            'rubber': (3*u.inch,-0.125*u.inch)
        }
        self.wing = {
            'center_span': 8 * u.inches,
            'center_chord': 2 * u.inches,
            'tip_span':3.75 * u.inches,
            'tip_chord': 1.75 * u.inches,
            'tip_dihedral': 7/8*u.inches,
        }
        self.stab = {
            'tip_span': (5 + 7/16) * u.inches,
            'center_chord': 1.75 * u.inches,
            'tip_chord': 1 * u.inches,
            'tip_dihedral': 7/8 * u.inches
        }
        self.motor = {
            'length': 18.0 * u.inches,
        }

        # calculate CG location
        x_cg = 0
        y_cg = 0
        W_sum = 0
        w = self.weights
        a = self.cg_arms
        for key in w:
            x_cg += w[key] * a[key][0]
            y_cg += w[key] * a[key][1]
            W_sum += w[key]
        self.x_cg = x_cg/W_sum
        self.y_cg = y_cg/W_sum
        self.airframe_wgt = W_sum + self.weights['rubber']
        self.flying_wgt = W_sum


        ## add calculated dimensions needed in later work
        self.wing['tip_angle'] = math.atan(self.wing['tip_dihedral']/self.wing['tip_span'])
        self.wing['projected_area'] = \
        self.wing['center_span'] * self.wing['center_chord'] \
            + 2 * (self.wing['center_chord'] + self.wing['tip_chord'])/2 *\
            self.wing['tip_span'] * math.cos(self.wing['tip_angle'])
        self.wing['projected_span'] = self.wing['center_span'] + 2 * \
            self.wing['tip_span'] * math.cos(self.wing['tip_angle'])
        self.wing['mean_chord'] = self.wing['projected_area']/self.wing['projected_span']
        self.wing['te_to_ac'] = 0.75 * self.wing['mean_chord']
        self.wing['tip_span'] * math.cos(self.wing['tip_angle'])

        self.stab['tip_angle'] = math.atan(self.stab['tip_dihedral']/self.stab['tip_span'])
        self.stab['projected_area'] = 2 * self.stab['tip_span'] * (self.stab['center_chord']
            + self.stab['tip_chord'] )/2\
            * math.cos(self.stab['tip_angle'])
        self.stab['tip_angle'] = math.atan(self.stab['tip_dihedral']/self.stab['tip_span']/2)
        self.stab['projected_span'] = 2 * self.stab['tip_span'] * math.cos(self.stab['tip_angle'])
        self.stab['mean_chord'] = self.stab['projected_area']/self.stab['projected_span']
        self.stab['te_to_ac'] = 0.75 * self.stab['mean_chord']

    def model_data(self):
        model = {
            'name': self.name,
            'wing': self.wing,
            'stab': self.stab,
            'weights': self.weights,
            'cg_arms': self.cg_arms,
            'cg': (self.x_cg, self.y_cg),
            'airframe_wgt': self.airframe_wgt,
            'flying_wgt': self.flying_wgt,
            'motor' : self.motor,
        }
        return model

if __name__ == '__main__':
    u = pint.UnitRegistry()
    m = Wart(u)
    data = m.model_data()
    for k in data:
        print(f'{k}:')
        item = data[k]
        if isinstance(item, dict):
            for kk in item:
                if isinstance(item[kk],tuple):
                    c = item[kk]
                    print(f'\t{kk}=({c[0]}.{c[1]}')
                else:
                    print(f'\t{kk}={item[kk]}')
        else:
            print(f'{k}: {item}')
