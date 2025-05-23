
# 🇰🇪 Kenya GDP Growth Forecast App

A Streamlit web application that forecasts Kenya’s quarterly GDP growth using the SARIMA model. This tool allows users to upload GDP data, visualize trends, and generate reliable forecasts complete with confidence intervals.

## 🔍 Overview

This application enables:
- Uploading quarterly GDP data
- Preprocessing of GDP data to compute quarterly growth
- Forecasting GDP growth using SARIMA models
- Interactive visualization of historical and forecasted values
- Downloading forecasts as a CSV file

## 📊 Features

- **Interactive Forecast Horizon:** Choose between 4 to 16 future quarters
- **SARIMA Forecasting:** Uses `pmdarima` to automatically select the best seasonal ARIMA model
- **Confidence Intervals:** Visualizes uncertainty with shaded confidence bands
- **User Interface:** Clean and responsive design built with Streamlit
- **Download Option:** Export forecasts to CSV for further analysis

## 🚀 How to Run the App

### Step 1: Clone the Repository
```bash
git clone https://github.com/RizikiLily/gdp-growth-forecast-app.git
cd gdp-growth-forecast-app
````

### Step 2: Set Up the Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit App

```bash
streamlit run app.py
```

## 📁 Directory Structure

```
├── streamlit_app.py                 # Main Streamlit application
├── sarima.py              # SARIMA model forecast logic
├── preliminary.py         # Preprocessing script
└── README.md              # Project documentation
```

## 📋 Expected CSV Format

Upload a file that includes quarterly GDP values with the following structure:

| Date       | GDP Growth        |
| ---------- | ---------- |
| 2018-03-31 | 0.0167458  |
| 2018-06-30 | 0.3252453 |
| ...        | ...        |

* `Date`: Must be in YYYY-MM-DD format and represent quarterly dates.
* `GDP`: Raw GDP figures as float or integer values.

## 🔧 Dependencies

* streamlit
* pandas
* matplotlib
* pmdarima

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed improvements.

## 📄 License

This project is licensed under the MIT License.

## 👩🏽‍💻 Author

**Lillian Riziki**
Aspiring Data Scientist
[GitHub](https://github.com/your-username) • [LinkedIn](https://www.linkedin.com/in/lillian-riziki/)
