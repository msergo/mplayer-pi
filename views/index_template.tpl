<!DOCTYPE html>
<html>
    <head>
        <script src="/static/js/play.js"></script>
    </head>
    <body>
        <div>  {{ now_playing }}  </div>
        <ul>
           % for station in stations:
                <li onclick="sendPlayReq('{{ station['name'] }}')" > {{ station['name'] }} </li>
           % end
        </ul>

    </body>
</html>
