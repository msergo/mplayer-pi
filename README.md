### Simple internet radio player for Raspberry Pi Zero (W) utilizing *mplayer* and external bluetooth speaker
See the blog post about this app https://sergiiwrites.online/2022/09/10/internet-radio-pi-zero.html  

#### Setting up
NB!: tested with python version 3.7.3
```bash 
virtualenv -p /usr/bin/python3 env
. env/bin/activate
pip install -r requirements.txt
python main.py 
```
#### Configuring as a systemd service
##### 1. Create file /etc/systemd/system/mplayer-pi.service
```
[Unit]
Description=mplayer-pi service

[Service]
User=pi
WorkingDirectory=/path/to/mplayer-pi
ExecStart=/path/to/mplayer-pi/env/bin/python3 -m main

[Install]
WantedBy=multi-user.target
```
##### 2. Enable service
```bash
systemctl enable mplayer-pi.service
```
##### 3. Start service
```bash
systemctl start mplayer-pi.service
```
