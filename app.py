from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@mysql-host/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a simple model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

# Home page with form and messages
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form['message']
        new_msg = Message(text=msg)
        db.session.add(new_msg)
        db.session.commit()
        return redirect('/')
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

