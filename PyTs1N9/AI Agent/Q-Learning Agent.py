import random

SIZE = 5
GOAL = (4, 4)
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Q = {}

def move(state, action):
    x, y = state
    dx, dy = ACTIONS[action]
    return (
        max(0, min(SIZE - 1, x + dx)),
        max(0, min(SIZE - 1, y + dy))
    )

def values(state):
    return Q.setdefault(state, [0.0] * len(ACTIONS))

def choose_action(state, epsilon):
    if random.random() < epsilon:
        return random.randrange(len(ACTIONS))
    return max(range(len(ACTIONS)), key=lambda a: values(state)[a])

# 训练
for episode in range(5000):
    state = (0, 0)

    for _ in range(100):
        action = choose_action(state, epsilon=0.1)
        next_state = move(state, action)

        reward = 100 if next_state == GOAL else -1

        old_q = values(state)[action]
        future_q = max(values(next_state))

        values(state)[action] = old_q + 0.1 * (
            reward + 0.9 * future_q - old_q
        )

        state = next_state

        if state == GOAL:
            break

# 使用训练结果
state = (0, 0)
path = [state]

while state != GOAL:
    action = choose_action(state, epsilon=0)
    state = move(state, action)
    path.append(state)

print(path)