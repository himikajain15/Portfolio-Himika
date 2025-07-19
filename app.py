from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(subject=f"Portfolio messages!! {name}",
                  recipients=['himikajain2110@gmail.com'],
                  body=f"From: {name} <{email}>\n\nMessage:\n{message}")

    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        print(e)
        flash('Failed to send email. Try again later.', 'error')

    return redirect(url_for('home'))

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
