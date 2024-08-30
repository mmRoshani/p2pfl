import time

from network.algorithm import NAEM, NSMC, T1, T2, k, tau
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

    neighbor_bag = node.get_neighbors()

    # First stage: NSMC for T1 rounds
    for t in range(T1):
        # Perform local training
        node.set_start_learning(rounds=1, epochs=1)

        # Update neighbor list using NSMC
        neighbor_list = NSMC(neighbor_bag, k)
        neighbor_bag = {key: neighbor_bag[key] for key in neighbor_list}

    # Set initial neighbor bag for the second stage
    B_T1_plus_1 = neighbor_bag

    # Second stage: Gossip communication and NAEM for T2 rounds
    for t in range(T1, T1 + T2):
        # Perform local training
        node.set_start_learning(rounds=1, epochs=1)

        # Gossip communication with peers sampled from the neighbor bag
        neighbor_list = NSMC(B_T1_plus_1, k)
        B_T1_plus_1 = {key: B_T1_plus_1[key] for key in neighbor_list}

        # Perform NAEM every τ rounds
        if t % tau == 0:
            B_T1_plus_1 = NAEM(node, B_T1_plus_1, k)
    # NetworkHelper.warning_logger(
    #     node.state.addr,
    #     f"node 3 neighbors {node.get_neighbors()}",
    # )

    # NetworkHelper.warning_logger(node.addr, "starting node 3 training")

    # node.set_start_learning(rounds=1, epochs=1)
    # NetworkHelper.warning_logger(node.state.addr, "finished node 3 training")

    # while True:
    #     time.sleep(1)

    #     # NetworkHelper.warning_logger(
    #     #     node.state.addr,
    #     #     f"waiting on node 3 on round {node.state.round} out of {node.state.total_rounds}",
    #     # )

    #     if node.state.round is None:
    #         break

    node.stop()
