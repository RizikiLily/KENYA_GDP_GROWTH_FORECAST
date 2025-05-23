import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from preliminary import preliminary_data
from sarima import sarima_forecast

# Streamlit page settings
st.set_page_config(page_title="Kenya GDP Growth Forecast", layout="wide")

def main():
    st.title("📈 Kenya GDP Growth Forecast App")
    st.write("Upload quarterly GDP data to generate GDP growth forecasts using SARIMA.")

    # File upload
    uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

    if uploaded_file:
        try:
            raw_df = pd.read_csv(uploaded_file, parse_dates=['Date'])
            raw_df.set_index("Date", inplace=True)
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            return

        # Preprocessing
        cleaned_df = preliminary_data(raw_df)

        # Forecasting period input
        forecast_periods = st.slider("Select forecast horizon (quarters)", min_value=4, max_value=16, step=4, value=8)

        # Forecast
        forecast_df = sarima_forecast(cleaned_df, periods=forecast_periods)

        # Plotting
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(cleaned_df.index, cleaned_df["gdp_growth"], label="Historical GDP Growth", marker="o")
        ax.plot(forecast_df.index, forecast_df["Forecast"], label="Forecasted GDP Growth", linestyle="--", marker="x")

        # Confidence intervals
        ax.fill_between(forecast_df.index,
                        forecast_df["Lower_CI"],
                        forecast_df["Upper_CI"],
                        color="gray",
                        alpha=0.3,
                        label="95% Confidence Interval")

        ax.set_title("Kenya Quarterly GDP Growth Forecast")
        ax.set_xlabel("Date")
        ax.set_ylabel("Growth Rate")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        # Show table
        st.subheader("📊 Forecast Data")
        st.dataframe(forecast_df)

        # Download button
        csv = forecast_df.to_csv().encode('utf-8')
        st.download_button(
            label="📥 Download Forecast CSV",
            data=csv,
            file_name='Kenya_gdp_growth_forecast.csv',
            mime='text/csv'
        )

    else:
        st.info("Please upload a CSV file with a 'Date' column and quarterly GDP data.")

if __name__ == "__main__":
    main()
