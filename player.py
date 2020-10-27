# credits: https://raw.githubusercontent.com/rikkt0r/mplayer-pi-radio/master/app/player.py

import json
import os
import subprocess


class Player:

    def __init__(self):

        self.pid = None
        self._now_playing = "nothing..."
        with open('configs/stations.json', 'r') as f:
            self._stations = json.loads(f.read())['stations']

    def __del__(self):
        self.stop()

    def get_station(self, name):
        for s in self._stations:
            if s['name'] in name:
                return s
        else:
            return None

    def get_active_station(self):

        return self._now_playing

    def get_station_list(self):
        return sorted(self._stations)

    def play(self, station_name):

        if self.pid:
            self.stop()

        self._now_playing = station_name

        mplayerargs = ['mplayer', '-softvol', '-ao', 'alsa:device=bluetooth', '2>&1>/dev/null']
        #mplayerargs = ['mplayer', '-softvol', '-vo', 'null', '2>&1>/dev/null'] # TODO: move to sep args
        station = self.get_station(station_name)

        if not station:
            print('Station not found')

        mplayerargs.append(station['url'])

        self.pid = subprocess.Popen(mplayerargs).pid

        return True

    def stop(self):
        if self.pid:
            os.kill(self.pid, 15)  # 15 = SIGTERM
        self.pid = None
        self._now_playing = "nothing..."
