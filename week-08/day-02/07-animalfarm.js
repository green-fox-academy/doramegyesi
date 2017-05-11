/* Create an Animal constructor
Every animal has a hunger value, which is a number
Every animal has a thirst value, which is a number
when creating a new animal object these values are created with the default 50 value
Every animal can eat() which decreases their hunger by one
Every animal can drink() which decreases their thirst by one
Every animal can play() which increases both by one

1Create a Farm constructor
Every farm has list of Animals
Every farm has slots which defines the number of free places for animals
Every farm can breed() which creates a new animal if there's place for it
Every farm can slaughter() which removes the least hungry animal*/

function animal(hunger, thirst) {
    this.hunger = 50;
    this.thirst = 50;
    this.eating = eat;
    this.drinking = drink;
    this.playing = play;
};

function eat() {
    this.hunger--;
};

function drink() {
    this.thirst--;
};

function play() {
    this.hunger++;
    this.thirst++;
};

var sloth = new animal();

sloth.eating();
console.log(sloth.hunger);

function farm() {
    this.listOfAnimals = [];
    this.slots = 21;
    this.breeding = breed;
    this.slaughtering = slaughter;
};

function breed() {
    if (this.slots > 0) {
        var newAnimal = new animal;
        this.listOfAnimals.push(newAnimal);
        this.slots--;
    }
};

function slaughter() {
    this.listOfAnimals.sort(function (a, b) {
        a.hunger - b.hunger;
    });
    this.listOfAnimals.shift();
};

var southforkRanch = new farm();

southforkRanch.breeding();
southforkRanch.breeding();
southforkRanch.breeding();
console.log(southforkRanch.listOfAnimals);
console.log(southforkRanch.slots);
southforkRanch.slaughtering();
console.log(southforkRanch.listOfAnimals);
