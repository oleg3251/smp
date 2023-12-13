import logging

from Lab8.financial_data_visualizer import MonthlyFinancialAnalyzer
from utils import UserInputHelper


# Represents financial data visualizer interface
class FinancialDataInterface:

    def __init__(self):
        logging.info('Initialize financial data interface')
        self.__financial_data_visualizer = MonthlyFinancialAnalyzer('files/data.csv')

    def run(self):
        logging.info('Executing financial data visualizer')
        while True:
            option = UserInputHelper.get_limited_user_input(
                "1-Explore data\n2-Show total income\n3-Show expenses\n4-Show profit\n5-Show all plots\n0-exit\n",
                ['1', '2', '3', '4', '5', '0'])
            if option == '1':
                self.__financial_data_visualizer.explore_monthly_financial_data()
            elif option == "2":
                self.__financial_data_visualizer.plot_total_income_distribution()
            elif option == "3":
                self.__financial_data_visualizer.plot_expenses_distribution()
            elif option == "4":
                self.__financial_data_visualizer.plot_profit_distribution()
            elif option == "5":
                self.__financial_data_visualizer.show_all_monthly_plots()
            else:
                break
