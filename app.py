from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///competences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Competence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    niveau = db.Column(db.String(50), nullable=False)
    semestre = db.Column(db.String(10), nullable=False)

# Création des tables au démarrage
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    competences = Competence.query.all()
    return render_template('index.html', competences=competences)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form['nom']
    niveau = request.form['niveau']
    semestre = request.form['semestre']
    competence = Competence(nom=nom, niveau=niveau, semestre=semestre)
    db.session.add(competence)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/supprimer/<int:id>')
def supprimer(id):
    competence = Competence.query.get(id)
    if competence:
        db.session.delete(competence)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
