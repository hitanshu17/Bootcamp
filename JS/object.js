
let name = 'Hitanshu';
let age = 21;
let hobby = 'reading';

const user = {
    name : 'Hitanshu',
    age : 22,
    hobby : 'reading',
    selectColor : null,
    friends : ['abc','xyz'],
    calculateAge : function(){
        console.log(`Hitanshu age ${this.age}`)
    }
}; 

// user.calculateAge();

// console.log(user);

//add

// user.email = 'test@gmail.com';
// user['phone'] = '2342';
// console.log(user);

//update

// user.age = user.age +5;
// console.log(user);

//delete

// delete user.age;
// console.log(user);

// user.calculateAge();

//Traversing Object

// for (let key in user){
//     console.log(key,user[key]);
// }

//another way

// console.log(Object.keys(user));
// console.log(Object.values(user));

//object destructuring

// const {name,age,book} = user;
// console.log(user.book);

// Cloning an object

const user2 = {
    name: 'abc',
    age: 40,
};

const copiedUser = {};
// copiedUser.name = user2.name;
// copiedUser.age = user2.age;

// console.log(copiedUser);

// for (let key in user2){
//     console.log(key,user[key]);
//     copiedUser[key] = user[key];
// }

// console.log(copiedUser);

//json data

const user3 = {
    name: 'Hitanshu',
    age: 30,
}

//object data to json format
const jsonData = JSON.stringify(user3);
console.log(jsonData)

//json format to object data
console.log(JSON.parse(jsonData));