#Algorithm

# 1 Show rules of RPSLS
    #show what beats what (create a class?)
        #send to gestures
# 2 Ask how many human players are playing (send to Games class)
    # check user input to make sure it is valid, otherwise reprompt
    # create a game class for each type of game ( 1 v 1 or 1 v AI)
# 3 based on choice start the right game
    #create gestures
        # give abilities from abilities class (rules class)
# 4 create a game class
#   Ask user which option they would like (validate)
    # always display list of gesture options
    #ask second user or
        #auto - generate ai choice
# 5 compare gestures using rules class?
#   determine winner for each game based on rules class
        #if tie ask for choices again
        # there must be a winner for each game
        # keep track of score
# 6 someone has to win 3 games to win round
    # something to keep track of wins (player attribute)


    #gestures (list) put in game.py
        #names = []
        # set method to generate random gesture for AI
        # think about who is responsible for holding the gestures that can be used
    #player (parent) & AI/Human (children of player)
        #type = person or AI/Human (inheritance)
        #gesture = comes from gestures choice
    #rules (function)
        # set each rule
        # set methods for which rule beats which
    #game
        #get player
        #get gesture
        #wins attribute for each player
            #get result based on rules
                #display winner each game and for the round
                # must win 3 games to win round
    