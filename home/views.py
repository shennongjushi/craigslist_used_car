from craigslist_used_car import app
from flask import render_template, redirect, flash, url_for, session, abort, request
from home.form import SearchForm
import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn['craigslist']
cars_coll = db['cars']

@app.route('/')
@app.route('/index')
def index():
    conditions = cars_coll.distinct('condition')
    cylinders = cars_coll.distinct('cylinder')
    fuels = cars_coll.distinct('fuel')
    sizes = cars_coll.distinct('size')
    title_statuses = cars_coll.distinct('title_status')
    transimissions = cars_coll.distinct('transimission')
    types = cars_coll.distinct('type')
    return render_template('index.html', conditions=conditions, cylinders=cylinders, fuels=fuels, sizes=sizes,title_statuses=title_statuses, transimissions= transimissions, types=types)
    
@app.route('/search', methods=('GET','POST'))
def search():
    if request.method == 'POST':
        condition = request.form['condition']
        cylinder = request.form['cylinder']
        fuel = request.form['fuel']
        size = request.form['size']
        title_status = request.form['title_status']
        transimission = request.form['transimission']
        type = request.form['type']
        make = request.form['make']
        year = request.form['year']
        #queries = cars_coll.find({"$and": [{"size": "size"},{"make":"make"}]}) 
        queries = cars_coll.find({"size": size})
        #results = []
        #for query in queries:
        #    results.append({
        #        'url':query['url'],
        #        'title':query['title']
        #    })
        return render_template('search.html', results=queries)
    else :
        return render_template('search.html')