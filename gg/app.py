from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'c16766c522df4d'
app.config['MAIL_PASSWORD'] = '40dc1c9b1df323'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/",methods = ['POST', 'GET'])
def index():
   msg = Message('Hello', sender = 'peter@mailtrap.io', recipients = ['lalalandtwitter276@gmail.com'])
   msg.body = "Hello, your tickets are confirmed!" 
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
