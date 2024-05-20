let list_todo= [];
console.log("- new to add a todo");
console.log("- list to see all the todos");
console.log("- delete to remove a specific todo");
console.log("- quit to exit de program");
let pick_cmd = prompt("what do you want to perform : ");
if (pick_cmd){
    while (!(pick_cmd.toLowerCase() === "quit")){
        let lower_cmd = pick_cmd.toLowerCase();
        if (lower_cmd === "new"){
            let todo_new = prompt("what is the todo : ")
            list_todo.push(todo_new);
            console.log(`${todo_new} has been to the list`)
        }
        let i=1;
        if (lower_cmd === "list"){
            console.log("********* TODO LIST *********")
            for (let prt_list of list_todo){
                console.log(`${i}. ${prt_list}`)
                i++;
            }
        }
        if (lower_cmd === "delete"){
            let todo_del = prompt("What is the number of the todo and delete the todo : ")
            list_todo.splice(todo_del)
        }
        pick_cmd = prompt("what do you want to perform : ");
    }
}
else{
    console.log("This is not a valid command")
}