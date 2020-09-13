from flask import Flask, render_template
from __init__ import app

# projects views

@app.route('/')
def index():
    '''
    view home page
    '''
    return render_template('index.html')
