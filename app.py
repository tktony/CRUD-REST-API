from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class User(db.Model): 
    __tablename__ = 'users'
    # columns in the DB: id, username, email
    id = db.Column(db.Integer, primary_key=True) # primary key
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
# initialize the database below       
db.create_all()

# create a test route
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({"message": "Test successful!"}),200)

# Endpoint 1: create a user - POST request with the body to endpoint
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(
            username=data['username'], 
            email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 201)
    except Exception as e:
        return make_response(jsonify({'messae': 'error creating a user'}), 500)
    
# Endpoint 2: get all users - GET request to endpoint
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all() # query all users from the DB
        return make_response(jsonify([user.json() for user in users]), 200) # return a list of users in JSON format, empty array if none exist
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users'}), 500)
    
# Endpoint 3: get a user by id - GET request to endpoint with the id in the URL
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first() # query the user by id from the DB
        if not user: # if the user does not exist, return 404
            return make_response(jsonify({'message': 'user not found'}), 404) 
        else: # if the user exists, return the user in JSON format
            return make_response(jsonify({'user': user.json()}), 200) # return the user in JSON format, empty object if none exist 
    except Exception as e:
        return make_response(jsonify({'message': 'error getting user'}), 500)
    
# Endpoint 4: update a user (most complicated function) - PUT request to endpoint with the id in the URL and the body to update
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first() 
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit() # we commit the new user 
            return make_response(jsonify({'message': 'user updated'}), 200) 
        else:
            return make_response(jsonify({'message': 'user not found'}), 404) 
    except Exception as e:
        return make_response(jsonify({'message': 'error updating user'}), 500)

# Endpoint 5: delete a user - DELETE request to endpoint with the id in the URL
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first() 
        if user:
            db.session.delete(user) # delete the user from the DB
            db.session.commit() # commit the changes to the DB
            return make_response(jsonify({'message': 'user deleted'}), 200) 
        else:
            return make_response(jsonify({'message': 'user not found'}), 404) 
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting user'}), 500)