
class Model(object):

	def __init__(self. ureg)
		self.ureg = ureg

	def get_properties(self):
		u = self.ureg
		return {
			'wing_projected_area': 30 * u.inches ** 2,
			'stab_projected_area': 15 * u.inches ** 2,
		}
