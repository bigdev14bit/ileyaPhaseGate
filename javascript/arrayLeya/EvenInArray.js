let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let addEven = []
let oddNumbers = []

for(let index = 0; index < array.length; index++) {
	if(array[index] % 2 == 0) {
		addEven.push(array[index])
	} else {
		oddNumbers.push(array[index])
	}
}

console.log("Even Numbers:",addEven);
console.log("Odd Numbers:",oddNumbers);
console.log("Both:",[addEven, oddNumbers]);
