
// syntax error ->
// reference error ->

// type error ->

// let country = true;
// console.log(country.toUpperCase());

// let pi = 3.1416942;
// console.log(pi.toFixed(2));

//custom error

// function div(a,b){
//     if(b === 0){
//         // throw 'kya kar raha hai tu';
//         throw new SyntaxError('kya kar raha hai tu');
//     }
//     return a/b;
// }

// console.log(div(4,0));

// try catch finally

function div(a,b){
    if(b === 0){
        throw new SyntaxError('kya kar raha hai bhai tu');
    }
    return a/b;
}

try { console.log(div(4,0)); }
catch(e) { console.log(e.name);  
console.log(e.message); }  
finally { console.log('Its working')}