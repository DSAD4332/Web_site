document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/products/')  // URL вашего API для получения товаров
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('products-container');
            data.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.innerHTML = `<h3>${product.name}</h3><p>${product.description}</p>`;
                container.appendChild(productDiv);
            });
        });
});

function addToCart(productId) {
    fetch('/api/cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Получение CSRF токена
        },
        body: JSON.stringify({product_id: productId})
    })
    .then(response => {
        if (response.ok) {
            alert('Товар добавлен в корзину!');
        }
    });
}