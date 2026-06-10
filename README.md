# Fictional Eureka - Collection of Interactive Pygame Applications

A collection of interactive Python applications built with Pygame, featuring a car driving simulator and a world digital clock.

## Projects Included

### 1. 🚗 Simple Car Prototype
An interactive car driving simulator with physics-based movement and obstacle avoidance.

**Features:**
- Smooth acceleration and deceleration with friction
- Realistic rotation and steering
- Collision detection with multiple obstacles
- Real-time velocity and angle display
- Grid-based environment

**Run:**
```bash
python simple_car_prototype.py
```

**Controls:**
- **UP/DOWN** - Accelerate/Decelerate
- **LEFT/RIGHT** - Rotate
- **SPACE** - Reset position

---

### 2. ⏰ Digital Clock - Multiple Time Zones
A beautiful world clock displaying the current time across 6 major time zones with an interactive UI.

**Features:**
- Real-time clock for 6 different time zones
- Neon color-coded clocks for visual distinction
- Interactive selection - click to see detailed information
- Displays time, date, timezone name, and UTC offset
- Dark mode with glowing effects
- Automatic updates every second

**Included Time Zones:**
- 🗽 New York (EST)
- 🇬🇧 London (GMT)
- 🗾 Tokyo (JST)
- 🇦🇺 Sydney (AEDT)
- 🇦🇪 Dubai (GST)
- 🌴 Los Angeles (PST)

**Run:**
```bash
python digital_clock_timezones.py
```

**Controls:**
- **Mouse Click** - Click on any clock to view detailed information
- **Click Elsewhere** - Deselect the selected clock

---

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

## Requirements

- Python 3.7+
- Pygame 2.5.0
- pytz 2024.1

## Project Structure

```
fictional-eureka/
├── simple_car_prototype.py       # Car driving simulator
├── digital_clock_timezones.py    # World clock application
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Future Enhancements

### Car Prototype:
- [ ] Multiple game modes (racing, time trials)
- [ ] Sound effects and music
- [ ] Terrain types (grass, water, sand)
- [ ] Speed boost items
- [ ] Two-player mode

### Digital Clock:
- [ ] More time zones (customizable)
- [ ] Alarm functionality
- [ ] Different clock styles (analog, binary)
- [ ] Weather integration
- [ ] Geolocation-based timezone auto-detection

## License

MIT License - Feel free to use and modify!

## Author

rajputhasnain816-ship-it

## Contributing

Feel free to fork, modify, and submit pull requests to improve these projects!
