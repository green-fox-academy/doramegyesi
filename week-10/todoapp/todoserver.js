'use strict';

const express = require('express');
const app = express();
const mysql = require("mysql");
const cors = require('cors');
const bodyParser = require('body-parser');
var response;

app.use('/assets', express.static('assets'));
app.use('/img', express.static('img'));
app.use(bodyParser.json());
app.use(cors());

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/todoapp.html');
});

const connect = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "todos"
});

connect.connect(function(err) {
    if(err) {
    console.log("could not connect");
    }
    console.log("connected successfully to database");
});

app.get('/todos', function(req, res) {
    connect.query('SELECT * FROM todolist', function(err, rows) {
        if (err) {
            console.log('could not find the table', err.message);
        } else {
            response = rows;
            console.log(response);
        }
        res.send(response);
    });
});

app.delete('/todos/:id', function(req, res) {
    connect.query('DELETE FROM todolist WHERE id = "'+ req.params.id +'"', function(err, rows) {
        if (err) {
            console.log('could not find the table', err.message);
        } else {
            response = rows;
            console.log(response);
        }
        res.send(response);
    });
});

app.post('/todos/', function(req, res) {
    connect.query('INSERT INTO todolist (text, completed) VALUES("'+ req.body.text +'", "'+ req.body.completed +'");', function(err, rows) {
        if (err) {
            console.log('could not find the table', err.message);
        } else {
            response = rows;
            console.log(response);
        }
        res.send(response);
	});
});

app.put('/todos/:id', function(req, res) {
    connect.query('UPDATE todolist SET completed = "'+ req.body.completed +'" WHERE id = "'+ req.params.id +'"', function(err, rows) {
        if (err) {
            console.log('could not find the table', err.message);
        } else {
            response = rows;
            console.log(response);
        }
        res.send(response);
	});
});

app.get('/todos/incomplete', function (req, res) {
    connect.query('SELECT * FROM todolist WHERE completed = 0', function(err, rows) {
        if (err) {
            console.log('could not find the table', err.message);
        } else {
            response = rows;
            console.log(response);
        }
        res.send(response);
    });
});

app.listen(3000, function() {
    console.log('server is running smoothly');
});
