from craigslist_used_car import app
from flask import render_template, redirect, flash, url_for, session, abort, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('search.html')