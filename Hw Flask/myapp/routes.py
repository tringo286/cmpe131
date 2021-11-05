from myapp import myapp_obj
from myapp.forms import TopCities 
from flask import render_template, flash, redirect, request
from myapp import db
from myapp.models import Cities

@myapp_obj.route("/", methods = ['GET', 'POST'])
def home():
	name = 'Tri'    
	title = 'Top Cities'    
	form = TopCities()
	db.create_all()
	cities = Cities.query.all()
	if form.validate_on_submit():
		if db.session.query(Cities).filter_by(city_name = form.city_name.data).first():
			flash('The city name already exists')
			return redirect('/')
		
		elif db.session.query(Cities).filter_by(city_rank = form.city_rank.data).first():
			flash(f'{form.city_name.data} was added')			
			name = request.form['city_name']
			rank = len(cities) + 1
			city = Cities(name, rank)
			db.session.add(city)
			db.session.commit()
			return redirect('/')

		name = request.form['city_name']
		rank = request.form['city_rank']
		flash(f'{form.city_name.data} was added')			
		city = Cities(name, rank)		
		db.session.add(city)
		db.session.commit()	
		return redirect('/')    
	return render_template('home.html',title = title ,name = name ,form = form, cities = cities)

