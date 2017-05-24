'use strict';

const playlist = document.querySelector('.playlist')

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
                playlistItem.innerText = item.title;
                playlist.appendChild(playlistItem);
            });
        }
    }
};

getPlaylists();
