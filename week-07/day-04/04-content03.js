/*  fill output1 with the first paragraph's content, text only.
  fill output2 with the first paragraph's content keeping the cat strong.*/

var firstPar = document.querySelector('p');

var firstOutput = document.querySelector('.output1');
firstOutput.textContent = firstPar.textContent;

var secondOutput = document.querySelector('.output2');
secondOutput.innerHTML = firstPar.innerHTML;
