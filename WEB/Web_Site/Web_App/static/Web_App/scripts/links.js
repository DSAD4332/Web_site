var cssFiles = [
    "{% static 'styles/navbar/style.css' %}",
    "{% static 'styles/navbar/cursor.css' %}",
    "{% static 'styles/navbar/search.css' %}"
];

for (var i = 0; i < cssFiles.length; i++) {
    var link = document.createElement('link');
    link.href = cssFiles[i];
    link.type = 'text/css';
    link.rel = 'stylesheet';
    document.head.appendChild(link);
}