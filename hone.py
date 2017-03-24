import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
from pprint import pprint

logging.debug("Start of H.O.N.E")

#Check to see if ingredients for the chosen recipe are in the pantry
def checkRecipe(testRecipe,pantry): 
    ingTypes = ['required','optional'];
    if checkIngredients(testRecipe,pantry,ingTypes[0]):
        print('You have the required ingredients ...',end='')
        if checkIngredients(testRecipe,pantry,ingTypes[1]):
            print('and the optional ingredients!')
            return 'Have all ingredients'
        else:
            print('but not all the optional ingredients.')
            return 'Missing optional ingredients'
    else:
        print('You do not have the required ingredients.')
        return False;

# check either required or optional ingredients, called by checkRecipe
def checkIngredients(testRecipe,pantry,reqOrOpt):
    for thisIngredient in testRecipe[reqOrOpt]:
        if not(thisIngredient in pantry):
            return False
    return True;

# Reduced recipe list for testing. 
# Each is a dictionary with three keys: 'required' and 'optional' for ingredients, and 'instructions'.
recipes={"moussaka-lasagne":
            {"required":("lasagne","aubergine","sweet potato",
                "swede", "kidney beans", "butter beans", 
                "tinned tomato", "oxo", "pepper",
                "butter","flour","milk",), #cinnamon removed here
            "optional":("wine","cinnamon","rosemary",
                "basil","nutmeg"),
            "instructions":"roast the aubergine and sweet potatoes, make a white sauce with 50g butter and 1 pint of milk, the rest goes in a sauce pan"},
        "salmon":
            {"required":("salmon","new potatoes","rocket"),
            "optional":("balsamic vinegar", "salad cream", 
                "pepper", "pesto", "mustard", "olive oil"),
            "instructions":"bake salmon in foil 200C about 20 min. olive oil, balsamic vinegar and mustard make a dressing or you can add the pesto to the pasta before you cook it"},
        "roasted vegetables":
            {"required":("courgette", "carrot", "aubergine",
                "onions", "garlic", "salt", "pepper", "oil"),
            "optional":("butternut squash","sweet potato", 
                "chicken","swede"),
            "instructions":"slather in oil, season and roast for a good while, turning halfway through"}    
         }
logging.debug("recipes has been defined for these dishes:"+str(recipes.keys()))

pantry =('aubergine','salmon','new potatoes','rocket')
logging.debug(pantry)

# Initialise list of recipes you have the ingredients for - empty initially
# don't like having 'Have all ingredients' and 'Missing optional ingredients' hard coded twice
listOfApproved={'Have all ingredients':[],'Missing optional ingredients':[]}
for thisRecipe in recipes:
    print('Checking: ',thisRecipe,end='- ')
    ingredientsOwned = checkRecipe(recipes[thisRecipe],pantry)
    if ingredientsOwned:
        listOfApproved[ingredientsOwned].append(thisRecipe)

print(listOfApproved)

#identify which recipes have all of their required ingredients in the pantry and the value is not none

#create a shopping list of things that are none or low in the pantry
#if i buy the full pantry everytime i go shopping that's too much to carry and it probs wont last while i eat it
#think of some clever way of deciding what I should buy

#create simple way to add the things bought to the pantry, these may not exactly match the shopping list so should be adjustable

#create a simple way to adjust the pantry based on the chosen recipe that's made

#also a simple way to adjust any of the values in the pantry because it is wrong for unforseen reasons

logging.debug("end of program")
