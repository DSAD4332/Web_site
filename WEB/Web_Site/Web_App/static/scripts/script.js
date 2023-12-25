/*
 * Copyright 2016 Small Batch, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
/* Web Font Loader v1.6.26 - (c) Adobe Systems, Google. License: Apache 2.0 */


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

document.addEventListener('DOMContentLoaded', function() {
let loginForm = document.querySelector('.login-wrapper');
let signupForm = document.querySelector('.signup-wrapper');

let signupToggleBtn = document.querySelector('#toggle-signup');
let loginToggleBtn = document.querySelector('#toggle-login');

let userBtn = document.querySelector('#signup-btn');
let loginCloseBtn = document.querySelector('#login-close-btn');
let signupCloseBtn = document.querySelector('#signup-close-btn');

let popupShadow = document.querySelector('.shadow')

userBtn.onclick = () => {
    signupForm.classList.remove('active-ls');
    popupShadow.style.opacity = "1";
    popupShadow.style.zIndex = "98";
    popupShadow.style.opacity = "1";
    popupShadow.style.zIndex = "98";

    addClass(loginForm, ['active-ls']);
    addClass(loginForm, ['active-ls']);

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
    popupShadow.style.opacity = "0";
    popupShadow.style.zIndex = "-1001";
    popupShadow.style.opacity = "0";
    popupShadow.style.zIndex = "-1001";
}

signupCloseBtn.onclick = () => {
    signupForm.classList.remove('active-ls');
    popupShadow.style.opacity = "0";
    popupShadow.style.zIndex = "-1001";
}

});
