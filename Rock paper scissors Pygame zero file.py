import pgzrun
import random

user_name = str(input("Please enter your name: "))
print ("")
print ("Hello {0}! Welcome to User VS. Machine!".format(user_name))

#Assigning variables to needed values for the game
name = user_name 
HEIGHT = 611
WIDTH = 965
score = int(0)
timer = 0
playing = False
bin_point = random.randint(1, 5)

#The actors that are included in the game
start = Actor("start_screen")
ocean = Actor("ocean pixel (final copy)")
waterbottle = Actor("waterbottle_cpt")
sodacan = Actor("sodacan")
detergentbottle = Actor("detergentbottle")
sodabottle = Actor("sodabottle")
metalcan = Actor("metalcan")

bin = Actor("recycle_bin")
bin.pos = 1000, 575

#The names of the fish is based on the position of the fish from left to right
fish_one = Actor("fish_one")
fish_two = Actor("fish_two")
fish_three = Actor("fish_three")
fish_four = Actor("fish_four")
fish_four = Actor("fish_four")
fish_five = Actor("fish_five")

audio_mute = Actor("audio_mute")
audio_play = Actor("audio_play")

#Interaction with the user
print ("")
user_play = str(input("Would you like to play (y/n): "))

if user_play == "y" or user_play == "Y":
    print ("Alright {0} let's begin!".format(user_name))
    print ("")
    user_play_choice = int(input("What would you like to play: 1 for Rock, Paper, Scissors, 2 for Save the Ocean, 3 for Guess the lucky number!: "))
elif user_play == "n" or user_play == "N":
    print ("")
    print ("No worries {0}!".format(user_name))
    quit()
else:
    user_play = str(input("I don't understand. Can you please enter your answer again: "))

if user_play_choice == 1:
    print ("")
    print ("Alright {}, let's play rock, paper, scissors!".format(name))
elif user_play_choice == 2:
    print ("")
    print ("Alright {}, let's save the ocean!".format(name))
elif user_play_choice == 3:
    print ("")
    print("Alright {}, Try to guess my lucky number!".format(name))

while user_play_choice != 1 and user_play_choice != 2 and user_play_choice != 3:
    user_play_choice = int(input("I don't understand that, please try again: "))
    break
    if user_play_choice == 1:
        print ("Alright {}, let's play rock, paper, scissors!".format(name))
    elif user_play_choice == 2:
        print ("Alright {}, let's save the ocean!".format(name))
    elif user_play_choice == 3:
        print("Alright {}, Try to guess my lucky number!".format(name))

#This is for the game rock, paper scissors.
rock = 1
paper = 2
scissors = 3

if user_play_choice == 1:
    print ("")
    user_choice = int(input("Please enter 1 for rock, 2 for paper or 3 for scissors: "))
    computer_choice = random.randint(1, 3)

    #This is if the user and the computer choose the same action.
    if user_choice == computer_choice:
        print ("")
        print ("You tied")

    #This is for rock.
    elif user_choice == 1:
        if computer_choice == scissors:
            print ("")
            print ("You win as rock crushes scissors.")
        else:
            print ("")
            print ("You lost")

    #This is for paper.
    elif user_choice == 2:
        if computer_choice == rock:
            print ("")
            print ("You win as Paper covers rock ")
        else:
            print ("")
            print ("You lost")

    #This is for scissors.
    elif user_choice == 3:
        if computer_choice == paper:
            print ("")
            print ("You win as scissors cuts paper")
        else:
            print ("")
            print ("You lost")

    #Saying thank you to the user for playing.
    print ("")
    print ("Thanks for playing!")

#This is for guess the lucky number game 
lucky_number = random.randint(1, 10)

if user_play_choice == 3:
    print ("")
    print ("You get 5 attempts to guess the lucky number. So, choose wisely ;)")
    print ("")
    user_guess = int(input("Please guess a number between 1 and 10: "))

#This would execute if the user guesses the number.
if user_play_choice == 3:
    while user_guess == lucky_number:
        print ("")
        print ("Correct!")
        print ("")
        print ("The lucky number was {}.".format(lucky_number))
        print("Thanks for playing!")
        break

#This would execute if the user didn't guess the lucky number.
if user_play_choice == 3:
    for i in range (4):
        if user_guess != lucky_number:
            print ("")
            print ("Incorrect! Try again")
            print ("")
            user_guess = int(input("Please guess a number between 1 and 10: ")) 
        elif user_guess == lucky_number:
            print ("")
            print ("Correct!")
            print ("")
            print ("The lucky number was {}.".format(lucky_number))
            break
    else:
        print ("")
        print ("You have 0 guesses left.")
        print ("")
        print ("The lucky number was {}.".format(lucky_number))

