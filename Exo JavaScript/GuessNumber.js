let max_num = prompt("Choose your max Number : ");
const regex = /^\d+$/;
while (!regex.test(max_num)){
    max_num = prompt("Choose your max Number : ");
}
const random_number=()=>{
    const ran_num = Math.floor(Math.random(1)*max_num);
    return (ran_num);
}
let ran_num = random_number();
console.log("Test : The number to guess is " + ran_num);
let guess_number = ran_num=>{
    let guessnum = prompt("Guess the right number : ");
    let n=1;
    while (!regex.test(guessnum)){
        guessnum = prompt("Guess the right number : ");
    }
    while (!(Number(guessnum)===ran_num)){
        n++;
        if (Number(guessnum)>ran_num){
            guessnum = prompt("Your Guess Number should be lower : ");
        }
        else if (Number(guessnum<ran_num)){
            guessnum = prompt("Your Guess Number should be higher : ");
        }
    }
    if (Number(guessnum)===ran_num);
        console.log(`You find it! with ${n} attemps`);
}
guess_number(ran_num)