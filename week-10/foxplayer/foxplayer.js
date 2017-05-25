'use strict';

const cors = require('cors');
const bodyParser = require('body-parser');
const express = require('express');
const app = express();

app.use('/assets', express.static('assets'));
app.use('/img', express.static('img'));
app.use(bodyParser.json());
app.use(cors());

var allPlaylists = [
	{ "id": 1, "title": "Songs for running", "system": 1},
	{ "id": 2, "title": "Music for programming", "system": 0},
	{ "id": 3, "title": "Relaxing", "system": 0},
	{ "id": 4, "title": "Crazy party music", "system": 0},
	{ "id": 5, "title": "Best roadtrip songs", "system": 0},
];

var allTracks = [
	{ "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
	{ "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" },
	{ "id": 28, "title": "Good song", "artist": "Cool guy", "duration": 921, "path": "c:/music/something.mp3" },
	{ "id": 72, "title": "Makes you cry", "artist": "Sassy sisters", "duration": 755, "path": "c:/music/bla.mp3" },
	{ "id": 53, "title": "Party hymn", "artist": "Crazy Dudes", "duration": 155, "path": "c:/music/zzla.mp3" },
	{ "id": 62, "title": "Your moms fav song", "artist": "Man With Sad Eyes", "duration": 84, "path": "c:/music/mom.mp3" },
	{ "id": 11, "title": "Relax", "artist": "A Girl", "duration": 145, "path": "c:/music/girl.mp3" }
];

app.get('/', function(req, res){
    res.sendFile(__dirname + '/foxplayer.html');
});

app.get('/playlists', function(req, res){
    res.send(allPlaylists);
});

app.get('/playlist-tracks:playlist_id', function(req, res){
    res.send(allTracks);
});

app.listen(3000, function(){
    console.log('server is running smoothly');
});
