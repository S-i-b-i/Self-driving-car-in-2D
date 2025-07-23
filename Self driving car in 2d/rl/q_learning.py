import numpy as np
import random
import pickle

class QLearningAgent:
    def __init__(self, state_size, action_size, alpha=0.1, gamma=0.95, epsilon=1.0,
                 epsilon_decay=0.995, epsilon_min=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

    def get_state_key(self, state):
        return tuple(int(s / 10) for s in state)

    def choose_action(self, state):
        key = self.get_state_key(state)
        if random.random() < self.epsilon or key not in self.q_table:
            return random.randint(0, self.action_size - 1)
        return int(np.argmax(self.q_table[key]))

    def update(self, state, action, reward, next_state):
        key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        if key not in self.q_table:
            self.q_table[key] = np.zeros(self.action_size)
        if next_key not in self.q_table:
            self.q_table[next_key] = np.zeros(self.action_size)

        best_future = np.max(self.q_table[next_key])
        self.q_table[key][action] = (1 - self.alpha) * self.q_table[key][action] + \
                                     self.alpha * (reward + self.gamma * best_future)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self, path="models/q_table.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self.q_table, f)

    def load(self, path="models/q_table.pkl"):
        with open(path, "rb") as f:
            self.q_table = pickle.load(f)
