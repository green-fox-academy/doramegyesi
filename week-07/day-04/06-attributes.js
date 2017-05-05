/*  1. Write the image's url to the console.
    2. Replace the image with a picture of yourself.
    3. Make the link point to the Green Fox Academy website.
    4. Disable the second button.
    5. Replace its text with 'Don't click me!'.*/

var imageUrl = document.querySelector('img');
console.log(imageUrl.getAttribute('src'));

imageUrl.setAttribute('src', 'https://scontent.fomr1-1.fna.fbcdn.net/v/t1.0-9/15541895_10154168034141334_5810053630532113183_n.jpg?oh=2329b0f27e54f4980a184effc5ee8597&oe=59887543');

imageUrl.style.height = 305 + 'px';
imageUrl.style.width = 400 + 'px';

var bestWebsite = document.querySelector('a');
bestWebsite.setAttribute('href', 'https://www.greenfoxacademy.com/');
