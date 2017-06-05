'use strict';

const playlist = document.querySelector('.playlist');
const tracks = document.querySelector('.tracks');
const audio = document.querySelector('audio');
const currentSong = document.querySelector('.currentTitle');
const currentArtist = document.querySelector('.currentArtist');

function ajaxreq(url, method, callback) {
	const req = new XMLHttpRequest();
	req.open(method, url);
	req.onreadystatechange = function() {
        if (req.readyState === 4 && req.status === 200) {
            var response = JSON.parse(req.response);
            callback(response);
		}
	}
	req.send();
};

const getPlaylists = function() {
    const req = new XMLHttpRequest();
    const method = 'GET';
    const url = 'http://localhost:3000/playlists';
    req.open(method, url);
    req.send();
    req.onreadystatechange = function() {
        if (req.readyState === 4 && req.status === 200) {
            var playlists = JSON.parse(req.response);
            console.log(playlists);
            playlists.forEach(function(item) {
                var playlistItem = document.createElement('div');
                playlistItem.setAttribute('class', 'playlistItem');
				playlistItem.setAttribute('id', item.id);
                playlistItem.innerText = item.title;
                playlist.appendChild(playlistItem);
				playlistItem.addEventListener('click', function() {
					ajaxreq('http://localhost:3000/playlists-tracks/' + item.id, 'GET', getTracklist);
				});
            });
        }
    }
};

// playlistitem eventlistener -- ajax a playlist-tracksre + element.title (get)
// utana szerver oldalon uj endpoint app.get() -- conn.query SELECT bla FROM bla
// res.send!
//ajaxnal a callback a gettracklist

const getTracklist = function() {
    const req = new XMLHttpRequest();
    const method = 'GET';
    const url = 'http://localhost:3000/playlists-tracks';
    req.open(method, url);
    req.send();
    req.onreadystatechange = function() {
        if (req.readyState === 4 && req.status === 200) {
            var tracklist = JSON.parse(req.response);
            console.log(tracklist);
			tracks.innerText = '';
            tracklist.forEach(function(item) {
                var tracklistItem = document.createElement('div');
                tracklistItem.setAttribute('class', 'tracklistItem');
                tracklistItem.innerText = item.title;
                tracks.appendChild(tracklistItem);
                tracklistItem.addEventListener('click', function() {
                    play(item.path);
                });
				tracklistItem.addEventListener('click', function() {
					currentSong.innerText = item.title;
					currentArtist.innerText = item.artist;
				})
            });
        }
    }
};

function play(path){
    audio.setAttribute('src', path)
    audio.play();
}

getPlaylists();
getTracklist();
