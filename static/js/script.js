function vote(btn){
    const csrf_token = btn.dataset.csrf;
    const [type, id, vote] = btn.id.split('-');
    const karma_element = document.getElementById(`${type}-${id}-karma`);
    const upvote_element = document.getElementById(`${type}-${id}-up`);
    const downvote_element = document.getElementById(`${type}-${id}-down`);

    vote_client(karma_element, upvote_element, downvote_element, vote);
    vote_server(type, id, vote, csrf_token);
}


function vote_server(type, id, vote, csrf_token){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", `/vote/${type}/`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrf_token);

    let value = 1;
    if (vote === "down"){
        value = -1;
    }

    xhr.send(JSON.stringify({
        "type": type,
        "id": id,
        "value": value
    }));
}


function vote_client(karma_element, upvote_element, downvote_element, vote){
    const start_state = karma_element.dataset.state;
    const [k, _] = karma_element.innerText.split(' ');
    let karma_value = parseInt(k);
    const classname = 'voted';

    if (start_state === "null"){
        if (vote === "up"){
            upvote_element.classList.add(classname);
            karma_value += 1;
            karma_element.dataset.state = "up";
        } else {
            downvote_element.classList.add(classname);
            karma_value -= 1;
            karma_element.dataset.state = "down";
        }
    } else if (start_state === "up"){
        if (vote === "up"){
            upvote_element.classList.remove(classname);
            karma_value -= 1;
            karma_element.dataset.state = "null";
        } else {
            upvote_element.classList.remove(classname);
            downvote_element.classList.add(classname);
            karma_value -= 2;
            karma_element.dataset.state = "down";
        }
    } else if (start_state === "down"){
        if (vote === "up"){
            upvote_element.classList.add(classname);
            downvote_element.classList.remove(classname);
            karma_value += 2;
            karma_element.dataset.state = "up";
        } else {
            downvote_element.classList.remove(classname);
            karma_value += 1;
            karma_element.dataset.state = "null";
        }
    }

    let points = " points";
    if (karma_value === 1 || karma_value === -1){
        points = " point";
    }
    karma_element.innerText = karma_value + points;
}
