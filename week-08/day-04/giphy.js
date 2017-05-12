'use strict';

/*Display gifs of a cute/funny topic using: https://github.com/0Giphy/GiphyAPI
Search/Find the images in the API
Display the list of the first 16 results's static thumbnail
If the user clicks on the thumbnail, display the animated GIF*/

let req = new XMLHttpRequest();
req.open('GET', 'http://api.giphy.com/v1/gifs/search?q=parks+and+recreation&api_key=dc6zaTOxFJmzC', true);
req.send();

console.log(req.onreadystatechange);
