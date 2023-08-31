label chapterone:
    "------{color=#FFC000}Chapter one{/size}: New School Life------"
    scene bedroom
    play music "audio/chapterone_bedroom.mp3"
    call showcharacter from _call_showcharacter_21
    you"Today is your first day of school, and you got up early in the morning excitedly."
    play sound "dialogue.mp3"
    you"As a graduate student of the School of Computing at the University of Dream, you have been interested in computers since you were a child."
    play sound "dialogue.mp3"
    you"Although you did not study computer-related subjects at university for some reason, now you finally have the opportunity to study your dream subject!"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_18
    mom"Come and have breakfast!"
    play sound "dialogue.mp3"
    call showcharacter from _call_showcharacter_22
    you"Hearing what mother said, you will:"
    play sound "dialogue.mp3"
    menu:
        "Answer her":
            play sound "click.mp3"
            scene diningroom
            call showcharacter from _call_showcharacter_23
            play sound "getpoints.mp3"
            you"Good morning mom, I'm coming!\n{color=#FFC000}Self management + 5, Relationship skills + 5{/size}. "
            $Self_management +=5
            $Relationship_skills +=5
            play sound "dialogue.mp3"
            you"You finish your breakfast and say goodbye to your family happily."
            play sound "dialogue.mp3"
        "Ignore her":
            play sound "click.mp3"
            you "You ignored her and go straight to school."
            play sound "dialogue.mp3"
    scene school
    play music "school.mp3"
    call showcharacter from _call_showcharacter_24
    you"After arriving at the school, you are very happy to see the new environment. You know that this is a new starting point in your life. "
    you"Although you are a little sad to leave home, you also know that you are going to a broader future."
    play sound "dialogue.mp3"
    you"Stepping into the new school, you are a little confused at first, but walked firmly to the dormitory area of the school. "
    play sound "dialogue.mp3"
    you"Just after you settled the luggage, you decided to go out for a stroll and familiarize yourself with the surrounding environment."
    play sound "dialogue.mp3"
    you"Where do you want to go now?"
    play sound "dialogue.mp3"
    menu choosetogo:
        "Canteen":
            play sound "click.mp3"
            scene canteen
            call showcharacter from _call_showcharacter_25
            you "The cafeteria is not open yet, but the environment looks clean."
            play sound "dialogue.mp3"
            you "What other places want to visit?"
            play sound "dialogue.mp3"
            jump choosetogo
        "Library":
            play sound "click.mp3"
            scene Library
            call showcharacter from _call_showcharacter_26
            you"The library is very quiet, some students are reading."
            play sound "dialogue.mp3"
            you "What other places want to visit?"
            play sound "dialogue.mp3"
            jump choosetogo
        "Gymnasium":
            play sound "click.mp3"
            scene Gymnasium
            call showcharacter from _call_showcharacter_27
            you"Gymnasium is big. Just in time, I'm going to run every morning in the future!"
            play sound "dialogue.mp3"
            you "What other places want to visit?"
            play sound "dialogue.mp3"
            jump choosetogo
        "Community camp":
            play sound "click.mp3"
    scene society
    play music "audio/chapterone_commuity.mp3"
    call showcharacter from _call_showcharacter_28
    you "There are many clubs in the activity room that are recruiting new students. You searched around and found the Association for Computing Machinery, which is exactly your purpose!"
    play sound "dialogue.mp3"
    you"Come to the table of the Association for Computing Machinery, and you see a group of like-minded students gathered together, passionately discussing the mysteries of computing."
    play sound "dialogue.mp3"
    you"One of the seniors saw you and greeted you warmly."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_19
    show lily at left 
    stranger "Hello, welcome to the recruitment of the Association for Computing Machinery! "
    play sound "dialogue.mp3"
    lily"I'm Lily, if you are interested in programming and want to join the association to learn, you are very welcome!"
    play sound "dialogue.mp3"
    "Lily smiled and held out her hand."
    play sound "dialogue.mp3"
    hide lily
    call showcharacter from _call_showcharacter_29
    you"You will?"
    menu:
        "Shake hands with her":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            you"Hello, nice to meet you!\n{color=#FFC000}Social awareness + 5, Relationship skills + 5{/size}"
            $Social_awareness += 5
            $Relationship_skills += 5
            play sound "dialogue.mp3"
            call hidecharacter from _call_hidecharacter_20
        "Don't shake her hand":
            play sound "click.mp3"
            you"(indifferent) Oh, hi."
            play sound "dialogue.mp3"
            call hidecharacter from _call_hidecharacter_21
            show lily at left 
            lily"(Embarrassed to put down hands)"
            play sound "dialogue.mp3"
            hide lily
    call showcharacter from _call_showcharacter_30
    you"I am very interested in programming and hope to join the association to learn."
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_22
    show lily at left 
    lily"It's great!"
    play sound "dialogue.mp3"
    lily"The atmosphere of the association is very good. We hold technology sharing and programming competitions every week. "
    play sound "dialogue.mp3"
    lily"You will have many opportunities to learn and improve yourself."
    play sound "dialogue.mp3"
    hide lily
    call showcharacter from _call_showcharacter_31
    play sound "getpoints.mp3"
    "You joined the Association for Computing Machinery.\n{color=#FFC000}knowledge + 10.{/size}"
    $knowledge+=10
    play sound "dialogue.mp3"
    scene schoolwoods_day
    play music "audio/schoolwoods.mp3"
    call showcharacter from _call_showcharacter_32
    you"After coming out of the club room, you walked around the school again."
    play sound "dialogue.mp3"
    scene schoolwoods_dusk
    call showcharacter from _call_showcharacter_33
    you"Soon it turns to dusk, and when you think back to the day, you think:"
    play sound "dialogue.mp3"
    menu:
        "It's about the same as the school life I imagined":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            you"I visited various places in the school, and I feel that the whole school is very beautiful~\n
            {color=#FFC000}Self awareness + 5, Responsible decision-making + 5.{/size}"
            $Self_awareness+=5
            $Responsible_decision_making+=5
            play sound "dialogue.mp3"
        "Met new friends, very happy":
            play sound "click.mp3"
            play sound "getpoints.mp3"
            you"I met senior sister Lily, she is a very good person.\n
            {color=#FFC000}Social awareness + 5, Relationship skills + 5.{/size}"
            $Social_awareness+=5
            $Relationship_skills+=5
            play sound "dialogue.mp3"
        "No idea":
            play sound "click.mp3"
            you"No idea, just another day passed."
            play sound "dialogue.mp3"
    "------End of chapter one------"
    play sound "dialogue.mp3"
    call hidecharacter from _call_hidecharacter_23
    scene map
    hide schoolwoods_dusk
    scene map
    play music "map.mp3"
    $month += 1
    $test_times += 3
    $showmonth = months[month]
    $leftmonth -= 1
    return 