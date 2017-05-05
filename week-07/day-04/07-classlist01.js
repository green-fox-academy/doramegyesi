/*  1. Does the third p have a cat class?
    If so, alert 'YEAH CAT!'
    2. If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
    3. If the first p has an 'apple' class, replace cat's content with 'dog'
    4. Make apple red
    5. Make balloon less balloon-like */

var classes = document.querySelectorAll('p');
alert('YEAH CAT!', classes[2].classList.contains('cat'));

if (classes[3].classList.contains('dolphin')) {
    classes[0].innerText = 'pear';
}

if (classes[0].classList.contains('apple')) {
    classes[2].innerText = 'dog';
}
