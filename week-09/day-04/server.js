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
        rows.forEach(row => {
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
        } res.send(result);
    });
});

app.get('/all', function get(req, res) {
    var books = '<ul>';
    conn.query('SELECT book_name FROM book_mast', function (err, rows) {
        if (err) {
            console.log('PROBLEM', err);
        } else {
            rows.forEach(row => {
                books += '<li>' + row.book_name + '</li>';
            });
            books += '</ul>';
        } res.send(books);
    });
});

app.get('/fulldata', function get (req, res) {
    var allData = '<table>';
    var queryAllData = 'SELECT book_mast.book_name, author.aut_name, category.cate_descrip, publisher.pub_name, book_mast.book_price ' + 'FROM book_mast ' +
    'JOIN author ON book_mast.aut_id = author.aut_id ' +
    'JOIN category ON book_mast.cate_id = category.cate_id ' +
    'JOIN publisher ON book_mast.pub_id = publisher.pub_id ;';
    conn.query(queryAllData, function (err, rows) {
        if (err) {
            console.log('PROBLEM', err);
        } else {
            allData += '<tr>' + '<th>' + 'title' + '</th>';
            allData += '<th>' + 'author' + '</th>';
            allData += '<th>' + 'category' + '</th>';
            allData += '<th>' + 'publisher' + '</th>';
            allData += '<th>' + 'price' + '</th>' + '</tr>';
            rows.forEach(row => {
                allData += '<tr>' + '<td>' + row.book_name + '</td>';
                allData += '<td>' + row.aut_name + '</td>';
                allData += '<td>' + row.cate_descrip + '</td>';
                allData += '<td>' + row.pub_name + '</td>';
                allData += '<td>' + row.book_price + '</td>' + '</tr>';
            });
            allData += '</table>';
        } res.send(allData);
    });
});

app.listen(3000, function() {
    console.log('server is running')
});
