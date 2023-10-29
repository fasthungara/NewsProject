var today = new Date();
var hourNow = today.getHours();
var greeting;

if (hourNow > 18) {
     greeting='Добрый вечер';
     } else if (hourNow > 12) {
      greeting = 'Добрый день';
      }
else {
      greeting = 'Приветствуем';
      }

document.write('<h3>' + greeting + today + '</h3>')