document.addEventListener('DOMContentLoaded', function() {
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

var orders = JSON.parse(localStorage.getItem('.order'));
var total = localStorage.getItem('total');

if (orders === null || orders === undefined) {
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if (total === null || total === undefined) {
    localStorage.setItem('total', JSON.stringify([]));
    total = localStorage.getItem('total');
}

var cart = document.querySelector('#cart');
cart.innerHTML = orders.length;

var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

function addProduct(pid) {
    pcart.innerHTML += 'new product'
}
});