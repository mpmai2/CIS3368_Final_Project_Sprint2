import mysql.connector
from mysql.connector import Error
import flask
from flask import jsonify, render_template, request
import datetime

# Creating the functions that connects the database to AWS and executes its queries
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Connecting my specific Database to MYSQL workbench
connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')

# Creating my cursor
mycursor = connect.cursor()


#Creating the table for trips
tripTable = '''CREATE TABLE Trip(
    id INT AUTO_INCREMENT PRIMARY KEY,
    destinationId INT,
    transportation VARCHAR(100),
    startDate DATE, 
    endDate DATE,
    tripName VARCHAR(250),
    FOREIGN KEY (destinationid) REFERENCES Destination(id)
    )
    '''
#mycursor.execute(tripTable)

#Creating the table for destinations
destinationTable = ''' CREATE TABLE Destination(
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100),
    city VARCHAR(100),
    sightseeing VARCHAR(250)
    )
    '''
#mycursor.execute(destinationTable)

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

#getting all of the data from the Trip table to display from user
@app.route('/trips', methods=['GET'])
def trips():
    connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
    mycursor = connect.cursor()
    mycursor.execute('SELECT * FROM Trip')
    data = mycursor.fetchall()
    return render_template ('trips.ejs', trip=data)

#allowing the user to add a trip
@app.route('/addTrip', methods=['POST'])
def addTrip():
    if request.method =='POST':
        ntripName = request.form['tripName']
        ntransportation = request.form['transportation']
        nstartDate = request.form['startDate']
        nendDate = request.form['endDate']

        #connecting route to the database and executing the query
        connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
        query = ''' INSERT INTO Trip(tripName, transportation, startDate, endDate) VALUES ('{}', '{}', '{}', '{}' )'''.format(ntripName, ntransportation, nstartDate, nendDate)
        execute_query(connect, query)

#allowing the user to edit a trip
@app.route('/editTrip', methods=['PUT'])
def editTrip():
    if request.method == 'PUT':
        tid = request.form['id']

        connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
        query = ''' UPDATE Trip WHERE id = {} '''.format(tid) 
        execute_query(connect, query)

#allowing the user to delete a trip
@app.route('/deleteTrip', methods=['DELETE'])
def deleteTrip():
    if request.method == 'DELETE':
        tid = request.form['id']

        connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
        query = ''' DELETE FROM Trip WHERE id = {} '''.format(tid) 
        execute_query(connect, query)

#getting all of the data from the Destination table to display from user
@app.route('/destination', methods=['GET'])
def destination():
    connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
    mycursor = connect.cursor()
    mycursor.execute('SELECT * FROM Destination')
    data = mycursor.fetchall()
    return render_template ('destination.ejs', destination=data)

# allowing the user to add a trip
@app.route('/addDestination', methods=['POST'])
def addDestination():
    if request.method =='POST':
        ncountry = request.form['country']
        ncity = request.form['city']
        nsightseeing = request.form['sightseeing']

        connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
        query = ''' INSERT INTO Destination (country, city, sightseeing) VALUES ('{}', '{}', '{}', '{}', '{}' )'''.format(ncountry, ncity, nsightseeing)
        execute_query(connect, query)

#allowing the user to edit a trip
@app.route('/editDestination', methods=['PUT'])
def editDestination():
    if request.method == 'PUT':
        did = request.form['id']

        connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
        query = ''' UPDATE Destination WHERE id = {} '''.format(did) 
        execute_query(connect, query)

#allowing the user to update a trip
@app.route('/deleteDestination', methods=['DELETE'])
def deleteDestination():
    if request.method == 'DELETE':
        did = request.form['id']

        connect = create_connection('cis3368.capnnzprbgld.us-east-2.rds.amazonaws.com', 'admin', 'mpm1860603', 'CIS3368db')
        query = ''' DELETE FROM Destination WHERE id = {} '''.format(did) 
        execute_query(connect, query)


app.run()