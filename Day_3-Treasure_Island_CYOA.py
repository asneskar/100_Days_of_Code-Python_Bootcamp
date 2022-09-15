print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

This program uses ASCII art copied from: https://ascii.co.uk/art

Welcome to Treasure Island.

Your mission is to find the treasure.

''')

river_crossing = input("You stand at the edge of a river.\nYou know that the treasure lies somewhere on the other side.\nDo you wait for a ferry, or do you try to swim across?\nwait or swim: ")
river_crossing = river_crossing.lower()
if river_crossing == "wait" or river_crossing == "w":
  print('''
  
             ***
            * //*
             //*
   **       **/|      **
 ************//***********
 ***********//************
   **      |/**       **
            **/|
            *//
            //*
           |/**
            **/|
***         *//         ***
 *****      //*      *****
  *******  |/**   *******
       *************
          *******
             *
  ''')
  direction = input("The ferry brought you safely across the river.\nOn the other side you find a trail.\nYou follow this trail for an hour before it splits in two.\nTo the north the trail winds down the edge of a bright valley with a quaint looking village at the bottom.\nTo the east the trail leads in to a dark, and heavy forest. Who knows what lies beyond.\nWhich direction do you choose to go?\nnorth or east: ")
  direction = direction.lower()
  if direction == "east" or direction == "e":
    print('''
    
                                                          ,
                                            .__ ._       \_.
                                     _, _.  '  \/   \.-  /
                                      \/     .-_`   // |/     \,
                     .-""""-.          \.   '   \`. ||  \.-'  /
                    F        Y        .-.`-(   _/\ V/ \\//,-' >-'   ._,
                   F          Y   .__/   `. \.   ' J   ) ./  / __._/
                  J         \, I    '   _/ \  \  | |  / /  .'-'.-' `
           (       L   \_.--.| \_.      ' .___ `\: | / .--'.-'"
         \ '\    .  L   /    \\/        ._/`-.`  \ .'.' .'---./__
    \__  '\ ) \._/   `-.__. ` \\_. '   .---.  \     /  /  ,   `  `
  --'  \\  ): // \,            `-.`__.'     `- \  /   / _/-.---.__.- .
     _.-`.'/ /'\_, ._     >--.-""'____.--"`_     '   /.'..' \   \   _/`
 _ .---._\ \'/ '__./__.-..  / .-|(    x_.-'___  |   :' /    _..---_' \\ 
 .:' /`\ `. `..'.--'\      /.' /`-`._  `-,'   ` '   I '_.--'__--..___.--.
     `  `. `\/'/  _.   _.-'      _.____./ .-.--""-. .-"    ' _..-.---'
  -._ .--.\ / /-./     /   .---'-//.___. .-'       \__ .--.  `    `.
 ,--'/.-. ^.   .-.--.  ` _/    _//     ./   _..   .'  `.    \ \    |_.
    /' | >.   ' | \._.-       '    _..'  `.' . `.       )    | |\  `
  ./ \ \'  ) c| /  \     \_..  .--'    ,\ \_/`  :    )  (`-. `.|`\\
   \'  / ,-.  | ` ./`  ._/ `\\'.--.,-((  `.`.__ |   _/   \    |)  `--._/`
______'\   |  < __________  //'  //  _)   )/-._`.  (,-')  )  / \_.    /\. _____
           |  |        .__./    //  '\  |//    `.\ '\ (  (  <`   ._  '
           >  |      _.  /   ..-\ _    _/ \_.  \ `\    \_ `---.-'__
        . /  `-   _.'        /   `   _/|       J  /`     `-,,-----.`-.
            '  .:'          '`      '          < `   f  I //        `\\_,
              '                         \.     J        I/\_.        ./
                                        `:     I  .:    K  `          `
                                         `,   J         L
                                           .  F  .-'    J
                                           .  I  (.   . I _.-.._
                                      _.---.J/      :'   L -'
                                         _.-'_.)     ` `-.`---.,_.
                                    .--""   .F' J) `.`L.__`-.___
                                           Y ..Z     ))   `--'  `-
                                             . '    :'
    ''')
    cabin = input("You walk through the forest jumping at every shadow.\nYou're constantly looking over your shoulder covinced something is following you.\nAfter a rather tense hour of making you're way through the forest you come across a clearing.\nIn the clearing you find a cabin.\nThe cabin has a door you could try. You also notice a cellar to the left, and what appears to be a gruesome looking shrine to the right.\nWhich would you like to check out?\ndoor, cellar, or shrine: ")
    cabin = cabin.lower()
    if cabin == "door" or cabin == "d":
      print('''
      
                                                 /\\
                                                /  \  /\\
                    ___________________      /\/    \/  \\
           /\      /\        ______    \    /   /\/\  /\/\\
          /  \    //_\       \    /\    \  /\/\/    \/    \\
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \\
 /\/\/\/       //_______\       \|__|      \\
/      \      /XXXXXXXXXX\                  \\
        \    /_I_II  I__I_\__________________\\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~
      ''')
      print("You reach for the door, and with the lightest touch it swings open.\nTo your surprise you find a chest in the middle of the room.\nIt's open, and neatly filled with 5lb bars of gold.\nCongratulations! You've won!")
    elif cabin == "cellar" or cabin == "c":
      print('''
      
 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,
 8                           8"b,    "Ya
 8                           8  "b,    "Ya
 8                    aaaaaaa8,   "b,    "Ya
 8                    8"b,    "Ya   "8""""""8
 8                    8  "b,    "Ya  8      8
 8             aaaaaaa8,   "b,    "Ya8      8
 8   A         8"b,    "Ya   "8"""""""      8
 8             8  "b,    "Ya  8             8
 8      aaaaaa88,   "b,    "Ya8         B   8
 8      8"b,    "Ya   "8"""""""             8
 8      8  "b,    "Ya  8                    8
 8aaaaaa8,   "b,    "Ya8                    8
 8"b,    "Ya   "8"""""""                    8
 8  "b,    "Ya  8                           8
 8,   "b,    "Ya8                           8
  "Ya   "8"""""""                           8
    "Ya  8                                  8
      "Ya8          Normand Veilleux        8
        """""""""""""""""""""""""""""""""""""
      ''')
      print("As you're making your way down the stairs into the cellar you hear a loud creaking.\nSuddenly you're falling forward.\nAs you painfully tumble down the stairs you lose consciousness.\nYou don't wake up. Game over!")
    elif cabin == "shrine" or cabin == "s":
      print('''
      
  @nnnnnnnn|--------------------------\\
  @uuuuuuuu|__________________________/
      ''')
      print("You walk up to the shrine. There's a gruesome scene in front of you.\nSomething has been sacrificed upon the altar.\nWhatever it was it's beyond recognition now.\nAs you're trying to understand what's in front of you a voice behind you says,\n'You're not a smart one are you?'\nYou feel a hard blow to the side of your head, and a sharp pain across your throat.\nThankfully you lose consciousness within seconds. Game over!")
    else:
      print("\nCommand not recognized.\nPlease restart the program, and try again.")
  elif direction == "north" or direction == "n":
    print('''
    
                       __.------.                          
                      (__  ___   )                         
                        .)e  )\ /                          
                       /_.------                           
                       _/_    _/                           
                   __.'  / '   `-.__                       
                  / <.--'           `\                     
                 /   \   \c           |                    
                /    /    )       x    \\                   
                |   /\    |c     / \.-  \\                  
                \__/  )  /(     (   \   <>'\\               
                     / _/ _\-    `-. \/_|_ /<>             
                    / /--/,-\     _ \     <>.`.            
                    \/`--\_._) - /   `-/\    `.\\           
                     /        `.     /   )     `\\          
                     \      \   \___/----'                 
                     |      /    `(                        
 ___________         \    ./\_   _ \\                       
   ______________    /     |  )    '|                      
 __________________ |     /   \     \     ___________   
                   /     |     |____.)                     
                  /      \  a88a\___/88888a.               
                 \_      :)8888888888888888888a.           
                /` `-----'  `Y88888888888888888            
                \____|         `88888888888P'
    ''')
    print("You're walking along the path. It's a pleasant day as you admire the beautiful valley village below.\nSuddenly you hear a scream to your right. Before you can react you fall to your left. Something is on top of you.\nA wild looking man is now laying into you. You're being robbed!\nUnfortunately this brigand isn't the type to leave his victims alive. Game over!")
  else:
    print("\nCommand not recognized.\nPlease restart the program, and try again.")
elif river_crossing == "swim" or river_crossing == "s":
  print('''
  
                                               ___.-----.______
                                   ___.-----'::::::::::::::::`---.___
                _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
   _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
  ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
 :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
  :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
   `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                  `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                        / `,--.\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
 _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                 ///--\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                 `'           _.'   (    /______     (   `-._   `-._,-'
    ()  ()                 .-' __.-//     /_______---'       `-._   `.
  * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
  `\ )( /*                `'`'                            /_______   _.'
    {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
     !|       `                                              ~~~
  ~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ''')
  print("You were too good of a snack for a hungry alligator to pass up!\nYou've been eaten! Game over!")
else:
  print("\nCommand not recognized.\nPlease restart the program, and try again.")
