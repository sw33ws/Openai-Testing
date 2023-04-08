// const taskList = document.getElementById('task-list');
// const addBtn = document.getElementById('add-btn');
// const newTask = document.getElementById('new-task');

// function addTask() {
//   if (newTask.value !== '') {
//     const li = document.createElement('li');
//     const checkbox = document.createElement('input');
//     checkbox.type = 'checkbox';
//     const label = document.createElement('label');
//     label.innerText = newTask.value;
//     li.appendChild(checkbox);
//     li.appendChild(label);
//     taskList.appendChild(li);
//     newTask.value = '';
//   }
// }

// addBtn.addEventListener('click', addTask);
// newTask.addEventListener('keydown', function(event) {
//   if (event.key === 'Enter') {
//     event.preventDefault();
//     addTask();
//   }
// });

// now asking for an updated javascript with a delete button

const taskList = document.getElementById('task-list');
const addBtn = document.getElementById('add-btn');
const newTask = document.getElementById('new-task');

function addTask() {
  if (newTask.value !== '') {
    const li = document.createElement('li');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    const label = document.createElement('label');
    label.innerText = newTask.value;
    const deleteBtn = document.createElement('button');
    deleteBtn.innerText = 'Delete';
    deleteBtn.classList.add('delete-btn');
    li.appendChild(checkbox);
    li.appendChild(label);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
    newTask.value = '';
  }
}

function deleteTask(event) {
  const task = event.target.parentElement;
  task.remove();
}

addBtn.addEventListener('click', addTask);
newTask.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    addTask();
  }
});

taskList.addEventListener('click', function(event) {
  if (event.target.type === 'checkbox') {
    event.target.nextElementSibling.classList.toggle('completed');
  }
  else if (event.target.classList.contains('delete-btn')) {
    deleteTask(event);
  }
});