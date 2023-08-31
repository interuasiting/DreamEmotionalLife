label testc:
    $number= [1,2,3]
    $paper = renpy.random.choice(number)
    $right = 0
    teacher"Start the test now ————"
    hide teacher
    if paper == 1:
        menu:
            "1.In C++, the inheritance relationship between classes has:"
            "A.Reflexivity":
                play sound "click.mp3"
                $right += 0
            "B.Symmetry":
                play sound "click.mp3"
                $right += 0
            "C.Transitivity":
                play sound "click.mp3"
                $right += 1
        menu:
            "2.Which of the following descriptions about the relationship between classes is correct:"
            "A.The is-a mechanism is called \"inheritance\"":
                play sound "click.mp3"
                $right += 1
            "B.The is-a relationship is symmetric.":
                play sound "click.mp3"
                $right += 0
            "C.Has-a indicates that a class partially uses another class.":
                play sound "click.mp3"
                $right += 0
        menu:
            "3.Which of the following descriptions about classes is correct:"
            "A.A parent class has the characteristics of a subclass":
                play sound "click.mp3"
                $right += 0
            "B.A class can only inherit from one class.":
                play sound "click.mp3"
                $right += 0
            "C.The is-a relationship is transitive.":
                play sound "click.mp3"
                $right += 1
        menu:
            "4.Which of the following descriptions about the relationship between classes is wrong:"
            "A.Each node in the DAG is a class definition, which has and only one predecessor node.":
                play sound "click.mp3"
                $right += 1
            "B.Each node in the DAG is a class definition, and its predecessor node is called the base class.":
                play sound "click.mp3"
                $right += 0
            "C.Each node in the DAG is a class definition, and its successor nodes are called derived classes.":
                play sound "click.mp3"
                $right += 0
        menu:
            "5.In the following description about class inheritance, the correct one is:"
            "A.When the derived class inherits the base class publicly, it can access all data members of the base class and call all member functions.":
                play sound "click.mp3"
                $right += 0
            "B.The derived class is also the base class, so they are equivalent.":
                play sound "click.mp3"
                $right += 0
            "C.A base class can have multiple derived classes, and a derived class can have multiple base classes.":
                play sound "click.mp3"
                $right += 1
    elif paper == 2:
        menu:
            "1.When a derived class inherits a base class publicly, all public members in the base class become ( ) of the derived class."
            "A.Private member":
                play sound "click.mp3"
                $right += 0
            "B.Protected member":
                play sound "click.mp3"
                $right += 0
            "C.Public member":
                play sound "click.mp3"
                $right += 1
        menu:
            "2.When a derived class inherits a base class privately, all public and protected members in the base class become ( ) of the derived class."
            "A.Private member":
                play sound "click.mp3"
                $right += 1
            "B.Protected member":
                play sound "click.mp3"
                $right += 0
            "C.Public member":
                play sound "click.mp3"
                $right += 0
        menu:
            "3.When a derived class protects a base class, all public and protected members in the base class become ( ) of the derived class."
            "A.Private member":
                play sound "click.mp3"
                $right += 0
            "B.Protected member":
                play sound "click.mp3"
                $right += 1
            "C.Public member":
                play sound "click.mp3"
                $right += 0
        menu:
            "4.No matter how the derived class inherits the base class, the ( ) of the base class cannot be used directly."
            "A.Private member":
                play sound "click.mp3"
                $right += 1
            "B.Protected member":
                play sound "click.mp3"
                $right += 0
            "C.Public member":
                play sound "click.mp3"
                $right += 0
        menu:
            "5.In C++, without explanation, the default inheritance method is ()."
            "A.Private":
                play sound "click.mp3"
                $right += 1
            "B.Protected":
                play sound "click.mp3"
                $right += 0
            "C.Public":
                play sound "click.mp3"
                $right += 0
    elif paper == 3:
        menu:
            "1.If a member function of a public derived class cannot directly access a member inherited from the base class, the member must be ( ) in the base class."
            "A.Private member":
                play sound "click.mp3"
                $right += 1
            "B.Protected member":
                play sound "click.mp3"
                $right += 0
            "C.Public member":
                play sound "click.mp3"
                $right += 0
        menu:
            "2.The following description about the member with the same name in the class hierarchy is wrong:"
            "A.C++ allows derived class members to have the same name as base class members.":
                play sound "click.mp3"
                $right += 0
            "B.When accessing a member with the same name in a derived class, shield the member with the same name of the base class.":
                play sound "click.mp3"
                $right += 0
            "C.A member of the base class with the same name cannot be accessed in a derived class.":
                play sound "click.mp3"
                $right += 1
        menu:
            "3.Which of the following descriptions about static members in the class hierarchy is correct:"
            "A.A static member defined in a base class that can only be accessed by objects of the base class.":
                play sound "click.mp3"
                $right += 0
            "B.Static members defined in the base class, shared throughout the class system.":
                play sound "click.mp3"
                $right += 1
            "C.Static members defined in the base class have the same access properties in the class hierarchy regardless of how the derived class inherits.":
                play sound "click.mp3"
                $right += 0
        menu:
            "4.A large application usually consists of multiple classes, and the classes work together with each other. There are three main relationships between them. Which of the following is not a relationship between classes is:"
            "A.Gets-a":
                play sound "click.mp3"
                $right += 1
            "B.Has-a":
                play sound "click.mp3"
                $right += 0
            "C.Uses-a":
                play sound "click.mp3"
                $right += 0
        menu:
            "5.In C++, the functions that can be inherited by derived classes are:"
            "A.Member function":
                play sound "click.mp3"
                $right += 1
            "B.Constructor":
                play sound "click.mp3"
                $right += 0
            "C.Destructor":
                play sound "click.mp3"
                $right += 0
    play sound "finishtest.mp3"
    show teacher at left with dissolve
    teacher "You answered a total of {color=#FF0000}[right]{/size} questions correctly."
    play sound "dialogue.mp3"
    if right > 0:
        $getmoney = right*20
        $getknowledge = right*5
        play sound "getpoints.mp3"
        teacher"Congratulations! You got {color=#FFC000}money + [getmoney]{/size} and {color=#FFC000}knowledge + [getknowledge]{/size}! Keep going next time!"
        $money += getmoney
        $knowledge += getknowledge
        play sound "dialogue.mp3"
    else:
        teacher"You didn't answer any of the questions correctly, you still need to keep working hard!"
        play sound "dialogue.mp3"
    $test_times -= 1
    teacher"You only left {color=#FF0000}[test_times]{/color} chance to join test."
    play sound "dialogue.mp3"
    return 
