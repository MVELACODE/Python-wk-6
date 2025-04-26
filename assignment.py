import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset
    dataset_path = "your_dataset.csv"  # Replace with the path to your dataset
    data = pd.read_csv(dataset_path)
    
    # Display the first few rows
    print("First few rows of the dataset:")
    print(data.head())
    
    # Explore the structure of the dataset
    print("\nDataset Info:")
    print(data.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())
    
    # Clean the dataset (fill or drop missing values)
    data = data.dropna()  # Dropping rows with missing values
    print("\nDataset after cleaning:")
    print(data.info())

except FileNotFoundError:
    print("Error: The dataset file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(data.describe())
    
    # Perform groupings and compute mean
    # Replace 'categorical_column' and 'numerical_column' with actual column names
    categorical_column = "your_categorical_column"  # Replace with a categorical column
    numerical_column = "your_numerical_column"  # Replace with a numerical column
    grouped_data = data.groupby(categorical_column)[numerical_column].mean()
    print(f"\nMean of {numerical_column} grouped by {categorical_column}:")
    print(grouped_data)
    
except KeyError:
    print("Error: One or more specified columns do not exist in the dataset.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 3: Data Visualization
try:
    # Line chart
    plt.figure(figsize=(10, 6))
    # Replace 'time_column' and 'value_column' with actual column names
    time_column = "your_time_column"  # Replace with a time-related column
    value_column = "your_value_column"  # Replace with a numerical column
    plt.plot(data[time_column], data[value_column], marker='o')
    plt.title("Line Chart")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.show()
    
    # Bar chart
    plt.figure(figsize=(10, 6))
    grouped_data.plot(kind='bar', color='skyblue')
    plt.title("Bar Chart")
    plt.xlabel(categorical_column)
    plt.ylabel(f"Average {numerical_column}")
    plt.show()
    
    # Histogram
    plt.figure(figsize=(10, 6))
    # Replace 'numerical_column' with an actual numerical column
    sns.histplot(data[numerical_column], kde=True, bins=20, color='purple')
    plt.title("Histogram")
    plt.xlabel(numerical_column)
    plt.ylabel("Frequency")
    plt.show()
    
    # Scatter plot
    plt.figure(figsize=(10, 6))
    # Replace 'numerical_column_x' and 'numerical_column_y' with actual column names
    numerical_column_x = "your_numerical_column_x"  # Replace with a numerical column
    numerical_column_y = "your_numerical_column_y"  # Replace with another numerical column
    sns.scatterplot(x=data[numerical_column_x], y=data[numerical_column_y], hue=data[categorical_column])
    plt.title("Scatter Plot")
    plt.xlabel(numerical_column_x)
    plt.ylabel(numerical_column_y)
    plt.legend(title=categorical_column)
    plt.show()

except KeyError:
    print("Error: One or more specified columns do not exist in the dataset.")
except Exception as e:
    print(f"An error occurred: {e}")