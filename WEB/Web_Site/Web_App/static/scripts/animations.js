function expandSearch() {
  const searchInput = document.querySelector('#search-input');

  searchInput.style.width = '500px';
  searchInput.style.opacity = '1';
  searchInput.focus();
  setTimeout(function () {
    const requests = [
      "А как какать?",
      "Мишк фреде верс спудимен",
      "бравл старс читы",
      "непон пон",
    ];
    
    let randomText = requests[Math.floor(Math.random() * requests.length)];

    searchInput.setAttribute('placeholder', randomText);

    let i = 0;
    let placeholder = "";

    function type() {
      const speed = 100;
    
      (i < randomText.length)
        placeholder += randomText.charAt(i);
        searchInput.setAttribute('placeholder', placeholder);
        i++;
    
        setTimeout(type, speed);
    }
    
    type();

  }, 1000);
}

let header = document.querySelector('.hat');
let searchblock = document.querySelector('.search-container')
let searchinput = document.querySelector('#search-input')

window.onscroll = () => {
  let scrollTop = document.documentElement.scrollTop;

  if (scrollTop > 60) {
      header.classList.add('active');
      searchblock.classList.add('active');
  } else {
      header.classList.remove('active');
      searchblock.classList.remove('active');
  }
}

document.addEventListener('DOMContentLoaded', function() {
    const category = document.getElementById('category');
    const carousel1 = document.getElementById('carousel1');
    const carousel2 = document.getElementById('carousel2');

    let currentPosition = 1;

    category.addEventListener('wheel', (event) => {
        event.preventDefault();

        currentPosition += (event.deltaY > 0) ? 1 : -1;

        currentPosition = Math.min(Math.max(currentPosition, 1), 5);

        carousel1.style.setProperty('--position', currentPosition);
        carousel2.style.setProperty('--position', currentPosition);
    });
});