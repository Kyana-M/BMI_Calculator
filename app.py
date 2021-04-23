from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail


app = Flask(__name__)

ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/BMI'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ujlyoywcpwaeso:2f1c15993ab55cde9eccaaa4b68d21df478195f6f8a5ba2c11fcf01243a7a328@ec2-3-208-224-152.compute-1.amazonaws.com:5432/d93tkqe9krd1pa'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#creating database object
db = SQLAlchemy(app)

class BMI(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200),unique = True)
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    bio = db.Column(db.Text())
    job = db.Column(db.String(200))


    def __init__(self,name,email,age,height,weight,bio,job):
        self.name = name
        self.email = email
        self.age = age
        self.height = height
        self.weight = weight
        self.bio= bio
        self.job = job

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit' , methods = ['POST'])
def submit():
     if request.method == 'POST':
         name  = request.form['user_name']
         email = request.form['user_email']
         age = request.form['user_age']
         height = request.form['height_name']
         weight = request.form['weight_name']
         bio = request.form['user_bio']
         job = request.form['user_job']
         if name == '' or email == '':
             return render_template('index.html' , message = 'Please Enter required fields')
         if db.session.query(BMI).filter(BMI.email == email).count() == 0:
             data = BMI(name,email,age,height,weight,bio,job)
             db.session.add(data)
             db.session.commit()
             send_mail(name,height , weight ,email)
             return render_template('success.html')
         else:
             return render_template('index.html' , message = 'You have already Submitted')


if __name__ == '__main__':
    app.run()
