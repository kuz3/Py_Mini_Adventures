#copyright kuz3 kav 4/24/94
#from sys import exit
weapon = "nothing" #testing string
flashlight = False #testing booleon
demon_key = False
boss_key = False
test = "nothing"
demon_light = False
take_sword = False
demon_moved = False
intro = True
def vault():
    print "You are in the inside of a vault. The vault is an endless library full of books \nwith a large open book in the center of the room."

    print "\nYou read the large book and learn that as each new story is written,\nfrom a child's bedtime story to a fictional love letter to the transcript for a new movie, \na new reality is created and that new story is brought into existence."
    print "\nAbove the room, there is no roof. You see an infinite sky with thousands of floating glass windows flying by, each window a door into another story."
    print "You look down and notice a pen rests on top of the large book."
    print "\nWhat will you dream into existence?"
    print "\t-The End."
    print "(Thank you for playing my first little game. The next one will be a little less predictable, a tad more interesting..\n\t -tylerk.net)"
def chamber_room():
    global flashlight
    global weapon
    global demon_key
    global demon_light
    global demon_moved
    global take_sword
     #practicing local var
    #demon_light = False..
    choice_sword = "\n1. Take sword "
    choice_attack = "\n2. Attack "
    choice_shine_light = "\n3. Shine light on Demon "
    choice_go = "\n4. Run"

    if not demon_moved and not demon_light:
        demon_stare = "A demon stares at you with rabid eyes."
    if not demon_moved and demon_light: #elif not working here
        demon_stare = "The demon is cowering in fear."
    else:
        demon_stare = " "
    if weapon == "nothing" and not demon_moved:
        sword_lying = "Behind the demon, a sword is lying on the ground."
    elif weapon == "nothing" and demon_moved:
        sword_lying = "A sword is lying on the ground."
    elif weapon == "sword": #unnecessary code.
        sword_lying = " "
    print "You're in a golden chamber. %s " % demon_stare, sword_lying
#below changes available choices
    if take_sword:
        choice_sword = " "
    if demon_light:
        choice_shine_light = " "
    if demon_moved:
        choice_attack = " "
        choice_go = "\n4. Leave "

    print "%s" %  choice_sword, choice_attack, choice_shine_light, choice_go

    next = raw_input("> ")
    if next == "1" and not take_sword and not demon_light:
        print "You try to take the sword and the demon devours your soul."
        dead("your corpse is thrown into an endless abyss.")

    if next == "1" and not take_sword and demon_light:
        print "You pick up the sword."
        take_sword = True
        weapon = "sword"
        chamber_room()
    elif next == "2" and weapon == "nothing" and not demon_moved:
        print "You have no weapon. The demon devours your soul."
        dead("your corpse is thrown into an endless abyss.")
    elif next == "2" and weapon == "sword" and not demon_light and not demon_moved:
        print "The demon lunges towards you and passes right through your sword, devouring your soul."
        dead("your corpse is thrown into an endless abyss.")

    elif next == "2" and weapon == "sword" and demon_light and not demon_moved:
        print "You raise your sword to the demon, and stab it through the chest. It disintegrates."
        print "A key rises from the ground and enters your soul."
        demon_moved = True
        demon_key = True
        chamber_room()
    elif next == "3" and not flashlight and not demon_light and not demon_moved:
        print "You have no light. The demon devours your soul."
        dead("your corpse is thrown into an endless abyss.")
    elif next == "3" and flashlight and not demon_light and not demon_moved:
        print "You shine your flashlight on the demon. It cowers in fear."
        demon_light = True
        chamber_room()
    elif next == "4":
        glass_pathway()
#    while True: # We will probably get rid of this.

def boss_room():
    global flashlight
    global weapon
    global boss_key
    if not flashlight:
        print "You see a flashlight lying on the floor."

    print "A figure in black approaches."
    print "With his eyes closed, the shadow draws a sword.."
    print "You have %s to fight with." % weapon

    if not flashlight:  #Rewrite this to be like chamber_room
        print "\n1. Take flashlight. \n2. Run \n3. Attack \n4. Shine light on figure."
    else:
        print "\n2. Run \n3. Attack \n4. Shine light on figure."

    next = raw_input("> ")
    if next == "1":
        print "You took the flashlight."
        flashlight = True
        #print flashlight #remove later
        boss_room()
    elif next == "2":
        glass_pathway()
    elif next == "3" and weapon == "nothing":
        dead("Your lungs fill with blood as you reach your hand to your heart before collapsing in a river of blood.")
    elif next == "3" and weapon == "sword":
        boss_key = True
        print "With a solid swing, the shadow falls. A pool of blood forms and flows to your feet."
        print "A key floats up from the ground and enters your soul."
        print "1. Continue?" #Rewrite this.. and have a local var change Run to Leave.
        next = raw_input("> ")
        next = int(next) # practicing, this allows me to not put 1 in quotes..
        if next == 1:
            glass_pathway() #change to next room
    elif next == "4" and not flashlight:
        dead("You have no light. You are sliced apart in the darkness.")
    elif next == "4" and flashlight:
        dead("The figure illuminates, cold eyes stare into your soul as you are sliced in half.")
    else:
        boss_room()

def dead(why):
    print why, "try again."
#    exit(0)

def glass_pathway():
  global flashlight
  global weapon
  global demon_key
  global boss_key
#debug
 # print "flashlight: %s" % flashlight
  #print "weapon: %s" % weapon
  #print "boss_key %s" % boss_key
  #print "demon_key %s" % demon_key
  print "You are standing on a floating glass path in endless space. \nStars are all you can see in this infinity."
  print "\nThis path in front of you splits into three, each path leading to a large door."
  print "The middle door has two large keyholes."
  print "\nWhich one do you take?"
  print "1. Left \n2. Middle \n3. Right"
  global intro
  if intro:
    print "(type a number and press enter)"
  next = raw_input("> ")
  if next == "1":
      intro = False
      chamber_room()
  elif next == "2" and boss_key == True and demon_key == True:
      print "Keys leave from your soul and fly into the keyholes. The door opens."
      intro = False
      vault()
  elif next == "2":
      dead("You walk up to the door and touch it. \nYour soul implodes and you disintegrate, your consciousness spiraling into madness.")
  elif next == "3":
      intro = False
      boss_room()
  else:
    dead("Oops.. You fall off the edge into eternity.")
glass_pathway()
