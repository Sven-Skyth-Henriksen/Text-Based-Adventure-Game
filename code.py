#Text-Based Adventure Game

print('Welcome to the text-based LOTR Adventure Game\n')
#Play again function
def play_again():
    print('\nDo you want to play again? (y or n)')

    answer = input('>').lower()

    if 'y' in answer:
        start()
    else:
        exit()

# Game over function
def game_over(reason):
    print('\n'+ reason)
    print('Gamer Over!')
    play_again()

#Location Function(Orc Camp)
def orc_camp():
    print('\nYou are in front of an Orc Camp.')
    print('And you see a hundreds of orcs')
    print('What are u going to do ? (1 or 2)')
    print('1) You go back and follower the left path')
    print('2) You try to sneak around the camp because you can see an wounded dwarf lying next to the walls')

    answer = input('>')

    if '1' in answer:
        print('You took the right choice!')
        orc()
    elif '2' in answer:
       game_over('The orcs saw you and hundreds of them are rushing towards you.')
    else:
        game_over('Go and learn how to type a number.')

#Location Function(Orc)
def orc():
    print('\nYou see a wounded orc lying on the ground')
    print('Maybe he is having some valuable Information !')
    print('What are u going to do ? (1 or 2)')
    print('1) You kill the orc.')
    print('2) Try to help the orc and take him with you to the outpost for interrogation.')

    answer = input('>')

    if '1' in answer:
        print('Better safe then sorry.')
        Stonehalls()
    elif '2' in answer:
        game_over('He he appreciated your help but in the end he killed you...You cant trust an orc.')
    else:
        game_over('Learn how to typ a number!')

#Location Function (Stonehalls)
def Stonehalls():
    print('\nAfter following the path.You finally reached the '
          'Stonehalls,a smaller dwarf-outpost in the Mines of Moria.')
    print('One of the dwarfs explain you the way to Durin´s way.')
    Durins_way()

#Location Durin`s way
def Durins_way():
    print('\nYou reach the chamber of the crossroads where Gandalf have been before you.')
    print('You see 3 ways and 1 of them is blocked by a pile of stones.')
    print('So have 2 options left.')
    print('1) You take the left road.')
    print('2) You take the right road.')

    answer = input('>')

    if '1' in answer:
        print('You go trough a long tunel. At the end you find the 21st hall... You won!')
        play_again()
    elif '2' in answer:
        game_over('On your way to Zirakzigil you encounter a horde of orcs.')
    else:
        game_over('Learn how to typ a number!')

#Start Function
def start():
    player_name = str(input('Please select a Name for your dwarf warrior: '))
    print(f'Hello {player_name}. Let`s start the adventure.\n')

#Intro
    print(f'''You entered Moria with a group of dwarfs to push the Orcs out for once at for all.
In the corner of the room at Durin´s Thershold stands the master of the expedition groups. He is coming over 
for a chat.

NPC: Welcome to Moria {player_name}. You join us at a momentous time! I am the master of the expedition group here at 
     Durin´s Threshold. Other expedition groups have already moved further on into the depths of Khazad-dûm, hoping to find
     Balin`s expedition of some years ago and learn of their fate.
    ''')

    print('So after talking to the master you got 2 options. He told you to reach the 21st hall. (l or r)')
    print('l) You go left.')
    print('r) You go right.')

    answer = input('>').lower()

    if 'l' in answer:
        print('You follower the left road.')
        orc()
    elif 'r' in answer:
        print('You follower the right road.')
        orc_camp()
    else:
        game_over('Don´t you know how to write properly?')

start()
