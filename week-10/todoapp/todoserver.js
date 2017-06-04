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
    connect.query('DELETE FROM todos WHERE id = "'+ req.params.id +'"', function(err, rows) {
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
});

app.listen(3000, function() {
    console.log('server is running smoothly');
});
