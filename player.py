# credits: https://raw.githubusercontent.com/rikkt0r/mplayer-pi-radio/master/app/player.py

import json
import os
import subprocess


class Player:

    def __init__(self):

        self.pid = None
        self.process = None
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
        return sorted(self._stations, key=lambda x: x['name'], reverse=True)

    def play(self, station_name):

        if self.pid:
            if self.get_active_station() == station_name:
                self.stop()
                return
            self.stop()

        self._now_playing = station_name

        mplayer_args = os.getenv('mplayerargs').split(' ')
        station = self.get_station(station_name)

        if not station:
            print('Station not found')

        mplayer_args.append(station['url'])

        self.process = subprocess.Popen(mplayer_args, stdout=subprocess.PIPE)
        self.pid = self.process.pid

        return

    def stop(self):
        if self.pid:
            os.kill(self.pid, 15)  # 15 = SIGTERM
        self.pid = None
        self._now_playing = "nothing..."
