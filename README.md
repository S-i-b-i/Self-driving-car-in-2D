# 🏎️ 2D Self-Driving Car Simulation using Q-Learning

A 2D simulation of a self-driving car trained using **Q-Learning** to navigate a racetrack using virtual sensors. Built using **Pygame** and **NumPy**, this project demonstrates reinforcement learning in a simple car racing environment with a custom road track and car sprite.

---

## 📸 Demo

![Simulation Screenshot](assets/screenshot.png)

---

## 🚗 Features

- Custom racetrack and realistic car sprite
- Sensor-based input for environment awareness
- Q-Learning based decision-making agent
- Smooth movement using velocity and rotation
- Modular environment and agent code

---

## 🧠 Q-Learning Overview

The agent (car) learns to drive by interacting with the environment and improving its Q-table over time. It gets rewarded for moving forward and penalized for collisions or off-track behavior.

---

## 🛠️ Requirements

- Python 3.x
- `pygame`
- `numpy`

Install dependencies using:

```bash
pip install -r requirements.txt
