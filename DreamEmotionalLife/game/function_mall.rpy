label function_mall:
    scene mall
    show seller at left with dissolve
    play music "mall.mp3"
    call hidecharacter from _call_hidecharacter_45
    seller"Welcome to the mall, what do you want to buy? "
    play sound "dialogue.mp3"
    menu buyproperties:
        seller "You have money : {color=#FF0000}[money]{/size}"
        "Self-awareness + {color=#FFC000}5{/size}(need money 60) ":
            play sound "click.mp3"
            if money >= 60:
                play sound "getpoints.mp3"
                $money -= 60
                $Self_awareness+=5
                seller "Successful purchase! Your Self-awareness now is {color=#FFC000}[Self_awareness]{/size}."
                play sound "dialogue.mp3"
            else:
                seller"Sorry you don't have enough money."
                play sound "dialogue.mp3"
            jump buyproperties
        "Self-management + {color=#FFC000}5{/size}(need money 60)":
            play sound "click.mp3"
            if money >= 60:
                play sound "getpoints.mp3"
                $money -= 60
                $Self_management+=5
                seller "Successful purchase! Your Self-management now is {color=#FFC000}[Self_management]{/size}."
                play sound "dialogue.mp3"
            else:
                seller"Sorry you don't have enough money."
                play sound "dialogue.mp3"
            jump buyproperties
        "Social awareness + {color=#FFC000}5{/size}(need money 60)":
            play sound "click.mp3"
            if money >= 60:
                play sound "getpoints.mp3"
                $money -= 60
                $Social_awareness+=5
                seller "Successful purchase! Your Social awareness now is {color=#FFC000}[Social_awareness]{/size}."
                play sound "dialogue.mp3"
            else:
                seller"Sorry you don't have enough money."
                play sound "dialogue.mp3"
            jump buyproperties
        "Relationship skills + {color=#FFC000}5{/size}(need money 60)":
            play sound "click.mp3"
            if money >= 60:
                play sound "getpoints.mp3"
                $money -= 60
                $Relationship_skills+=5
                seller "Successful purchase! Your Relationship skills now is {color=#FFC000}[Relationship_skills]{/size}."
                play sound "dialogue.mp3"
            else:
                seller"Sorry you don't have enough money."
                play sound "dialogue.mp3"
            jump buyproperties
        "Responsible decision-making + {color=#FFC000}5{/size}(need money 60)":
            play sound "click.mp3"
            if money >= 60:
                play sound "getpoints.mp3"
                $money -= 60
                $Responsible_decision_making+=5
                seller "Successful purchase! Your Responsible decision-making now is {color=#FFC000}[Responsible_decision_making]{/size}."
                play sound "dialogue.mp3"
            else:
                seller"Sorry you don't have enough money."
                play sound "dialogue.mp3"
            jump buyproperties
        "Test times + {color=#FFC000}1{/size}(need money 80)":
            play sound "click.mp3"
            if money >= 80:
                play sound "getpoints.mp3"
                $money -= 80
                $test_times+=1
                seller "Successful purchase! Your Test times now is {color=#FFC000}[test_times]{/size}."
                play sound "dialogue.mp3"
            else:
                seller"Sorry you don't have enough money."
                play sound "dialogue.mp3"
            jump buyproperties
        "Back":
            play sound "click.mp3"
            hide seller
            scene map
            call hidecharacter from _call_hidecharacter_46
            play music "map.mp3"
            return 