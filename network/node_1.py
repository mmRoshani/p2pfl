from network.network_helper import NetworkHelper
from p2pfl.learning.pytorch.mnist_examples.mnistfederated_dm import MnistFederatedDM
from p2pfl.learning.pytorch.mnist_examples.models.mlp import MLP
from p2pfl.node import Node


def node_1() -> None:
    node = Node(
        MLP(),
        MnistFederatedDM(sub_id=0, number_sub=3),
        address="127.0.0.1:3001",
    )
    node.start()

    NetworkHelper.warning_logger(
        node.state.addr,
        f"node 1 neighbors {node.get_neighbors()}",
    )

    input("Press any key to stop\n")

    # Stop the node
    node.stop()
