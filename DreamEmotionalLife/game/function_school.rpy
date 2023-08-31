####School#####
label function_school: 
    play music "school.mp3"
    scene school
    call hidecharacter from _call_hidecharacter_47
    show teacher at left with dissolve
    teacher "Welcome to shcool, what do you want to do?"
    play sound "dialogue.mp3" 
    menu menu_school:
        "Learn Knowledge": #Learn Knowledge
            play sound "click.mp3"
            teacher"Which subject do you want to learn?"
            play sound "dialogue.mp3" 
            menu learnknowledge:
                "C++":
                    hide teacher
                    play sound "click.mp3"
                    call screen learnc
                    jump learnknowledge
                "Java":
                    hide teacher
                    play sound "click.mp3"
                    call screen learnjava
                    jump learnknowledge
                "Back":
                    play sound "click.mp3"
                    show teacher at left
                    jump menu_school    
        "Join Test": #Join Test
            play music "testc.mp3"
            play sound "click.mp3"
            teacher"Welcome to join test, you still left {color=#FF0000}[test_times]{/color} chance."
            play sound "dialogue.mp3" 
            teacher"There will be 5 questions in each test. Answering a question correctly will give you {color=#FFC000}money + 20{/size} and {color=#FFC000}knowledge + 5{/size}. There will be no reward for wrong answers."
            play sound "dialogue.mp3" 
            if test_times > 0: 
                menu menu_test:
                    teacher"What kinds of test do you want to join?"
                    "C++":
                        play sound "click.mp3"
                        if test_times > 0:
                            call testc from _call_testc
                            jump menu_test
                        else:
                            teacher"You have no chance to take the test this month, please come back next month."
                            jump menu_test
                    "Java":
                        play sound "click.mp3"
                        if test_times > 0:
                            call testjava from _call_testjava
                            jump menu_test
                        else:
                            teacher"You have no chance to take the test this month, please come back next month."
                            jump menu_test
                    "Back":
                        play sound "click.mp3"
                        show teacher at left
                        jump menu_school
            else:
                play sound "wrong.mp3" 
                teacher"You have no chance to take the test this month, please come back next month."
                play sound "dialogue.mp3" 
                jump menu_school 
        "Back":
            play sound "click.mp3"
            hide teacher
            scene map
            play music "map.mp3"
            call hidecharacter from _call_hidecharacter_48
            return


screen learnc:
    frame:
        xcenter 0.5
        ycenter 0.5
        xsize 1280
        ysize 720
        viewport:
            xinitial 0.0 
            yinitial 0.0
            scrollbars "vertical" 
            mousewheel True
            draggable True
            pagekeys True
            vbox:
                spacing 10
                text "C++ Introduction" size 60 color "#FFC000" bold True
                vbox:
                    text "C++ is a cross-platform language that can be used to create high-performance applications."
                    text"C++ was developed by Bjarne Stroustrup, as an extension to the C language."
                    text"C++ gives programmers a high level of control over system resources and memory.The language was updated 4 major times in 2011, 2014, 2017, and 2020 to C++11, C++14, C++17, C++20."
                text "C++ Variables" size 60 color "#FFC000" bold True 
                vbox:
                    text "Variables are containers for storing data values."
                    text "In C++, there are different types of variables (defined with different keywords), for example:"
                    text "int - stores integers (whole numbers), without decimals, such as 123 or -123."
                    text "double - stores floating point numbers, with decimals, such as 19.99 or -19.99."
                    text "char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes."
                    text "string - stores text, such as \"Hello World\". String values are surrounded by double quotes."
                    text "bool - stores values with two states: true or false."
                text "C++ Data Types" size 60 color "#FFC000" bold True
                vbox:
                    text "Basic data types can be divided into integer, floating point, character."
                    text "Integers can generally be divided into short integers (short), integers (int), long integers (long long)."
                    text "Floating point type is a decimal number, which can be divided into single precision (float) and double precision (double)."
                    text "Character constants are uniformly coded using ASCII codes, and the range of standard ASCII codes is 0~127, which includes control characters or communication-specific characters and commonly used displayable characters."
                vbox:
                    text "Please search online for more tutorials." color "#FFC000"
                textbutton "Back":  
                    text_size 40 
                    text_color "#99CCFF"
                    activate_sound "audio/click.mp3"
                    action Return('learnc')  
screen learnjava:
    frame:
        xcenter 0.5
        ycenter 0.5
        xsize 1280
        ysize 720
        viewport:
            xinitial 0.0 
            yinitial 0.0
            scrollbars "vertical" 
            mousewheel True
            draggable True
            pagekeys True
            vbox:
                spacing 10
                text "Java Introduction" size 60 color "#FFC000" bold True
                vbox:
                    text "Java is a popular programming language, created in 1995."
                    text "It is owned by Oracle, and more than 3 billion devices run Java."
                    text "It is used for"
                    text "Mobile applications (specially Android apps)、Desktop applications、Web applications"
                    text" Web servers and application servers、Games、Database connection、And much, much more!"
                text "Java Variables" size 60 color "#FFC000" bold True 
                vbox:
                    text "Variables are containers for storing data values."
                    text "In Java, there are different types of variables, for example:"
                    text "String - stores text, such as \"Hello\". String values are surrounded by double quotes."
                    text "int - stores integers (whole numbers), without decimals, such as 123 or -123."
                    text "float - stores floating point numbers, with decimals, such as 19.99 or -19.99."
                    text "char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes."
                    text "boolean - stores values with two states: true or false."
                text "Java Data Types" size 60 color "#FFC000" bold True
                vbox:
                    text "Data types are divided into two groups:"
                    text "Primitive data types - includes byte, short, int, long, float, double, boolean and char."
                    text "Non-primitive data types - such as String, Arrays and Classes (you will learn more about these in a later chapter)."
                vbox:
                    text "Please search online for more tutorials." color "#FFC000"
                textbutton "Back":  
                    text_size 40 
                    text_color "#99CCFF"
                    activate_sound "audio/click.mp3"
                    action Return('learnjava')

