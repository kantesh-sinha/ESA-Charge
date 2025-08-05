# ethernet_comm_test.py
import threading
import time
from sim.ethernet_comm import start_server, start_client

def run_full_socket_test():
    # Start server in a thread
    server_thread = threading.Thread(target=start_server, kwargs={"host": "localhost", "port": 5000}, daemon=True)
    server_thread.start()

    # Give server time to start
    time.sleep(1)

    # Run client normally
    start_client(host="localhost", port=5000)

if __name__ == "__main__":
    run_full_socket_test()
