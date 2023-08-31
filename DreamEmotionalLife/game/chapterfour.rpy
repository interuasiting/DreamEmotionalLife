label chapterfour:
    "------{color=#FFC000}Chapter four{/size}: Unknown father's love------"
    scene school
    play music "audio/schoolgate.mp3"
    call showcharacter from _call_showcharacter_7
    you"One day, when you came out of school, you saw a middle-aged man standing at the door. He was dressed in shabby clothes and looked anxious, meanwhile he keeps coughing."
    play sound "dialogue.mp3"
    you"You think maybe this person is in some trouble, so you go up to him and ask him."
    play sound "dialogue.mp3"
    you"Hello, may I ask what trouble you have encountered? Is there anything I can do to help you?"
    call hidecharacter from _call_hidecharacter_4
    show father at left
    play sound "cough.mp3"
    stranger"Hello(cough), I came to school to visit my son Henry, but I can't get in touch with him(cough)."
    play sound "dialogue.mp3"
    hide father
    call showcharacter from _call_showcharacter_8
    you"Don't worry, I'll help you contact him."
    play sound "dialogue.mp3"
    "You dial the number he gave you, and a young man's voice is on the other end of the line."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_5
    show henryblack at left
    stranger"Hello?"
    play sound "dialogue.mp3"
    hide henryblack
    call showcharacter from _call_showcharacter_9
    you"Hello, is this Henry? Your father came to the school to look for you, and he is at the school gate now."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_6
    show henryblack at left
    stranger"(impatiently) I don't have time to go."
    play sound "dialogue.mp3"
    hide henryblack
    call showcharacter from _call_showcharacter_10
    "You are surprised why his attitude is so bad, but the other party hangs up the phone immediately."
    play sound "dialogue.mp3"
    "You told the father about the situation, he just smiled bitterly."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_7
    show father at left
    play sound "cough.mp3"
    stranger"Thank you(cough). I'd better wait for him at the door(cough)."
    play sound "dialogue.mp3"
    hide father
    call showcharacter from _call_showcharacter_11
    you"You decide:"
    play sound "dialogue.mp3"
    menu:
        "Call again and tell him to come to his father":
            play sound "click.mp3"
            $unlockhenry += 1
            you"You felt you couldn't just leave this father alone, so you called back.\n{color=#FFC000}Social awareness + 5, Responsible decision-making + 5{/size}"
            play sound "dialogue.mp3"
            you"Hello, I think you'd better come over, your father looks like he's been waiting here for you for a long time."
            play sound "dialogue.mp3"
            call hidecharacter from _call_hidecharacter_8
            show henryblack at left
            stranger "Fine, I'm coming over."
            play sound "dialogue.mp3"
            hide henryblack
            call showcharacter from _call_showcharacter_12
            "You were relieved to hear him say that, and after saying goodbye to that father you left."
            play sound "dialogue.mp3"
        "The rest is none of my business. Leave here":
            play sound "click.mp3"
            you"Since this father has said so, I'd better mind my own business."
            play sound "dialogue.mp3"
    scene square
    play music "audio/square.mp3"
    call showcharacter from _call_showcharacter_13
    "On this day, you're walking along the road when you suddenly hear the person next to you chatting and vaguely hear Henry's name."
    play sound "dialogue.mp3"
    "You turn around and see a man, and by the sound of his voice it's the same guy from the phone call the other day, he should be henry."
    play sound "dialogue.mp3"
    "You want to know what followed that day, whether he went to see his father or not. So you move forward to talk to him."
    play sound "dialogue.mp3"
    "You walk over and realise that he's actually a classmate of yours, you've seen him in class, you just don't know him."
    play sound "dialogue.mp3"
    you"Hello, you must be Henry. I'm the one who called for your father the other day."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_9
    show henry at left
    "He also seemed to recognise you as his classmate."
    play sound "dialogue.mp3"
    henry"Oh, it's you. I still didn't go over."
    play sound "dialogue.mp3"
    hide henry
    call showcharacter from _call_showcharacter_14
    you"May I take the liberty of asking why you treated your father so badly?"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_10
    show henry at left
    henry"He brought this on himself."
    play sound "dialogue.mp3"
    "Henry began to tell his past."
    play sound "dialogue.mp3"
    henry"When my mother left us when I was a child, he started drinking every day and instead of going to work, he would get drunk and lie in front of the supermarket."
    play sound "dialogue.mp3"
    henry"I was still in primary school at that time, and there was no one to cook for me, so I had to go out and collect some bottles by myself every day and sell them for money to buy food."
    play sound "dialogue.mp3"
    henry"When I started junior high school, he didn't pay my school fees, and if it wasn't for the kind people who helped me pay my school fees, I would have had to drop out of school."
    play sound "dialogue.mp3"
    henry"Usually, I don't know what he's doing, and I can't reach him at all."
    play sound "dialogue.mp3"
    henry"Because my family was poor I didn't have a lot of clothes to wear, only a few clothes all year round. My classmates teased and bullied me."
    play sound "dialogue.mp3"
    henry"Once I was bullied so hard I fought back and ended up injuring the opposite side, so the teacher called both parents to school. The father of the other came and scolded me the whole time."
    play sound "dialogue.mp3"
    henry"And him? Couldn't get in touch at all at first, and when got in touch later, the first thing he did when he came to school and saw me was to give me a hard time, not caring what the truth was."
    play sound "dialogue.mp3"
    henry"Then I got into university with my own hard work, but the tuition fees were not enough, so I worked hard during the holidays to earn tuition fees, and in the meantime, as usual, I couldn't get in touch with him."
    play sound "dialogue.mp3"
    henry"I guess it was probably another drunken lie-in somewhere."
    play sound "dialogue.mp3"
    henry"I really hate him."
    play sound "dialogue.mp3"
    henry"Then the day before school started, he appeared out of the blue and gave me a sum of money, just enough for tuition, and I don't know where he got it. Probably not a regular source."
    play sound "dialogue.mp3"
    hide henry
    call showcharacter from _call_showcharacter_15
    "After listening to him, you feel as if his father did do something wrong, and it's understandable that he has such an attitude."
    play sound "dialogue.mp3"
    "Suddenly you remember the way his father looked that day and his anxious attitude, you think:"
    play sound "dialogue.mp3"
    menu:
        "Could there be some misunderstanding?":
            play sound "click.mp3"
            $unlockhenry += 1
            you"It is sounds that your father does have a problem, but I saw him dressed in rags the other day, he looks tired, coughs all the time, and his health may not be very good recently."
            play sound "dialogue.mp3"
            play sound "getpoints.mp3"
            you"And it did seem like he waited a long time for you, like he really missed you and wanted to see you.\n{color=#FFC000}Self awareness + 5, Relationship skills + 5{/size}"
            play sound "dialogue.mp3"
            $Self_awareness+=5
            $Relationship_skills+=5
            call hidecharacter from _call_hidecharacter_11
            show henry at left
            "After hearing you say that, Henry instead showed a look of uncertainty."
            play sound "dialogue.mp3"
            henry"I really haven't seen him or talked to him in a long time. He has offered to see me a few times and I have not said yes."
            play sound "dialogue.mp3"
            hide henry
            call showcharacter from _call_showcharacter_16
            you"Faced with this situation, you prepared:"
            play sound "dialogue.mp3"
            menu:
                "Persuade him to visit his father\n(Need Self awareness >= 40 and Relationship skills >= 35)" if Self_awareness >= 20 and Relationship_skills >= 20:
                    $unlockhenry += 1
                    play sound "click.mp3"
                    you"Maybe there's some kind of misunderstanding? Why don't you meet him for a good heart-to-heart talk!\n{color=#FFC000}Self management + 5, Social awareness + 5{/size}"
                    play sound "dialogue.mp3"
                    $Self_management+=5
                    $Social_awareness+=5
                    call hidecharacter from _call_hidecharacter_12
                    show henry at left
                    "henry's expression turned firm for a moment."
                    play sound "dialogue.mp3"
                    henry"I see, I'll visit him, thank you!"
                    play sound "dialogue.mp3"
                    "Henry said goodbye to you."
                    play sound "dialogue.mp3"
                    hide henry
                "What's been said has been said, and the rest is none of my business":
                    play sound "click.mp3"
                    you"Fine, it's up to you."
                    play sound "click.mp3"
                    "You said goodbye to henry."
                    play sound "dialogue.mp3"
        "His father had it all coming to him":
            play sound "click.mp3"
            you"I think you did the right thing, after all your father do something so outrageous."
            play sound "dialogue.mp3"
            "You said goodbye to henry."
            play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_13
    if unlockhenry < 3:
        scene classroom
        play music "audio/henrybe.mp3"
        "After some days."
        play sound "dialogue.mp3"
        call showcharacter from _call_showcharacter_17
        "You suddenly found that you hadn't seen Henry in class recently, and you didn't know where he went. So you asked your classmates about him."
        play sound "dialogue.mp3"
        call hidecharacter from _call_hidecharacter_14
        classmate"You mean Henry, his father was seriously ill, and will probably pass away soon. So Henry went home. I heard that there have been many misunderstandings between them."
        play sound "dialogue.mp3"
        classmate"Henry's father really loves him and has done a lot for him, but Henry doesn't know anything, and his father never told him anything."
        play sound "dialogue.mp3"
        classmate"what a tragedy between them!"
        play sound "dialogue.mp3"
    else:
        scene coffee
        play music "audio/henryhe.mp3"
        call showcharacter from _call_showcharacter_18
        "The next day."
        play sound "dialogue.mp3"
        "You get a call from Henry, he invites you to meet at the coffee."
        play sound "dialogue.mp3"
        call hidecharacter from _call_hidecharacter_15
        show henry at left
        henry"I invite you to meet just to thank you specifically for what you have done for me and my father."
        play sound "dialogue.mp3"
        henry"There were many misunderstandings between me and him, but they are all solved now."
        play sound "dialogue.mp3"
        henry"He said that it was really wrong for him to drink too much every day when I was in primary school, but later he came to his senses. He found out that he still had a son to support, and he couldn't go on being decadent like this."
        play sound "dialogue.mp3"
        henry"When he was in junior high school, he often couldn't be contacted because he was doing hard work on the construction site and had no time to answer the phone. He said that his education is too low, and he can only do these extremely hard jobs."
        play sound "dialogue.mp3"
        henry"The time I was invited by a parent, he actually got into a fight with the parent who scolded me after I left, because that person scolded me in front of him."
        play sound "dialogue.mp3"
        henry"He also worked hard during the holidays before I go to college, and finally saved enough for my tuition the day before I started school."
        play sound "dialogue.mp3"
        henry"Now that I am in college, he can finally work less hard, but his body has become very poor due to years of hard work, and he fell ill badly."
        play sound "dialogue.mp3"
        henry"He didn't want anything else, just wanted to see me more in the remaining days."
        play sound "dialogue.mp3"
        hide henry
        call showcharacter from _call_showcharacter_19
        you"Is he really very ill?"
        play sound "dialogue.mp3"
        call hidecharacter from _call_hidecharacter_16
        show henry at left
        henry"(Shakes head) It's actually not as serious as he thought, but it will definitely become serious if it is not treated in time. I will definitely send him to therapy now, and take good care of him."
        play sound "dialogue.mp3"
        henry"I really want to say thank to you!"
        play sound "dialogue.mp3"
        hide henry
        call showcharacter from _call_showcharacter_20
        "After Henry left, you couldn't help but smile happily when you recalled what happened in the past few days."
        play sound "dialogue.mp3"
        you"Fortunately, Henry's father's love was finally known."
        play sound "dialogue.mp3"
        "Unlock the achievement {color=#ED7D31}\"It's not too late\"{/size}"
        $achievementhenry = True
        play sound "dialogue.mp3"
    "------End of chapter four------"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_17
    scene map
    hide schoolwoods_dusk
    scene map
    play music "map.mp3"
    $month += 1
    $test_times += 3
    $showmonth = months[month]
    $leftmonth -= 1
    return 