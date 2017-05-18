'use strict';

var mysql = require('mysql');
var express = require('express');
var app = express();

var conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'bookstore'
});

conn.query('SELECT * FROM author;', function (err, rows) {
    if (err) {
        console.log('Yeah it is not working like this', err);
    } else {
        console.log('Data received:\n')
        rows.forEach(row=>{
            console.log(row.country)
        });
    }
});

app.get('/', function get(req, res) {
    var result = [];
    conn.query('SELECT * FROM author', function (err, rows) {
        if (err) {
            console.log('PROBLEM', err);
        } else {
            rows.forEach( function(row) {
                result.push(row.aut_name);
            });
        }
        res.send(result);
    });
});

app.listen(3000, function() {
    console.log('server is running')
});
