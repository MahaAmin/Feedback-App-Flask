from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_email 

app = Flask(__name__)

ENV = 'dev'

if ENV == 'prod':
    # dev env
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/lexus'
else:
    # prod env
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://atrguyztjkncpo:3d0398d6ba6c23630bde048978a46604c6a645b8caa28abd470464edf87ed0cc@ec2-3-215-207-12.compute-1.amazonaws.com:5432/d782v5la5tvj7s'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

        #print(customer, dealer, rating, comments)
        # check customer and dealer fields are not empty
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter the required fields!')
        
        # enable customer to give feedback only once
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer,rating,comments)
            db.session.add(data)
            db.session.commit()

            # send email
            send_email(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback!')




if __name__ == '__main__':
    app.run()