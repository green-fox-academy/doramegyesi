/*1. Alert the content of the heading.
  2. Write the content of the first paragraph to the console.
  3. Alert the content of the second paragraph.
  4. Replace the heading's content with 'New content'.
  5. Replace the last paragraph's content with the first paragraph's content.*/

var heading = document.querySelector('title');
alert(heading.textContent);

var firstPar = document.querySelector('p');
console.log(firstPar.textContent);

var secondPar = document.querySelector('.other');
alert(secondPar.textContent);
