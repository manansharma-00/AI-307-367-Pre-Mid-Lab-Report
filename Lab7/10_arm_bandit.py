import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

class Environment:

    def _init_(self, n_arms):
        self.n_arms = n_arms
        self.means = np.ones(n_arms) * 0.5  # Initialize all mean-rewards equally (e.g., 0.5)

    def step(self, action):
        # Pull arm and get stochastic reward (1 for success, 0 for failure)
        return 1 if (np.random.random() < self.means[action]) else 0

    def update_means(self):
        # Random walk for each arm's mean reward
        self.means += np.random.normal(0, 0.01, self.n_arms)
        self.means = np.clip(self.means, 0, 1)  # Keep means within [0, 1] bounds

class Agent:

    def _init_(self, nActions, eps):
        self.nActions = nActions
        self.eps = eps
        self.n = np.zeros(nActions, dtype=np.int) # action counts n(a)
        self.Q = np.zeros(nActions, dtype=np.float) # value Q(a)

    def update_Q(self, action, reward):
        # Update Q action-value given (action, reward)
        self.n[action] += 1
        self.Q[action] += (1.0/self.n[action]) * (reward - self.Q[action])

    def get_action(self):
        # Epsilon-greedy policy
        if np.random.random() < self.eps: # explore
            return np.random.randint(self.nActions)
        else: # exploit
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max()))

# Start multi-armed bandit simulation
def experiment(env, agent, N_episodes):
    actions, rewards = [], []
    for episode in range(N_episodes):
        action = agent.get_action() # sample policy
        reward = env.step(action) # take step + get reward
        agent.update_Q(action, reward) # update Q
        actions.append(action)
        rewards.append(reward)
        env.update_means()  # Update the mean rewards with random walk
    return np.array(actions), np.array(rewards)

# Settings
n_arms = 10  # number of arms
N_experiments = 1000  # number of experiments to perform
N_steps = 500  # number of steps (episodes)
eps = 0.1  # probability of random exploration (fraction)
save_fig = True  # save file in the same directory
output_dir = os.path.join(os.getcwd(), "output")

# Run multi-armed bandit experiments
print(f"Running multi-armed bandits with nActions = {n_arms}, eps = {eps}")
R = np.zeros((N_steps,))  # reward history sum
A = np.zeros((N_steps, n_arms))  # action history sum
for i in range(N_experiments):
    env = Environment(n_arms)  # initialize environment with dynamic means
    agent = Agent(n_arms, eps)  # initialize agent
    actions, rewards = experiment(env, agent, N_steps)  # perform experiment
    if (i + 1) % (N_experiments / 100) == 0:
        print(f"[Experiment {i + 1}/{N_experiments}] n_steps = {N_steps}, reward_avg = {np.sum(rewards) / len(rewards)}")
    R += rewards
    for j, a in enumerate(actions):
        A[j][a] += 1

# Plot reward results
R_avg = R / np.float(N_experiments)
plt.plot(R_avg, ".")
plt.xlabel("Step")
plt.ylabel("Average Reward")
plt.grid()
ax = plt.gca()
plt.xlim([1, N_steps])
if save_fig:
    if not os.path.exists(output_dir): os.mkdir(output_dir)
    plt.savefig(os.path.join(output_dir, "rewards.png"), bbox_inches="tight")
else:
    plt.show()
plt.close()

# Plot action results
for i in range(n_arms):
    A_pct = 100 * A[:, i] / N_experiments
    steps = list(np.array(range(len(A_pct))) + 1)
    plt.plot(steps, A_pct, "-",
             linewidth=4,
             label=f"Arm {i + 1}")
plt.xlabel("Step")
plt.ylabel("Count Percentage (%)")
leg = plt.legend(loc='upper left', shadow=True)
plt.xlim([1, N_steps])
plt.ylim([0, 100])
for legobj in leg.legendHandles:
    legobj.set_linewidth(4.0)
if save_fig:
    if not os.path.exists(output_dir): os.mkdir(output_dir)
    plt.savefig(os.path.join(output_dir, "actions.png"), bbox_inches="tight")
else:
    plt.show()
plt.close()