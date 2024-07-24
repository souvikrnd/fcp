from flask import Flask, render_template, request, url_for, flash, redirect
from flask_mail import Mail, Message


# flashcraftproductions@gmail.com
# Mystartup@2023

app = Flask(__name__)

app.secret_key = "mail"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']= 'flashcraftproductions@gmail.com'
app.config['MAIL_PASSWORD']='hvsgqqckrppolisc'

mail= Mail(app)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method =='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        contact = request.form['contact']
        message = request.form['message']
        
        msg = Message('New Form Submission',
                      sender= 'flashcraftproductions@gmail.com',
                      recipients=['flashcraftproductions@gmail.com'])
        msg.body=f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nContact No: {contact}\nMessage: {message}"
                    
        mail.send(msg)
        flash('Your form is submitted')
        return redirect(url_for('home'))
        
    return render_template('home.html')

@app.route('/bussiness_card')
def bussiness_card():
    return render_template('bussiness_card.html')



@app.route('/apparel')
def apparel():
    return render_template('apparel.html')

if __name__ == '__main__':
    app.run(debug=True)
