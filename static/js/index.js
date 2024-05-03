document.addEventListener("DOMContentLoaded", function () {
  const taskInput = document.getElementById("task-input");
  const addTaskButton = document.getElementById("add-task");
  const taskList = document.getElementById("task-list");

  addTaskButton.addEventListener("click", addTask);

  function addTask() {
    const taskText = taskInput.value.trim();

    if (taskText == "") {
      return;
    }

    const li = document.createElement("li");
    li.innerHTML = `
<input type= "checkbox">
<span>${taskText}</span>
<button class="delete-button">Delete</button>
`;
    const checkbox = li.querySelector("input[type=checkbox] ");
    const deleteButton = li.querySelector(".delete-button");

    checkbox.addEventListener("change", toggleTaskCompletion);
    deleteButton.addEventListener("click", deleteTask);

    taskList.appendChild(li);
    taskInput.value = "";
  }
  function toggleTaskCompletion(event) {
    const taskText = event.target.nextSibling;
    if (event.target.checked) {
      taskText.taskList.add("completed");
    } else {
      taskText.taskList.remove("completed");
    }
  }

  function deleteTask(event) {
    const taskText = event.target.parentElement;
    taskText.removeChild(li);
  }
});
