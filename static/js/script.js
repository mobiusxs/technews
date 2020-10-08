/**
 * Send the vote to the server as a POST request
 *
 * Example usage:
 *      onclick="vote(this)"
 *
 * @param  {Element} btn The up or down vote icon element
 */
function vote(btn){
    const csrf_token = btn.dataset.csrf;
    const [type, id, vote] = btn.id.split('-');
    const karma_element = document.getElementById(`${type}-${id}-karma`);
    const upvote_element = document.getElementById(`${type}-${id}-up`);
    const downvote_element = document.getElementById(`${type}-${id}-down`);

    vote_client(karma_element, upvote_element, downvote_element, vote);
    vote_server(type, id, vote, csrf_token);
}


/**
 * Send the vote to the server as a POST request
 *
 * @param  {String} type Can be one of [thread, comment]
 * @param  {String} id   The id for the content being voted on
 * @param  {String} vote Can be one of [up, down]
 * @param  {String} csrf CSRF token passed into the template
 */
function vote_server(type, id, vote, csrf){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", `/vote/${type}/`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrf);

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


/**
 * Update the client to reflect voting action.
 * Increment/decrement the score and change the icon color as necessary.
 * Icon color is handled by adding/removing a CSS class.
 * State is stored as a data attribute on the element
 * which displays the karma value.
 * There are 3 possible states [null, up, down]
 * and 6 possible state transitions.
 *
 * @param  {Element} karma_element    The element displaying the karma value
 * @param  {Element} upvote_element   The upvote icon
 * @param  {Element} downvote_element The downvote icon
 * @param  {String}  vote             Can be one of [up, down]
 */
function vote_client(karma_element, upvote_element, downvote_element, vote){
    const start_state = karma_element.dataset.state;
    const classname = 'voted';
    let karma_value = parseInt(karma_element.innerText.split(' ')[0]);
    let end_state = start_state;

    /**
     * For each possible state:
     * - add remove color class
     * - get new karma value
     * - get new state
     */
    if (start_state === "null"){
        if (vote === "up"){
            upvote_element.classList.add(classname);
            karma_value += 1;
            end_state = "up";
        } else {
            downvote_element.classList.add(classname);
            karma_value -= 1;
            end_state = "down";
        }
    } else if (start_state === "up"){
        if (vote === "up"){
            upvote_element.classList.remove(classname);
            karma_value -= 1;
            end_state = "null";
        } else {
            upvote_element.classList.remove(classname);
            downvote_element.classList.add(classname);
            karma_value -= 2;
            end_state = "down";
        }
    } else if (start_state === "down"){
        if (vote === "up"){
            upvote_element.classList.add(classname);
            downvote_element.classList.remove(classname);
            karma_value += 2;
            end_state = "up";
        } else {
            downvote_element.classList.remove(classname);
            karma_value += 1;
            end_state = "null";
        }
    }

    // handle plurality of "point" based on karma value
    let points = " points";
    if (karma_value === 1 || karma_value === -1){
        points = " point";
    }

    // Update state and karma
    karma_element.dataset.state = end_state;
    karma_element.innerText = karma_value + points;
}
