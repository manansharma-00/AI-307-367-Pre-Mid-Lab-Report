<<<<<<< HEAD
import numpy as np

def binary_bandit_A(action):
    """
    Simulates binary bandit A with probabilities of success [0.1, 0.2].
    Args:
        action (int): Action to take (1 or 2).
    Returns:
        int: Reward (1 for success, 0 for failure).
    """
    probabilities = [0.1, 0.2]  # Success probabilities for actions 1 and 2
    return 1 if np.random.rand() < probabilities[action - 1] else 0

def binary_bandit_B(action):
    """
    Simulates binary bandit B with probabilities of success [0.8, 0.9].
    Args:
        action (int): Action to take (1 or 2).
    Returns:
        int: Reward (1 for success, 0 for failure).
    """
    probabilities = [0.8, 0.9]  # Success probabilities for actions 1 and 2
    return 1 if np.random.rand() < probabilities[action - 1] else 0
=======
import numpy as np

def binary_bandit_A(action):
    """
    Simulates binary bandit A with probabilities of success [0.1, 0.2].
    Args:
        action (int): Action to take (1 or 2).
    Returns:
        int: Reward (1 for success, 0 for failure).
    """
    probabilities = [0.1, 0.2]  # Success probabilities for actions 1 and 2
    return 1 if np.random.rand() < probabilities[action - 1] else 0

def binary_bandit_B(action):
    """
    Simulates binary bandit B with probabilities of success [0.8, 0.9].
    Args:
        action (int): Action to take (1 or 2).
    Returns:
        int: Reward (1 for success, 0 for failure).
    """
    probabilities = [0.8, 0.9]  # Success probabilities for actions 1 and 2
    return 1 if np.random.rand() < probabilities[action - 1] else 0
>>>>>>> c233d70a206ccb7319170a0a637b305b3060019a
