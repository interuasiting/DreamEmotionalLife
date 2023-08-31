image selectsexbg:
    contains:
        "selectSexBg.jpg" 
        size(1920,1080)
image introduction:
    contains:
        "introduction.jpg" 
        size(1920,1080)
image map: 
    contains:
        "map.png" 
        size(1920,1080)
image school: 
    contains:
        "school.jpg" 
        size(1920,1080)
image diningroom: 
    contains:
        "diningroom.jpg" 
        size(1920,1080)
image canteen:
    contains:
        "canteen.jpg" 
        size(1920,1080)
image Gymnasium:
    contains:
        "Gymnasium.jpg" 
        size(1920,1080)
image Library:
    contains:
        "library.jpg" 
        size(1920,1080)
image society:
    contains:
        "society.jpg" 
        size(1920,1080)
image schoolwoods_day:
    contains:
        "schoolwoods_day.jpg" 
        size(1920,1080)
image schoolwoods_dusk:
    contains:
        "schoolwoods_dusk.jpg" 
        size(1920,1080)
image bedroom:
    contains:
        "bedroom.jpg" 
        size(1920,1080) 
image mall:
    contains:
        "mall.jpg" 
        size(1920,1080) 
image schoolbedroom:
    contains:
        "schoolbedroom.jpg" 
        size(1920,1080) 
image corridor:
    contains:
        "corridor.jpg" 
        size(1920,1080)
image classroom:
    contains:
        "classroom.jpg"
        size(1920,1080)
image coffee:
    contains:
        "coffee.jpg"
        size(1920,1080)
image lake:
    contains:
        "lake.jpg"
        size(1920,1080)
image breadshop:
    contains:
        "breadshop.png"
        size(1920,1080)
image lakeday:
    contains:
        "lakeday.jpg"
        size(1920,1080)
image theater:
    contains:
        "theater.jpg"
        size(1920,1080)
image square:
    contains:
        "square.jpg"
        size(1920,1080)
image space:
    contains:
        "space.png"
        size(1920,1080)
image contest:
    contains:
        "contest.jpg"
        size(1920,1080)
image graduation:
    contains:
        "graduation.jpg"
        size(1920,1080)
image trueend:
    contains:
        "trueend.jpg"
        size(1920,1080)
image normalend:
    contains:
        "normalend.jpg"
        size(1920,1080)
image badend:
    contains:
        "badend.jpg"
        size(1920,1080)
define amy = Character("You",image = "amy")
define bob = Character("You",image = "bob")
define you = Character("You")
define teacher = Character("Teacher",image = "teacher")
define mom = Character("Mom")
define lily = Character("Lily",image = "lily")
define seller = Character("Seller",image = "seller")
define cathy = Character("Cathy",image = "cathy")
define cathyhappy = Character("Cathy",image = "cathyhappy")
define neighbor = Character("Neighbor",image = "neighbor")
define classmate = Character("Classmate")
define henry = Character("Henry",image = "henry")
define heryblack = Character("Henry",image = "henryblack")
define herysad = Character("Henry",image = "henrysad")
define jack2 = Character("Jack",image = "Jack2")
define jack = Character("Jack",image = "Jack")
define stranger = Character("???")
define father = Character("Antony",image = "father")
define fatherhappy = Character("Antony",image = "fatherhappy")
define member1 = Character("MemberA")
define member2 = Character("MemberB")
define member3 = Character("MemberC")
define moderator = Character("Moderator",image = "moderator")
define judges = Character("Judges",image = "moderator")

default sex = ""


