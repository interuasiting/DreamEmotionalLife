label chaptertwo:
    "------{color=#FFC000}Chapter two{/size}: The mysterious girl------"
    scene schoolbedroom
    play music "audio/schoolbedroom.mp3"
    call showcharacter from _call_showcharacter_38
    you"In the blink of an eye, a month has passed, and you had a very happy time at school this month, but you discovered a very strange thing."
    play sound "dialogue.mp3"
    you"It is your neighbor. You have never known her name. Every time you meet her, she always walk quickly with head down. When you greet her, she ignores you."
    play sound "dialogue.mp3"
    you"hello neighbor!"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_26
    show cathy at left 
    neighbor"(Head down and walk quickly)"
    play sound "dialogue.mp3"
    hide cathy
    call showcharacter from _call_showcharacter_39
    you"One day, you made some biscuits and wanted to share them with your friends. Suddenly, you are reminded of this strange neighbor."
    play sound "dialogue.mp3"
    menu:
        "Are you going to knock on her door and give her some cookies?"
        "Yes":
            play sound "click.mp3"
            scene corridor
            call showcharacter from _call_showcharacter_40
            play sound "knockdoor.mp3"
            you"(Knock on the door.)"
            play sound "dialogue.mp3"
            you"(There was no response, Maybe no one was home.)"
            play sound "dialogue.mp3"
            play sound "getpoints.mp3"
            you"Maybe next time.\n{color=#FFC000}Self awareness + 5, Relationship skills + 5{/size}."
            play sound "dialogue.mp3"
            $Self_awareness +=5
            $Relationship_skills +=5
            play sound "dialogue.mp3"
        "No":
            play sound "click.mp3"
            you "Forget it, i feels like she doesn't like me very much."
            play sound "dialogue.mp3"
    scene classroom
    call showcharacter from _call_showcharacter_41
    play music "audio/classroom.mp3"
    you"When you chatted with your classmates, you talked about this strange neighbor, but you didn't expect your classmates to know this person."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_27
    classmate"I've heard of the person you mentioned. It seems that she is often bullied at school, which may cause her to be a little withdrawn, so that's why she doesn't want to get in touch with you."
    play sound "dialogue.mp3"
    call showcharacter from _call_showcharacter_42
    you "After hearing what your classmate say, you think:"
    play sound "dialogue.mp3"
    menu:
        "She is so poor, I want to help her!":
            play sound "click.mp3"
            "After hearing what your classmate said, your heart was filled with sympathy, and you decided to take the initiative to approach her, hoping to become her friend and provide her with some support and help."
            play sound "getpoints.mp3"
            "{color=#FFC000}Self awareness + 5, Social awareness + 5{/size}."
            play sound "dialogue.mp3"
            $Self_awareness+=5
            $Social_awareness+=5
        "None of my business":
            play sound "click.mp3"
            you"It seems to have nothing to do with me."
            play sound "dialogue.mp3"
    you"Anyway, you decide to get to know her and see if you can give her a little help."
    play sound "dialogue.mp3"
    scene corridor
    call showcharacter from _call_showcharacter_43
    "You met her again in the corridor."
    you"Hello! I am your neighbor, I see that you are not very happy alone every day, and I am a little worried about you. I want to be your friend, can I?"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_28
    show cathy at left
    neighbor"Hearing your words, she raised head and looked at your expression timidly."
    play sound "dialogue.mp3"
    "(Unlock cathy related episodes need Social awareness >= 30 and Relationship skills >= 30)"
    play sound "dialogue.mp3"
    if Social_awareness>=30 and Relationship_skills >=30:
        neighbor"It seems that have made up mind because of your past performance."
        play sound "dialogue.mp3"
        play sound "getpoints.mp3"
        cathy"(nodding shyly)My name is cathy.{color=#FFC000}(Unlock cathy related episodes){/size}"
        $unlockcathy = True
        play sound "dialogue.mp3"
        hide cathy
        call showcharacter from _call_showcharacter_44
        you "You talk to her briefly, and don't blurt out things like wanting to help her. After all, you're only officially acquainted now, and those words would be better said when you're on better terms."
    else:
        "The value of your attribute {color=#FF0000}does not{/size} satisfy the requirement."
        play sound "dialogue.mp3"
        neighbor"Putting her head down again, didn't say anything."
        play sound "dialogue.mp3"
        hide cathy
        call showcharacter from _call_showcharacter_45
        you"(helplessly)Fine.It seems there's no such opportunity to get to know her."
        play sound "dialogue.mp3"
    if unlockcathy == True:
        scene coffee
        play music "audio/coffee.mp3"
        "Gradually, you and cathy became good friends and she told you about her."
        play sound "dialogue.mp3"
        show cathy at left
        cathy"I've always had a weak character and I didn't dare say anything when people bullied me."
        play sound "dialogue.mp3"
        cathy"So some people knew about it and thought it would be fun to bully me and often made fun of me."
        play sound "dialogue.mp3"
        cathy"I also knew it was wrong for them to be like that, but I just didn't have the courage to fight them."
        play sound "dialogue.mp3"
        hide cathy
        call showcharacter from _call_showcharacter_46
        you"Once you know that it is her personality that causes her to be bullied, you often encourage her to be brave and say \"no\" to those who bully her."
        play sound "dialogue.mp3"
        you"Unfortunately, the results have not been very good, and perhaps an opportunity to make her truly brave is still missing."
        play sound "dialogue.mp3"
        scene schoolwoods_day
        call showcharacter from _call_showcharacter_47
        you"One day, you've just come out of the library, and as you pass through the grove you see a few people standing in front of Cathy. You don't know what these people are saying, you just see cathy crying."
        play sound "dialogue.mp3"
        you"You decide:"
        play sound "dialogue.mp3"
        menu:
            "Go and berate them. Tell them it's wrong.":
                play music "audio/fight.mp3"
                play sound "click.mp3"
                you"You walked over to stand in front of cathy and yelled at the group. They are always bullying and afraid of tough people, so when they saw you being so fierce, they naturally walked away in despair."
                play sound "dialogue.mp3"
                play sound "getpoints.mp3"
                you"{color=#FFC000}Self management + 5, Responsible decision-making + 5{/size}"
                $Self_management+=5
                $Responsible_decision_making+=5
                play sound "dialogue.mp3"
                call hidecharacter from _call_hidecharacter_29
                show cathyhappy at left
                cathy"Staring at you blankly, and then seeing that group of people leaving in desperation, it seemed that she really understood something."
                play sound "dialogue.mp3"
                cathy "(whisper)Thank you my friend."
                scene coffee
                call showcharacter from _call_showcharacter_48
                play music "audio/cathyhe.mp3"
                "After that day, cathy became more and more cheerful."
                play sound "dialogue.mp3"
                "She even told you one day that when those people bullied her again, she resisted and went back, and they didn't bully her anymore."
                play sound "dialogue.mp3"
                you"I'm so happy for you!"
                play sound "dialogue.mp3"
                call hidecharacter from _call_hidecharacter_30
                show cathyhappy at left 
                cathy"Yes, it's all thanks to you, you changed my life, thank you!"
                play sound "dialogue.mp3"
                hide cathyhappy
                "Unlock the achievement {color=#ED7D31}\"A New Life\"{/size}"
                $achievementcathy = True
            "Watching silently.Wanting cathy to really change is still up to her.":
                play sound "click.mp3"
                you"I've told her so much, and it's up to her to make real changes."
                play sound "dialogue.mp3"
                "You stood there watching for a long time, until the group got bored and walked away, cathy was still sobbing with her head down."
                play sound "dialogue.mp3"
                call hidecharacter from _call_hidecharacter_31
                show cathy  at left
                cathy "(About to leave but suddenly see you)"
                play sound "dialogue.mp3"
                cathy "(lowered her head again, not knowing what to think)"
                play sound "dialogue.mp3"
                scene corridor
                play music "audio/cathybe.mp3"
                call showcharacter from _call_showcharacter_49
                "After this day, you never saw cathy again and can't contact with her."
                play sound "dialogue.mp3"
                $unlockcathysecond = True
                "Soon after, you find out that new neighbors have moved in next door. No one knows where Cathy has gone."
                play sound "dialogue.mp3"
    else:
        scene schoolbedroom
        play music "audio/cathybe.mp3"
        call showcharacter from _call_showcharacter_50
        "The days go on and on and you still live a disjointed life with your neighbours. "
        play sound "dialogue.mp3"
        "Only one day you suddenly notice that a new one seems to have moved in next door and no one knows where your old neighbour has gone."
        play sound "dialogue.mp3"
    "------End of chapter two------"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_32
    scene map
    hide schoolwoods_dusk
    scene map
    play music "map.mp3"
    $month += 1
    $test_times += 3
    $showmonth = months[month]
    $leftmonth -= 1
    return 