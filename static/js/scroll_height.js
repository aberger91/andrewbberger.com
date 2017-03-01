window.addEventListener('scroll', function() {
   var elem = document.body;
   var a = elem.scrollTop;
   var b = elem.scrollHeight - window.innerHeight;
   var c = (a / b) * 100;
   document.getElementById("scrollHeight").innerHTML = c.toFixed(1)
})
