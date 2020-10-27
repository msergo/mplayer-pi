function sendPlayReq(name) {
    const id = '123';
    console.log(JSON.stringify({ name }));
    return fetch('/play', {
        method: 'POST',
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
        body: JSON.stringify({ name })
    })
        .then(response => console.log(response))
        .catch(err => console.log(err));
}
