
// const numbers = [1,2,3,4,5,6,7,8];

//add in prefix
//numbers.unshift(9,10,11);

//add in postfix
//numbers.push(18,19,20);

//add in between [position,no of values to be deleted, value to be added]
//numbers.splice(7,0,16,17)

//removing elements

// numbers.shift(); //remove from front
// numbers.pop(); //remove from behind
// numbers.splice(2,3);

//console.log(numbers);

//searching elements

//console.log(numbers.includes(3));
// console.log(numbers.includes(3,6)); //starting searching from a particular index 
// console.log(numbers.indexOf(0));
// console.log(numbers.lastIndexOf(8));

//finding objects in array

// const doctors = [
//     {name: 'kazi', age: 17},
//     {name: 'Jack', age: 27},
//     {name: 'Ariyan', age:37},
// ]; 

// const result = doctors.find(function(doctor){ //declared a call back funtion then pass the parameter in this case doctor
//     //return doctor.name === 'kazi';
//     return doctor.age > 2;
// });

// console.log(result);

//ilterating in array

// const number  = [1,2,3,4,5,6]

// for (let index = 0; index < number.length; index++) {
//     console.log(index, number[index]);
// }

//or we can do this

// for (let num of number){
//     console.log(number)
// };

//or we can do this 

// number.forEach(function(num,index){
//     console.log(num,index);
// });

//Sorting and reversing

// const numbers = [5,8,1,2,3,9];

// console.log(numbers.sort());
// console.log(numbers.reverse());

// const doctors = [
//     {name: 'Jack', age: 27},
//     {name: 'kazi', age: 17},
//     {name: 'Ariyan', age:3},
//     {name: 'xyz', age:31},
//     {name: 'abc', age:1},
// ]; 

// doctors.sort(function(d1,d2){
//      if (d1.age > d2.age) return +1;
//      if (d1.age === d2.age) return 0;
//      if (d1.age < d2.age) return -1;
// }).reverse();
// console.log(doctors);

// every and some
// some = at least one element passes the test
// every = all elements pass the test

// const numbers = [6,8,-3,5,2,7,9];

// const data = numbers.every(function(num){
//     return num > 0;
// })

// console.log(data);

// const data2 = numbers.some(function(num){
//     return num > 0;
// })

// console.log(data2);

//COMBINE 2 array

// const num1 = [1,2,3];
// const num2 = [4,5,6,7];

// const num = num1.concat(num2);
// console.log(num)

// SPLICE

// const numbers = [1,2,3,4,5,6,7,8];
// const slideArray = numbers.slice(3,6);
// console.log(slideArray);

// Spread

// const numbers = [1,2,3,4,5,6,7,8];
// console.log(...numbers);

// combing 2 array using spread

// const num1 = [1,2,3];
// const num2 = [4,5,6,7];

// const num = [...num1,...num2];
// console.log(num)

// joining array using join method

// let num3 = [1,2,3,4];
// let joinArray = num3.join('');
// console.log(joinArray);

//Filtering an array

let numbers = [1,2,3,4,5,6];

let onlyOddNumbers = [];

for (let num of numbers){
    if(num % 2 == 1){
        onlyOddNumbers.push(num);
    }
}
console.log(onlyOddNumbers);

//or we can do this prebuild function hai ye waala

const onlyOddNumbers2 = numbers.filter(function(num){
    return num % 2 === 1;
})

console.log(onlyOddNumbers2);