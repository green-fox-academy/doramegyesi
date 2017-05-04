/* replace the list items' content with items from this list:
   ['apple', 'banana', 'cat', 'dog'] */

var list = document.querySelectorAll('li');
var newList = ['apple', 'banana', 'cat', 'dog'];

for (var e = 0; e < list.length; e++) {
    list[e].textContent = newList[e];
};
