import time

from network.algorithm import NAEM, NSMC, T1, T2, k, tau
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
    #     f"node 2 neighbors {node.get_neighbors()}",
    # )

    # NetworkHelper.warning_logger(node.addr, "starting node 2 training")

    # node.set_start_learning(rounds=1, epochs=1)

    # NetworkHelper.warning_logger(node.addr, "finished node 2 training")
    # while True:
    #     time.sleep(1)

    #     if node.state.learner is not None:
    #         NetworkHelper.warning_logger(
    #             node.addr,
    #             f"node 2 evaluation metrics is {node.state.learner.get_eval_results()}",
    #         )

    #     if node.state.round is None:
    #         break

    node.stop()
