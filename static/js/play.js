function sendPlayReq(name) {
    return fetch('/play', {
        method: 'POST',
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
        body: JSON.stringify({ name })
    })
        .then(response => console.log(response))
        .catch(err => console.log(err));
}

function sendStopReq() {
    return fetch('/stop', { method: 'POST' })
        .then(response => console.log(response))
        .catch(err => console.log(err));
}