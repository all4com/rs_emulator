## Server list

- The server list is sent by DUMMY packet handler

# command server(websockets)

## all server exit

curl http://127.0.0.1:8080/api/v1/commands/?cmd=exit

## login server exit

curl http://127.0.0.1:8080/api/v1/commands/?cmd=exit&srv=login_server

## game server exit

curl http://127.0.0.1:8080/api/v1/commands/?cmd=exit&srv=game_server

# history

10/23
Automatically restart the server when the exit command is executed
Supports commands for all servers
