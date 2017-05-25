'use strict';

const playlist = document.querySelector('.playlist')
const tracks = document.querySelector('.tracks')

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
                playlistItem.setAttribute('class', 'playlistItem')
                playlistItem.innerText = item.title;
                playlist.appendChild(playlistItem);
            });
        }
    }
};

const getTracklist = function() {
    const req = new XMLHttpRequest();
    const method = 'GET';
    const url = 'http://localhost:3000/playlist-tracks:playlist_id';
    req.open(method, url);
    req.send();
    req.onreadystatechange = function() {
        if (req.readyState === 4 && req.status === 200) {
            var tracklist = JSON.parse(req.response);
            console.log(tracklist);
            tracklist.forEach(function(item) {
                var tracklistItem = document.createElement('div');
                tracklistItem.setAttribute('class', 'tracklistItem')
                tracklistItem.innerText = item.title;
                tracks.appendChild(tracklistItem);
            });
        }
    }
};

/*const audio = document.querySelector('audio')

function pausePlay(event) {
    switch (event.keyCode) {
        case 32:
            if (play) {
                audio.pause();
                play = false;
            } else {
                audio.play();
                play = true;
            }
            break;
        }
  return false;
}

window.addEventListener("keydown", onKeyDown, false);
</script>
*/
getPlaylists();
getTracklist();
