var test = require('tape');
var summarize = require('./03-sum.js');

test('sum the elements', function(t) {
  var actual = new summarize().sum([]);
  var expected = 0;
  t.equal(actual, expected);
  t.end();
});
