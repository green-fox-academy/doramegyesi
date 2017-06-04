'use strict';

const list = document.querySelector('.list');

const getTodoList = function() {
    const req = new XMLHttpRequest();
    const method = 'GET';
    const url = 'http://localhost:3000/todos';
    req.open(method, url);
    req.send();
    req.onreadystatechange = function() {
        if (req.readyState === 4 && req.status === 200) {
            var todoList = JSON.parse(req.response);
            console.log(todoList);
            todoList.forEach(function(item) {
                var todo = document.createElement('div');
                todo.setAttribute('class', 'todo');
                todo.innerText = item.text;
                list.appendChild(todo);
			});
        }
    }
};

getTodoList();
