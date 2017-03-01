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
