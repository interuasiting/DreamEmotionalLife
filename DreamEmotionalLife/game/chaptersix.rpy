label chaptersix:
    "------{color=#FFC000}Chapter six{/size}: Graduation------"
    scene graduation
    play music "audio/graduation.mp3"
    call showcharacter from _call_showcharacter_34
    "The six months in school have passed in a blink of an eye, and you have your graduation ceremony. Think back to these six months, you met a lot of people, a lot of things happened."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_24
    ###lily
    show lily at left
    "You joined the Association for Computing Machinery and met senior sister Lily."
    play sound "dialogue.mp3"
    hide lily
    ###cathy
    if unlockcathy == False: ##be1
        show cathy at left 
        "You met a strange neighbor whose name you didn't know until she moved out."
        play sound "dialogue.mp3"
        hide cathy
    elif unlockcathy == True and unlockcathysecond == True:##be2
        show cathy at left 
        "You met your neighbor cathy. You had become good friends, but she left without saying goodbye after a certain day. It may be because of your unintentional behavior that broke her heart."
        play sound "dialogue.mp3"
        hide cathy
    elif unlockcathy == True and unlockcathysecond == False:##he
        show cathyhappy at left
        "You met your neighbor cathy, and you became good friends. At the same time, with your help, she bravely defeated the bully and successfully changed herself."
        play sound "dialogue.mp3"
        $cathyend = True
        $perfect += 1
        hide cathyhappy
    ###jack
    if unlockjack == 0:##be1
        show jack at left
        "You met Jack, his dream was to become a violinist, but unfortunately he lost to reality in the end."
        play sound "dialogue.mp3"
        hide jack
    elif unlockjack == 1:##be2
        show jack at left
        "You meet Jack, whose dream is to become a violinist. He is still trying to convince his parents to realize his dream to this day."
        play sound "dialogue.mp3"
        hide jack
    else:##he
        show jack2 at left
        "Your good friend jack, he has held several violin concerts, and he is walking towards his dream step by step."
        play sound "dialogue.mp3"
        $jackend = True
        $perfect += 1
        hide jack2
    ###henry
    if unlockhenry < 3:
        show henrysad at left
        "You think of the father and son. Their story is a tragedy. You heard that Henry's father has passed away."
        play sound "dialogue.mp3"
        hide henrysad
    else:
        show henry at left
        "You think of the father and son. They actually love each other very much, but there are too many misunderstandings. Fortunately, it is not too late."
        play sound "dialogue.mp3"
        $henryend = True
        $perfect += 1
        hide henry
    ####
    if unlockwin == True and knowledge >= 100:
        call showcharacter from _call_showcharacter_35
        $lilyend = True
        $perfect += 1
        "In last month's competition, through the joint efforts of everyone in your association, you won the first prize. Everyone is very happy."
        play sound "dialogue.mp3"
    else:
        call showcharacter from _call_showcharacter_36
        "It is a pity that you did not win the competition last month and did not draw a successful conclusion to study life."
        play sound "dialogue.mp3"
    "The headmaster's voice interrupted your recollection, he read your name."
    play sound "dialogue.mp3"
    "You walked up to the stage to accept the diploma in his hand."
    play sound "dialogue.mp3"
    if lilyend == True or cathyend == True or jackend == True or henryend == True:
        if perfect == 4:
            play music "audio/perfect.mp3"
        else:
            play music "audio/ordinal.mp3"
        "You are suddenly pleasantly surprised to find that besides your parents, your friends are also here."
        play sound "dialogue.mp3"
        call hidecharacter from _call_hidecharacter_25
        if lilyend == True:
            show lily at left
            lily"Congratulations on graduating! You must come to our association dinner tonight!"
            play sound "dialogue.mp3"
            hide lily
        if cathyend == True:
            show cathyhappy at left
            cathy"Congratulations my best friend! Thank you for changing my life."
            play sound "dialogue.mp3"
            hide cathyhappy
        if jackend == True:
            show jack2 at left
            jack"Congratulations on graduating! This is a song I created specially for you, I hope you like it."
            play sound "dialogue.mp3"
            hide jack2
        if henryend == True:
            show henry at left
            henry"Congratulations! Thank you for clearing up the misunderstanding between me and my father. He is in much better health now, and he came to the scene today."
            play sound "dialogue.mp3"
            hide henry
            show fatherhappy at left
            fatherhappy"Congratulations! Thank you for bringing me and my son back together."
            play sound "dialogue.mp3"
            hide fatherhappy
        call showcharacter from _call_showcharacter_37
        if perfect == 4:
            "Your friends have all sent you their wishes, and you think, this is the best graduation gift you can ever receive."
            play sound "dialogue.mp3"
            "During these six months of study and life, you not only gained knowledge, but also met them more preciously. These bits and pieces have gathered into your growth."
            play sound "dialogue.mp3"
            "You think, you are no longer afraid of the future, you have clearly seen that your future is bright."
            play sound "dialogue.mp3"
            "Unlock the achievement {color=#FF0000}\"\[True End\]Sparkling Life\"{/size}"
            $achievementtrueend = True
            play sound "dialogue.mp3"
        else:
            "Your friends are sending you blessings, and even though some people you know don't come, you're still happy."
            play sound "dialogue.mp3"
            "You think it's time to move on to the next stage of your life."
            play sound "dialogue.mp3"
            "Unlock the achievement {color=#ED7D31}\"\[Normal End\]Keep Going\"{/size}"
            $achievementnormalend = True
            play sound "dialogue.mp3"
    else:
        play music "audio/bad.mp3"
        "Although you know a lot of people, none of them came to your graduation except your parents."
        play sound "dialogue.mp3"
        "You are a little sad, but you know that life is like this, everyone is a passerby, and the only ones who can accompany you in the end are your family members."
        play sound "dialogue.mp3"
        "Unlock the achievement {color=#0070C0}\"\[Bad End\]Travel Alone\"{/size}"
        $achievementbadend = True
        play sound "dialogue.mp3"
    "------End of chapter six------"
    call endgame from _call_endgame
    return 