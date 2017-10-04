## Environnement setup

1. Make sure python 2.7 is installed
1. install virtualenv `pip install virtualenv`
1. Create a virtual environment `virtualenv -p /usr/bin/python2.7 env`
1. Activate the environment `source env/bin/activate`
1. Install Flask `pip install flask`
1. Set the main program file `export FLASK_APP=main.py`
1. Run the server locally `flask run`

## Description
This is a very basic website that ask the user for its username and password, sends a 4 digit code by SMS using the [Twilio](https://www.twilio.com/) API and waits for the user to enter the 2nd factor auth code. For the sake of simplicy, the password is sent to the API in clear text format which is totally unsafe. The goal of this lab is to demonstrate our understanding of the 2nd factor authentification.
