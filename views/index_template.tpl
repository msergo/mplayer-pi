<!DOCTYPE html>
<html>
    <head>
        <script src="/static/play.js"></script>
        <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
           % for station in stations:
                <div id="{{station['id']}}" class="station-item" onclick="sendPlayReq('{{ station['name'] }}', '{{ station['id'] }}')" >
                    {{ station['name'] }}
                </div>
           % end
    </body>
</html>
