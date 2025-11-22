import streamlit as st
import gymnasium as gym
import numpy as np
import time

# Streamlit page config
st.set_page_config(page_title="Taxi RL Simulator", page_icon="🚕")

# Taxi passenger & destination coordinates
LOCATIONS = {0:(0,0), 1:(0,4), 2:(4,0), 3:(4,3)}

def render_grid(state):
    taxi_row = (state // 25) % 5
    taxi_col = (state // 5) % 5
    pass_loc = state % 5
    dest = (state // 125)

    grid = [["🟩" for _ in range(5)] for _ in range(5)]
    grid[0][0]=grid[0][4]=grid[4][0]=grid[4][3]="🟥"

    px, py = LOCATIONS[pass_loc] if pass_loc < 4 else (taxi_row, taxi_col)
    dx, dy = LOCATIONS[dest]

    grid[taxi_row][taxi_col] = "🚕"
    grid[px][py] = "🧍"
    grid[dx][dy] = "🏁"

    return "\n".join(["".join(r) for r in grid])

# Load trained models
Q_qlearning = np.load("models/qlearning.npy")
Q_sarsa = np.load("models/sarsa.npy")

# UI
st.title("🎮 Taxi-v3 Live Simulation — Graphical UI")
st.subheader("Visualize trained RL agent performance using Q-Learning or SARSA")

algorithm = st.selectbox("Select Algorithm", ["Q-Learning", "SARSA"])
episodes = st.slider("Episodes", 1, 5000, 10)
speed = st.slider("Playback Speed (seconds / step)", 0.001, 1.0, 0.08)

run = st.button("▶ Start Simulation")

# Simulation start
if run:
    env = gym.make("Taxi-v3")  # Using normal environment (no ANSI)

    Q = Q_qlearning if algorithm == "Q-Learning" else Q_sarsa
    placeholder = st.empty()
    total_reward = 0

    for ep in range(episodes):
        state, _ = env.reset()
        done = False

        while not done:
            action = np.argmax(Q[state])
            state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            total_reward += reward

            grid_ui = render_grid(state)
            placeholder.markdown(f"```\n{grid_ui}\n```")
            time.sleep(speed)

    st.success(f"🏁 Simulation Completed for {episodes} Episodes!")
    st.metric("Total Reward", total_reward)
    st.metric("Average Reward / Episode", round(total_reward / episodes, 2))

