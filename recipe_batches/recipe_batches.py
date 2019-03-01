#!/usr/bin/python

#Didn't need to use the math library
import math

def recipe_batches(recipe, ingredients):
  if len(recipe) is not len(recipe):
    return 0
  # Keeping track of how many times recipe divided by ingredients
  count = []
  # Iterate through recipe as the first loop because it set the standard
  # ingredients needed to fulfill the recipe
  for recipe_name, recipe_value in recipe.items():
    #Iterate the ingredients and check for matching key values
    for ingredient_name, ingredient_value in ingredients.items():
      #Comparing for matching key values
      if recipe_name == ingredient_name:
        #Add into the list variable count of the quotient of ingredients divided by recipe
        count.append(ingredient_value // recipe_value)
      #Comparing if the key in recipe match up with ingredients

  #This will return the lowest number of each ingredients
  return min(count)


# -- Understanding the Problem
# - Need to make comparison from ingredients to recipe
# - Return the amount of batches that can be made with ingredients
# 
# -- Make a Plan
# - Iterate through recipe and ingredients comparing the key / values
# - First Loop will be the recipe since it is setting precendences
# - Second Loop will be the ingredients, if it key match with recipe key, then divide put into the list
# -- Carry out a Plan
#
#
# -- Improve on the result

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 51, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))