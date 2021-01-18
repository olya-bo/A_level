var x = 5;

let y = 26;

console.log(typeof y == 'number')

const z = 55;

console.log(y);

let name = 'Anton';

name = 99;

let lastName = null;

let isXEqualY = x == y;

console.log(isXEqualY);

console.log(name * x);

let a = b = c = 67;

let someString = '11' + 6

let array = [1, 2, 3, 4, 5, x, y, name, '2456 bla']

array.push(888)

let field 

let objectMainField = 'person-adress'

let person = {
	name: "Anton",
	age: 24,
	education: [
		{
			university: 'KNNN'
		},
		{
			university: 'dffd0',
		}
		],
		'person-adress': 'Kharkiv'

	}

console.log(person[objectMainField])

person.education[0].university = 'Sharaga'

let cars = [
	{ 
		name: 'BMW', 
		models: [
		{
			model: "X5",
			prise : 7777,
		},
		{
			model: "M3",
			prise : 666,
		}
		],
	},
	{
		name: 'Mersedes', 
		models: [
		{
			model: "600",
			prise : 1234,
		},
		{
			model: "ml 350",
			prise : 666,
		}
		]
	}
]

let age = 2021 - 1996
let namee = 'Olha'
let lastNamee = 'Bocharova'
let fullName = namee + ' ' + lastNamee

const firstPerson = {
	name: 'Oleg',
	age: 17,
}

const secondPerson = {
	name: 'Maria',
	age: 23,
}

if (firstPerson.age >= 18) {
	console.log('You can buy this alco')
} else {
	console.log('I will not sell you this alco')
}

if (secondPerson.age >= 18) {
	console.log('You can buy this alco')
} else {
	console.log('I will not sell you this alco')
}

if (firstPerson.age >= 18) {
	console.log('You can buy this alco')
} else if (firstPerson.name === 'Oleg'){
	console.error('You are so small')
} else {
	console.log('I will not sell you this alco')
}


const canISellAlco = (firstPerson.age >= 18)
 ? 'yes'
 : (firstPerson.name == 'Oleg'
 	? 'you are bad man'
 	: 'no')

const newX = ++x;

const anotherX = x++;

let group_list = [
	{
		name: 'Ihor',
		age: 45,
	},
	{
		name: 'Sasha',
		age: 23,
	},
	{
		name: 'Andrey',
		age: 30,
	},
]


for (let i =0; i < group_list.length; i ++) {
	const item = group_list[i]

	if (item.age < 28){
	 continue;
	}

	console.log(item.name)

	if (item.age == 30) break;
}