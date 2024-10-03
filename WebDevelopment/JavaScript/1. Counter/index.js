const increasebtn = document.getElementById('increase');
const decreasebtn = document.getElementById('decrease');
const resetbtn = document.getElementById('reset');
const count_label = document.getElementById('output');

let count = 0;

increasebtn.onclick = function(){
    count++;
    count_label.textContent = count;
}

decreasebtn.onclick = function(){
    count--;
    count_label.textContent = count;
}

resetbtn.onclick = function(){
    count = 0;
    count_label.textContent = count;
}