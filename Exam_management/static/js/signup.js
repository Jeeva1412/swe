
function validateForm() {
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("password2").value;

    if (username.trim() == "") {
        alert("Please enter a username");
        return false;
    }

    if (email.trim() == "") {
        alert("Please enter an email");
        return false;
    } else if (!isValidEmail(email)) {
        alert("Please enter a valid email");
        return false;
    }

    if (password.trim() == "") {
        alert("Please enter a password");
        return false;
    }
    if (password.trim().length < 6){
      alert("password enter more than 8 character");
      return false;
    } 

    return true;
}

function isValidEmail(email) {
    // Simple email validation regex
    var emailRegex = /^\S+@\S+\.\S+$/;
    return emailRegex.test(email);
}
