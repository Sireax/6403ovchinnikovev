import numpy as np
import pandas as pd

from data_analysis.module.decorators import type_check


class DataAnalyzer:

    @type_check((pd.DataFrame,))
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def get_data(self) -> pd.DataFrame:
        return self.data

    def find_max(self, window: int) -> None:
        max_column = f'max_{window}'
        self.data[max_column] = self.data['tavg'].rolling(window=window).max()

    def find_min(self, window: int) -> None:
        max_column = f'min_{window}'
        self.data[max_column] = self.data['tavg'].rolling(window=window).min()

    @type_check((int,))
    def moving_average(self, window: int) -> None:
        ma_column = f'moving_average_{window}'
        self.data[ma_column] = self.data['tavg'].rolling(window=window).mean()

    @type_check((int,))
    def calculate_difference(self, window: int = 3) -> None:
        ma_column = f'moving_average_{window}'
        if ma_column not in self.data:
            self.moving_average(window)
        self.data['temperature_difference'] = self.data[ma_column].diff()

    @type_check((int, int,))
    def auto_corr(self, lag: int, window: int) -> None:
        ma_column = 'moving_average_' + str(window)
        if ma_column not in self.data.columns:
            self.moving_average(window)

        self.data[f'autocorrelation_lag_{lag}'] = self.data[ma_column].rolling(window=window).apply(
            lambda x: x.autocorr(lag=lag) if len(x) >= lag else np.nan
        )


if __name__ == "__main__":
    pass
