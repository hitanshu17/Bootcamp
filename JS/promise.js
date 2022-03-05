
//A Promise is a JavaScript object that links producing code and consuming code. A Promise will become a container for future value.
//  Eg:- if you order any food on any site to deliver it to your place that order record will be the promise and the food will be the value of that promise.

// setTimeout(function(){
//     console.log('Hi Ariyan');
// },3000);

const promise = new Promise(function(resolve,reject){
    setTimeout(() => {
        resolve(1);
        reject(new Error('Some error'));
    },2000);

});

console.log(promise);
