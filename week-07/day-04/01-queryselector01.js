/*1. store the element that says 'The King' in the 'king' variable.
console.log it.
2. store the element that contains the text 'The Conceited Man'
in the 'conceited' variable.
show the result in an 'alert' window.
3. store 'The Businessman' and 'The Lamplighter'
in the 'businessLamp' variable.
console.log each of them.
4. store 'The King' and 'The Conceited Man'
in the 'conceitedKing' variable.
alert them one by one.
5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
in the 'noBusiness' variable.
console.log each of them.
6. store 'The Businessman' in the 'allBizniss' variable.
show the result in an 'alert' window.*/

var king = document.querySelector('#b325');
console.log(king.innerText);

var conceited  = document.querySelectorAll('.asteroid')[1];
alert(conceited.innerText);

var businessLamp = document.querySelectorAll('.big');
console.log(businessLamp[0].innerText, businessLamp[1].innerText);
