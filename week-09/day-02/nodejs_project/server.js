'use strict';
var express = require('express');
var app = express();

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.use('/assets', express.static('assets'));

//var doubling = document.selectQuery('.doubling');
//doubling.addEventListener('click'

app.get('/doubling', function(req, res) {
    if (req.query === {} || req.query.input === undefined) {
        res.send( {
            error: 'Please provide an input!'
        });
    } else {
        res.send( {
            received: parseInt(req.query.input),
            result: req.query.input * 2
        })
    }
});

app.get('/greeter', function(req, res) {
    if (req.query.name === undefined) {
        res.send( {
            error: 'Please provide a name!'
        });
    } else if (req.query.title === undefined) {
        res.send( {
            error: 'Please provide a title!'
        });
    }
     else {
        res.send( {
            welcome_message: 'Oh, hi there ' + req.query.name + ', my dear ' + req.query.title + '!'
        })
    }
});

app.get('/appenda/:a', function(req, res) {
    res.send( {
        appended: req.params.a + 'a'
    });
});

app.listen(8080);
