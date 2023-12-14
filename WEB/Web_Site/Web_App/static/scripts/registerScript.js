// static/js/script.js

function registerUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match');
        return;
    }

    const xhr = new XMLHttpRequest();
    const url = '/register/';
    const data = JSON.stringify({ username, password });

    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert('Registration successful');
        } else if (xhr.readyState === 4 && xhr.status !== 200) {
            alert('Registration failed');
        }
    };

    xhr.send(data);
}
