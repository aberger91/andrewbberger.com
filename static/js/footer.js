window.addEventListener('scroll', function() {
   var elem = document.body;
   var a = elem.scrollTop;
   var b = elem.scrollHeight - window.innerHeight;
   var c = (a / b) * 100;
   document.getElementById("scrollHeight").innerHTML = c.toFixed(1) + '%'
})

function getDatetime() {
    var d = new Date();

    minutes = d.getMinutes().toString().length == 1 ? '0'+d.getMinutes() : d.getMinutes();
    hours = d.getHours().toString().length == 1 ? '0'+d.getHours() : d.getHours();
    ampm = d.getHours() >= 12 ? 'pm' : 'am';

    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    var date = days[d.getDay()]+' '+months[d.getMonth()]+' '+d.getDate()+' '+d.getFullYear()+' '+hours+':'+minutes+ampm;
    document.getElementById('footer-left-black').innerHTML = date;
}

function toggleDropUp () {
    document.getElementsByClassName("dropup-content")[0].classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches("#footer-dropup-button")) {
        var dropdowns = document.getElementsByClassName("dropup-content");
        for (var x=0; x<dropdowns.length; x++) {
            var openDropUp = dropdowns[x];
            if (openDropUp.classList.contains("show")) {
                openDropUp.classList.remove("show");
            }
        }
    }
    else {
        toggleDropUp();
    }
}

window.onclick = function(event) {
    if (event.target.matches("#comments-button")) {
        if (document.getElementById('comments-textarea').style.height != '20%') {
            slideDown();
        } else {
            var pos = 20;
            var elem = document.getElementById('comments-textarea');

            var id = setInterval(frame, 10);
            function frame () {
                if (pos == 0) {
                    clearInterval(id);
                } else {
                    pos--;
                    elem.style.height = pos + '%';
                }
            }
            elem.style.display = 'none'
            document.getElementById('comments-submit').style.display = 'none'
        }
    }
}

function slideDown() {
    var elem = document.getElementById('comments-textarea');
    elem.style.display = 'inline'
    var pos = 0;
    var id = setInterval(frame, 10);
    function frame () {
        if (pos == 20) {
            clearInterval(id);
        } else {
            pos++;
            elem.style.height = pos + '%';
        }
    }
    document.getElementById('comments-submit').style.display = 'inline'
}

window.addEventListener("scroll", 
    function(){
        var lastScrollTop = 0;
        var st = window.pageYOffset || document.documentElement.scrollTop;
        if (st > lastScrollTop) {  // scroll down
            header = document.getElementById("navbar-floating").style.display = "none";
            footer = document.getElementsByClassName("footer")[0].style.display = "inline-block";
        } else { // up
            header = document.getElementById("navbar-floating").style.display = "inline-block";
            footer = document.getElementsByClassName("footer")[0].style.display = "none";
        }
        lastScrollTop = st;
    },
    false);

