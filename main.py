from flask import Flask, render_template, request, redirect
from Crypto.PublicKey import RSA
import random
import math
from twilio.rest import Client
app = Flask(__name__)

# db
db = {}
db['alice'] = "azerty"

g = 13
p = 541

global authCode
authCode = 0

@app.route('/')
def hello_world():
	return render_template("./signin.html")

@app.route("/authok")
def authok():
	return "User Auth ok !!"

@app.route("/authfail")
def authfail():
	return "User auth failed"

@app.route("/submit", methods=['POST'])
def submit():
	print(request.form['username'] + " " + request.form['pwd'])
	# send sms
	# Your Account SID from twilio.com/console
	account_sid = "AC87d93b6e2c9aed16927bf1bae8df9315"
	# Your Auth Token from twilio.com/console
	auth_token  = "78910343e04aaf92055ab36db426206f"

	client = Client(account_sid, auth_token)
	
	if db[request.form['username']] == request.form['pwd']:
		# generate auth code
		global authCode
		authCode  = random.randint(1000, 9999);
		print(authCode)
	
		message = client.messages.create(
    	to="+33646504232", 
    	from_="+33757903970",
    	body="Please enter auth code : " + str(authCode))
	
	return "OK"

@app.route("/verify", methods=['POST'])
def verify():
	print("verifying : " + request.form['verify'])
	print(authCode)
	if int(request.form['verify']) == authCode:
		print("User 2-authenticated");
		return redirect("/authok")
 	else:
		print("Auth. failed")
		return redirect("/authfail")
	
