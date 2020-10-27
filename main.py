import bottle
from bottle import template, run, post, get, static_file, request, redirect

from player import Player

mplayer = Player()
bottle.TEMPLATES.clear()


@get('/static/js/<filename>')
def serve_static_js(filename):
    return static_file(filename, root='static/js')


@get('/')
def index():
    stations = mplayer.get_station_list()
    now_playing = mplayer.get_active_station()
    return template('index_template', now_playing=now_playing, stations=stations)


@post('/play')
def play():
    body = request.json
    try:
        name = body['name']
        mplayer.play(name)
    except Exception:
        return template('<b>shit happened')
    redirect('/')


run(host='localhost', port=8080)
