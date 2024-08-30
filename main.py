import threading

from network.node_1 import node_1
from network.node_2 import node_2
from network.node_3 import node_3


def start():

    node_1_thread = threading.Thread(target=node_1)
    node_2_thread = threading.Thread(target=node_2)
    node_3_thread = threading.Thread(target=node_3)

    node_1_thread.start()
    node_2_thread.start()
    node_3_thread.start()

    node_1_thread.join()
    node_2_thread.join()
    node_3_thread.join()


if __name__ == "__main__":
    start()
