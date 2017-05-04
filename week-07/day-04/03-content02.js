//  fill every paragraph with the last one's content.

var allPar = document.querySelectorAll('p');
allPar.forEach(function(element) {
    element.textContent = allPar[3].textContent;
});
