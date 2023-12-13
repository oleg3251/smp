import logging

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# Analyze financial data from file
class MonthlyFinancialAnalyzer:
    # Constructor
    def __init__(self, csv_file_path):
        logging.info('Initialize finance analyzer')
        self.df = pd.read_csv(csv_file_path)

    # Explores financial data
    def explore_monthly_financial_data(self):
        logging.info('Exploring financial data')
        min_values = self.df.min()
        max_values = self.df.max()

        print("Minimum values:")
        print(min_values)

        print("\nMaximum values:")
        print(max_values)

    # Shows total income distribution
    def plot_total_income_distribution(self):
        logging.info('Showing total income distribution')
        total_income_distribution = self.df
        total_income_distribution.plot(kind='pie', y='Total_Income', autopct='%1.1f%%',
                                       title='Total Income Distribution')
        plt.show()

    # Shows expenses distribution
    def plot_expenses_distribution(self):
        logging.info('Showing expenses distribution')
        expenses_distribution = self.df
        expenses_distribution.plot(kind='bar', x='Month', y='Expenses',
                                   xlabel='Month', ylabel='Expenses (Dollars)', title='Monthly Expenses Distribution')
        plt.show()

    # Shows profit distribution
    def plot_profit_distribution(self):
        logging.info('Showing profit distribution')
        profit_distribution = self.df
        profit_distribution.plot(kind='bar', x='Month', y='Profit',
                                 xlabel='Month', ylabel='Profit (Dollars)', title='Monthly Profit Distribution')
        plt.show()

    # Shows all monthly plots
    def show_all_monthly_plots(self):
        logging.info('Showing all monthly plot')
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        self.plot_total_income_distribution_subplot(axes[0, 0])
        self.plot_expenses_distribution_subplot(axes[0, 1])
        self.plot_profit_distribution_subplot(axes[1, 0])
        plt.savefig('files/monthly_plot.png')
        self.plot_expenses_distribution_plotly()
        plt.show()

    # Sets total income distribution
    def plot_total_income_distribution_subplot(self, ax):
        logging.info('Setting total income distribution')
        total_income_distribution = self.df
        ax.pie(total_income_distribution['Total_Income'], autopct='%1.1f%%',
               labels=total_income_distribution['Month'], startangle=90)
        ax.set_title('Total Income Distribution')

    # Sets expenses distribution
    def plot_expenses_distribution_subplot(self, ax):
        logging.info('Setting expenses distribution')
        expenses_distribution = self.df
        ax.bar(expenses_distribution['Month'], expenses_distribution['Expenses'])
        ax.set_xlabel('Month')
        ax.set_ylabel('Expenses (Dollars)')
        ax.set_title('Monthly Expenses Distribution')

    # Setts profit distribution
    def plot_profit_distribution_subplot(self, ax):
        logging.info('Setting profit distribution')
        profit_distribution = self.df
        ax.bar(profit_distribution['Month'], profit_distribution['Profit'])
        ax.set_xlabel('Month')
        ax.set_ylabel('Profit (Dollars)')
        ax.set_title('Monthly Profit Distribution')

    # Sets expenses distribution
    def plot_expenses_distribution_plotly(self):
        logging.info('Setting expenses distribution')
        fig = px.bar(self.df, x='Month', y='Expenses', title='Monthly Expenses Distribution')
        fig.write_html('files/monthly_plot.png')
