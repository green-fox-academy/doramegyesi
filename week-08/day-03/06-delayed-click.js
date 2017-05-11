'use strict'

//Create a simple HTML document with one button. If the user clicks the button it should wait 2 seconds and it should show a text under the button: 2 seconds ellapsed

let bigButton = document.querySelector('button');
let textToShow = document.querySelector('p');

function showTextLater() {
    setTimeout(function() {
        actuallyShowText();
    }, 2000);
};

function actuallyShowText() {
    textToShow.innerText = '2 seconds elapsed';
};

bigButton.addEventListener('click', showTextLater);
