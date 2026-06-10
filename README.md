# Fictional Eureka - Collection of Interactive Pygame Applications

A comprehensive collection of interactive Python applications built with Pygame, featuring games, tools, and utilities.

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

### 3. 🌦️ Weather Dashboard
A real-time weather dashboard fetching data from OpenWeatherMap API displaying weather for 6 major cities.

**Features:**
- Real-time weather data from OpenWeatherMap API
- 6 global cities with weather information
- Current temperature, feels like, humidity, pressure, wind speed
- Weather description with emoji icons
- Detailed weather cards for quick info
- Interactive city selector buttons
- Auto-refresh every 60 seconds
- Manual refresh with R key

**Included Cities:**
- 🗽 New York
- 🇬🇧 London
- 🗾 Tokyo
- 🇦🇺 Sydney
- 🇦🇪 Dubai
- 🌴 Los Angeles

**Run:**
```bash
python weather_dashboard.py
```

**Controls:**
- **Mouse Click** - Select different cities
- **R Key** - Manual refresh
- Auto-updates every minute

---

### 4. 😂 Random Joke Generator
A fun joke generator with multiple API sources and a favorites system.

**Features:**
- Multiple joke API sources (Official Joke API, JokeAPI, Random User Jokes)
- Random joke generation
- Favorites system (save your funny jokes!)
- Joke history tracking (last 50 jokes)
- Statistics dashboard
- Color-coded joke categories
- Interactive UI with easy controls

**Run:**
```bash
python joke_generator.py
```

**Controls:**
- **SPACE** - Generate new joke
- **Mouse Click** - Navigate buttons
- **"🔄 Next Joke"** - Get a new joke
- **"❤️ Favorite"** - Save to favorites
- **"📜 History"** - View past jokes
- **ESC** - Close history popup

---

### 5. ✓ To-Do List Application
A full-featured to-do list application with local JSON storage and task management.

**Features:**
- Add, complete, and delete tasks
- Task priority levels (Low, Normal, High)
- Color-coded priority indicators
- Filter tasks (All, Active, Completed)
- Sort tasks (By Date, By Priority)
- Task statistics dashboard
- Local JSON file storage (automatic save/load)
- Persistent data between sessions
- Task creation with timestamps
- Keyboard and mouse controls

**Run:**
```bash
python todo_app.py
```

**Controls:**
- **Click on input box** - Add new task
- **Type task name** - Enter task description
- **ENTER** - Save task
- **Click priority buttons** - Set priority level
- **Click checkbox** - Mark task complete
- **Click ✕** - Delete task
- **Click filter buttons** - Filter view
- **Click sort buttons** - Change sort order

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
- requests 2.31.0

## Project Structure

```
fictional-eureka/
├── simple_car_prototype.py       # 🚗 Car driving simulator
├── digital_clock_timezones.py    # ⏰ World clock
├── weather_dashboard.py          # 🌦️ Weather dashboard
├── joke_generator.py             # 😂 Joke generator
├── todo_app.py                   # ✓ To-do list
├── todos.json                    # 💾 Task storage (auto-created)
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Data Storage

- **To-Do List**: Tasks are automatically saved to `todos.json` in the application directory
- **Joke History**: Stored in memory during the session
- **Weather Data**: Fetched in real-time, no local storage

## Features by Application

| Feature | Car | Clock | Weather | Jokes | To-Do |
|---------|-----|-------|---------|-------|-------|
| Real-time Data | - | ✓ | ✓ | - | ✓ |
| Local Storage | - | - | - | Memory | JSON |
| API Integration | - | - | ✓ | ✓ | - |
| Interactive UI | ✓ | ✓ | ✓ | ✓ | ✓ |
| Multiple Items | ✓ | ✓ | ✓ | ✓ | ✓ |
| Statistics | - | - | ✓ | ✓ | ✓ |

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

### Weather Dashboard:
- [ ] 5-day forecast
- [ ] Weather alerts
- [ ] More cities (customizable)
- [ ] Historical weather data
- [ ] UV index information

### Joke Generator:
- [ ] Joke categories (programming, knock-knock, etc.)
- [ ] Joke sharing functionality
- [ ] Export favorites
- [ ] Dark/Light theme toggle
- [ ] Multilingual jokes

### To-Do List:
- [ ] Due date reminders
- [ ] Task categories/tags
- [ ] Cloud synchronization
- [ ] Recurring tasks
- [ ] Export to CSV
- [ ] Search functionality
- [ ] Dark/Light theme toggle

## License

MIT License - Feel free to use and modify!

## Author

rajputhasnain816-ship-it

## Contributing

Feel free to fork, modify, and submit pull requests to improve these projects!

## Getting Started

1. **Clone the repo** and install dependencies
2. **Pick an application** and run it:
   ```bash
   python simple_car_prototype.py
   python digital_clock_timezones.py
   python weather_dashboard.py
   python joke_generator.py
   python todo_app.py
   ```
3. **Enjoy!** Each application is self-contained and ready to use.

---

**Happy coding! 🚀**
