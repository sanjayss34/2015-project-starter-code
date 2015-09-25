from app import app
from jinja2 import Template
from flask import render_template
import models
treasures = []


@app.route('/', methods=['GET'])
def index():
	current_treasures = [39.95, 75.19, "Center"]
	for t in models.TreasurePoint.query.all():
		current_treasures.append(t.latitude)
		current_treasures.append(t.longitude)
		current_treasures.append(t.notes)
	return render_template('template.html', treasures=current_treasures)

@app.route('/coordinates', methods=['POST'])
def add_treasure():
    latitude = request.args.get('latitude', 39.95, type=float)
    longitude = request.args.get('longitude', 75.19, type=float)
    notes = request.args.get('notes', '', type=str)
    treasures.append(TreasurePoint(latitude=latitude, longitude=longitude, notes=notes))
    return redirect(url_for('app.index'))
