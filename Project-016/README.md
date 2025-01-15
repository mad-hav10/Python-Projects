# Turtle Dot Pattern

This project uses Python's `turtle` graphics library to create a beautiful pattern of colored dots arranged in a grid. The dots are randomly chosen from a predefined list of RGB colors, creating a visually appealing mosaic.

## Requirements

- Python 3.x
- `turtle` graphics library (comes pre-installed with Python)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/turtle-dot-pattern.git
   ```

2. Navigate to the project directory:

   ```bash
   cd turtle-dot-pattern
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

## How It Works

The script creates a grid of dots with the following steps:

1. **Color List**: A list of RGB color values is defined, and the turtle randomly selects one color for each dot.
2. **Turtle Setup**: The turtle starts at a specific position on the screen, facing a certain direction.
3. **Movement**: The turtle moves across the screen, drawing a dot at each position. After completing a row, it moves to the next row to continue drawing.
4. **Pattern**: The turtle draws 10 rows of 10 dots each, with the colors randomly selected from the list.

## Features

- **Random Colors**: Each dot is randomly colored using an RGB value.
- **Grid Layout**: The dots are arranged in a grid of 10 rows and 10 columns.
- **Interactive**: The screen remains open until you click on it to exit.

## Example

![Dot Pattern Example](example_image.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
