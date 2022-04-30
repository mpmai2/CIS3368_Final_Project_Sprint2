import mysql.connector
import flask
import sql
from datetime import datetime, date, time
from flask import jsonify
from flask import request
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#establishing the connection to the database
conn = create_connection('cis3368.cqsy5faq0diz.us-east-2.rds.amazonaws.com', 'Hunter_Barrows', '538303!Hpb!', 'CIS3368db')

#setting up the application
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show erros in browser

#CRUD Operations for destination table

#Getting information from the destination table as GET: http://127.0.0.1:5000/api/destination
@app.route('/api/destination', methods=['GET'])
def api_all_destinations():
    destination_query = "SELECT * FROM destination"
    destination = execute_read_query(conn, destination_query)
    return {'destination': destination}

#Adding destination as POST: http://127.0.0.1:5000/api/destination
@app.route('/api/add_destination', methods=['POST'])
def add_destination():
    request_data = request.get_json()
    newCountry = request_data['country']
    newCity = request_data['city']
    newSightseeing = request_data['sightseeing']
    destination_add = "INSERT INTO destination (country, city, sightseeing) VALUES ('%s', '%s', '%s')" % (newCountry, newCity, newSightseeing)
    execute_query(conn, destination_add)
    return 'Destination added successfully'

#Deleting destination by ID as DELETE: http://127.0.0.1:5000/api/destination
@app.route('/api/delete_destination', methods=['DELETE'])
def delete_destination():
    request_data = request.get_json()
    idToDelete = request_data['id']
    delete_statement = "DELETE FROM destination WHERE id = %s" % (idToDelete)
    execute_query(conn, delete_statement)
    return 'Destination deleted successfully'

#Updating the destination as PUT: http://127.0.0.1:5000/api/destination
@app.route('/api/edit_destination', methods=['PUT'])
def update_destination():
    request_data = request.get_json()
    idToUpdate = request_data['id']
    Ucountry = request_data['country']
    Ucity = request_data['city']
    Usightseeing = request_data['sightseeing']
    update_make_query = """
            UPDATE destination
            SET country = '%s',
            city = '%s',
            sightseeing = '%s'
            WHERE ID = %s""" % (Ucountry, Ucity, Usightseeing, idToUpdate)
    execute_query(conn, update_make_query)
    return "Updated destination successfully"

# CRUD operations for trip table

#Getting information from the trip table as GET: http://127.0.0.1:5000/api/trip
@app.route('/api/trip', methods=['GET'])
def api_all_trips():
    trip_query = "SELECT * FROM trip"
    trip = execute_read_query(conn, trip_query)
    return {'trip': trip}

#Adding trip as POST: http://127.0.0.1:5000/api/trip
@app.route('/api/add_trip', methods=['POST'])
def add_trip():
    request_data = request.get_json()
    transportation = request_data['transportation']
    startdate = request_data['startdate']
    enddate = request_data['enddate']
    tripname = request_data['tripname']
    destinationid = request_data['destinationid']
    trip_add = "INSERT INTO trip (destinationid, transportation, startdate, enddate, tripname) VALUES (%s, '%s', '%s', '%s', '%s')" % (destinationid, transportation, startdate, enddate, tripname)
    execute_query(conn, trip_add)
    return 'Trip added successfully'


#Deleting trip by ID as DELETE: http://127.0.0.1:5000/api/trip
@app.route('/api/delete_trip', methods=['DELETE'])
def delete_trip():
    request_data = request.get_json()
    id = request_data['id']
    delete_statement = "DELETE FROM trip WHERE id = %s" % (id)
    execute_query(conn, delete_statement)
    return 'Trip deleted successfully'

#Updating the trip as PUT: http://127.0.0.1:5000/api/trip
@app.route('/api/edit_trip', methods=['PUT'])
def update_trip():
    request_data = request.get_json()
    id = request_data['id']
    destinationid = request_data['destinationid']
    transportation = request_data['transportation']
    startdate = request_data['startdate']
    enddate = request_data['enddate']
    tripname = request_data['tripname']
    update_make_query = """
            UPDATE trip
            SET destinationid = '%s',
            transportation = '%s',
            startdate = '%s',
            enddate = '%s',
            tripname = '%s'
            WHERE ID = %s""" % (destinationid, transportation, startdate, enddate, tripname, id)
    execute_query(conn, update_make_query)
    return "Updated trip successfully"

#dictionary for users to authenicate login
authorizedusers=[
    {
        #default user
        'username': 'username',
        'password': 'password',
        'role': 'default',
        'token': '0',
        'admininfo': None
    },
    {
        #admin user
        'username': 'hpbarrow',
        'password': '0123456789',
        'role': 'admin',
        'token': '1',
        'admininfo': 'CIS3368 gives students the opportunity to be great coders'
    }
]


#authenticate with username and password with GET: http://127.0.0.1:5000/api/usernamepw
#test this in postman by creating a header parameters
@app.route('/api/usernamepw', methods=['GET'])
def usernamepw():
    username = request.headers['username'] #get the header parameters from request headers as dictionary
    pw = request.headers['password']
    for au in authorizedusers: #loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == pw: #found an auth. user
            sessiontoken = au['token']
            admininfo = au['admininfo']
            returninfo = []
            returninfo.append(au['role'])
            returninfo.append(sessiontoken)
            returninfo.append(admininfo)
            return jsonify(returninfo)
    return 'SECURITY ERROR'

app.run()

