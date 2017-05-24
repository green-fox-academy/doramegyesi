'use strict';

const express = require('express');
const app = express();

var allPlaylists = [
	{ "id": 1, "title": "Favorites", "system": 1},
	{ "id": 2, "title": "Music for programming", "system": 0},
	{ "id": 3, "title": "Driving", "system": 0},
	{ "id": 5, "title": "Fox house", "system": 0},
];

app.get('/', function(req, res){
    res.send('FOXPLAYER');
});

app.get('/playlists', function(req, res){
    res.send(allPlaylists);
});

app.listen(3000, function(){
    console.log('server is running smoothly');
});
