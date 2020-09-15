import random
def start():
    global game,dillon,ryan
    game=Game()
    dillon = Player('Dillon')
    ryan = Player('Ryan')
    game.players = dillon,ryan
    
#example
# name = player()
# name.title                ''

### todo   ###
#------------#
#setup player A
#targeting player B
#interrupts. think of all the possible options that players can interrupt in and
    #for each card allow a section so that they can intererupt in each round
        #breakdown. create a popup for eachcard they can use in that segment of
            #round breakdown


################################################################################
##``````````````````````````````Graphic Stuff`````````````````````````````````##
################################################################################
#allow under card rows for attachments under each chatacter and locations


#####################################END########################################
class Game:
    def __init__(self):
        self.players = []
        self.winner = ''
        self.round_number = 0
        self.player_order = []
    

    def control(self): #only after plays are declared
#setup
##        for i in self.players:
##            i.setup()
##        for i in self.players:
##            for j in i.characters_under_control_temp:
##                i.characters_under_control.append(j)
##            for j in i.locations_under_control_temp:
##                i.locations_under_control.append(j)
##            for j in i.attachments_under_control_temp:
##                i.attachments_under_control.append(j)
##            i.characters_under_control_temp = []
##            i.locations_under_control_temp = []
##            i.attachments_under_control_temp = []
##        print(i.name,i.characters_under_control)
###plot 1
##    #1.1 plot phase begins
##    #1.2 choose plots
##        for i in self.players:
##            i.plot_phase(0)
##    #1.3
##        for i in self.players:
##            i.plot_phase(1)
##    #1.3.2 (Skipped)
##        inits = []
##        arr = []
##        for i in self.players:
##            inits.append(i.initiative)
##        max = max(self.players.inititive)###broken??????????????????????????????
##        if inits.count(max) > 1:
##            return
    #1.3.3 when revealed abilities
    #1.4 Action window
    #1.5 Plot phase ends
#influence 2
    #2.1 phase begins
    #2.2 bid in order
        bidding_array = []
        for i in self.players: #self.player_order
            string = ' '
            bidding = i.bidding_power
            while bidding >= 0:
                string = string + str(bidding) + ' '
                bidding -= 1
            x=1000000
            while x >= int(i.bidding_power):
                y = self.prompt('How much do you want to bid on Iron Throne',1,string)
                try:
                    y = int(y)
                except:
                    y = 1000000
                x = int(y)
            bidding_array.append(x)
            
        maxi = max(bidding_array)
        if bidding_array.count(maxi)==1:
            bidwinner = self.players[bidding_array.index(maxi)]#self.player_order
            bidwinner.bidding_power-=maxi
            bidwinner.faction_card_power-=maxi
            bidwinner.power_total-=maxi
            for i in self.players:
                i.iron_throne = False
            bidwinner.iron_throne = True
        else:
            current_holder = ''
            for i in self.players:
                if i.iron_throne == True:
                    current_holder = i
                    i.iron_throne = False
            bidwinners = []
            bidwinners.append(self.players[bidding_array.index(maxi)])#self.player_order
            bidwinners.append(self.players[bidding_array.index(maxi,bidding_array.index(maxi)+1)])
            bidwinner = ''
            bidwinners2 = []
            for i in bidwinners:
                bidwinners2.append(i.name)
            bidwinners3 =''
            while bidwinners3 not in bidwinners2:
                bidwinners3 = current_holder.prompt("Break the tie, who gets the Iron Throne",1,bidwinners2)
            for i in self.players:
                if i.name == bidwinners3:
                    bidwinner = i
            bidwinner.bidding_power -= maxi
            bidwinner.power_total -= maxi
            bidwinner.faction_card_power -= maxi##option for multiple bidding locations
            bidwinner.iron_throne = True
                        
            
            
    
    
        
        




    def prompt(self, description, number_of_options, options = []):
        output = input(description+' '.join(options))
        return output
    
    def win_condition(self):
        for i in self.players:
            if i.power_total >= 15 and i.iron_throne == True:
                print(i.name + 'IS THE WINNER')
                print('END GAME')
                print('END GAME')
                print('END GAME')
                print('END GAME')
                print('END GAME')
                print('END GAME')
                print('END GAME')
                print('END GAME')
                return i.name
        else:
            return False

        
