const AVATAR_URL = 'https://eu.ui-avatars.com/api/?name='

const createUserCardElement = (user) => {
	const {
		name,
		email,
		website
	} = user

	const userCard = document.createElement('div')
	//userCard.textContent = user.name
	userCard.className = 'user-card'

	const info = document.createElement('div')
	info.className = 'user-info'

	const userName = document.createElement('h4')
	userName.textContent = name


	const userEmail = document.createElement('div')
	userEmail.textContent = `Email: ${email}, website: ${website}`

	const userAvatar = document.createElement('img')
	userAvatar.src = AVATAR_URL + user.name

	userCard.appendChild(userAvatar)
	userCard.appendChild(info)
	info.appendChild(userName)
	info.appendChild(userEmail)
	//img.after(info)

	return userCard

}

const createUserCard = (user) => {
	const userCard = createUserCardElement(user)

	userListElem.appendChild(userCard)

}

const showUsers = (users) => {
	/*const newTag = document.createElement('div');
	newTag.textContent = 'Im create'

	document.body.appendChild(newTag)*/

	users.forEach(createUserCard)
}