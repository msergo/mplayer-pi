<!DOCTYPE html>
<html>

<head>
    <script src="/static/play.js"></script>
    <link rel="stylesheet" href="/static/styles.css">
</head>

<body>
    % for station in stations:
    <div id="{{station['id']}}" class="station-item {{ 'now-playing' if station['name'] == now_playing else '' }}"
        onclick="sendPlayReq('{{ station['name'] }}', '{{ station['id'] }}')">
        <img src="{{station['icon']}}" alt="{{station['name']}}" class="station-icon">
    </div>
    % end
    <br>
    %
    <img src="/static/volume-up.png" alt="volume" class="button" onclick="changeVolumeLevel('increase')">
    <img src="/static/volume-down.png" alt="volume" class="button" onclick="changeVolumeLevel('decrease')">
    %
    <br>
</body>

</html>