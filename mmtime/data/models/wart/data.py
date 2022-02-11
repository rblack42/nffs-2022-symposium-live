import pint
u = pint.UnitRegistry()
import math


class Model(object):

	model_name = 'wart-a6'

	model_data = {
		weights : {
    		'motor_stick': 0.22*u.grams,
    		'tail_boom': 0.08*u.grams,
    		'stab': 0.25*u.grams,
    		'wing': 0.42*u.grams,
    		'prop': 0.23*u.grams,
    		'rubber': 0.86*u.grams
		},
		cg_arms : {
    		'prop': (0*u.inch,-0.125*u.inch),
    		'wing': (2.25*u.inch, (7/8)*u.inch),
    		'stab': ((6+8.5-1)*u.inch,0.125*u.inch),
    		'motor_stick': (3*u.inch,0.0625*u.inch),
    		'tail_boom': (10.0*u.inch,0.125*u.inch),
    		'rubber': (3*u.inch,-0.125*u.inch)
		},
		wing : {
    		'center_span': 8 * u.inches,
    		'center_chord': 2 * u.inches,
    		'tip_span':3.75 * u.inches,
    		'tip_chord': 1.75 * u.inches,
    		'tip_dihedral': 7/8*u.inches,
		}
		stab : {
    		'tip_span': (5 + 7/16) * u.inches,
    		'center_chord': 1.75 * u.inches,
    		'tip_chord': 1 * u.inches,
    		'tip_dihedral': 7/8 * u.inches
		}
	}

	def __init__(self):
		## add calculated dimensions needed in later work
		wing['tip_angle'] = math.atan(wing['tip_dihedral']/wing['tip_span'])
		wing['projected_area'] = \
		wing['center_span'] * wing['center_chord'] \
     		+ 2 * (wing['center_chord'] + wing['tip_chord'])/2 *\
			wing['tip_span'] * math.cos(wing['tip_angle'])
		wing['projected_span'] = wing['center_span'] + 2 * \
		wing['mean_chord'] = wing['projected_area']/wing['projected_span']
		wing['te_to_ac'] = 0.75 * wing['mean_chord']
		wing['tip_span'] * math.cos(wing['tip_angle'])

		stab['projected_area'] = 2 * stab['tip_span'] * (stab['center_chord']
            + stab['tip_chord'] )/2\
         	* math.cos(stab['tip_angle'])
		stab['tip_angle'] = math.atan(stab['tip_dihedral']/stab['tip_span']/2)
		stab['projected_span'] = 2 * stab['tip_span'] * math.cos(stab['tip_angle'])
		stab['mean_chord'] = stab['projected_area']/stab['projected_span']
		stab['te_to_ac'] = 0.75 * stab['mean_chord']

	def return_model():
		return wart_a6


