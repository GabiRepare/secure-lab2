from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("./signin.html")

@app.route("/submit", methods=['POST'])
def submit():
	print(request.form['username'])
	return "OK"
