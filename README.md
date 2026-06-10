# Fictional Eureka - Simple Car Prototype

An interactive car driving simulator built with Pygame. Control a car, navigate obstacles, and explore the game world!

## Features

- 🚗 **Smooth Car Physics** - Realistic acceleration, deceleration, and friction
- 🛑 **Collision Detection** - Hit obstacles and bounce back
- 🎮 **Intuitive Controls** - Arrow keys for movement and rotation
- 🎨 **Visual Feedback** - Real-time velocity and angle display
- 🏗️ **Obstacle Navigation** - Multiple obstacles to navigate around

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rajputhasnain816-ship-it/fictional-eureka.git
cd fictional-eureka
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python simple_car_prototype.py
```

## Controls

| Key | Action |
|-----|--------|
| **UP Arrow** | Accelerate forward |
| **DOWN Arrow** | Decelerate / Reverse |
| **LEFT Arrow** | Rotate counter-clockwise |
| **RIGHT Arrow** | Rotate clockwise |
| **SPACE** | Reset car position |

## Game Mechanics

- The car accelerates smoothly and gradually slows down with friction
- Maximum velocity is 15 units, reverse speed is 7.5 units
- Collision with obstacles reduces velocity by 20%
- The red dot on the car indicates the front direction
- Grid background helps visualize movement

## Project Structure

```
fictional-eureka/
├── simple_car_prototype.py   # Main game file
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Future Enhancements

- [ ] Multiple game modes (racing, time trials)
- [ ] Sound effects and music
- [ ] Terrain types (grass, water, sand)
- [ ] Speed boost items
- [ ] Two-player mode
- [ ] Score/leaderboard system

## License

MIT License - Feel free to use and modify!

## Author

rajputhasnain816-ship-it
