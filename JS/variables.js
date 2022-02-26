
// var name = 'Hitanshu';
// console.log(name);

let price = 250;
const name = 'Hitanshu'; //const value cannot be changed while variable declared using 'var' variable value can be updated again and again
console.log(price,name);

let age = 45;
console.log(typeof age); //typeof helps you know data type of the variable

let isMarried = false;
console.log(typeof isMarried);

let colors = undefined;
console.log(typeof colors);

let selectColor = null;
console.log(typeof selectColor);

let user = {
    name : 'Hitanshu',
    age : 30,
    hobby : 'reading',
};  

console.log(user);
console.log(user.name);
console.log(user['name']);

//prototype is an object that is associated with every functions and objects by default in JavaScript, where function's prototype property is accessible and modifiable and object's prototype property (aka attribute) is not visible. Every function includes prototype object by default.

let friends = ['abc','def','xyz'];
console.log(friends);
console.log(friends[0]);
console.log(friends.length); //indicates how many arguments the array/function has/expects

function showMyName(){
    console.log('My name is Hitanshu');
}

showMyName();

function showMyName2(name){  //with name as parameter
    console.log('My name is',name);
    console.log(`My name is ${name}`);
}

showMyName2('ABC');

function CalSum(num1,num2){
    const sum = num1 + num2;
    return sum;
}

const result =  CalSum(20,30);
console.log(result);

console.log(`${10+10}`);

 
