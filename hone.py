#!/usr/bin/env python
import logging
#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug("Start of H.O.N.E")

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
        #print('You do not have the required ingredients.')
        return False;

def checkIngredients(testRecipe,pantry,reqOrOpt):
    for thisIngredient in testRecipe[reqOrOpt]:
        if (thisIngredient not in pantry) or pantry[thisIngredient]=='none':
            return False
    return True;


recipes={"moussaka-lasagne":
            {"required":("lasagne","aubergine","sweet potato",
                "swede", "kidney beans", "butter beans", 
                "tinned tomato", "oxo", "pepper",
                "butter","flour","milk",),
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

pantry ={'aubergine':'some','salmon':'some','new potatoes':'some','rocket':'some'}
logging.debug(pantry)
# add recipe names to 
listOfApproved={'Have all ingredients':[],'Missing optional ingredients':[]}
for thisRecipe in recipes:
    print('Checking: ',thisRecipe)
    ingredientsOwned = checkRecipe(recipes[thisRecipe],pantry)
    if ingredientsOwned:
        listOfApproved[ingredientsOwned].append(thisRecipe)

print(listOfApproved)

logging.debug("end of program")
