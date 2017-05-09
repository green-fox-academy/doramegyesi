'use strict';
// 1st
// Call the ride method of the volvo, with 42 as a parameter

var volvo = {
  type: "Volvo",
  fuel: 23,
  consumption: 0.06,
  kms: 43000,
  ride: function (km) {
    this.kms += km;
    this.fuel -= km * this.consumption;
    return this.fuel;
}
};


console.log(volvo.ride(42));
