'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function createRactangles(a, b) {
    this.getArea = function() {
        return a*b;
    }
    this.getCircumference = function() {
        return 2*(a+b);
    }
};

var rectOne = new createRactangles(8, 7);

console.log(rectOne.getArea());
