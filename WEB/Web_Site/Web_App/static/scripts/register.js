// add class
function addClass(elem, classArr) {
    for (let i = 0; i < classArr.length; i++) {
        elem.classList.add(`${classArr[i]}`);
    }
}

// remove class
function removeClass(elem, classArr) {
    for (let i = 0; i < classArr.length; i++) {
        elem.classList.remove(`${classArr[i]}`);
    }
}

// get class name
function getClassName(elem, classPos) {
    let classString = elem.getAttribute('class');
    let className = classString.split(' ')[classPos];

    return className;
}


let popupShadow = document.querySelector('.popup-shadow');

let loginForm = document.querySelector('.login-wrapper');
let signupForm = document.querySelector('.signup-wrapper');

let signupToggleBtn = document.querySelector('#toggle-signup');
let loginToggleBtn = document.querySelector('#toggle-login');

let userBtn = document.querySelector('#login-or-signup');
let loginCloseBtn = document.querySelector('#login-close-btn');
let signupCloseBtn = document.querySelector('#signup-close-btn');

userBtn.onclick = () => {

    addClass(loginForm, ['animate__animated', 'animate__bounceInDown', 'active-ls']);

    setTimeout(() => {
        removeClass(loginForm, ['animate__animated', 'animate__bounceInDown']);
    }, 1200);

}

signupToggleBtn.onclick = () => {
    loginForm.classList.remove('active-ls');
    signupForm.classList.add('active-ls');
}

loginToggleBtn.onclick = () => {
    signupForm.classList.remove('active-ls');
    loginForm.classList.add('active-ls');
}

loginCloseBtn.onclick = () => {
    loginForm.classList.remove('active-ls');
}

signupCloseBtn.onclick = () => {
    signupForm.classList.remove('active-ls');
}