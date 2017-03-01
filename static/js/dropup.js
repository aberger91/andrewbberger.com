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
        toggleDropUp()
    }
}
