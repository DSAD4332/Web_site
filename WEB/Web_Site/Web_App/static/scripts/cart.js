var hours = 0;
var now = new Date.getTime();
var stepTime = localStorage.getItem('stepTime')

if (stepTime == NULL) {
    localStorage.setItem('stepTime', now)
}
else {
    if (now - stepTime > hours*60*60*1000) {
        localStorage.clear();
        localStorage.setItem('stepTime', now)
    }
}

