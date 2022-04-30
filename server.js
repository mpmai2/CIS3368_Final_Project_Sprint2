// var express = require('express');
// var alert = require('alert');
//
// var app = express();
// const bodyParser = require("body-parser");
// const { json } = require('body-parser');
// app.use(bodyParser.urlencoded({
//     extended: true
// }));
// const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));
//
//
// python_url = "http://127.0.0.1:5000/api"
//
//
// // set the view engine to ejs
// app.set('view engine', 'ejs');
//
// // index page
// app.get('/', function (req, res) {
//     res.render('pages/index');
// })
//
//
// app.get('/all_employees2', function(req,res){
//     fetch(python_url+"/get_employees2")
//     .then(response =>response.json())
//     .then(results =>{
//         // console.log(results)
//         const employees = results.employees.map(function(result){
//             var employees = {"emp_ID":result.emp_ID,
//                         "emp_First_Name":result.emp_First_Name,
//                         "emp_Last_Name" : result.emp_Last_Name,
//                         "emp_Role" : result.emp_Role,
//                         "emp_Bookable" : result.emp_Bookable
//             }
//             return employees
//         })
//         const my_result = {
//                         employees : employees}
//         console.log(my_result)
//         res.render('pages/employees2',{
//             my_result : my_result
//         })
//     })
//     .catch(_ => {
//         res.render('pages/error')
//     })
// })
//
// app.post('/delete_employees', function(req, res) {
//     var postData = parseInt(req.body.emp_ID)
//     // console.log(postData)
//     const data = {emp_ID:postData}
//     console.log(data)
//     fetch(python_url + "/delete_employees", {
//         method: 'DELETE',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data)
//     })
//         .then(response => {
//             //reloads the page
//             res.redirect('back')
//         })
// })
//
// app.post('/add_employees', function (req, res) {
//     var firstname = req.body.emp_First_Name
//     var lastname = req.body.emp_Last_Name
//     var role = req.body.emp_Role
//     var bookable = req.body.emp_Bookable
//     const data = { firstname: firstname, lastname: lastname, role: role, bookable: bookable }
//     console.log(data)
//     fetch(python_url + "/add_employees", {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data)
//     })
//         .then(response => {
//             //reloads the page
//             res.redirect('back')
//         })
// })
// app.post('/edit_employees', function (req, res) {
//     var emp_ID = req.body.emp_ID
//     var firstname = req.body.emp_First_Name
//     var lastname = req.body.emp_Last_Name
//     var role = req.body.emp_Role
//     var bookable = req.body.emp_Bookable
//     const data = {emp_ID:emp_ID,firstname:firstname,lastname:lastname,role:role,bookable:bookable}
//     console.log(data)
//     fetch(python_url + "/edit_employees", {
//         method: 'PUT',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data)
//     })
//         .then(response => {
//             //reloads the page
//             res.redirect('back')
//         })
// })



// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));

python_url = "http://127.0.0.1:5000/api"

var selectedID = "";
app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// index page
app.get('/', function(req, res) {

    res.render('pages/index', {
    });

});

app.get('/create', function(req, res) {

    res.render('pages/create', {
    });

});


app.get('/all_trip', function(req, res) {
    fetch(python_url+"/trip")
    .then(response =>response.json())
    .then(results =>{
        // console.log(results)
        const trip = results.trip.map(function(result){
            var trip = {"id":result.id,
                        "destinationid":result.destinationid,
                        "transportation":result.transportation,
                        "startdate" : result.startdate,
                        "enddate" : result.enddate,
                        "tripname" : result.tripname
            }
            return trip
        })
        const my_result = {
                        trip : trip}
        console.log(my_result)

    res.render('pages/edit',{
            my_result : my_result
        })
    })
})

app.post('/edit_trip', function (req, res) {
    var id = req.body.id
    var destinationid = req.body.destinationid
    var transportation = req.body.transportation
    var startdate = req.body.startdate
    var enddate = req.body.enddate
    var tripname = req.body.tripname
    const data = {id:id,destinationid:destinationid,transportation:transportation,startdate:startdate,enddate:enddate,tripname:tripname}
    console.log(data)
    fetch(python_url + "/edit_trip", {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            //reloads the page
            res.redirect('back')
        })
})

app.post('/delete_trip', function(req, res) {
    var postData = parseInt(req.body.id)
    // console.log(postData)
    const data = {id:postData}
    console.log(data)
    fetch(python_url + "/delete_trip", {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            //reloads the page
            res.redirect('back')
        })
})

app.post('/add_trip', function (req, res) {
    var destinationid = req.body.destinationid
    var transportation = req.body.transportation
    var startdate = req.body.startdate
    var enddate = req.body.enddate
    var tripname = req.body.tripname
    const data = {destinationid:destinationid,transportation:transportation,startdate:startdate,enddate:enddate,tripname:tripname}
    console.log(data)
    fetch(python_url + "/add_trip", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            //reloads the page
            res.redirect('back')
        })
})

// Destination Table


app.listen(8080);
console.log('8080 is the magic port');