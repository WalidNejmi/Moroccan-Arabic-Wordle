# Moroccan Wordle

A culturally-tailored version of the popular word-guessing game, designed specifically for Arabic speakers.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Implementation](#implementation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Full Arabic language support
- Customizable word length (currently set to 5 letters)
- Color-coded feedback using ANSI codes
- Point-based scoring system
- Both console and graphical (PyGame) versions

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/moroccan-wordle.git
   ```
2. Navigate to the project directory:
   ```
   cd moroccan-wordle
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Implementation

### Console Version
- Implemented in Python
- Uses text files for word storage (e.g., `5.txt` for 5-letter words)
- Employs ANSI color codes for visual feedback

### Graphical Version
- Built with PyGame
- Features custom background and Arabic font
- Provides real-time visual feedback and error messages

## Testing

- Input validation for various scenarios
- Word list integrity checks
- Scoring system accuracy verification
- Color display consistency across terminals
- Performance optimization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.