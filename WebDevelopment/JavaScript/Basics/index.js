// to print in console

// console.log(`Hello world`); 
// console.log('I like Data science!')

// to give a alert to user

// window.alert(`This is an alert`);

// single line comments
/* multiple line comments
this 
is 
a 
comments
*/

// document.getElementById("myh1").textContent = `Hello`;
// document.getElementById("myp").textContent = `I like Data science`;

// // variables 
// let age = 22;
// let price = 10.99;
// let gpa = 6.1;
// let firstname = "Anoop";

// // checking the type of variable
// console.log(typeof(age));
// console.log(typeof(price));
// console.log(typeof(gpa));

// console.log(`You are ${age} years old`);
// console.log(`The price is: $${price}`);
// console.log(`My GPA is: ${gpa}`);
// console.log(`My name is: ${firstname}`);

// Accept user input

// 1. Easy way
// let username;
// username = window.prompt(`What is your username: `)
// console.log(username)

// 2 using text box
// let username;
// document.getElementById("btn").onclick = function(){
//     username = document.getElementById("mytext").value;
//     document.getElementById("h1").textContent = `Hello ${username}`
// }

// type conversion
// age = "1"
// console.log(typeof age)

// converted_age = Number(age)
// console.log(typeof converted_age)

// Const - A variable that cant be changed "Constant"
// const pi = 3.14159
// let radius;
// let circumference;

// // radius = window.prompt(`Radius Of a Circle: `)
// // radius = Number(radius) 

// circumference = 2 * pi * radius
// // console.log(circumference)

// document.getElementById('btn').onclick = function(){
//     radius = document.getElementById("radius").value;
//     radius = Number(radius);
//     circumference = 2 * pi * radius;
//     document.getElementById("result").textContent = circumference + 'cm';
// }

// console.log(Math.PI);
// let a = 2.34;
// console.log(a)
// b = Math.round(a)
// console.log(b)
// b = Math.floor(a)
// console.log(b)
// b = Math.ceil(a)
// console.log(b)
// b = Math.trunc(a)
// console.log(b)
// b = Math.pow(a)
// console.log(b)
// b = Math.sqrt(a)
// console.log(b)
// b = Math.log(a)
// console.log(b)
// b = Math.sin(a)
// console.log(b)
// b = Math.cos(a)
// console.log(b)
// b = Math.tan(a)
// console.log(b)
// b = Math.abs(a)
// console.log(b)
// b = Math.sign(a)
// console.log(b)
// b = Math.max(a)
// console.log(b)
// b = Math.min(a)
// console.log(b)

// random number
// let randumNumber = Math.floor(Math.random() * 100) + 1;
// console.log(randumNumber)

// to make sure checkbox checked use .checked

// ternary operator - used it like if condition but when there is less option
// let age = 19;
// let message = age > 20 ? "You are an adult" : "you are not an adult";
// console.log(message)

// switch statements - can be efficient replcaement for if

// string methods
//indexof
// length
// trim()
// toUppercase()
// toLowercase()
// repeat()
// startswith()
// endswith()
// includes()
// replceAll()
// padStart()
// padEnd()

// slice
// const fullname = 'Anoop George'
// let firstname = fullname.slice(0, 5)
// console.log(firstname)