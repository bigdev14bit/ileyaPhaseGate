let myArray = [1, 1, 1, 1];

let reverse = [];

for(let index = myArray.length - 1; index > -1; index--) {
	reverse.push(myArray[index])
}

console.log("Original:",myArray);
console.log("Reverse:",reverse);

if(reverse === myArray) {
	console.log("True");
} else {
	console.log("False");
}
