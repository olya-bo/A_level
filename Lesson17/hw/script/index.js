//Task 1
let number = parseInt(prompt('Put number'));
while (isNaN(number)) {
	alert("It's not number");
	number = parseInt(prompt('Put number'));
}

function is_positive (x) {
	if (x >= 0) {
		alert(x + " - it's positive number");
	} else {
		alert(x + " - it's  negative number");
	}
}

is_positive(number);


//Task 2
let x = 0;
let sum = 0;
let i = 0;

for (i; i < 10; i++) {
	x += 5;
	sum += x;
}

alert("Sum first 10 numbers multiples of 5 = " + sum)

//Task 3
let len_array = parseInt(prompt('Put len array'));
let y = 0;
let numbers_array = [];
let big_numbers = []

for (y; y < len_array; y++) {
	numbers_array.push(parseInt(prompt('Put number')));
}

for (i = 0; i < numbers_array.length; i++) {
	const item = numbers_array[i];
	if (item > 50) {
		big_numbers.push(item)
	}
}

if (big_numbers.length > 0) {
	alert("Numbers greater than 50: " + big_numbers)
} else {alert("No numbers greater than 50")}