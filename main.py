from p2pfl.node import Node
from p2pfl.learning.pytorch.mnist_examples.mnistfederated_dm import MnistFederatedDM
from p2pfl.learning.pytorch.mnist_examples.models.mlp import MLP

master = Node(
    MLP(),
    MnistFederatedDM(),
)
slave_1 = Node(
    MLP(),
    MnistFederatedDM(),
)

slave_2 = Node(
    MLP(),
    MnistFederatedDM(),
)

# Start nodes
master.start()
slave_1.start()
slave_2.start()

# Connect nodes
slave_1.connect(master.addr)
slave_2.connect(master.addr)
slave_2.connect(slave_1.addr)

# Start learning
slave_1.set_start_learning(rounds=2, epochs=1)
slave_2.set_start_learning(rounds=2, epochs=1)
