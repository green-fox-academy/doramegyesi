var test = require('tape');
var fruit = require('./02-apples.js');

test('return apple', function(t) {
  var actual = new fruit('apple').getApple();
  var expected = 'apple';
  t.equal(actual, expected);
  t.end();
});
