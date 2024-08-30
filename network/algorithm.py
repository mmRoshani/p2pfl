import random

from p2pfl.node import Node

T1 = 2
T2 = 2
tau = 1
k = 1


def NSMC(neighbor_bag, k):
    # Convert dictionary keys to a list
    neighbor_list = list(neighbor_bag.keys())
    # Select k neighbors uniformly at random from the neighbor list
    if len(neighbor_bag) < k:
        return neighbor_bag
    return random.sample(neighbor_list, k)


def NAEM(node: Node, neighbor_bag, k):
    # Update the neighbor bag based on evaluation metrics
    eval_results = node.state.learner.get_eval_results()

    # Create a dictionary to store evaluation metrics for each neighbor
    neighbor_metrics = {}
    for neighbor in neighbor_bag.keys():
        # Assuming eval_results is a list of dictionaries with 'test_metric' as a key
        for result in eval_results:
            if neighbor in result:
                neighbor_metrics[neighbor] = result[neighbor]["test_metric"]

    # Sort neighbors based on evaluation metrics
    sorted_neighbors = sorted(
        neighbor_metrics.keys(), key=lambda x: neighbor_metrics[x], reverse=True
    )

    # Return the top k neighbors
    return {key: neighbor_bag[key] for key in sorted_neighbors[:k]}
