# Flight Price Prediction

## Overview
This project aims to predict flight ticket prices based on various factors such as airline, departure time, arrival time, duration, total stops, and other relevant parameters. The model leverages machine learning techniques to provide accurate price predictions.

## Features
- Predicts flight ticket prices based on user input.
- Utilizes machine learning models like Linear Regression, Decision Tree, Random Forest, and XGBoost.
- Web interface for easy user interaction.
- Data preprocessing including handling missing values, feature encoding, and feature scaling.

## Dataset
The dataset used for training the model consists of flight details, including:
- Airline
- Date of journey
- Source
- Destination
- Route
- Duration
- Total stops
- Additional information
- Price (Target variable)

## Tech Stack
- **Programming Language**: Python
- **Libraries Used**: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Machine Learning Models**: Linear Regression, Decision Tree, Random Forest, XGBoost
- **Web Framework (Optional for Deployment)**: Flask/Streamlit

## Installation
1. Clone the repository:
 
     git clone https://github.com/AiswaryaAlluri/flight-price-prediction.git
   
3. Navigate to the project directory:
   
     cd flight-price-prediction

4. Install dependencies:
   
     pip install -r requirements.txt
   

## Usage
1. Run the Python script for training the model:

     python train_model.py

2. To launch the web application (if implemented):
      python app.py
   
4. Enter the required flight details in the web UI to get a predicted price.

## Model Performance
- Evaluation metrics such as RMSE, MAE, and R-squared are used to assess model accuracy.
- Hyperparameter tuning is performed to enhance prediction performance.

## Future Enhancements
- Integrating live flight data.
- Improving prediction accuracy with deep learning models.
- Deploying the model as a cloud-based API.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with improvements.

## License
This project is open-source and available under the MIT License.

