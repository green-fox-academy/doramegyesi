var test = require('tape');
var summarize = require('./03-sum.js');

test('sum the elements', function(t) {
  var actual = new summarize().sum([1, 2, 3]);
  var expected = 6;
  t.equal(actual, expected);
  t.end();
});

test('sum an empty array', function(t) {
  var actual = new summarize().sum([]);
  var expected = 0;
  t.equal(actual, expected);
  t.end();
});

test('sum one element', function(t) {
  var actual = new summarize().sum([5]);
  var expected = 5;
  t.equal(actual, expected);
  t.end();
});
