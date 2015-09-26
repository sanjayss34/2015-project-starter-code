from . import db
from datetime import datetime


class treasurepoint(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(80), unique=True)
    #email = db.Column(db.String(120), unique=True)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')
	latitude = db.Column(db.Float, unique=False)
	longitude = db.Column(db.Float, unique=False)
	notes = db.Column(db.String, unique=False)
    #def __init__(self, username, email):
	def __init__(self, latitude, longitude, notes):
		#self.username = username
        #self.email = email
		self.latitude = latitude
		self.longitude = longitude
		self.notes = notes

	def __repr__(self):
		return [self.latitude, self.longitude, self.notes]

	#def is_cool(self):
        #return (self.username == 'aharelick')


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	body = db.Column(db.Text)
	pub_date = db.Column(db.DateTime, default=datetime.utcnow())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % self.title


