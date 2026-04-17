# Student Score Prediction using Machine Learning

## Overview

This project implements a basic Machine Learning model to predict a student's final score based on key factors such as hours studied, previous scores, and sleep hours. It uses a Linear Regression algorithm from scikit-learn.

## Features

* Data loading and preprocessing using pandas
* Training and testing split of dataset
* Model training using Linear Regression
* Prediction on test data
* Evaluation using Mean Absolute Error
* User input support for real-time prediction

## Technologies Used

* Python
* pandas
* scikit-learn

## Project Structure

* main.py: Contains the complete implementation of the machine learning model
* data.csv: Dataset used for training and testing the model

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/student-score-predictor.git

2. Navigate to the project directory:
   cd student-score-predictor

3. Install required dependencies:
   pip install pandas scikit-learn

## Usage

Run the following command to execute the program:
python main.py

The program will:

* Display the dataset
* Train the model
* Show predictions and error
* Allow you to input custom values for prediction

## Model Details

The model used in this project is Linear Regression. It establishes a relationship between independent variables (hours studied, previous scores, sleep hours) and the dependent variable (final score).

## Evaluation Metric

Mean Absolute Error (MAE) is used to evaluate the performance of the model.

## Future Improvements

* Add data visualization
* Improve model accuracy with advanced algorithms
* Convert the project into a web application
* Add a user interface

## License

This project is open-source and available for educational purposes.
