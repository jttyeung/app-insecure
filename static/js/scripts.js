"use strict";


// Show or hide answer/hint on page
var showAnswer = document.getElementById('show-answer');
showAnswer.addEventListener('click', revealHideAnswer);

function revealHideAnswer() {
  if (showAnswer.innerHTML === 'Show Answer') {
    document.getElementById('reveal-info').removeAttribute('hidden');
    showAnswer.innerHTML = 'Hide Answer';
  } else {
    document.getElementById('reveal-info').setAttribute('hidden', true);
    showAnswer.innerHTML = 'Show Answer';
  }
}
