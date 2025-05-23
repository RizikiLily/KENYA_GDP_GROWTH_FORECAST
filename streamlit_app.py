import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from preliminary import preliminary_data
from sarima import sarima_forecast

st.set_page_config(page_title="Kenya GDP Growth Forecast", layout="wide")

def main():
    st.title("Kenya GDP Growth Forecast App")
    st.write("Upload quarterly GDP data to generate GDP growth forecasts using SARIMA.")
    uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

    if uploaded_file:
        raw_df = pd.read_csv(uploaded_file, parse_dates=['Date'])
        raw_df.set_index("Date", inplace=True)
        #Preprocess
        cleaned_df = preliminary_data(raw_df)
        #Forecast
        forecast_df = sarima_forecast(cleaned_df, periods=8)
        #Check shapes
        #st.write("Shape of historical GDP growth:", cleaned_df["gdp_growth"].shape)
        #st.write("Shape of forecast data:", forecast_df["Forecast"].shape)

        #Plot actual + forecast
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(cleaned_df.index, cleaned_df["gdp_growth"], label="Historical GDP Growth", marker="o")
        ax.plot(forecast_df.index, forecast_df["Forecast"], label="Forecasted GDP Growth", linestyle="--", marker="x")
        ax.set_title("Kenya Quarterly GDP Growth Forecast")
        ax.set_xlabel("Date")
        ax.set_ylabel("Growth Rate")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        #Show tables
        st.subheader("Forecast Data")
        st.write(forecast_df)

if __name__ == "__main__":
    main()