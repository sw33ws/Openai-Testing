const textToSpeech = window.speechSynthesis;

const speakButton = document.getElementById('speak-button');
const textArea = document.getElementById('text-to-speech');

speakButton.addEventListener('click', () => {
    const text = textArea.value;
    const utterance = new SpeechSynthesisUtterance(text);

    textToSpeech.speak(utterance);
});