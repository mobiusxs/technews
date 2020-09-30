function vote(btn){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", `/vote/${btn.dataset.type}/`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', btn.dataset.csrf);
    xhr.send(JSON.stringify({
        "type": btn.dataset.type,
        "id": btn.dataset.id,
        "value": btn.dataset.value
    }));
}