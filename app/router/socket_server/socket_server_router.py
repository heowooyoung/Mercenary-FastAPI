from fastapi import APIRouter

from app.router.socket_server.socket_server_exception import check_duplicate_request

socket_server_router = APIRouter()

import importlib
socket_server_module = importlib.import_module("app.includes.Mercenary-Socket-Server.socket_server")
server_instance = None


@socket_server_router.get("/start-socket-server")
def start_socket_server():
    print("start socket server")

    global server_instance
    is_duplicated_request = check_duplicate_request(server_instance)
    if is_duplicated_request is True:
        return False

    server_instance = socket_server_module.SocketServer('0.0.0.0', 33333)
    server_instance.start()

    return True
