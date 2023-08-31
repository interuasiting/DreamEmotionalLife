label chapterfive:
    "------{color=#FFC000}Chapter five{/size}: Computer Design Contest------"
    scene society
    play music "audio/chapterfive_society.mp3"
    "With contest coming up this month, you and the members of the Association often get together to discuss games to be made."
    play sound "dialogue.mp3"
    show lily at left 
    lily"First of all, what kind of game do you think we should make?"
    play sound "dialogue.mp3"
    hide lily
    member1"Love ! The theme of love is enduring!"
    play sound "dialogue.mp3"
    member2"Friendship! The strong friendship makes people yearn for!"
    play sound "dialogue.mp3"
    member3"Family! The beautiful intimacy is touching!"
    play sound "dialogue.mp3"
    call showcharacter from _call_showcharacter
    you"You're going to propose?"
    menu:
        "Funny":
            play sound "click.mp3"
            you"I think it can be a funny theme, so the game will be very interesting."
            play sound "dialogue.mp3"
        "Science":
            play sound "click.mp3"
            you"I think it could be a sci-fi theme, with fantastic future technology that would make the game interesting."
            play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter
    "After a lot of discussion, everyone finally decided on the theme of science fiction."
    play sound "dialogue.mp3"
    show lily at left 
    lily"Okay, then we have decided on the theme of our game, let's call it \"Space Adventure\"."
    play sound "dialogue.mp3"
    lily"This game will combine sci-fi elements and puzzle-solving elements. Players need to solve various puzzles in the virtual world and finally reach the ultimate goal."
    play sound "dialogue.mp3"
    "Then there is the game division of work. Some members are responsible for writing the storyline of the game, and some are responsible for designing the game screen and sound effects. You are assigned to write program code."
    play sound "dialogue.mp3"
    hide lily
    call showcharacter from _call_showcharacter_1
    "The part you are responsible for is more difficult and time-consuming than others, and your thoughts on this are:"
    play sound "dialogue.mp3"
    menu:
        "This is a great opportunity to challenge myself!":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            "Your coding ability is not strong, and you think this is just a good opportunity to improve your level.\n{color=#FFC000}Self awareness + 5, Self management + 5{/size}"
            play sound "dialogue.mp3"
            $Self_awareness+=5
            $Self_management+=5
            $unlockcontest += 1
        "It's not fair, why should I have to do the most troublesome job":
            play sound "click.mp3"
            "You think this is unfair, but seeing everyone is happy, you don't want to spoil the fun by protesting, so you comfort yourself that you can only spend more time at ordinary times."
            play sound "dialogue.mp3"
            play sound "getpoints.mp3"
            "{color=#FFC000}Social awareness + 5, Relationship skills + 5{/size}"
            play sound "dialogue.mp3"
            $Social_awareness+=5
            $Relationship_skills+=5
    scene Library
    play music "audio/library.mp3"
    call showcharacter from _call_showcharacter_2
    "Over the next few weeks, members of the association devoted a lot of time and energy to intensive work. You also often go to the library to check relevant materials."
    play sound "dialogue.mp3"
    "You also encountered a lot of difficulties in the process of coding."
    play sound "dialogue.mp3"
    "Right now, you have been solving this bug for three days, but you still haven’t succeeded. You going to:"
    play sound "dialogue.mp3"
    menu:
        "Try again!":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            "You think it's normal for you to feel that you're going to have a hard time at the moment, and it's important to keep trying.\n{color=#FFC000}Self management + 5, Responsible decision-making + 5{/size}"
            play sound "dialogue.mp3"
            $Self_management+=5
            $Responsible_decision_making+=5
            "With your continuous efforts, you finally solved it successfully!"
            $unlockcontest += 1
            play sound "dialogue.mp3"
        "Give up":
            play sound "click.mp3"
            "You don't think you can do it, so you contact Lily and tell her you are not capable enough to complete this task, so ask her to find someone else."
            play sound "dialogue.mp3"
            call hidecharacter from _call_hidecharacter_1
            show lily at left 
            lily"Fine, I will ask other members to assist you to carry it out together."
            play sound "dialogue.mp3"
            hide lily
            call showcharacter from _call_showcharacter_3
            "With the assistance of other members, you successfully solved the bug."
            play sound "dialogue.mp3"
    scene square
    "Soon, the game production was coming to an end, and members of the association began to prepare promotional and presentation materials for the game."
    play sound "dialogue.mp3"
    "They plan to design beautiful posters, presentations, and an engaging demo video to showcase the game's highlights and ideas."
    play sound "dialogue.mp3"
    call showcharacter from _call_showcharacter_4
    you"Would you like to help do it with them?"
    play sound "dialogue.mp3"
    menu:
        "Yes":
            play sound "click.mp3"
            you"Let me join you !"
            play sound "dialogue.mp3"
            play sound "getpoints.mp3"
            "With your joint efforts, a very good promotional material has been produced.\n{color=#FFC000}Social awareness + 5, Relationship skills + 5{/size}"
            play sound "dialogue.mp3"
            $Social_awareness+=5
            $Relationship_skills+=5
            $unlockcontest += 1
        "No":
            play sound "click.mp3"
            you"It is enough to have them do this."
            play sound "dialogue.mp3"
    "There are still three days before the end of the competition, do you think you need to optimize the game?"
    play sound "dialogue.mp3"
    menu:
        "Yes":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            "You feel that you should try to improve the game and make it even better, even if there is only one day left!\n{color=#FFC000}Self management + 5, Responsible decision-making + 5{/size}"
            play sound "dialogue.mp3"
            "With your suggestion, everyone continued to work overtime, constantly optimizing every aspect of the game to ensure its quality and integrity."
            play sound "dialogue.mp3"
            $Self_management+=5
            $Responsible_decision_making+=5
            $unlockcontest += 1
        "It's enough":
            play sound "click.mp3"
            you"I think the game is pretty much done."
            play sound "dialogue.mp3"
    scene contest
    play music "audio/space.mp3"
    "Competition day"
    play sound "dialogue.mp3"
    show moderator at left
    moderator"The next entry is from the Dream University - Association for Computing Machinery. The name of the game is {color=#FFC000}Space Adventure{/size}. Please watch a demonstration of the game!"
    play sound "dialogue.mp3"
    hide moderator
    scene space
    "(Show game)"
    play sound "dialogue.mp3"
    "(Members explain the game's creativity and design ideas)"
    play sound "dialogue.mp3"
    if unlockcontest == 4:
        $unlockwin = True
    scene contest
    play music "audio/beat.mp3"
    "(Awaiting the final decision of the judges)"
    play sound "dialogue.mp3"
    show moderator at left
    moderator"The winner of this competition is ——— "
    play sound "dialogue.mp3"
    if unlockwin == True and knowledge >= 100:
        play music "audio/win.mp3"
        moderator"Game from Dream University Association for Computing Machinery ——— {color=#FF0000}Space Adventures{/size}! Congratulations!"
        play sound "dialogue.mp3"
        moderator"This is the judges' comment ——— "
        play sound "dialogue.mp3"
        hide moderator
        judges"The game screen is exquisite, the sound effect is realistic, the gameplay is innovative, and various puzzles and challenges are full of fun. It's a rare good game!"
        play sound "dialogue.mp3"
        call showcharacter from _call_showcharacter_5
        "You win! Everyone is cheering and excited, your hard work has got the best return!"
        play sound "dialogue.mp3"
        "At this moment, you are really thankful that you have achieved perfection in any step at the beginning."
        play sound "dialogue.mp3"
        "Unlock the achievement {color=#ED7D31}\"Competition Victory\"{/size}"
        $achievementfive = True
        play sound "dialogue.mp3"
    else:
        play music "audio/lose.mp3"
        moderator"Game from Sun University —— Harry's day! Congratulations!"
        play sound "dialogue.mp3"
        moderator"The evaluation of the judges for the game of Dream University Association for Computing Machinery is as follows —— "
        play sound "dialogue.mp3"
        hide moderator
        judges"The game screen is ordinary, the sound effect is average, and the gameplay is not innovative enough."
        play sound "dialogue.mp3"
        call showcharacter from _call_showcharacter_6
        "Unfortunately, you did not win the game. Faced with so many days of hard work, it is a lie for everyone to say that they are not sad."
        play sound "dialogue.mp3"
        "If only I had worked harder in the first place."
        play sound "dialogue.mp3"
        call hidecharacter from _call_hidecharacter_2
        "Unfortunately, there is no if."
        play sound "dialogue.mp3"
    "------End of chapter five------"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_3
    scene map
    hide schoolwoods_dusk
    scene map
    play music "map.mp3"
    $month += 1
    $test_times += 3
    $showmonth = months[month]
    $leftmonth -= 1
    return 