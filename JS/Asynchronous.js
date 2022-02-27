// Asynchornous Programming

// setTimeout(function(){
//     console.log('Hello World');
// }, 2000); //2000milisecond -> 2sec

// function fetchUser(){
//     setTimeout(function(){
//         //console.log('Hello World');
//         return {
//             name: 'Ariyan',
//             age: 20,
//         }
//     }, 2000);
// }

// const user = fetchUser();
// console.log(user);

function fetechUser(userId,callback){
    setTimeout(function(){
        console.log('Hi Hello World');
        const fetechedUser = {
            id: userId,
            name: 'kazi',
            email: 'kazi@gmail.com',
        }
        callback(fetechedUser);
    },2000);
}

fetechUser(12345,function(user){
    console.log(user);
})