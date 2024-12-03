import unittest
import pandas as pd
from data_analysis.module.data_analyzer import DataAnalyzer


class TestWeatherData(unittest.TestCase):

    def setUp(self):
        data = {
            'tavg': [20, 22, 21, 23, 24, 22, 20, 19, 21, 23]
        }
        self.df = pd.DataFrame(data)
        self.data_analyzer = DataAnalyzer(self.df)

    def test_get_data(self):
        result = self.data_analyzer.get_data()
        self.assertTrue(result.equals(self.df))

    def test_moving_average(self):
        self.data_analyzer.moving_average(3)
        self.assertIn('moving_average_3', self.data_analyzer.data.columns)

    def test_calculate_difference(self):
        self.data_analyzer.calculate_difference()
        self.assertIn('temperature_difference', self.data_analyzer.data.columns)

    def test_autocorrelation(self):
        self.data_analyzer.auto_corr(1, 1)
        self.assertIn('autocorrelation_lag_1', self.data_analyzer.data.columns)


if __name__ == '__main__':
    unittest.main()
