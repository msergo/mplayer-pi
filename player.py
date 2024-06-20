# credits: https://raw.githubusercontent.com/rikkt0r/mplayer-pi-radio/master/app/player.py

import json
import os
import subprocess


class Player:
    def __init__(self):
        self.pid = None
        self.process = None
        self._now_playing = "nothing..."
        self._volume_level = 50

        with open("configs/stations.json", "r") as f:
            self._stations = json.loads(f.read())["stations"]

    def __del__(self):
        self.stop()

    def get_station(self, name):
        for s in self._stations:
            if s["name"] in name:
                return s
        else:
            return None

    def get_active_station(self):
        return self._now_playing

    def get_station_list(self):
        return sorted(self._stations, key=lambda x: x["id"], reverse=False)

    def play(self, station_name):
        if self.pid:
            if self.get_active_station() == station_name:
                self.stop()
                return

            self.stop()

        self._now_playing = station_name

        player_args = os.getenv("PLAYER_ARGS").split(" ")
        station = self.get_station(station_name)

        if not station:
            print("Station not found")

        if player_args[0] == "mplayer" and station["url"].endswith(".m3u8"):
            player_args.append("-playlist")

        player_args.append(station["url"])

        self.process = subprocess.Popen(
            player_args, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
        )
        self.pid = self.process.pid

        return

    def stop(self):
        if self.pid:
            os.kill(self.pid, 9)  # 9 = SIGKILL
        self.pid = None
        self._now_playing = "nothing..."

    def change_volume_level(self, action):
        if action == "increase":
            self._volume_level = self._volume_level + 10
        elif action == "decrease":
            self._volume_level = self._volume_level - 10

        os.system(os.getenv("VOLUME_LEVEL_COMMAND") + str(self._volume_level) + " &")

    def get_volume_level(self):
        return self._volume_level
