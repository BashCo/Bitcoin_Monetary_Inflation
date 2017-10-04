function getBlockheight () {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "https://bitcoincash.blockexplorer.com/api/status", false);
  xhr.setRequestHeader('Content-Type', 'text/xml');
  xhr.send();
  response = JSON.parse(xhr.response);
  return response.info["blocks"];
}

function getSecondsRemaining (blockheight, targetblock, interval) {
  blocksremaining = targetblock - blockheight;
  secondsremaining = blocksremaining * interval * 1000;
  return secondsremaining
}

function calculateEDA () {
  var EDA = Math.random() >= 0.3; // seems about right
  if (EDA == true) {
    EDA = Math.floor(Math.random() * (240 - 30) + 30); // Satoshi's original vision
  }
  else {
    EDA = Math.floor(Math.random() * (43200 - 21600) + 21600); // Satoshi's other original vision
  }
  return EDA
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
targetblock = 630000; // Bcash halving block
interval = calculateEDA(); // generous approximation of block interval based on EDA fluctuations

var halvingday = new Date(Date.parse(new Date()) + getSecondsRemaining(blockheight, targetblock, interval));

var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: "numeric", minute: "numeric"}; 
var optionsTZ = {timeZoneName: "long"}; 

document.getElementById("endday").innerHTML = halvingday.toLocaleDateString('en-EN', options); 
document.getElementById("tz").innerHTML = (halvingday.toLocaleDateString('en-EN', optionsTZ)).split(", ")[1]; 
document.getElementById("blockinfo").innerHTML = "current block: " + blockheight +  "<br>halving block: " + targetblock + "<br>blocks remaining: " + (targetblock - blockheight) + "<br>estimated block interval: " + Math.floor(interval / 60) + " minutes";
console.log("This is a joke, same as Bcash and EDA.")

initializeClock('clockdiv', halvingday);

