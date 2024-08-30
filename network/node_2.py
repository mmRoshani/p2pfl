import time

from network.network_helper import NetworkHelper
from p2pfl.learning.pytorch.mnist_examples.mnistfederated_dm import MnistFederatedDM
from p2pfl.learning.pytorch.mnist_examples.models.mlp import MLP
from p2pfl.node import Node


def node_2():
    node = Node(
        MLP(),
        MnistFederatedDM(sub_id=1, number_sub=3),
        address="127.0.0.1:3002",
    )
    node.start()

    # Connect to the first node
    node.connect("127.0.0.1:3001")

    time.sleep(4)

    NetworkHelper.warning_logger(
        node.state.addr,
        f"node 2 neighbors {node.get_neighbors()}",
    )

    NetworkHelper.warning_logger(node.addr, "starting node 2 training")

    node.set_start_learning(rounds=1, epochs=1)

    NetworkHelper.warning_logger(node.addr, "finished node 2 training")
    while True:
        time.sleep(1)

        if node.state.learner is not None:
            NetworkHelper.warning_logger(
                node.addr,
                f"node 2 evaluation metrics is {node.state.learner.get_eval_results()}",
            )

        if node.state.round is None:
            break

    node.stop()
