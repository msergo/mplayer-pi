#!/bin/bash

# This script is used to run the service and watchdog
exec /home/pi/apps/mplayer-pi/env/bin/python3 -m main &

watchdog() {
    while(true); do
        FAIL=0

        nc -z localhost 8080 || FAIL=1

        if [[ $FAIL -eq 0 ]]; then
            /bin/systemd-notify WATCHDOG=1;
            sleep $(($WATCHDOG_USEC / 2000000))
        else
            echo `date` FAILED=$FAIL >> error.log
            sleep 1
        fi
    done
}

watchdog