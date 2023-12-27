
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



var cart = document.querySelector('#cart');
var total = localStorage.getItem('ptotal');
var orders = JSON.parse(localStorage.getItem('orders'));
var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');


var wrappercart = document.querySelector('.cart-wrapper');
let cartcloseBtn = document.querySelector('#cart-close-btn');
let popupShadow = document.querySelector('.shadow');
    
    cart.onclick = () => {
    wrappercart.classList.add('active-lss');
    popupShadow.style.opacity = "1";
    popupShadow.style.zIndex = "98";
    };
    
    cartcloseBtn.onclick = () => {
    wrappercart.classList.remove('active-lss');
    popupShadow.style.opacity = "0";
    popupShadow.style.zIndex = "-1001";
    };

var cartsize = orders.length;

if (orders === null || orders === undefined) {
    localStorage.setItem('orders', JSON.stringify([]));
}

if (total === null || total === undefined) {
    localStorage.setItem('total', JSON.stringify([]));
}

orders[cartsize] = [name, size, price];
localStorage.setItem('orders', JSON.stringify([orders]));
localStorage.setItem('total', total);
total = Number(total) + Number(Productprice);
localStorage.setItem('total', total);
ptotal.innerHTML = 'Total:' + total + '$';