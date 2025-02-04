from client import RPCClient
import unittest
from main import start_server
from threading import Event, Thread

class TestMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.server_run_event = Event()
        self.server_run_event.set()
        self.server_thread: Thread = Thread(target=start_server, args=[self.server_run_event])
        self.server_thread.start()
        self.client = RPCClient('0.0.0.0', 8080)
        self.client.connect()
    
    def tearDown(self) -> None:
        self.client.disconnect()
        # Interrupt the server thread
        self.server_run_event.clear()
        self.server_thread.join()

    def test_hello_world(self):
        response = self.client.hello_world()
        self.assertEqual(response, "Hello World")

    def test_directory(self):
        response = self.client.directory()
        self.assertEqual(response, ['hello_world', 'directory'])
        self.server_run_event.clear()
        self.server_thread.join()

if __name__ == '__main__':
    unittest.main()
