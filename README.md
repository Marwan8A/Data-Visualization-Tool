
# Data Visualization Tool

A Python command-line application for loading, filtering, sorting, and visualizing character statistics from CSV files. Supports both interactive commands and batch processing.

## Features

- **CSV Data Management:** Load and filter character data by occupation, weapon, strength, or luck.
- **Sorting Algorithms:** Sort records by agility, armor, intelligence, or health in ascending or descending order using bubble sort, selection sort, and insertion sort.
- **Data Visualization:** Generate attribute frequency charts using Matplotlib.
- **Curve Fitting:** Calculate polynomial best-fit equations to analyze relationships between character attributes and health using NumPy.
- **Batch Processing:** Execute multiple commands from a text file.

## Technologies

- Python
- NumPy
- Matplotlib

## Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd Data-Visualization-Project
```

### 2. Install Dependencies

```bash
pip install numpy matplotlib
```

### 3. Prepare a CSV File

The application expects character data with the following columns:

```text
Occupation,Strength,Agility,Stamina,Personality,Intelligence,Luck,Armor,Weapon
```

**Note:** A sample CSV dataset is not included in the repository.

### 4. Run the Application

For interactive mode:

```bash
python text_UI.py
```

Available commands:

| Command | Description |
|---------|-------------|
| L | Load and filter CSV data |
| S | Sort loaded records |
| C | Calculate a polynomial curve fit |
| H | Generate a histogram |
| E | Exit the application |

For batch mode:

```bash
python batch_UI.py
```

Enter the path to a text file containing semicolon-separated commands, one per line.

Example:

```text
L;characters.csv;All
S;A;Agility;Y
H;Strength
E
```

## Project Structure

| File | Description |
|------|-------------|
| `text_UI.py` | Interactive command-line interface |
| `batch_UI.py` | Batch command processing |
| `load_data.py` | CSV loading, filtering, and health calculations |
| `sort.py` | Sorting algorithm implementations |
| `histogram.py` | Data visualization using Matplotlib |
| `curve_fit.py` | Polynomial curve fitting using NumPy |

## Notes

- The application requires a CSV file following the specified character-statistics schema.
- Matplotlib charts open in a separate window.
- The repository contains the source code but does not include a sample dataset or automated test suite.
