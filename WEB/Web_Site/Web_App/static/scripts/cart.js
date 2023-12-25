document.addEventListener('DOMContentLoaded', function() {
    console.log('Скрипт загружен, событие DOMContentLoaded сработало.');
    let productCard;
let productView;
let closeBtn = document.querySelector('#product-close-btn');

function cardSelector(cid) {
    console.log('Функция cardSelector выполнена для карты', cid);
    productCard = document.getElementById('card' + cid);
    productCard.onclick = () => {
        openView(cid);
        popupShadow.style.opacity = "1";
        popupShadow.style.zIndex = "98";
    };
}

function openView(vid) {
productView = document.getElementById('view' + vid);
productView.classList.add('active-lss');
}



closeBtn.onclick = () => {
productView.classList.remove('active-lss');
popupShadow.style.opacity = "0";
popupShadow.style.zIndex = "-1001";
}
var hours = 0;
var now = new Date().getTime(); // Corrected: Use new Date() to create a Date object
var stepTime = localStorage.getItem('stepTime');

if (stepTime == null) { // Corrected: Use null instead of NULL
localStorage.setItem('stepTime', now);
} else {
if (now - stepTime > hours * 60 * 60 * 1000) {
localStorage.clear();
localStorage.setItem('stepTime', now);
}
}

const carousel1 = document.querySelector('.w-dyn-items1');
const carousel2 = document.querySelector('.w-dyn-items2');

let currentPosition = 1;

carousel1.addEventListener('wheel', (event) => {
event.preventDefault();

currentPosition += (event.deltaY > 0) ? 1 : -1;

currentPosition = Math.min(Math.max(currentPosition, 1), 10);

carousel1.style.setProperty('--position', currentPosition);
});

carousel2.addEventListener('wheel', (event) => {
event.preventDefault();

currentPosition += (event.deltaY > 0) ? 1 : -1;

currentPosition = Math.min(Math.max(currentPosition, 1), 10);

carousel2.style.setProperty('--position', currentPosition);
});

var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');
var wrappercart = document.querySelector('.cart-wrapper');
var popupShadow = document.querySelector('.shadow');

cart.onclick = () => {
wrappercart.classList.add('active-lss');
popupShadow.style.opacity = "1";
popupShadow.style.zIndex = "98";
}

closeBtn.onclick = () => {
wrappercart.classList.remove('active-lss');
popupShadow.style.opacity = "0";
popupShadow.style.zIndex = "-1001";
}

function addProduct(pid) {
pcart.innerHTML += '<li>' + pid + '</li>';
}

});