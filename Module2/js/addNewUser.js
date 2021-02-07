function createFormField(config) {
	const { 
		name,
		text,
		placeholder
	} = config

	const label = document.createElement('div')
	label.textContent = text;
	label.className = 'label'

	const input = document.createElement('input')
	input.name = name;
	input.placeholder = placeholder;

	const wrapper = document.createElement('div')
	wrapper.className = 'form-field'

	wrapper.appendChild(label)
	wrapper.appendChild(input)

	return wrapper
}

const FORM_CONFIG = [ 
	{
		name:'name',
		text:'Name',
		placeholder: 'Enter your name',
	},
	{
		name:'email',
		text:'Email',
		placeholder: 'Enter your email',
	},
	{
		name:'website',
		text:'Website',
		placeholder: 'Enter your website',
	},
]

const BUTTON_CONFIG = [
	{
		type: 'button',
		text: 'Cancel',
		color: 'danger',
	},
	{
		type: 'submit',
		text: 'Save',
		color: 'success',
	},
]

function createButton(config) {
	const { 
		type,
		text,
		color
	} = config

	const button = document.createElement('button')
	button.type = type
	button.textContent = text
	button.className = `button-${color}`

	return button
}

function onSubmit(event) {
	event.preventDefault()

	/*const{
		target: {
			elements
		}
	} = event*/

	const errorMessageOnPage = document.querySelector('form span')
	if (errorMessageOnPage) {
		errorMessageOnPage.remove()
	}

	const form = event.target
	// const form = document.querySelector('.user-add-form')

	const elements = form.elements

	const newUser = {
		name: elements.name.value,
		email:elements.email.value,
		website: elements.website.value,
		id: Math.random(),
	}

	if (newUser.name.length < 4 || newUser.email.length < 4 || newUser.website.length < 4) {
		const errorMessage = document.createElement('span')

		errorMessage.textContent = 'Error! Length should be more than 3.'
		errorMessage.style = "color: red;"

		form.insertBefore(errorMessage, form.firstChild)

	} else {

		const userCard = createUserCardElement(newUser)

		userCard.style = 'border: 5px solid lightgreen;'
		setTimeout(function () {
	        userCard.style = ''
	    }, 5000);

		form.after(userCard)

		form.remove()
	}
}

function onButtonClick(event) {
	if (!document.querySelector('.user-add-form')) {
		const form = document.createElement('form')

		form.className = 'user-add-form'

		FORM_CONFIG.forEach(config => {
			const formField = createFormField(config)

			form.appendChild(formField)
		})

		const addUserButton = event.currentTarget

		const buttonsWrapper = document.createElement('div')
		buttonsWrapper.className = 'buttons-wrepper'

		BUTTON_CONFIG.forEach(config => {
			const button = createButton(config)

			if (config.type === 'button') {
				button.onclick = () => {
					form.remove()
				}
			}

			buttonsWrapper.appendChild(button)
		})

		form.appendChild(buttonsWrapper)

		form.onsubmit = onSubmit

		addUserButton.after(form)
	}
}

function addNewUserButtonHandler () {
	const buttonElement = document.getElementById('add-new-user');

	

	buttonElement.onclick = onButtonClick;
}

