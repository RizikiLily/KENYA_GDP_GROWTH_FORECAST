import pandas as pd
from pmdarima import auto_arima

def sarima_forecast(df, periods = 8, alpha=0.05):
    df['gdp_growth'] = df['GDP'].pct_change()
    df = df.dropna()
    series = df['gdp_growth']
    model = auto_arima(
        series,
        seasonal=True,
        m=4,
        d=0,
        stepwise=True,
        trace=True,
        suppress_warnings=True
    )
    forecast, conf_int = model.predict(n_periods = periods, return_conf_int=True,alpha=alpha)
    #Generate future dates
    last_date = df.index[-1]
    future_dates = pd.date_range(start=last_date + pd.offsets.QuarterBegin(), periods=periods, freq='QS')
    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecast": forecast,
        "Lower_CI": conf_int[:,0],
        "Upper_CI": conf_int[:, 1]
        })
    forecast_df.set_index("Date", inplace=True)
    return forecast_df