//Task 2.1

let someText = 'Backend is glass Away Still Something'

function fistLetter(arrText) {

	let letters = [];
	let TextArr = arrText.split(' ')

	TextArr.forEach((element) => 
		letters.push(element[0])
	)
	console.log(letters)
	return letters.join('')

}

console.log(fistLetter(someText))



// Task 2.2

let number = +(prompt('Put number'));

function isNumber(x) {
	if (isNaN(x)) {
		alert('Invalid data type');
	} else {
		const today = new Date();
		const todayData = today.toLocaleString('en-GB').replaceAll('/', '.');
		/*const data1 = 'd.m.y, h:m:s';
		  .replace('d', today.getDate())
		  .replace('m', today.getMonth()+1)
		  .replace('y', today.getFullYear())

		  .replace('h', today.getHours())
		  .replace('m', today.getMinutes())
		  .replace('s', today.getSeconds());*/

		alert(todayData);
	}
}

isNumber(number)



//Task 3.1

function printMyself () {
    console.log(arguments);
	console.log(arguments.callee);
}
printMyself(10, false, "google")



//Task 3.2

function userInfo () {
	if (this.registered) {
		console.log('Registration date: ' + this.data)
	} else {
		console.log('Unregistered user: ' + this.name)
	}
}

let user1 = {
	name : 'Olha',
	registered : true,
	data: '24.01.2021',
	getInfo: userInfo,
}

let user2 = {
	name : 'Lola',
	registered : false,
	data: '00.00.0000',
	getInfo: userInfo,
}

user1.getInfo()
user2.getInfo()



//Task 3.3

let users = {
    14587: {
            name: "Ivan",
            email: "ivan78@gmail.com"
    },
    28419: {
            name: "Georg",
            email: "georg.klep@gmail.com"
    },
    41457: {
            name: "Stephan",
            email: "stephan.borg@gmail.com"
    }
}

let posts = {
    7891451: {
            author: 14587,
            text: "Imagine we can encapsulate these secondary responsibilities in functions"
    },
    7891452: {
            author: 28419,
            text: `В конструкторе ключевое слово super используется как функция, вызывающая родительский конструктор. 
                    Её необходимо вызвать до первого обращения к ключевому слову this в теле конструктора. 
                    Ключевое слово super также может быть использовано для вызова функций родительского объекта`
    },
    7891453: {
            author: 28419,
            text: `DOM не обрабатывает или не вынуждает проверять пространство имен как таковое. 
                    Префикс пространства имен, когда он связан с конкретным узлом, не может быть изменен`
    },
    7891454: {
            author: 14587,
            text: "Ключевое слово super используется для вызова функций, принадлежащих родителю объекта"
    }
}


let comments = {
    91078454: {
            postId: 7891451,
            author: 28419,
            text: `The static String.fromCharCode() method returns a string created 
                    from the specified sequence of UTF-16 code units`
    },
    91078455: {
            postId: 7891451,
            author: 41457,
            text: `HTML элемент <template> — это механизм для отложенного рендера клиентского контента, 
                    который не отображается во время загрузки, но может быть инициализирован при помощи JavaScript`
    },
    91078457: {
            postId: 7891452,
            author: 41457,
            text: "Глобальный объект String является конструктором строк, или, последовательностей символов"
    },
    91078458: {
            postId: 7891452,
            author: 14587,
            text: `The Element.namespaceURI read-only property returns the namespace URI of the element, 
                    or null if the element is not in a namespace`
    }
}


function getCurrentPostComments ( postId ) {
    let res = []
    for (key in comments) {
        if (comments[key]['postId'] === postId) {
            let item = comments[key]
            res.push({
                text: item.text,
                author: users[item.author]['name']
            })
        }
    }

    return res
}

console.log ( getCurrentPostComments ( 7891451 ) )