label start:
    default months = ['','September', 'October', 'November','December','January','February','March','April','May']
    default month = 1
    default init_times = 3
    default addition_times = 0
    default test_times = init_times + addition_times
    default Self_awareness = 20
    default Self_management = 20
    default Social_awareness = 20
    default Relationship_skills = 20
    default Responsible_decision_making = 20
    default money = 100
    default knowledge = 0
    default unlockcathy = False
    default unlockcathysecond = False
    default unlockjack = 0
    default unlockhenry = 0
    default unlockcontest = 0
    default unlockwin = False 
    default lilyend = False
    default cathyend = False
    default jackend = False
    default henryend = False
    default perfect = 0
    default achievementcathy = False
    default achievementjack = False
    default achievementhenry = False
    default achievementlily = False
    default achievementtrueend = False
    default achievementbadend = False
    default achievementnormalend = False
    default finialend = ""
    
    play music "choosesex.mp3" fadeout 1
    scene selectsexbg
    "{color=#FF0000}This game is purely fictitious, any similarity is purely accidental.{/size}"
    play sound "dialogue.mp3"    
    "In order to have a better gaming experience, it is recommended that you turn up the music and sound effects of the game. It is recommended to adjust the music to 2/3 position and sound to full position."
    play sound "dialogue.mp3"    
    show amy_choose at right
    show bob at left
    "Please select your character sex:"
    play sound "dialogue.mp3"    
    menu :
        "Male": 
            play sound "click.mp3"
            $sex = "male"
        "Female":
            play sound "click.mp3"
            $sex = "female"
    call hidecharacter from _call_hidecharacter_49
    hide text
    hide amy_choose
    
    scene introduction
    call showcharacter from _call_showcharacter_67
    you "You are a postgraduate student at the University of Dream and you are about to start {color=#FF0000}six months {/size}of study. Which is from september to next year's february."
    play sound "dialogue.mp3" 
    you "You have a total of five attribute values, which are \n{color=#FFC000}\'Self-awareness\' ,{color=#FFC000}\'Self-management\' ,
    {color=#FFC000} \'Social awareness\' , {color=#FFC000}\'Relationship skills\' , {color=#FFC000}\'Responsible decision-making\'{/size}."
    play sound "dialogue.mp3" 
    you "In the initial stage of the game, each of your attributes is worth {color=#FF0000}20{/size} points."
    play sound "dialogue.mp3" 
    you "Each of your options results in different changes to your stats as the game progresses."
    play sound "dialogue.mp3" 
    you "When meet some special options, if one of your attributes {color=#FF0000}does not meet{/size} the standard, you can {color=#FF0000}not {/size}choose that option."
    play sound "dialogue.mp3" 
    you "In the game, your different choices will also lead to different changes in the plot."
    play sound "dialogue.mp3" 
    you "In the initial stage, your money amount is {color=#FF0000}100{/size}."
    play sound "dialogue.mp3" 
    you "Your other attribute is: {color=#FFC000}knowledge{/size}, which is now {color=#FF0000}0{/size}. And its growth method will be introduced later."
    play sound "dialogue.mp3" 
    you "Now start your happy study life~"
    play sound "dialogue.mp3" 

    
    play music "map.mp3"
    scene map
    "Here is the map, here you can go to various places."
    play sound "dialogue.mp3" 
    "Want to view the tutorial?"
    play sound "dialogue.mp3" 
    menu:
        "Yes":  
            play sound "click.mp3"
            "In the map, there are four places: School, Mall, Home, and Plot. Click the button to view the introduction of the corresponding location."
            play sound "dialogue.mp3" 
            call tutorial from _call_tutorial
        "No":
            play sound "click.mp3"
    "Ok, let's enter the game now!"

    
    scene map
    $showmonth = months[month]
    $leftmonth = 6
    menu menu_map:
        "This month is {color=#FF0000}[showmonth]{/size}. \nYou have {color=#FF0000}[leftmonth]{/size} months left to graduate."
        "School":
            play sound "click.mp3"
            call function_school from _call_function_school
            jump menu_map
        "Mall":
            play sound "click.mp3"
            call function_mall from _call_function_mall
            jump menu_map
        "Home":
            play sound "click.mp3"
            call function_home from _call_function_home
            jump menu_map
        "Plot":
            play sound "click.mp3"
            if month == 1:
                call chapterone from _call_chapterone
            elif month == 2:
                call chaptertwo from _call_chaptertwo
            elif month == 3:
                call chapterthree from _call_chapterthree
            elif month == 4:
                call chapterfour from _call_chapterfour
            elif month == 5:
                call chapterfive from _call_chapterfive
            else:
                call chaptersix from _call_chaptersix
                return
            jump menu_map
    return


label showcharacter:
    if sex == "male":
        show bob at left with dissolve
    else:
        show amy at left with dissolve
    return

label hidecharacter:
    hide amy
    hide bob
    return 
    

label tutorial:
    menu menu_tutorial:
        "School":
            play sound "click.mp3"
            "In school, you can learn about computers. At the same time, you can also participate in the test. You will have {color=#FF0000}3{/size} test opportunities every month. You can get {color=#FF0000}money{/size} and{color=#FF0000} knowledge{/size} attribute if you pass the test, and nothing if you fail the test."
            play sound "dialogue.mp3" 
            "If the monthly test time is not used up, the remaining can be accumulated."
            play sound "dialogue.mp3" 
            jump menu_tutorial
        "Mall":
            play sound "click.mp3"
            "In mall, you can use money to buy attribute points and test times."
            play sound "dialogue.mp3" 
            jump menu_tutorial
        "Home":
            play sound "click.mp3"
            "In home, You can check your attribute points."
            play sound "dialogue.mp3" 
            jump menu_tutorial
        "Plot":
            play sound "click.mp3"
            "In plot, you can continue to experience the main storyline."
            play sound "dialogue.mp3" 
            "Once you enter the plot, you will enter {color=#FF0000}the next {/size}month."
            play sound "dialogue.mp3" 
            jump menu_tutorial
        "I understand all":
            play sound "click.mp3"
            return
label function_home:
    play music "homebg.mp3"
    scene bedroom
    call showcharacter from _call_showcharacter_68
    "Welcome back, these are your current attributes."
    call screen showhome
    scene map
    call hidecharacter from _call_hidecharacter_50
    play music "map.mp3"
    #menu viewproperties:
    #    "Self-awareness":
    #        play sound "click.mp3"
    #        "Your self-awareness is {color=#FF0000}[Self_awareness]{/size}."
    #        play sound "dialogue.mp3"
    #        jump viewproperties
    #   "Self-management":
    #        play sound "click.mp3"
    #        "Your self-management is {color=#FF0000}[Self_management]{/size}."
    #        play sound "dialogue.mp3"
    #        jump viewproperties
    #    "Social awareness":
    #        play sound "click.mp3"
    #        "Your social awareness is {color=#FF0000}[Social_awareness]{/size}."
    #        play sound "dialogue.mp3"
    #        jump viewproperties
    #    "Relationship skills":
    #        play sound "click.mp3"
    #        "Your relationship skills is {color=#FF0000}[Relationship_skills]{/size}."
    #        play sound "dialogue.mp3"
    #        jump viewproperties
    #    "Responsible decision-making":
    #        play sound "click.mp3"
    #        "Your responsible decision-making is {color=#FF0000}[Responsible_decision_making]{/size}."
    #        play sound "dialogue.mp3"
    #        jump viewproperties
    #    "Money":
    #        play sound "click.mp3"
    #        "Your money is {color=#FF0000}[money]{/size}."
    #        play sound "dialogue.mp3"
    #        jump viewproperties
    #    "Knowledge":
    #        play sound "click.mp3"
    #        "Your knowledge is {color=#FF0000}[knowledge]{/size}."
    #        play sound "dialogue.mp3"
    #        jump viewproperties
    #    "Back":
    #        play sound "click.mp3"
    #        scene map
    #        call hidecharacter from _call_hidecharacter_50
    #        play music "map.mp3"
    #        return 
screen showhome():
    frame:
        xcenter 0.5
        ycenter 0.5
        xsize 1280
        ysize 720
        
        add "summary.png" size (1268, 708)
        vbox:
            spacing 10 xcenter 0.5 ycenter 0.5
            text "{color=#000000}Self awareness:{/size}[Self_awareness]" size 60 color "#FFC000"  xcenter 0.5
            text "{color=#000000}Self management:{/size}[Self_management]" size 60 color "#FFC000"  xcenter 0.5
            text "{color=#000000}Social awareness:{/size}[Social_awareness]" size 60 color "#FFC000"  xcenter 0.5
            text "{color=#000000}Relationship skills:{/size}[Relationship_skills]" size 60 color "#FFC000"  xcenter 0.5
            text "{color=#000000}Responsible decision-making:{/size}[Responsible_decision_making]" size 60 color "#FFC000"  xcenter 0.5
            text "{color=#000000}Money:{/size}[money]" size 60 color "#FFC000"  xcenter 0.5
            text "{color=#000000}Knowledge:{/size}[knowledge]" size 60 color "#FFC000"  xcenter 0.5
            textbutton "Back":  
                    text_size 40 
                    text_color "#99CCFF"
                    xcenter 0   
                    activate_sound "audio/click.mp3"
                    action Return('')   



