from sys import exit
def entrance():
    print("""On your long journey in the forest you've came across a cave. You decided to go into the cave
            to find lost treasure (or what's left of some treasure). The entrance to the cave started to cave in.
            you barely made it, which is good, but you dropped your well made sword and you're stuck inside and the only way to go down deep inside the cave. """)
            
    print(""" before you went down deep inside the cave you scanned the room for loot that you could use. You find a skeleton
             at the corner of the room. With the skeleton there was a leather bag, a beaten up sword and shield. You walked over
             and take the sword and shield. you opened the leather bag and saw only 5 pieces of gold.
            """)
            
    print("""Are you ready to go down now?
    """)        
    print("YES or NO")
    
    
    while True:
        choice = input('> ')
        
        if "yes" in choice.lower() or "go down" in choice.lower():
            print("Alright let's go!")
            hallway()
        elif "no" in choice.lower():
            print("Well too bad you have to.")

def hallway():
    print("""It took you about ten minutes to reach down the hole, at the bottom of the hole there's was a hallway covered with broken stone and moss.
    You see a skeleton on the floor again with some more loot, as soon you got near it the skeleton jumped up and attacked you.
    luckily you blocked the attack with your shield, you jumped back as far as you can to make som distance between you and the skeleton.
    the skeleton is still getting up off the floor. Should you ATTACK it now or wait and DEFEND?
    """)
    
    while True:
        choice = input('> ')
        
        if "attack" in choice.lower() or "Attack" in choice.lower():
            print("You charged at the skeleton and slash is will all your might, it took you a few tries but you finally killed it. ")
            room()
        
        elif "defend" in choice.lower():
            print("""You sat there preparing yourself for the skeleton to attack. Apparently the skeleton is really fast! He came up from behind
            you and stabbed you in the back.
            """)
            print("Game Over!")
            gameover()
        
def room():
    print("""After defeating the skeleton you entered through some doors into a room. In the room there was a giant who looks injured.
    should you SNEAK passed him and leave the room or HEAL his injuries so be nice?
    """)
    while True:
        choice = input('> ')
        
        if "sneak past" in choice.lower() or "sneak" in choice.lower():
            print("You sneaked past the giant thats bleeding to death... Nice I bet you feel proud.")
            spiders()
        
        elif "heal" in choice.lower() or "heal him" in choice.lower():
            print("You healed the giant with your healing spell. He thanked you and as a reward gave you 50 pieces of gold for you troubles.")
            spiders()

def spiders():
    print(""" You entered into another hallway covered from ceiling to floor in spiderwebs. You analyzed the room and saw spiders everywhere.
    you assume that the spiders have poison fangs ready to bit you. Your only options so far is to RUN straight into them to reach the other side, or FIGHT your
    way through. you could also just STAND there and think of other options.
    """)
    while True:
        choice = input('> ')
        if "stand" in choice.lower() or "stand still" in choice.lower():
            print("After standing there for a bit a spider came up from behind and stabbed you with its your poisonous fangs.")
            print("Everything became blurry and you fall down.")
            print("Game Over!")
            gameover()
        
        elif "fight" in choice.lower():
            print("You stood your ground and put up your shield and ready your sword. You must've fought off about 30 at once but they overcame you.")
            print("you started to faint, not being able to move...")
            print("Game Over!")
            gameover()
            
        elif "run" in choice.lower():
            print("""You decided to brace yourself and ran through the spiders and spider's web. sadly on of the spiders bite you in the leg and you started
            to black out.
            """)
            spiders2()

def spiders2():
    print("You opened your eyes and saw two vials in front of you but you couldn't tell what they were. You best hope is that one of them in the antidote from the poison")
    print("You only have time to take one. which one should you take, the LEFT one or the RIGHT one. You should hurry you don't have much time.")
    
    while  True:
        choice = input('> ')
        if "left" in choice.lower():
            print("You quickly opened the vial and chugged it down. A whole minute went by and nothing happened, then everything went black.")
            print("Game Over!")
            gameover()
        
        elif "right" in choice.lower():
            print("You quickly opened the vial and chugged is down. A whole minute past and you started to feel better.")
            print("You got up and ran for the door, leaving the room full of poisonous spiders.")
            lastroom()

def lastroom():
    print("You rested for a bit to let the antidote fully recover you.")
    print("You looked around, noticing that you entered another room.")
    print("there's a light coming through a hole in the ceiling with a ladder.")
    print("You were planning on leaving but you look around more and saw that there's gold everywhere (how did you not notice it before the exit?)")
    print("You could LEAVE now but you could also TAKE some treasure with you... what should you do.")
    
    while True:
        choice = input('> ')
        if "leave" in choice.lower():
            print("instead of being greedy you left the gold alone and left the cave.")
            theend()
        
        elif "take" in choice.lower():
            print("You took as much gold as you can and left (what you thought something bad was gonna happen?)")
            theend()
        
def theend():
    print("""You finally made it to the top of the ladder. The sun blinded you when you reached the top.
    You finally made it out of the cave, and you made a lot of gold (I assume).
    The End.
    """)
    exit(0)
def gameover():
    print("You died (That's it.)")
    exit(0)
entrance()
