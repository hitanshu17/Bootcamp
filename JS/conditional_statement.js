// Syntax -> if (condition1) {
//     statements
// } else if(condition2){
//     statements
// } else(condition3){
//     statements
// }

let number1 = 10;
let number2 = 2;

let maxValue;
if(number1 > number2){
    maxValue = number1;
}else{
    maxValue = number2;
}
console.log(maxValue);

/* Switch */

let color = 'black';

switch (color){
    case 'black':
        console.log('This is black');
        break;
    case 'white':
        console.log('This is white');
        break;
    case 'red':
        console.log('This is red');
        break;
}

/* Ternary Operator */

// ? -> then
// : -> else

let max = number1 > number2 ? number1 :number2;
console.log(max);

/* ************** */
let num = 15;
if (num % 3 === 0 && num % 5 === 0){
    console.log('FizzBuzz');
} else if  (num % 3 === 0){
    console.log('Fizz');
} else if (num % 5 === 0){
    console.log('Buzz');
} else {
    console.log('Nothing');
}

console.log(num % 3 === 0 && num % 5 === 0 ? 'Fizzbuzz' : number % 3 == 0 ? 'Fizz' : number % 5 === 0  ? 'Buzz': 'Nothing' ); 

let number = -10

switch(true){
    case (number > 0):
    console.log('+ve Number');
    break;

    case number === 0:
    console.log('Zero Number');
    break;

    case number < 0:
    console.log("-ve Number");
    break;
}