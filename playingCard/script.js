const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
const suits = ['&hearts;', '&diams;', '&clubs;', '&spades;'];

const cardValue = values[Math.floor(Math.random() * values.length)];
const cardSuit = suits[Math.floor(Math.random() * suits.length)];

const cardValueElement = document.querySelector('.card-value');
const cardSuitElement = document.querySelector('.card-suit');

cardValueElement.innerHTML = cardValue;
cardSuitElement.innerHTML = cardSuit;