#This is for save the ocean. 
def draw():
    global playing
    #This would be for the start screen
    screen.draw.text("Hello {0}".format(name), center = (500, 250), fontsize = 37, fontname = "lato regular")
    screen.draw.text("Welcome to save the ocean!", center = (500, 305), fontsize = 37, fontname = "lato regular")
    screen.draw.text("Click anywhere to begin!", center = (500, 360), fontsize = 37, fontname = "lato regular")

    #This would be for the game
    if user_play_choice == 2:
        if playing == True:
            ocean.draw()

            waterbottle.draw()
            sodacan.draw()
            detergentbottle.draw()
            sodabottle.draw()
            metalcan.draw()

            fish_one.draw()
            fish_two.draw()
            fish_three.draw()
            fish_four.draw()
            fish_five.draw()

            bin.draw()

            audio_mute.draw()
            audio_play.draw()

            screen.draw.text("Score: {0}".format(str(score)), topleft=(15, 35), fontsize = 33)
            screen.draw.text("Timer: {0}".format(str(int(timer))), topleft=(15, 65), fontsize = 33)

#This function is used for the timer
def update(dt):
    global timer
    global playing

    if playing == True:
        if timer < 15:
            timer += dt
            if timer > 11:
                bin.left -= 5

        #This would execute if the timer has reached 15 seconds
        else:
            print("")
            print ("Times up!")
            print("")
            print ("Your score is {0}.".format(score))
            print("")
            if score == 5:
                print ("You've won! Congradutations {0}!".format(name))
                print("")
            elif score > 5:
                print ("Wow you got more than 5 points!")
                print("")
                print ("You've won! Congradutations {0}!".format(name))
                print("")
            else:
                print ("You've lost. You didn't save the ocean!")
                print("")

            print("Thanks for playing Save the Ocean!")
            quit()


#This would place place the actors in a certain positions
def place_bin():
    bin.x = 1000
    bin.y = 575

def place_waterbottle():
    waterbottle.x = 125
    waterbottle.y = 450
def place_fish_one():
    fish_one.x = 125
    fish_one.y = 520

def place_fish_two():
    fish_two.x = 290
    fish_two.y = 450
def place_sodacan():
    sodacan.x = 290
    sodacan.y = 520

def place_fish_three():
    fish_three.x = 460
    fish_three.y = 520
def place_detergentbottle():
    detergentbottle.x = 460
    detergentbottle.y = 450

def place_fish_four():
    fish_four.x = 630
    fish_four.y = 450
def place_sodabottle():
    sodabottle.x = 630
    sodabottle.y = 520

def place_fish_five():
    fish_five.x = 800
    fish_five.y = 520
def place_metalcan():
    metalcan.x = 800
    metalcan.y = 450

def place_audio_mute():
    audio_mute.x = 80
    audio_mute.y = 110
def place_audio_play():
    audio_play.x = 35
    audio_play.y = 110

#This block of code is used if the user clicks something
def on_mouse_down(pos):
    global score
    global playing

    #This would be used if the user clicks the screen in the beginning
    if start.collidepoint(pos):
        playing = True

    #These blocks of code is for the actors
        if waterbottle.collidepoint(pos):
            print ("")
            print ("Good Job! You picked up a water bottle.")
            waterbottle.image = "transparent_picture"
            score += 1
            sounds.correct_sound.play()
            StopIteration
        elif sodacan.collidepoint(pos):
            print ("")
            print ("Good Job! You picked up a soda can.")
            sodacan.image = "transparent_picture"
            score += 1
            sounds.correct_sound.play()
            StopIteration
        elif detergentbottle.collidepoint(pos):
            print ("")
            print ("Good Job! You picked up a detergent bottle.")
            detergentbottle.image = "transparent_picture"
            score += 1
            sounds.correct_sound.play()
            StopIteration
        elif sodabottle.collidepoint(pos):
            print ("")
            print ("Good Job! You picked up a soda bottle.")
            sodabottle.image = "transparent_picture"
            score += 1
            StopIteration
            sounds.correct_sound.play()
        elif metalcan.collidepoint(pos):
            print ("")
            print ("Good Job! You picked up a metal can.")
            metalcan.image = "transparent_picture"
            score += 1
            StopIteration
            sounds.correct_sound.play()

        #This would be for the recycling bin.
        elif bin.collidepoint(pos):
            print ("")
            print("You picked up the recycling bin! You got {0} points!".format(bin_point))
            bin.image = "transparent_picture"
            score += bin_point
            StopIteration
            sounds.correct_sound.play()

        #This block of code is for the fish
        elif fish_one.collidepoint(pos) or fish_two.collidepoint(pos):
            print ("")
            print ("Don't pick up the marine animals! Pick up the plastic!")
            score -= 1
            sounds.incorrect_sound.play()
        elif fish_three.collidepoint(pos) or fish_four.collidepoint(pos) or fish_five.collidepoint(pos):
            print ("")
            print ("Don't pick up the marine animals! Pick up the plastic!")
            score -= 1
            sounds.incorrect_sound.play()

        #This would be for music
        elif audio_mute.collidepoint(pos):
            music.pause()
        elif audio_play.collidepoint(pos):
            music.unpause()

#This would be the background music
if user_play_choice == 2:
    music.play ("bensound-allthat")
    music.set_volume(0.3)

#This would place the objects and buttons in the game
place_waterbottle()
place_sodacan()
place_detergentbottle()
place_sodabottle()
place_metalcan()

place_bin()

place_fish_one()
place_fish_two()
place_fish_three()
place_fish_four()
place_fish_five()

place_audio_mute()
place_audio_play()

#This would allow the game to run
pgzrun.go()