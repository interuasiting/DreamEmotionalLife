label chapterthree:
    "------{color=#FFC000}Chapter three{/size}: Dream and Reality------"
    scene schoolbedroom
    play music "audio/chapterthree_schoolbedroom.mp3"
    call showcharacter from _call_showcharacter_51
    you "As you've been studying for the past two months, you've realised that you're enjoying Computer Science more and more as a profession, but you're still considering whether you'd like to continue in the industry in the future."
    play sound "dialogue.mp3"
    you "One day You received a message from Lily, she asked you to go to the activity room of the association."
    play sound "dialogue.mp3"
    scene society
    show lily at left
    lily "It's been two months since you joined the Association, do you think you've gained a lot from it?"
    play sound "dialogue.mp3"
    hide lily
    call showcharacter from _call_showcharacter_52
    you "Yes, of course!"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_33
    show lily at left
    lily "That's good. There's a competition coming up. We'd like to invite you to join as a member. We want to make a game."
    play sound "dialogue.mp3"
    hide lily
    call showcharacter from _call_showcharacter_53
    you "Your idea is:"
    play sound "dialogue.mp3"
    menu:
        "I'll take it seriously!":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            you "This is my first time participating in a competition, and I will definitely prepare well!\n{color=#FFC000}Self management + 5, Relationship skills + 5{/size}"
            play sound "dialogue.mp3"
        "Just do it casually, don't take it too seriously.":
            play sound "click.mp3"
            you"It's just an ordinary competition, so I don't have to take it so seriously."
            play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_34
    show lily at left
    lily "The competition will be held in {color=#FF0000}January{/size} next year.\n(One of the game winning conditions: {color=#FF0000}Knowledge >= 100{/size})"
    play sound "dialogue.mp3"
    hide lily
    call showcharacter from _call_showcharacter_54
    you"OK!"
    play sound "dialogue.mp3"
    scene lake
    play music "audio/lake.mp3"
    call showcharacter from _call_showcharacter_55
    you"This night, you were walking along the school lake alone, and suddenly heard a melodious sound of a violin."
    play sound "dialogue.mp3"
    you"You find out that there is a man playing the violin." 
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_35
    show jack2 at left
    "Finding someone looking at him, he stopped."
    play sound "dialogue.mp3"
    hide jack2
    show jack at left
    stranger"Hello, what can I do for you?"
    play sound "dialogue.mp3"
    hide jack
    call showcharacter from _call_showcharacter_56
    you"Sorry to bother you, I just wanted to say that you play the violin really well!"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_36
    show jack at left
    jack"Thank you! I'm Jack."
    play sound "dialogue.mp3"
    hide jack
    call showcharacter from _call_showcharacter_57
    "You chatted with Jack, the two of you unexpectedly got along very well."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_37
    show jack at left
    "Jack is a talented young man who is obsessed with the violin and has a deep love for music. His dream is to become an excellent violinist and use music to convey his emotions and ideas."
    play sound "dialogue.mp3"
    "However, Jack's dreams collide with his family values. His parents firmly believed that music, while a wonderful hobby, was not enough for his future career."
    play sound "dialogue.mp3"
    "They expect Jack to choose a more \"practical\" career and create a stable life for himself and his family.They believe that the violin can be used as a hobby, but it is not suitable to be Jack's main development direction."
    play sound "dialogue.mp3"   
    jack"I really like the violin, but my parents' attitude is also very firm, and I don't know what to do in the future."
    play sound "dialogue.mp3"
    scene breadshop
    play music "audio/coffee.mp3"
    call showcharacter from _call_showcharacter_58
    "Jack and you have gradually become good friends, and you share bits and pieces of study and life together. You saw him put his emotions into his violin playing, and every performance was intoxicating."
    play sound "dialogue.mp3"
    "However, you also noticed that he seemed hesitant and helpless in the face of family pressure."
    play sound "dialogue.mp3"
    you"Do you want to encourage him to follow his dreams?"
    play sound "dialogue.mp3"
    menu:
        "Yes\n(Need Relationship skills >= 40 and Responsible decision-making >= 30)" if Relationship_skills >= 40 and Responsible_decision_making >= 30:
            play sound "click.mp3"
            $unlockjack += 1
            you"Jack, I think you can stick to your dreams, and of course I understand your parents' concerns."
            play sound "dialogue.mp3"
            you"You know many successful musicians who have faced similar dilemmas, but they have finally achieved success through their love and persistence in music."
            play sound "dialogue.mp3"
            play sound "getpoints.mp3"
            you"The journey of life is full of challenges, but if you firmly believe in your dreams and work hard, you will be able to achieve your goals.\n{color=#FFC000}Self management + 5, Responsible decision-making + 5{/size}"
            $Self_management+=5
            $Responsible_decision_making+=5
            play sound "dialogue.mp3"
        "No":
            play sound "click.mp3"
            you"Let it be, his parents' words are not without reason."
            play sound "dialogue.mp3"
    scene lakeday
    call showcharacter from _call_showcharacter_59
    "Over the next few days, Jack and you worked out a plan to help him find a balance between school and music." 
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_38
    show jack at left
    "He tried his best to use time management to balance his study and violin practice, insisted on practicing the violin every day, and constantly improved his playing skills."
    play sound "dialogue.mp3"
    "At the same time, he also actively participates in the activities of the school music club, sharing his talents with other students who love music."
    play sound "dialogue.mp3"
    hide jack
    call showcharacter from _call_showcharacter_60
    you"In addition, do you think you should persuade him to talk to his parents again?"
    play sound "dialogue.mp3"
    menu:
        "Yes":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            you"Jack, I think you can talk openly with your parents again, show them your hard work and achievements, and let them see your dedication and determination to music.\n{color=#FFC000}Social awareness + 5, Relationship skills + 5{/size}"
            $Social_awareness+=5
            $Responsible_decision_making+=5
            $unlockjack += 1
            play sound "dialogue.mp3"
            call hidecharacter from _call_hidecharacter_39
            show jack at left
            jack"You are right, I should try again." 
            play sound "dialogue.mp3"
            "Through in-depth communication with his parents, they gradually began to understand Jack's dream and provided him with more support and encouragement."
            play sound "dialogue.mp3"
            hide jack
        "No":
            play sound "click.mp3"
            you"It's enough with his own efforts."
            play sound "dialogue.mp3"
            call hidecharacter from _call_hidecharacter_40
    "Time passed..."
    play sound "dialogue.mp3"
    if unlockjack == 0:
        scene coffee
        play music "audio/jackbe.mp3"
        call showcharacter from _call_showcharacter_61
        "You meet Jack at a coffee, and you ask Jack how he is doing."
        call hidecharacter from _call_hidecharacter_41
        play sound "dialogue.mp3"
        show jack at left
        jack "(Sad) My parents still insisted on their opinions."
        play sound "dialogue.mp3"
        jack"Maybe wanting to become a violinist can only be my dream forever."
        play sound "dialogue.mp3"
        hide jack
    elif unlockjack == 1 :
        scene coffee
        play music "audio/jackbe2.mp3"
        call showcharacter from _call_showcharacter_62
        "You meet Jack at a coffee, and you ask Jack how he is doing recently."
        call hidecharacter from _call_hidecharacter_42
        play sound "dialogue.mp3"
        show jack at left
        jack "(Calmly)They recognized my efforts, although not as strongly as before, they still believed that their ideas were correct."
        play sound "dialogue.mp3"
        jack"Maybe one day in the future they will suddenly figure it out, maybe never..."
        play sound "dialogue.mp3"
        hide jack
    else:
        scene theater
        play music "audio/jackhe.mp3"
        "Over time, Jack has made remarkable progress both academically and musically. He has achieved excellent academic results and also showed his style on the music stage."
        play sound "dialogue.mp3"
        "His parents gradually changed their attitude and began to support him in pursuing a music career."
        play sound "dialogue.mp3"
        call showcharacter from _call_showcharacter_63
        "Today is Jack's violin concert, and you are invited to attend."
        play sound "dialogue.mp3"
        call hidecharacter from _call_hidecharacter_43
        show jack2 at left
        "On the stage, Jack moved the audience with his moving violin sound."
        play sound "dialogue.mp3"
        hide jack2
        call showcharacter from _call_showcharacter_64
        you"Jack has realized his music dream, I am really happy for him!"
        play sound "dialogue.mp3"
        you"He realized his dream and found his future, what about me?"
        play sound "dialogue.mp3"
        you"what will my future be like?"
        play sound "dialogue.mp3"
        "Unlock the achievement {color=#ED7D31}\"Dreams Come True\"{/size}"
        $achievementjack = True
        play sound "dialogue.mp3"
    "------End of chapter three------"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_44
    scene map
    hide schoolwoods_dusk
    scene map
    play music "map.mp3"
    $month += 1
    $test_times += 3
    $showmonth = months[month]
    $leftmonth -= 1
    return 