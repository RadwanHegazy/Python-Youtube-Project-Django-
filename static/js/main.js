// view the var
document.getElementById('view').onclick = function(){
    document.getElementById('view').classList.toggle('view');
    document.getElementById('list').classList.toggle('view')
}

// view change password fileds
document.getElementById('changepas').onclick = function(){
    document.getElementById('over').classList.toggle('view')
}

document.getElementById('closeIn').onclick = function(){
    document.getElementById('over').classList.toggle('view')
}

