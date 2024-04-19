const user = {
  firstName: "John",
  lastName: "NewYork",
  age: 30,
  aYearHasPast: function () {
    this.age = this.age + 1;
  },
  printAge: function () {
    console.log(`${this.firstName} ${this.lastName} is ${this.age} years old`);
  },
};
user.aYearHasPast();
user.printAge();
