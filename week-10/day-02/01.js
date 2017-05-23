'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals(voice) {
    this.voice = voice;
    this.say = function() {
        console.log(this.voice);
    }
};

var sloth = new Animals('mmmpfhhm -.-');
sloth.say();

var cockroach = new Animals('destroy!');
cockroach.say();