class Player:
    def __init__(self,name):
        self.debug = True
        self.name = name                ##player name
        self.players = []               ##list of players
        self.legal_deck = False         ##Is the player’s deck legal?	
        self.iron_throne = False        ##Does the player hold it?
        self.target_player = ''         ##Which opponent are you targeting?
        self.power_total = 0            ##How much power does the player have?
        self.gold_pool = 0              ##How much gold does the player have?
        self.initiative = 0             ##What is the player’s initiative?
        self.reserve = 0                ##What is the player’s reserve value?
        self.claim = 0                  ##What is the player’s claim value?
        self.hand = []                  ##Cards in hand/order
        self.draw_deck = ['1','2','3','4','5','6','7','8','9','1','1','2','13'
                          ,'14','15','16','17','18','19','20']             ##Cards in the draw deck in order
        self.discard_pile = []          ##What cards are in the discard pile?
        self.dead_pile = []             ##What cards are in the dead pile?
        self.faction_card = ''          ##What is the player’s faction card?
        self.under_faction_card = []    ##What cards are under the faction card?
        self.shadows = []               ##What cards does the player have in shadows?
        self.agenda_card = ''           ##What agenda does the player have?
        self.title_card = ''            ##What title does the player have?
        self.plot_deck = []             ##What plots are in the plot deck?
        self.used_plot_pile = []        ##What plots are in the used plot pile?
        self.revealed_plot_card = ''    ##What is the player’s revealed plot card?
        self.characters_under_control = []   ##
        self.locations_under_control = []   ##
        self.attachments_under_control = [] ##
        self.characters_under_control_setup = []   ##
        self.locations_under_control_setup = []   ##
        self.attachments_under_control_setup = [] ##
        self.removed_from_play = []     ## mace tyrel 2nd and others
        self.faction_card_power = 0
        self.bidding_power = 7###########################################0


    def temp(self):
        self.claim = random.choice([1,2,3])

    def draw_cards(self, number_of_cards, limiter=0):
        if number_of_cards-limiter > 0:
            for i in range(number_of_cards-limiter):
                self.hand.append(self.draw_deck[0])
                self.draw_deck.remove(self.draw_deck[0])
        return 
    
    def prompt(self, description, number_of_options, options = []):
        output = input(description+' '.join(options))
        return output
        return #######################################################################

    def put_into_play(self,selected_card):
        ####bad temp
        self.characters_under_control_temp.append(selected_card)
        return########################################################################

    def shuffle_deck(self):
        random.shuffle(self.draw_deck)
        return #######################################################################

    def reveal_plot(self,selected_plot):
        return #######################################################################
    
    def current_modifiers(self,mod_type): 
        modifiers = 0
        for i in characters_under_control:
            current_bonus = 0
            ##retrieve mod_type bonus
            modifiers += current_bonus
        for i in locations_under_control:
            current_bonus = 0
            ##retrieve mod_type bonus
            modifiers += current_bonus
        for i in attachments_under_control:
            current_bonus = 0
            ##retrieve mod_type bonus
            modifiers += current_bonus
        agenda_bonus = 0
        #retrieve agenda bonus for mod_type
        modifiers += agenda_bonus

    def start_round(self):
        self.plot_phase()
        self.influence_phase()
        
    
    def select_cards(self):
        end = False
        self.hand.append('None')
        while end == False:
            selected_card = self.prompt('Select cards to play', len(self.hand), self.hand)
            if selected_card == 'None':
                self.hand.remove('None')
                end=True
            else:
                shadow_tag = False
                ##retrieve selected card shadow tag T/F
                if shadow_tag == True:
                    shadow_card = self.prompt('Put card into shadows or into play', 2, ['Shadows','into play'])
                    if shadow_card == 'Shadows':
                        if self.gold_pool >= 2:                            
                            self.shadows.append(selected_card)
                            self.hand.remove(selected_card)
                            self.gold_pool -= 2
                        else:
                            self.prompt('Not enough gold remaining', 1, ['OK'])
                    else:
                        card_type = 'Event'
                        ##retrieve selected card type
                        if card_type != 'Event':
                            cost = 0
                            ###retrieve selected card cost 
                            if cost <= self.gold_pool:
                                self.put_into_play(selected_card)
                                self.gold_pool -= cost
                                self.hand.remove(selected_card)
                            else:
                                self.prompt('Not enough gold remaining', 1, ['OK'])
                        else:
                            self.prompt('Cannot play events in setup', 1, ['OK'])
                else:
                    card_type = 'Character'
                    ##retrieve selected card type
                    if card_type != 'Event':
                        cost = 0
                        ###retrieve selected card cost 
                        if cost <= self.gold_pool:
                            self.put_into_play(selected_card)
                            self.gold_pool -= cost
                            self.hand.remove(selected_card)
                        else:
                            self.prompt('Not enough gold remaining', 1, ['OK'])
                    else:
                        self.prompt('Cannot play events in setup', 1, ['OK'])
        return

        ##prepare for action window
        ##back and forth action windows
                    
    def setup(self):
        self.draw_cards(7)
        if self.debug == True:
            print(self.hand)
        mulligan = self.prompt("Mulligan",2,['Yes','No'])
        if mulligan == 'Yes':
            for i in self.hand:
                self.draw_deck.append(i)
            self.shuffle_deck()
            self.hand = []
            self.draw_cards(7)
        self.gold_pool = 8
        self.select_cards()
        ##attach attachments to cards
        self.draw_cards(7-len(self.hand))
        self.gold_pool = 0
        #start_round()####

    def plot_phase(self,iteration):
        if iteration == 0:
            selected_plot = prompt('Choose plot card',len(self.plot_deck),plot_deck)
        ##wait for opponent to pick plot asfhalkdjhflksdjhflkajsd
        if iteration == 1:
            init = 0
            ##retrieve plot initive
            init_modifiers = 0
            init_modifiers = self.current_modifiers('Initiative')
            self.initiative = init + init_modifiers
        ##determine player order  ahlkdjhfklsjdhf
        ##when_revelaed ability ay9qh489ghldafg489
        #action window
        ##allow for those 2 cards card that gets to repick plot cards
        return

    def influence_phase(self):
        #bidding power stuffffff
        if self.players > 2:
            if self.iron_throne == True:
                titles = []
                #retrieve all titles
                self.title_card = prompt('Select Title',len(titles),titles)
            else:
                #wait for turn order for title to be selected
                titles = []
                #retrieve remaining titles
                self.title_card = prompt('Select Title',len(titles),titles)
            #wait for titles to be selected, then reveal titles
                
        

##        
##    def draw_cards(self, number, limiter=0):
##
##        return
##
##    def setup(self):
##        draw_cards(7)
##        self.gold = 8
##
##    def hand(self):
##        
##
##    def play_card(self,index):
##        marshaling_action(self, card_name = '')
##        return
##
##    def marshaling_action(self, card_name):
##        return
##    def action(self, card_name):
##        return
##    def challenges_action(self, card_name):
##        return
##
##    def kneel_card(self, player, index):
##        
##
##    def new_round(self):
##        return
##        
##    def new_plot(self):
##        return
##        
