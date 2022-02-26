//increment
for (let index = 1; index <= 4; index++){
    console.log('Test1',index)
}

//decrement
for (let index = 5; index >= 1; index--){
    console.log('Test2',index)
}

/* While loop*/
let index = 1;
while(index <= 5){
    console.log('Test3',index);
    index++
}

/* Do while */

let index2 = 1;
do{
    console.log('Test4',index2);
    index2++;
} while(index2 <=5);

//Note:-> while loop lets you iterate the code block as long as the specified condition is true. In the do-while loop, the condition is checked after executing the loop. So, even if the condition is true or false, the code block will be executed for at least one time.

/* For in loop */

const objs = {
    name: 'ABC',
    age: 30,
}

for (let key in objs){
    console.log(key, objs[key]);
}

/* For of loop*/

let number = [1,2,3,4,5];

for(let index in number) { //will get property data
    console.log(index);
}

for (let num of number){ //to get value directly or property related data
    console.log(num);
}

/* Nested Loop */

for (let i = 1; i<= 3; i++){
    for (let j = 1; j<=3;j++){
        console.log('J',j);
    }
    console.log('i',i);
}