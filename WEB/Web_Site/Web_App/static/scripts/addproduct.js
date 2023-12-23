function addProduct() {
    // Получаем значения формы
    var productName = document.getElementById("productName").value;
    var productType = document.getElementById("productType").value;
    var productPrice = document.getElementById("productPrice").value;
    var productImage = document.getElementById("productImage").files[0];
    var productDescription = document.getElementById("productDescription").value;

    // Создаем уникальный идентификатор для товара
    var productId = "product_" + Date.now(); // Используем метку времени для простоты, можно использовать другой метод генерации

    // Создаем новый блок товара
    var productBlock = document.createElement("div");
    productBlock.className = "product-card-wrapper w-dyn-item";
    productBlock.setAttribute("role", "listitem");
    productBlock.id = productId; // Присваиваем уникальный идентификатор блоку

    // Создаем элементы для деталей продукта
    var aElement = document.createElement("a");
    aElement.href = "/product/" + productId; // Используем уникальный идентификатор в URL

    var productCard = document.createElement("div");
    productCard.className = "product-card w-inline-block";

    var imageWrapper = document.createElement("div");
    imageWrapper.className = "product-card-image-wrapper";

    var imageElement = document.createElement("img");
    // Обработка загрузки файлов различается, это всего лишь заполнитель
    imageElement.src = productImage ? URL.createObjectURL(productImage) : '';
    imageElement.alt = "";

    var headingElement = document.createElement("h6");
    headingElement.className = "product-card-heading";
    headingElement.textContent = productName;

    var priceElement = document.createElement("div");
    // Здесь может быть логика для установки цены
    priceElement.className = "product-card-price";
    priceElement.innerHTML = productPrice; // Пример, замените на свою логику

    // Собираем структуру элементов
    imageWrapper.appendChild(imageElement);
    aElement.appendChild(imageWrapper);
    aElement.appendChild(headingElement);
    aElement.appendChild(priceElement);
    productCard.appendChild(aElement);
    productBlock.appendChild(productCard);

    // Добавляем блок товара на страницу каталога
    var catalogElement = document.getElementById("catalog");
    if (catalogElement) {
        catalogElement.appendChild(productBlock);
    }
}