from myapp import myapp_obj
from myapp.forms import TopCities 
from flask import render_template, flash, redirect
from myapp import db
from myapp.models import Cities

@myapp_obj.route("/", methods=['GET', 'POST'])
def home():
	name = 'Tri'    
	title = 'Top Cities'    
	form = TopCities()
	db.create_all()
	city = Cities.query.all()

	if form.validate_on_submit():				
		name = form.city_name.data
		rank = form.city_rank.data				
		flash(f'{form.city_name.data} was added')						
		city = Cities(name,rank)		
		db.session.add(city)
		db.session.commit()	
		return redirect('/')
    
	return render_template('home.html',title=title ,name=name ,form=form, cities=city)

