from myapp import db

class Cities(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	city_name = db.Column(db.String(64), unique = True, index = True)
	city_rank = db.Column(db.Integer, unique = True)

	def __init__(self, city_name, city_rank):
		self.city_name = city_name
		self.city_rank = city_rank		

	def __repr__(self):
                return f'{self.city_name}'
