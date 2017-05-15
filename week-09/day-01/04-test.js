var test = require('tape');
var compare = require('./04-anagram.js');

test('compare words', function(t) {
  t.equal(compare('life', 'file'), true);
  t.end();
});

test('compare words', function(t) {
  t.equal(compare('sloth', 'cockroach'), false);
  t.end();
});
