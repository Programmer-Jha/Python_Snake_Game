# Python_Snake_Game
This is a classic Snake game built using Python’s Pygame library, enhanced with exciting new gameplay mechanics and user-friendly features. The game offers an engaging and visually appealing experience with smooth controls, real-time scoring, and a competitive high score tracking system.

## Features

- **Interactive Player Name Input:** Enter your name at the start for a personalized experience.
- **Smooth Controls:** Use arrow keys to navigate the snake around the game window.
- **Dynamic Food Items:**
  - Normal food appears as bright orange squares, increasing the snake’s length and score by 1 point.
  - Special “big ball” bonus food appears every 5 normal foods eaten. It’s a large purple circle with an 11-second countdown timer displayed inside it.
- **Time-Based Bonus Points:** The special food’s value starts at 11 points and decreases by 1 each second until it disappears, encouraging quick action.
- **Accurate Collision Detection:** Collision with walls, snake’s own body, and special food uses precise logic for fair gameplay.
- **Persistent High Score:** Saves and loads the highest score along with the player’s name in a file (`highscore.txt`).
- **Clean and Clear UI:** Displays current score and high score prominently during gameplay.

## How to Run

1. Make sure you have Python 3 installed.
2. Install Pygame if you haven't already:
```bash
pip install pygame
```
3. Download or clone this repository.
4. Run the game:
```bash
python Snake_Game.py
```

## Controls

- **Arrow Keys:** Move the snake up, down, left, and right.
- **C key:** Restart the game after a crash.
- **Q key:** Quit the game after a crash.

## Gameplay Tips

- Try to eat the special big ball as quickly as possible to maximize your points.
- Avoid hitting the walls or the snake’s own body.
- Compete against yourself by beating your high score!

## Project Structure

- `snake_game.py` — Main game code.
- `highscore.txt` — Stores the high score and player name (created automatically).

## Technologies Used

- Python 3
- Pygame library for game development

## License

This project is open-source and free to use.

---

Enjoy the game! Feel free to contribute or report issues.

## Developed By: Aniket Kumar Jha