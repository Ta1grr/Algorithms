#!/usr/bin/python

import argparse

def find_max_profit(prices):
    profit = min(prices) - max(prices)
    return profit

    # Buy = int
    # Sell = int
    # Selling = list
    # for i in range(0, len(prices)):
    #     if i <= prices[i]:
    #         Buy = prices[i]

#prices = [1050, 270, 1540, 3800, 2]

#Understanding the problem
# You can only buy once, then sell only at the largest profit.
# The indices inside list is unknown
# Need to figure out when I set to Buy

#Option 1:
# When looping through list, take index [0] as the first number as comparison
# Set the first lowest number as Buy
# Loop through the list and grab the lowest number, skip the last one because you have to sell.
# Then loop through the list and get the largest number

#Option 2:
# Create two variables, Buy and Sell
# Loop through list, 
# Compare from lowest, if it is lower, assign the lowest to Buy
# If Buy is an int, keep looping until Sell is replaced with largest int.
# If it's larger, replace larger.
# Once finish iterating through list, subtract largest from lowest
# Return the result of the difference.

#Notes:
# Could slice the rest off once Buy is assigned then loop through it again and compare to sell
# It has to iterate from left to right 
# When comparing the 1st number against the 2nd number, if it is lower, replace, if next number is greater than 
# min() = grab the smallest number
# max() = grab the largest number

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))