from flask import Flask, render_template, request
from random import randint
import math
app = Flask(__name__)

#db = ['Alice', ]

g = 13
p = 541 

@app.route('/')
def hello_world():
	return render_template("./signin.html")

@app.route("/submit", methods=['POST'])
def submit():
	print(request.form['username'])
	# generate 
	b = randint(1, 80)
	beta = math.pow(g, b) % p
	print("beta = ", int(beta))

	return "OK"
