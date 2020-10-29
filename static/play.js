const NOW_PLAYING_CLASS = 'now-playing';
const STATION_ITEM_CLASS = 'station-item';

function sendPlayReq(name, id) {
    [...document.getElementsByClassName(STATION_ITEM_CLASS)]
        .filter(x => x.id !== id)
        .forEach(x => x.classList.remove(NOW_PLAYING_CLASS));

    document.getElementById(id).classList.toggle(NOW_PLAYING_CLASS);
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
