'use strict';

const express = require('express');
const app = express();
const mysql = require("mysql");
const cors = require('cors');
const bodyParser = require('body-parser');

app.use('/assets', express.static('assets'));
app.use('/img', express.static('img'));
app.use(bodyParser.json());
app.use(cors());

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/todoapp.html');
});

app.listen(3000, function() {
    console.log('server is running smoothly');
});
