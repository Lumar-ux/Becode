const callTwice = function (func, times) {
  for (let i = 0; i < times; i++) {
    func();
  }
};
// Here, the callTwice function takes another function as a parameter and call it two times
const rollDie = function () {
  const roll = Math.floor(Math.random() * 6 + 1);
  console.log(roll);
};
callTwice(rollDie, 2);
