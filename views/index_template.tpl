<!DOCTYPE html>
<html>

<head>
    <script src="/static/play.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/styles.css">
</head>

<body class="d-flex flex-column align-items-center">
    <div class="container text-center">
        <div class="row justify-content-center">
            % for station in stations:
            <div id="{{station['id']}}"
                class="station-item {{ 'now-playing' if station['name'] == now_playing else '' }}"
                onclick="sendPlayReq('{{ station['name'] }}', '{{ station['id'] }}')">
                <img src="{{station['icon']}}" alt="{{station['name']}}" class="station-icon img-fluid">
            </div>
            % end
        </div>
        <br>
        <div class="text-center">
            <img src="/static/volume-up.png" alt="volume" class="control-button"
                onclick="changeVolumeLevel('increase')">
            <img src="/static/volume-down.png" alt="volume" class="control-button"
                onclick="changeVolumeLevel('decrease')">
        </div>
    </div>
    <br>
</body>

</html>