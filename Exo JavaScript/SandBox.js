// let ls1 = [2, 4, 3];
// let ls2 = [5, 6, 4];
// var addTwoNumbers = (l1, l2)=> {
//   let revl1 = l1.reverse().join("");
//   let revl2 = l2.reverse().join("");
//   let sum = Number(revl1) + Number(revl2);
//   let final_sum = String(sum).split("").reverse().map(Number);
//   return (final_sum);
// };
// console.log(addTwoNumbers(ls1, ls2));

// const users = [
//   {
//     firstName: "Vito",
//     lastName: "Corleone",
//   },
//   {
//     firstName: "William",
//     lastName: "Wallace",
//   },
//   {
//     firstName: "Harry",
//     lastName: "Potter",
//   },
//   {
//     firstName: "Amadeus",
//     lastName: "Mozart",
//   },
//   {
//     firstName: "Barack",
//     lastName: "Obama",
//   },
// ];
// for (i=1;i<=users.length;i++){
//   console.log(`${i}. My full name is ${users[i-1].firstName} ${users[i-1].lastName}`);
// }
// try {
//     console.log("hello");
//   } catch {
//     console.log("The above code didn't work");
//   }

//   console.log("End of program");

// const todos = [
//     {
//     id:1,
//     text: "take out trash",
//     isCompleted:true
// },
// {
//     id:2,
//     "text": "Meeting with boss",
//     isCompleted:true
// },
// {
//     id:1,
//     text: "Dentist appt",
//     isCompleted:false
// },
// ];
// delete todos[1].text
// console.log(todos[1]);
// function DNAtoRNA(dna) {
//     for (let i=0;i<dna.length;i++)
//       if (dna[i]==="T"){
//         dna.replace("T","U");
//       }
//     return(dna);
//   }
//   console.log(DNAtoRNA("GCAT"));

// function removeExclamationMarks(s) {
//     let st1="";
//     for (let i=0;i<s.length;i++){
//       if (s[i]!=="!"){
//         st1+=s[i];
//     }
//   }
//   return (st1);
// }
// console.log(removeExclamationMarks("He!ll!oW!or!ld!"));

// function repeatStr (n, s) {
//     let f="";
//     for (let i=0;i<5;i++){
//       f = f + s;
//     }
//     return (f);
//   }
//   repeatStr(5,"re")

// const grow=x=>eval(x.join("*"))
//   console.log(grow([1,2,3,4]));

// function removeChar(str){
//     msg="";
//     if(str>2){
//       msg=str.slice(1,-1)
//     }
//     return (msg);
//   };
//   console.log(removeChar("Hello")) // ell

// function encode(str,n){
//   let char=[];
//   let val=0;
//   let j=0;
//   for(let i=0;i<str.length;i++){
//       val=str.charCodeAt(i)-"a".charCodeAt(0)+1;
//       char.push(val);
//       let enc = Array.from(String(n),Number)
//       if(i % String(n).length===0){
//         j = 0;
//       }
//       char[i]+=enc[j];
//       j++;
//   }
//   return (char);
// }
// console.log(encode("scout", 19399));

// function add(arr) {
//   let sum = [];
//   let current=0;
//   for (let i=1;i<arr.length;i++){
//     current=arr[i];
//     for (let j = i-1; j >= 0; j--){
//       current+=arr[j]
//     }
//     sum.push(current);
//   }
//   sum.unshift(arr[0])
//   return (sum)
// }
// function highAndLow(numbers){
//   const list_num=numbers.split(' ').map(Number);
//   let n1 = Math.max(...list_num);
//   let n2 = Math.min(...list_num);
//   return(`${n1} ${n2}`);
// }
// console.log(highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"));

function isIsogram(str){
  var i, j;
  str = str.toLowerCase();
  for(i = 0; i < str.length; ++i)
    for(j = i + 1; j < str.length; ++j)
      if(str[i] === str[j])
        return false;
  return true;
}
console.log(isIsogram("Dermatoglyphics"))
console.log(isIsogram("aba"))