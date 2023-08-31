label endgame:
    call showcharacter from _call_showcharacter_65
    if achievementtrueend == True:
        $finialend = "True End"
        scene trueend
    elif achievementnormalend == True:
        $finialend = "Normal End"
        scene normalend
    elif achievementbadend == True:
        $finialend = "Bad End"
        scene badend
    play music "audio/endmusic.mp3"
    call showcharacter from _call_showcharacter_66
    "Congratulations on completing the game. Below is your game summary."
    play sound "dialogue.mp3"
    call screen showend
    "There are three endings in this game, welcome to continue to experience."
    play sound "dialogue.mp3"
    "This game is produced by {color=#F496E0}Xinyi Luo{/size}, and all resources come from the Internet."
    play sound "dialogue.mp3"
    "You can continue to enjoy the song for the rest of the time, or you can continue to the next round of the game."
    play sound "dialogue.mp3"
    "Goodbye."
    play sound "dialogue.mp3"
    return

screen showend():
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
            text "{color=#000000}Achieve the ending:{/size}[finialend]" size 60 color "#ff0000"  xcenter 0.5
            textbutton "Back":  
                    text_size 40 
                    text_color "#99CCFF"
                    xcenter 0   
                    activate_sound "audio/click.mp3"
                    action Return('')   
