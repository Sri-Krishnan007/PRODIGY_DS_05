# PRODIGY_DS_05

# Accident Data Analysis

This project provides a basic exploratory data analysis (EDA) of a traffic accidents dataset using Python. The code generates summary statistics and visualizations to help understand accident patterns related to time, weather, severity, and location.

## Features

- **Libraries Used**: `pandas`, `numpy`, `seaborn`, `matplotlib`
- **Data Loading**: Reads a CSV file containing accident records.
- **Data Exploration**: Displays info, head, and missing values.
- **Datetime Processing**: Extracts day of week, month, and hour from the accident time.
- **Visualization**:
  - Accidents by day of the week
  - Accidents by month
  - Accidents by hour of the day
  - Accidents by weather conditions
  - Accidents by severity
  - Accident hotspots (scatter plot if latitude/longitude present)

## Usage

1. **Install dependencies**:
    ```
    pip install pandas numpy seaborn matplotlib
    ```

2. **Prepare your data**:
    - Place your accidents CSV file (e.g., `AccidentsBig.csv`) in a known location.
    - Update the `file_path` variable in the code to the full path of your dataset.

3. **Run the analysis**:
    - Execute the Python script in your environment. The script will generate various plots and display summary information.

4. **Interpreting results**:
    - The script prints dataset info, previews the first few rows, and shows missing values.
    - Count plots visualize accidents grouped by time and conditions.
    - A scatter plot maps accident hotspots if location data (`latitude`, `longitude`) is available.

## Notes

- Ensure your CSV file contains the following columns (or update code as needed):
    - `Time`: Timestamp of the accident
    - `Weather_Conditions`: Weather during the accident
    - `Accident_Severity`: Severity rating
    - `latitude`, `longitude`: Location data (for hotspot visualization)
- If your data has different column names, modify the script accordingly.
- The script assumes that the `Time` column is in a format directly convertible by `pd.to_datetime`.

## Example Plots

- Accidents by day of the week
- Accidents by month
- Accidents by hour
- Accidents by weather conditions
- Accident severity distribution
- Geographic distribution of accidents (hotspots)

## License

This project is provided for educational and exploratory purposes. Adapt and extend as needed for your data and requirements.
