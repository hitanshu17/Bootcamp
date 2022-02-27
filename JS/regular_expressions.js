
const regExp = /ariyan/i; //i MAKES IT NOT CASE SENSITIVE

// console.log(regExp.test('Hi, i am Ariyan'));
// console.log(regExp.source);
// console.log(regExp.exec('hI hELLO aRIYAN'));

const str = 'Hi hello ariyan'
console.log(str.match(regExp)); //same as regExp.exec('hI hELLO aRIYAN')
console.log(str.search(regExp)); //display index
console.log(str.replace(regExp,'kazi'));