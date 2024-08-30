import time

from p2pfl.learning.pytorch.mnist_examples.mnistfederated_dm import MnistFederatedDM
from p2pfl.learning.pytorch.mnist_examples.models.mlp import MLP
from p2pfl.node import Node

from .network_helper import NetworkHelper


def node_3():
    node = Node(
        MLP(),
        MnistFederatedDM(sub_id=2, number_sub=3),
        address="127.0.0.1:3003",
    )
    node.start()

    # Connect to the first node
    node.connect("127.0.0.1:3002")

    time.sleep(4)

    NetworkHelper.warning_logger(
        node.state.addr,
        f"node 3 neighbors {node.get_neighbors()}",
    )

    NetworkHelper.warning_logger(node.addr, "starting node 3 training")

    node.set_start_learning(rounds=1, epochs=1)
    NetworkHelper.warning_logger(node.state.addr, "finished node 3 training")

    while True:
        time.sleep(1)

        # NetworkHelper.warning_logger(
        #     node.state.addr,
        #     f"waiting on node 3 on round {node.state.round} out of {node.state.total_rounds}",
        # )

        if node.state.round is None:
            break

    node.stop()
