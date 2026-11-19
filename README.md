# 🐢 Turtle Crossing Game

A classic arcade-style street-crossing game built with Python's built-in `turtle` graphics module. Guide the turtle safely across multi-lane traffic to reach the top of the screen—each successful crossing increases your score and accelerates incoming vehicles.

---

## ✨ Features

* **Progressive Difficulty:** Traffic speed starts at `5` units per tick and increases by `10` units each time the player reaches the finish line.
* **Randomized Traffic Generation:** Dynamically spawns colorful vehicles across random vertical lanes.
* **Real-Time Collision Detection:** Continuously checks proximity between the player and active vehicles, triggering a `GAME OVER` state upon impact.
* **Live Score Tracking:** Displays and updates the player's current score at the top of the screen using a custom `Scoreboard` component.
* **Modular OOP Architecture:** Clean separation of responsibilities across dedicated modules (`Player`, `CarManager`, `Scoreboard`, and the main game loop).

---

## 📂 Project Structure

```text
turtle-crossing/
├── main.py           # Entry point, screen setup, input bindings, and main game loop
├── player.py         # Player turtle class, movement controls, and position reset logic
├── car_manager.py    # Vehicle spawning, movement updates, and speed scaling
├── scoreboard.py     # Score display, score increments, and Game Over rendering
└── README.md         # Project documentation
```

---

## 🛠️ Requirements

* **Python 3.x** (tested on Python 3.8+)
* No external third-party packages required—uses only Python standard library modules (`turtle`, `time`, `random`).

> **Note for Linux users:** If `tkinter` (required by `turtle`) is not pre-installed with your Python distribution, install it via your package manager (e.g., `sudo apt install python3-tk`).

---

## 🚀 Getting Started

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/your-username/turtle-crossing.git
   cd turtle-crossing
   ```

2. **Ensure module filenames match imports:**
   Make sure your files are named `main.py`, `player.py`, `car_manager.py`, and `scoreboard.py` inside the same directory.

3. **Run the game:**
   ```bash
   python main.py
   ```

---

## 🎮 Controls & Gameplay

| Key | Action |
| :--- | :--- |
| **`Up` Arrow** | Move the turtle forward (`10` units upward) |
| **Mouse Click** | Close the game window after `GAME OVER` |

### Rules
1. Start at the bottom of the screen `(0, -280)`.
2. Dodge oncoming horizontal traffic while moving upward.
3. Reach the finish line (`y >= 280`) to earn **+1 point**, reset to the starting position, and increase car speed.
4. Colliding with any car ends the game immediately.

---

## ⚙️ Customization

You can easily tweak gameplay balance by adjusting the constants at the top of each module:

* **`player.py`**
  * `MOVE_DISTANCE`: Distance the turtle moves per key press (default: `10`).
  * `FINISH_LINE_Y`: Vertical coordinate required to score (default: `280`).
* **`car_manager.py`**
  * `COLORS`: List of available vehicle colors.
  * `STARTING_MOVE_DISTANCE`: Initial car speed (default: `5`).
  * `MOVE_INCREMENT`: Speed boost added after each point scored (default: `10`).
* **`scoreboard.py`**
  * `FONT`: Font family, size, and style used for HUD text.
