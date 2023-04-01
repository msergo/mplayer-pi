<!DOCTYPE html>
<html>
    <head>
        <script src="/static/play.js"></script>
        <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
          % 
           <div class="button" onclick="changeVolumeLevel('increase')"> Vol + </div>
           <div class="button" onclick="changeVolumeLevel('decrease')"> Vol - </div>
           %
           <br>

           % for station in stations:
                <div id="{{station['id']}}" class="station-item {{ 'now-playing' if station['name'] == now_playing else '' }}" onclick="sendPlayReq('{{ station['name'] }}', '{{ station['id'] }}')" >
                    {{ station['name'] }}
                </div>
           % end
    </body>
</html>
