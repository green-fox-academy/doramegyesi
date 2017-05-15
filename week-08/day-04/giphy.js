'use strict';

/*Display gifs of a cute/funny topic using: https://github.com/0Giphy/GiphyAPI
Search/Find the images in the API
Display the list of the first 16 results's static thumbnail
If the user clicks on the thumbnail, display the animated GIF*/

let req = new XMLHttpRequest();
req.open('GET', 'http://api.giphy.com/v1/gifs/search?q=parks+and+recreation&api_key=dc6zaTOxFJmzC', true);
req.send();

req.onreadystatechange = function() {
    if (req.readyState === 4 && req.status === 200) {
        var listOfGifs = JSON.parse(req.response);
    }
    createThumbnails(listOfGifs.data);
};

let body = document.querySelector('body')
let createThumbnails = function(gifs) {
    for (let i = 0; i < 16; i++) {
        let oneGif = document.createElement('img');
        oneGif.setAttribute('src', gifs[i].images.downsized_still.url);
        oneGif.addEventListener('click', function() {
            oneGif.setAttribute('src', gifs[i].images.original.url);
        });
    body.appendChild(oneGif);
    }
};
