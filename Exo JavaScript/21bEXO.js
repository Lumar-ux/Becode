//21b.exercice

// const dice = (faces, times) => {
//   for (let i = 1; i <= times; i++) {
//     console.log(`Die ${i}: ${Math.floor(Math.random() * faces + 1)}`);
//   }
// };
// dice(6, 5);

// const repeat = (el,times) => {
//     let fel = "";
//     for (let i = 0; i < times; i++){
//         fel = fel + el;
//     }
//     return(fel)
// }
// console.log(repeat("$",5));

// const greet=(firstName,lastName)=>{
//     console.log(`This is ${firstName} ${lastName[0]}`)
// }
// greet("Marlon", "Brandon");

// const sum = (nb1,nb2)=>{
//     return (nb1+nb2)
// }
// const myVariable = sum(3, 6);
// console.log(myVariable);

// const isShortWeather = temp=>{
//     if(temp>=24){
//         return (console.log(true));
//     }else{
//         return (console.log(false));
//     }
// }
// isShortWeather(13); // false
// isShortWeather(27); // true
// isShortWeather(-7); // false

// const capitalize=str=>{
//     return(console.log(str[0].toUpperCase()+str.slice(1)))
// }
// capitalize("eggplant"); // "Eggplant"
// capitalize("pamplemousse"); // "Pamplemousse"
// capitalize("squid"); //"Squid"

// const sumArray=ar=>{
//     let som=0;
//     for (let el of ar){
//         som += el;
//     }
//     return (console.log(som));
// }
// sumArray([1, 2, 3]); // 6
// sumArray([2, 2, 2, 2]); // 8
// sumArray([50, 50, 1]); // 101

// const returnDay=dy=>{
//     const day=[null,"Monday", "Thuseday","Wednesday","Thursday","Friday","Saturday","Sunday"]
//     return(console.log(day[dy]))
// }
// returnDay(1); // "Monday"
// returnDay(7); // "Sunday"
// returnDay(4); // "Thursday"
// returnDay(0); // null