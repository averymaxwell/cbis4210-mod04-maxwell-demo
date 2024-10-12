from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/runners')
def runners():
    return render_template('runners.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

