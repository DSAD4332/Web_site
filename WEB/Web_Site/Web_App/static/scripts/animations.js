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
let sectionContent = document.querySelector('hr');

window.onscroll = () => {
  let scrollTop = document.documentElement.scrollTop;

  if (scrollTop > header.offsetHeight) {
      header.classList.add('active');
  } else {
      header.classList.remove('active');
  }
}