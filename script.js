function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function saveData() {
    let email, password, passwordconfirm, username, age;
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;
    passwordconfirm = document.getElementById("password").value;
    username = document.getElementById("password").value;
    age = document.getElementById("password").value;
    console.log(email + password + passwordconfirm + username + age)
}

var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var character = document.getElementById("character");
var minlength = document.getElementById("minlength");
var maxlength = document.getElementById("maxlength");

myInput.onfocus = function() {
    document.getElementById("message").style.display = "block";
}

myInput.onblur = function() {
    document.getElementById("message").style.display = "none";
}

myInput.onkeyup = function() {
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
    }

    if (myInput.value.length >=8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("Valid");
        length.class.List.add("invalid");
    }
    
    if (myInput.value.length <=20) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }
} 
