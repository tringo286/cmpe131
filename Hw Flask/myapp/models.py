from myapp import db

class Cities(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	cityname = db.Column(db.String(64), unique = True, index = True)
	cityrank = db.Column(db.Integer, unique = True)

	def __init__(self,cityname,cityrank):
		self.cityname = cityname
		self.cityrank = cityrank

	def set_rank(self,cityrank):
		self.cityrank = cityrank

	def set_name(self,cityname):
		self.cityname = cityname

	def __repr__(self):
                return f'{self.cityname}'
