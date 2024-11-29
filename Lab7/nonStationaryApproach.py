<<<<<<< HEAD
import os
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

class Environment:
    def __init__(self, probs):
        self.probs = probs  # success probabilities for each arm

    def step(self, action):
        # Pull arm and get stochastic reward (1 for success, 0 for failure)
        return 1 if (np.random.random() < self.probs[action]) else 0

class Agent:
    def __init__(self, nActions, eps, alpha):
        self.nActions = nActions
        self.eps = eps
        self.alpha = alpha
        self.Q = np.zeros(nActions, dtype=np.float64)  # action-value estimates Q(a)

    def update_Q(self, action, reward):
        # Update Q action-value using the non-stationary reward formula
        self.Q[action] += self.alpha * (reward - self.Q[action])

    def get_action(self):
        # Epsilon-greedy policy
        if np.random.random() < self.eps:  # explore
            return np.random.randint(self.nActions)
        else:  # exploit
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max()))

# Start multi-armed bandit simulation
def experiment(probs, N_episodes, agent):
    env = Environment(probs)  # initialize arm probabilities
    actions, rewards = [], []
    for episode in range(N_episodes):
        action = agent.get_action()  # sample policy
        reward = env.step(action)  # take step + get reward
        agent.update_Q(action, reward)  # update Q
        actions.append(action)
        rewards.append(reward)
    return np.array(actions), np.array(rewards)

# Settings
probs = [0.10, 0.50, 0.60, 0.80, 0.10,
         0.25, 0.60, 0.45, 0.75, 0.65]  # bandit arm probabilities of success
N_experiments = 10000  # number of experiments to perform
N_steps = 1000  # number of steps (episodes)
eps = 0.1  # probability of random exploration (fraction)
alpha = 0.1  # learning rate
save_fig = True  # save file in same directory
output_dir = os.path.join(os.getcwd(), "output")

# Run multi-armed bandit experiments
print("Running multi-armed bandits with nActions = {}, eps = {}, alpha = {}".format(len(probs), eps, alpha))
R = np.zeros((N_steps,))  # reward history sum
A = np.zeros((N_steps, len(probs)))  # action history sum
for i in range(N_experiments):
    agent = Agent(len(probs), eps, alpha)  # initialize agent for each experiment
    actions, rewards = experiment(probs, N_steps, agent)  # perform experiment
    if (i + 1) % (N_experiments / 100) == 0:
        print("[Experiment {}/{}] ".format(i + 1, N_experiments) +
              "n_steps = {}, ".format(N_steps) +
              "reward_avg = {}".format(np.sum(rewards) / len(rewards)))
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
for i in range(len(probs)):
    A_pct = 100 * A[:, i] / N_experiments
    steps = list(np.array(range(len(A_pct))) + 1)
    plt.plot(steps, A_pct, "-",
             linewidth=4,
             label="Arm {} ({:.0f}%)".format(i + 1, 100 * probs[i]))
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
=======
import os
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

class Environment:
    def __init__(self, probs):
        self.probs = probs  # success probabilities for each arm

    def step(self, action):
        # Pull arm and get stochastic reward (1 for success, 0 for failure)
        return 1 if (np.random.random() < self.probs[action]) else 0

class Agent:
    def __init__(self, nActions, eps, alpha):
        self.nActions = nActions
        self.eps = eps
        self.alpha = alpha
        self.Q = np.zeros(nActions, dtype=np.float64)  # action-value estimates Q(a)

    def update_Q(self, action, reward):
        # Update Q action-value using the non-stationary reward formula
        self.Q[action] += self.alpha * (reward - self.Q[action])

    def get_action(self):
        # Epsilon-greedy policy
        if np.random.random() < self.eps:  # explore
            return np.random.randint(self.nActions)
        else:  # exploit
            return np.random.choice(np.flatnonzero(self.Q == self.Q.max()))

# Start multi-armed bandit simulation
def experiment(probs, N_episodes, agent):
    env = Environment(probs)  # initialize arm probabilities
    actions, rewards = [], []
    for episode in range(N_episodes):
        action = agent.get_action()  # sample policy
        reward = env.step(action)  # take step + get reward
        agent.update_Q(action, reward)  # update Q
        actions.append(action)
        rewards.append(reward)
    return np.array(actions), np.array(rewards)

# Settings
probs = [0.10, 0.50, 0.60, 0.80, 0.10,
         0.25, 0.60, 0.45, 0.75, 0.65]  # bandit arm probabilities of success
N_experiments = 10000  # number of experiments to perform
N_steps = 1000  # number of steps (episodes)
eps = 0.1  # probability of random exploration (fraction)
alpha = 0.1  # learning rate
save_fig = True  # save file in same directory
output_dir = os.path.join(os.getcwd(), "output")

# Run multi-armed bandit experiments
print("Running multi-armed bandits with nActions = {}, eps = {}, alpha = {}".format(len(probs), eps, alpha))
R = np.zeros((N_steps,))  # reward history sum
A = np.zeros((N_steps, len(probs)))  # action history sum
for i in range(N_experiments):
    agent = Agent(len(probs), eps, alpha)  # initialize agent for each experiment
    actions, rewards = experiment(probs, N_steps, agent)  # perform experiment
    if (i + 1) % (N_experiments / 100) == 0:
        print("[Experiment {}/{}] ".format(i + 1, N_experiments) +
              "n_steps = {}, ".format(N_steps) +
              "reward_avg = {}".format(np.sum(rewards) / len(rewards)))
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
for i in range(len(probs)):
    A_pct = 100 * A[:, i] / N_experiments
    steps = list(np.array(range(len(A_pct))) + 1)
    plt.plot(steps, A_pct, "-",
             linewidth=4,
             label="Arm {} ({:.0f}%)".format(i + 1, 100 * probs[i]))
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
>>>>>>> c233d70a206ccb7319170a0a637b305b3060019a
