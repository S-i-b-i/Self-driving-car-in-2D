import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, FPS
from env.track import Track
from env.car import Car
from env.track import Track
from rl.q_learning import QLearningAgent
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, FPS

ACTIONS = [
    {'acc': 1, 'turn': 0},   # forward
    {'acc': 1, 'turn': -1},  # left
    {'acc': 1, 'turn': 1},   # right
    {'acc': 0, 'turn': -1},  # brake left
    {'acc': 0, 'turn': 1},   # brake right
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2D Self-Driving Car - Q Learning")
    clock = pygame.time.Clock()

    car = Car(300, 200)  
    track = Track()
    agent = QLearningAgent(state_size=5, action_size=len(ACTIONS))

    try:
        agent.load("models/q_table.pkl")
        print("Loaded saved Q-table.")
    except FileNotFoundError:
        print("No saved Q-table found. Starting fresh.")

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)
        track.draw(screen)

        state = car.sensor.readings
        action_index = agent.choose_action(state)
        car.update_rl(ACTIONS[action_index], track)  
        next_state = car.sensor.readings

        # Reward logic
        if track.is_colliding(car.x, car.y):
            reward = -100
            car.x, car.y, car.angle, car.speed = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0
        else:
            reward = 1

        agent.update(state, action_index, reward, next_state)
        car.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                agent.save("models/q_table.pkl")
                print("Q-table saved!")
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
