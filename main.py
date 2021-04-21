#!/usr/bin/env python3 

#Program Notes
"""
Aurthor : Frank Lamar
Email   : lamar.frankie@protonmail.com
Purpose : Python Web App to Generate Password
Date    : 01-02-2021
"""

import argparse
import random
import string

password_bank = string.ascii_letters + string.punctuation + string.digits

from flask import Flask

app = Flask(__name__)
password_min_length = 8
password_max_length = 16

@app.route("/")
def index():
    return "Hello DevSecOps! <br/> <br/> Welcome to my Password Generator"

@app.route("/generate-password")
def generate_password():

    password = "".join(random.choice(password_bank) for x in range(random.randint(password_min_length,password_max_length)))
    
    return "Your password is: <br/> <br/>" + password

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)