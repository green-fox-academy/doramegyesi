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
                list.appendChild(todo);
                var todoText = document.createElement('div');
                todoText.innerText = item.text;
                todoText.setAttribute('class', 'todotext');
                todo.appendChild(todoText);
                var icons = document.createElement('div');
                icons.setAttribute('class', 'icons');
                todo.appendChild(icons)
                var trash = document.createElement('div');
                trash.setAttribute('class', 'trash');
                icons.appendChild(trash);
                console.log(item.text);
                console.log(item.completed);
                var check = document.createElement('div');
                if (item.completed === '0') {
                    check.setAttribute('class', 'no');
                } else {
                    check.setAttribute('class', 'yes');
                };
                icons.appendChild(check);
			});
        }
    }
};

getTodoList();
