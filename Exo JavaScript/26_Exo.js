const numbers = [1, 2, 3, 4, 5];
const squareNumbers = numbers.map(num => num * num);
console.log(squareNumbers);
const squareNumbers3 = numbers.forEach((num) => {console.log(num * num)});
// const squareNumbers2 = numbers.forEach(function(num) {console.log(num * num)});