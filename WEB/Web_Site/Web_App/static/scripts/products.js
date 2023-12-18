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


function addProduct() {
    // Получаем данные из формы
    const productName = document.getElementById('productName').value;
    const productType = document.getElementById('productType').value;
    const productImage = document.getElementById('productImage').files[0];
    const productDescription = document.getElementById('productDescription').value;

    // Создаем объект FormData для передачи данных на сервер
    const formData = new FormData();
    formData.append('productName', productName);
    formData.append('productType', productType);
    formData.append('productImage', productImage);
    formData.append('productDescription', productDescription);

    // Отправляем данные на сервер (здесь нужно использовать AJAX или другие методы)
    // Например, с использованием Fetch API или jQuery AJAX

    // Пример с использованием Fetch API (необходимо заменить URL на ваш)
    fetch('http://127.0.0.1:1113/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Обработка ответа от сервера (например, вывод сообщения об успешном добавлении)
        console.log(data);
        alert('Товар успешно добавлен!');
    })
    .catch(error => {
        // Обработка ошибок
        console.error('Ошибка при добавлении товара:', error);
        alert('Произошла ошибка. Попробуйте еще раз.');
    });
}