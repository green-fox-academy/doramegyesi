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

// 2nd
// Call the refuel function on the ferrari object using the bind method, with 52 as a parameter

var ferrari = {
  type: "Ferrari",
  fuel: 0,
  consumption: 0.12,
  kms: 9000,
  ride: function (km) {
    this.kms += km;
    this.fuel -= km * this.consumption;
    return this.fuel;
  }
};

function refuel(liters) {
  this.fuel += liters
  return this.fuel
};

var refuelFerrari = refuel.bind(ferrari);
console.log(refuelFerrari(52));
