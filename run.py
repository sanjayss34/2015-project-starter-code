from app import app, db
app.run(host='0.0.0.0', port=5000, debug=True)
db.drop_all()
db.session.commit()
db.create_all()
db.session.commit()