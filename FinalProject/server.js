// load the things we need
const { default: axios } = require('axios');
var express = require('express');
var app = express();

// set the view engine to ejs
app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: false}))

// login page
app.get('/', function(req, res) {
    res.render('pages/login');
});

// home page
app.get('/home', function(req, res) {
    res.render('pages/home');
});

// displays all of the trips
app.get('/trips', function(req, res) {
    res.render('pages/trips');
});

// adds a trip
app.post('/addTrip', (req,res) => {
  res.render('/pages/addTrip');
});

//updates a trip
app.put('/editTrip', (req,res) => {
  res.render('/pages/editTrip');
});

//deletes a trip
app.delete('/deleteTrip', (req,res) => {
  res.render('/pages/deleteTrip');
});

// displays all of the destinations
app.get('/destination', function(req, res) {
    res.render('pages/destination');
});

// adds a destination
app.post('/addDestination', (req,res) => {
  res.render('/pages/addDestination');
});

//updates a destination
app.put('/editDestination', (req,res) => {
  res.render('/pages/editDestination');
});

//deletes a destintaion
app.delete('/deleteDestination', (req,res) => {
  res.render('/pages/deleteDestination');
});

// brings user to sign out page
app.get('/signout', (req,res) => {
    res.render('/pages/signout');
  });
  

app.listen(8080);
console.log('8080 is the magic port');
