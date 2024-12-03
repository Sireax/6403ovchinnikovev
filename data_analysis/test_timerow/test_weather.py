import unittest
import pandas as pd
from ..module.weather_code import WeatherDataContainer


class TestWeatherData(unittest.TestCase):

    def setUp(self):
        data = {
            'tavg': [20, 22, 21, 23, 24, 22, 20, 19, 21, 23]
        }
        self.df = pd.DataFrame(data)
        self.weather_data = WeatherDataContainer(self.df)

    def test_get_data(self):
        result = self.weather_data.get_data()
        self.assertTrue(result.equals(self.df))

    def test_moving_average(self):
        self.weather_data.moving_average(3)
        self.assertIn('moving_average_3', self.weather_data.data.columns)

    def test_calculate_difference(self):
        self.weather_data.calculate_difference()
        self.assertIn('temperature_difference', self.weather_data.data.columns)

    def test_autocorrelation(self):
        self.weather_data.auto_corr(1, 1)
        self.assertIn('autocorrelation_lag_1', self.weather_data.data.columns)


if __name__ == '__main__':
    unittest.main()
