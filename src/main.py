from server import RPCServer
from threading import Event

def hello_world():
  return "Hello World"

methods = [hello_world]

def start_server(run_event: Event) -> RPCServer:
  server = RPCServer()
  for method in methods:
    server.registerMethod(method)
  server.run(run_event)
  return server

if __name__ == "__main__":
  run_event = Event()
  start_server(run_event)