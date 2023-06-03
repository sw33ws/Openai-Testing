const openBtn = document.getElementById('openBtn');
const closeBtn = document.getElementById('closeBtn');
const myDialog = document.getElementById('myDialog');

openBtn.addEventListener('click', () => {
    myDialog.showModal();
});

closeBtn.addEventListener('click', () => {
    myDialog.close();
});
