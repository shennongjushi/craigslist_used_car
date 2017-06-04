from craigslist_used_car import db

class Make(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), unique=True)
    models = db.relationship('Model', backref='make',lazy='dynamic')
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    
class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    name = db.Column(db.String(35))
    def __init__(self, year, name):
        self.year = year
        self.name = name
    def __repr__(self):
        return self.year + ' ' + self.name

class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(10), unique=True)
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(10), unique=True)
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value
    
class Color(db.Mode):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(15), unique=True)
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value
    
class Fuel(db.Mode):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(10), unique=True) 
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value

class Condition(db.Mode):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Condition(db.string(15), unique=True)
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    condition_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'))
    fuel_id = db.Column(db.Integer, db.ForeignKey('fuel.id'))
    cylinder = db.Column(db.Integer)
    odometer = db.Column(db.Integer)
    latitude = db.Column(db.Double)
    longitude = db.Column(db.Double)
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    link = db.Column(db.String(100))
    images = db.Column(db.Text)
    
    def __init__(self, make, model, condition, size, type, color, fuel, cylinder, odometer, latitude, 
    longitude, price, date, description, link, images):
        self.make_id = make.id
        self.model_id = model.id
        self.condition_id = condition.id
        self.size_id = size.id
        self.type_id = type.id
        self.color_id = color.id
        self.fuel_id = fuel.id
        self.cylinder = cylinder
        self.odometer = odometer
        self.latitude = latitude
        self.longitude = longitude
        self.price = price
        self.date = date
        self.description = description
        self.link = link
        self.images = images
        
    def __repr__(self):
        return '<Post %r>' % self.username   
        
    
   
        
    