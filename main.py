import os

import bottle
from bottle import template, run, post, get, static_file, request, redirect
from dotenv import load_dotenv

from player import Player

load_dotenv()
mplayer = Player()
bottle.TEMPLATES.clear()


@get("/static/<filename>")
def serve_static_file(filename):
    return static_file(filename, root="static/")


@get("/")
def index():
    stations = mplayer.get_station_list()
    now_playing = mplayer.get_active_station()
    volume_level = mplayer.get_volume_level()

    return template(
        "index_template",
        now_playing=now_playing,
        stations=stations,
        volume_level=volume_level,
    )


@post("/play")
def play():
    body = request.json
    try:
        name = body["name"]
        mplayer.play(name)
    except Exception as err:
        print("Error: {0}".format(err))
        return template("<b>what a bummer!")

    redirect("/")


@post("/change-volume")
def change_volume():
    body = request.json
    action = body["action"]

    mplayer.change_volume_level(action)


run(host="0.0.0.0", port=os.getenv("PORT"))
