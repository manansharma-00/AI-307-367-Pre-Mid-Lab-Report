import numpy as np
import matplotlib.pyplot as plt
from binaryBandit import binary_bandit_A, binary_bandit_B

def multi_armed_bandit(n_experiments, n_steps, epsilon):
    """
    Runs the multi-armed bandit experiment using epsilon-greedy strategy.
    
    Args:
        n_experiments (int): Number of experiments.
        n_steps (int): Number of steps per experiment.
        epsilon (float): Probability of exploration.
    """
    # Tracking action history and rewards
    actions_A = np.zeros(n_steps)
    actions_B = np.zeros(n_steps)
    rewards_A = np.zeros(n_steps)
    rewards_B = np.zeros(n_steps)

    for experiment in range(n_experiments):
        nA = nB = 0  # Counts of actions taken
        Q_A = Q_B = 0  # Estimated values for bandits A and B

        for step in range(n_steps):
            # Epsilon-greedy action selection
            if np.random.rand() < epsilon:
                action = np.random.randint(1, 3)  # Random action (1 or 2)
            else:
                if Q_A > Q_B:
                    action = 1  # Choose bandit A
                elif Q_B > Q_A:
                    action = 2  # Choose bandit B
                else:
                    action = np.random.randint(1, 3)  # Break tie randomly

            # Get reward and update estimates
            if action == 1:
                reward = binary_bandit_A(action)
                nA += 1
                Q_A += (reward - Q_A) / nA
            else:
                reward = binary_bandit_B(action)
                nB += 1
                Q_B += (reward - Q_B) / nB

            # Record actions and rewards
            actions_A[step] += (action == 1)
            actions_B[step] += (action == 2)
            rewards_A[step] += (action == 1) * reward
            rewards_B[step] += (action == 2) * reward

        # Optional: Print progress every 10% of experiments
        if experiment % (n_experiments // 10) == 0:
            print(f"Experiment {experiment}/{n_experiments} completed.")

    # Plotting average rewards
    plt.figure(figsize=(10, 5))
    plt.plot(np.cumsum(rewards_A) / (np.arange(1, n_steps + 1)), 'r-', label='Bandit A', linewidth=2)
    plt.plot(np.cumsum(rewards_B) / (np.arange(1, n_steps + 1)), 'b-', label='Bandit B', linewidth=2)
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')
    plt.title('Average Rewards for Binary Bandits')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plotting action selection percentages
    plt.figure(figsize=(6, 4))
    action_counts = [np.mean(actions_A) * 100, np.mean(actions_B) * 100]
    plt.bar(['Bandit A', 'Bandit B'], action_counts, color=['red', 'blue'])
    plt.xlabel('Bandit')
    plt.ylabel('Percentage of Actions (%)')
    plt.title('Action Selection Percentage for Binary Bandits')
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    n_experiments = 100  # Number of experiments
    n_steps = 500        # Number of steps per experiment
    epsilon = 0.5        # Exploration probability  

    multi_armed_bandit(n_experiments, n_steps, epsilon)
