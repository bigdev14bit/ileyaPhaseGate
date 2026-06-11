let myArray = [4, 7, 9, 10, 16, 18];
let perfectSquare = [];

function perfectSquare() {
	for(let numbers : myArray) {
		number = 0;

		while(number * number <= numbers) {
			if(number * number === numbers) {
				perfectSquare.push(numbers);
				break;
			}

			number = number + 1;
		}
	}
}

console.log(perfectSquare());
console.log("Original:",myArray);
console.log("Perfect square:",perfectSquare);
