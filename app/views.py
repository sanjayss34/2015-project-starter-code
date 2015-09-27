from app import app
from jinja2 import Template
from flask import render_template, request, redirect, url_for
import models
from app import db
treasures = []


@app.route('/', methods=['GET'])
def index():
	current_treasures = [39.952, -75.195, "Center"]
	for t in models.treasurepoint.query.all():
		current_treasures.append(t.latitude)
		current_treasures.append(t.longitude)
		current_treasures.append(t.notes)
	return render_template('template.html', treasures=current_treasures)

@app.route('/health', methods=['GET'])
def health():
    return 'Everything is fine', 200

@app.route('/coordinates', methods=['POST'])
def add_treasure():
    coordinate_objs = request.json['coordinates']
    for c in coordinate_objs:
        #latitude = request.args.get('latitude', 39.952, type=float)
        #longitude = request.args.get('longitude', -75.195, type=float)
        #notes = request.args.get('notes', "nothing", type=str)
        treasures.append(models.treasurepoint(latitude=c['latitude'], longitude=c['longitude'], notes=c['notes']))
        db.session.add(models.treasurepoint(latitude=c['latitude'], longitude=c['longitude'], notes=c['notes']))
        db.session.commit()
    return redirect(url_for('index'))
