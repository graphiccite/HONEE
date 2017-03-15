import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
from pprint import pprint

logging.debug("Start of H.O.N.E")
#recipes contains all the recipes, oddly enough. Each is a dictionary with three keys: essential ingredients, optional ones and insturctions on how to cook it
recipes = {
    "mousakasagne":{"required":("lasagne","aubergine","sweet potato","swede","kidney beans", "butter beans", "tinned tomato", "oxo","cinamon","pepper","butter","flour","milk",),
                  "optional":("wine","cinnamon","rosemary","basil","nutmeg"),
                  "instructions":"roast the aubergine and sweet potatoes, make a white sauce with 50g butter and 1 pint of milk, the rest goes in a sauce pan"},
    "salmon":{"required":("salmon","new potatoes","rocket"),
            "optional":("balsamic vinegar", "salad cream", "pepper","pesto","mustard","olive oil"),
            "instructions":"bake salmon in foil 200C about 20 min. olive oil, balsamic vinegar and mustard make a dressing or you can add the pesto to the pasta before you cook it"},
    "roasted vegetables":{"required":("courgette","carrot","aubergine","onions","garlic","salt","pepper","oil"),
             "optional":("butternut squash","sweet potato","chicken","swede",),
             "instructions":"slather in oil, season and roast for a good while, turning halfway through"},
    "chilli":{"required":("minced beef","tinned tomato","oxo","kidney beans", "onions","carrot","chilli","rice","tomato puree"),
              "optional":("wine","butter beans","rosemary"),
              "instructions":"just cook"},
    "stir fry":{"required":("garlic","noodles","onions","soy sauce"),
                "optional":("broccoli","carrot","water chestnut","asparagus","chicken","spring onion","ginger","red pepper","mushroom","chinese sauce","beef","cashews"),
                "instructions":"fry it"},
    "curry":{"required":("onions","red pepper","chicken","curry sauce","rice"),
             "optional":(),
             "instructions":"fry chicken to seal then add veg, once that's done pour the sauce in until heated. Dont forget teh rice!"},
    "fajita":{"required":("tortillas", "chicken","red pepper","onions","spice mix","salsa","mayonaise"),
              "optional":("cheese"),
              "instructions":"eat loads, try not to over stuff"},
    "lasagne":{"required":("lasagne","minced beef","oxo","tinned tomato","onions","carrot","mushroom","butter","flour","milk",),
               "optional":("wine","rosemary","thyme","parsely","bail","nutmeg"),
               "instructions":"white sauce is 50g butter, 1 pint milk and some flour"},
    "pasta bake":{"required":("pasta","antipasti","cheese"),
                  "optional":(),
                  "instructions":"cook pasta, chop antipasti, mix in a ovenable dish, scatter with cheese then bake till crispy"},
    "bolognase":{"required":("tinned tomato","minced beef","carrot","mushroom","pasta"),
                 "optional":("basil","parsely"),
                 "instructions":""},
    "wonton soup":{"required":("wonton soup","broccoli","asparagus","garlic"),
                   "optional":(),
                   "instructions":"best with tenderstem broccoli. fry the veg gently, eat with cosco soup"},
    "roast pork sholder":{"required":("pork","potatos","carrot","broccoli"),
                          "optional":(),
                          "instructions":"dammed tastey but well complex, best ask Cat"},
    "tagine":{"required":("carrot","courgette","aubergine"),
              "optional":("cous cous","apricots"),
              "instructions":"arrange delicately in a tagine, add shit tons of spices. Things too high up will be out of the water and probs wont cook too well"},
    "leon salad":{"required":("cous cous", "chicken","petite pois pees","avacardo","lime","broccoli"),
                  "optional":("mint","pomegranite"),
                  "instructions":"fry the chicken lightly cook the broccoli, pees and cook the cous cous, mix up and eat"},
    "avacado mango chicken":{"required":("avacardo","mango","chicken","lime","chilli"),
                             "optional":(),
                            "instructions":"fry the chicken, cut the fruits and serve up"}    
}
logging.debug("recipes has been defined for these dishes:"+str(recipes.keys()))

#check that there are no slightly different duplicate ingredients
allingredients=[]
for dish in recipes.keys():
    for item in recipes[dish]["required"]:
        allingredients.append(item)
allingredients=list(set(allingredients))        
allingredients.sort()
logging.debug("all the ingredients to check there are no typoes \n" + "\n".join(allingredients))

#create a pantry with all the ingredients as keys and how much we have as value c(none,low,some)
pantry = {}
for item in allingredients:
    pantry.update({item:"none"})
logging.debug(pantry)

#identify which recipes have all of their required ingredients in the pantry and the value is not none

#create a shopping list of things that are none or low in the pantry
#if i buy the full pantry everytime i go shopping that's too much to carry and it probs wont last while i eat it
#think of some clever way of deciding what I should buy

#create simple way to add the things bought to the pantry, these may not exactly match the shopping list so should be adjustable

#create a simple way to adjust the pantry based on the chosen recipe that's made

#also a simple way to adjust any of the values in the pantry because it is wrong for unforseen reasons

logging.debug("end of program")
