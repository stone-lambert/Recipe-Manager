import random
from collections import ChainMap
from stack import Stack
from queue import Queue 
from tree import Tree

def get_defaut_recipe():

    tree_root = Tree("Fried Eggs", None)
    data_list = ["Eggs", "Salt", "Pepper", "Butter"]
    children = []
    for data in data_list:
        child = Tree(data, tree_root)
        children.append(child)
    for child in children:
        tree_root.add_child(child)
    
    ingredients = ["Eggs", "Salt", "Pepper", "Butter"]
    default_recipe_ingredients = {}
    for ingredient in ingredients:
        default_recipe_ingredients[ingredient] = random.randint(10000, 99999)
    
    steps = ["Turn on pan to medium high heat", "Take butter out the fridge and let sit for at least an hour",
    "Take out salt and pepper", "Take out eggs"]
    default_recipe_preperation = Stack()
    for step in steps:
        default_recipe_preperation.push(step)
    
    steps = ["Add butter to pan and let it melt", "Crack the egg", "Add egg to pan",
    "Add salt and pepper", "Flip after 5 minutes", "Take off pan after 2 minutes"]
    default_recipe_steps = Queue()
    for step in steps:
        default_recipe_steps.enqueue(step)
        
    return [tree_root, default_recipe_ingredients, default_recipe_preperation, default_recipe_steps]
    
def display_ingredients(root, level=0):
    print("    "*level + "- " + str(root.data))
    for child in root.children:
        display_ingredients(child, level+1)

def get_custom_recipe():
    
    recipe_name = input("What is the name of your recipe? ")
    tree_root = Tree(recipe_name, None)
    
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or type 'done' to finish): ")
        if ingredient == 'done':
            break
        ingredients.append(ingredient)
    
    children = []
    for data in ingredients:
        child = Tree(data, tree_root)
        children.append(child)
    for child in children:
        tree_root.add_child(child)
    
    custom_recipe_ingredients = {}
    for ingredient in ingredients:
        custom_recipe_ingredients[ingredient] = random.randint(10000, 99999)
    
    custom_recipe_preperation = Stack()
    print("\nNow enter your preparation steps, in order.")
    while True:
        step = input("Enter a preparation step (or type 'done' to finish): ")
        if step == 'done':
            break
        custom_recipe_preperation.push(step)
    
    custom_recipe_steps = Queue()
    print("\nNow enter your cooking steps, in order.")
    while True:
        step = input("Enter a cooking step (or type 'done' to finish): ")
        if step == 'done':
            break
        custom_recipe_steps.enqueue(step)
        
    return [tree_root, custom_recipe_ingredients, custom_recipe_preperation, custom_recipe_steps]


user_input = input("Welcome to the Recipe Helper Program! Would you like to: \n1: make your own recipe, or \n2: follow the default recipe of Fried Eggs? ")

while user_input != "1" and user_input != "2":
    user_input = input("Please make a valid choice. ")
    
  if user_input == "1":
    
    recipe = get_custom_recipe()
    root = recipe[0]
    print("\nHere are the ingredients for the recipe:")
    display_ingredients(root)
    input("\nPlease hit enter when you are ready to move onto the next step.\n")
    
    ingredients = recipe[1]
    print("Here are the item codes at the store for each ingredient: ")
    for key, value in ingredients.items():
        print(key + ": " + str(value))
    input("\nPlease hit enter when you are ready to move onto the next step.\n")
    
    stack = recipe[2]
    print("Here are the preparation steps of the recipe. Hit enter when ready to move to the next step:")
    index = 1
    while stack.peek() != None:
        data = stack.pop()
        input(str(index) + ". " + str(data))
        index += 1 

    print()        
    queue = recipe[3]
    print("Here are the baking steps for the recipe. Hit enter when ready to move to the next step:")
    index = 1
    while queue.display() != None:
        data = queue.dequeue() 
        input(str(index) + ". " + str(data))
        index += 1
    
    print("\nEnjoy!")

if user_input == "2":
    
    recipe = get_defaut_recipe()
    root = recipe[0]
    print("\nHere are the ingredients for the recipe:")
    display_ingredients(root)
    input("\nPlease hit enter when you are ready to move onto the next step.\n")
    
    ingredients = recipe[1]
    print("Here are the item codes at the store for each ingredient: ")
    for key, value in ingredients.items():
        print(key + ": " + str(value))
    input("\nPlease hit enter when you are ready to move onto the next step.\n")
    
    stack = recipe[2]
    print("Here are the preparation steps of the recipe. Hit enter when ready to move to the next step:")
    index = 1
    while stack.peek() != None:
        data = stack.pop()
        input(str(index) + ". " + str(data))
        index += 1 

    print()        
    queue = recipe[3]
    print("Here are the baking steps for the recipe. Hit enter when ready to move to the next step:")
    index = 1
    while queue.display() != None:
        data = queue.dequeue() 
        input(str(index) + ". " + str(data))
        index += 1
    
    print("\nEnjoy!")
