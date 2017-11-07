function getBlockheight () {
  //return 470000 + 600; // testing
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "https://blockexplorer.com/api/status?q=getBlockCount", false);
  xhr.setRequestHeader('Content-Type', 'text/xml');
  xhr.send();
  response = JSON.parse(xhr.response);
  return response.blockcount;
}

function getSecondsRemaining (blockheight, targetblock, interval) {
  blocksremaining = targetblock - blockheight;
  secondsremaining = blocksremaining * interval * 1000;
  return secondsremaining
}

function getTimeRemaining(endtime) {
  var t = Date.parse(endtime) - Date.parse(new Date());
  var seconds = Math.floor((t / 1000) % 60);
  var minutes = Math.floor((t / 1000 / 60) % 60);
  var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
  var days = Math.floor(t / (1000 * 60 * 60 * 24));
  return {
    'total': t,
    'days': days,
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds
  };
}

function initializeClock(id, endtime) {
  var clock = document.getElementById(id);
  var daysSpan = clock.querySelector('.days');
  var hoursSpan = clock.querySelector('.hours');
  var minutesSpan = clock.querySelector('.minutes');
  var secondsSpan = clock.querySelector('.seconds');

  function updateClock() {
    var t = getTimeRemaining(endtime);

    daysSpan.innerHTML = t.days;
    hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
    minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
    secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

    if (t.total <= 0) {
      clearInterval(timeinterval);
    }
  }

  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}

blockheight = getBlockheight();
targetblock = 494784; // 2x fork block
interval = 600; // ten minute blocks

var forkday = new Date(Date.parse(new Date()) + getSecondsRemaining(blockheight, targetblock, interval));

var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "numeric", minute: "numeric"}; 
var optionsTZ = {timeZoneName: "long"}; 

var locale = navigator.language || 'en-EN';
if (locale !== 'en' && locale !== 'EN-US' && locale !== 'en-EN')
  options.hour12 = true

document.getElementById("endday").innerHTML = forkday.toLocaleDateString('en-EN', options); //toLocaleFormat('%B %d, %Y at %H:%M');
document.getElementById("tz").innerHTML = (forkday.toLocaleDateString('en-EN', optionsTZ)).split(", ")[1]; 
document.getElementById("blockinfo").innerHTML = "current block: " + blockheight +  "<br>fork block: " + targetblock + "<br>blocks remaining: " + (targetblock - blockheight);
console.log(blockheight);
console.log(forkday);

initializeClock('clockdiv', forkday);

