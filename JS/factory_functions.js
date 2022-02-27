
// const user1 = {
//     name: 'ARIYAN',
//     age: 40,
//     walk : function(){
//         console.log('oo bhai');
//     }
// }

// console.log(user1);


// const user2 = {
//     name: 'kazi',
//     age: 30,
//     walk : function(){
//         console.log('oo bhai2');
//     }
// }

// console.log(user2);

// function user(name,age){
//     const userObje ={
//         name,
//         age,
//         walk : function(){
//             console.log('oo bhai');
//         }
//     };
//     return userObje;
// }

// const user1 = user('ariyan',20);
// const user2 = user('kazi',21);

// console.log(user1,user2);

//constructor functions

// function user(name,age){
//     console.log(this);
//     this.name = name;
//     this.age = age;
//     this.walk = function(){
//         console.log('oo bhai');
//     };
// }

// const user1 = new user('Ariyan',30);
// console.log(user1);

// Creating object using factory and constructor functions

const homeAddress1= {
    street : 'A',
    city : 'B',
    zipCode : 'C',
}

console.log(homeAddress1);

function homeAddress(street,city,zipCode) {
    return {
        street,
        city,
        zipCode,
    };
}

function homeAddress2(street,city,zipCode) {
        this.street = street;
        this.coty = city;
        this.zipCode = zipCode;
}

const homeAddress3 = new homeAddress2('x','y','z')


console.log(homeAddress('a','b','c'));
console.log(homeAddress3);
