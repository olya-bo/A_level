function testUserText ( userText ) {
      // variant 1
      // замеяем символ открытия тега на символ < который выглядит так же
      return userText.split("<").join("&lt")
}
function insertUserText ( userText ) {
      var x = document.createElement ( 'div' )
      // variant 2
      // Вносим контент в div как текст а не html
      x.innerText = testUserText ( userText )
      document.body.appendChild ( x )
}

insertUserText (`<svg/onload='document.write("Looser");
                  document.body.style.backgroundColor="black";
                  document.body.style.color="red";
                  document.body.style.fontSize="50px";
                  document.body.style.fontWeight="bold";
                  document.body.style.textAlign="center";
                  document.body.style.paddingTop="45%";'>`)
