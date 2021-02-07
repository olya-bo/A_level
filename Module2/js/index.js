/*console.log(1)

setTimeout (
	function () {
		console.log(3)
	},
	2000
)*/

/*setInterval(
	) // постоянно через какое-то время обновляется

console.log(2) */


const URL = 'https://jsonplaceholder.typicode.com';

const usersURL = URL + '/users';

let users = [];

const getUsers = async () => {
	const getUsersReq = await fetch(usersURL);
	const data = await getUsersReq.json();

	users = data;

	/*getUsersReq.then(
		function (res) {
			res.json().then(
				function (parsedRes) {
					console.log(parsedRes)
				}
			)
		}
	)*/
}

const userListElem = document.getElementById('user-list');

const start = async () => {
	await getUsers();

	showUsers(users)
	addNewUserButtonHandler();

	/*const element = document.getElementById('test-id')
	const spanElements = document.getElementsByClassName('text')
	console.log(element)
	console.log(spanElements)*/

}

function getNumber() {
	let number = 0;

	return () => {
		return ++number;
	}
}

//замыкание. если number + 1 то будет 1,1
const newFunction = getNumber();
let newNumber = newFunction();
console.log(newNumber); //1
newNumber = newFunction();
console.log(newNumber);//2

start();