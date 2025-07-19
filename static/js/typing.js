const typingElement = document.querySelector('.typing');
const phrases = [
  "AI Developer",
  "Cybersecurity Intern",
  "Full-Stack Coder",
  "GenAI Enthusiast"
];

let currentPhraseIndex = 0;
let currentCharIndex = 0;
let typingForward = true;

function type() {
  const phrase = phrases[currentPhraseIndex];
  if (typingForward) {
    currentCharIndex++;
    if (currentCharIndex === phrase.length) {
      typingForward = false;
      setTimeout(type, 1000);
      return;
    }
  } else {
    currentCharIndex--;
    if (currentCharIndex === 0) {
      typingForward = true;
      currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
    }
  }

  typingElement.textContent = phrase.substring(0, currentCharIndex);
  setTimeout(type, 100);
}

type();
