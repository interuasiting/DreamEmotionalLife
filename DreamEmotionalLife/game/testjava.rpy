label testjava:
    $number= [1,2,3]
    $javapaper = renpy.random.choice(number)
    $right = 0
    teacher"Start the test now ————"
    hide teacher
    if javapaper == 1:
        menu:
            "1.The following are java basic types:"
            "A.String":
                play sound "click.mp3"
                $right += 0
            "B.Array":
                play sound "click.mp3"
                $right += 0
            "C.Byte":
                play sound "click.mp3"
                $right += 1
        menu:
            "2.Which of the following identifier is legal:"
            "A.new":
                play sound "click.mp3"
                $right += 0
            "B.$ Us dollars":
                play sound "click.mp3"
                $right += 1
            "C.1234":
                play sound "click.mp3"
                $right += 0
        menu:
            "3.Which of the following is true about the result of executing the program?"
            "A.The number 2 is printed and a run-time exeception terminates execution.":
                play sound "click.mp3"
                $right += 1
            "B.The number 2 is printed and there is no abnormal termination.":
                play sound "click.mp3"
                $right += 0
            "C.The number 1 is printed and there is no abnormal termination.":
                play sound "click.mp3"
                $right += 0
        menu:
            "4. A Java array that contains n components will be indexed from through:"
            "A.0, n-1":
                play sound "click.mp3"
                $right += 1
            "B.1, n":
                play sound "click.mp3"
                $right += 0
            "C.0, n":
                play sound "click.mp3"
                $right += 0
        menu:
            "5.An object that contains methods that traverse an vector linearly from start to finish is known as a(n):"
            "A.Loop":
                play sound "click.mp3"
                $right += 0
            "B.Iterator":
                play sound "click.mp3"
                $right += 1
            "C.Int":
                play sound "click.mp3"
                $right += 0
    elif javapaper == 2:
        menu:
            "1.The class java.util.ArrayList implements a collection that"
            "A.cannot be accessed using an integer index":
                play sound "click.mp3"
                $right += 0
            "B.can only store instances of the class java.lang.String":
                play sound "click.mp3"
                $right += 0
            "C.can grow to accommodate new items":
                play sound "click.mp3"
                $right += 1
        menu:
            "2.Array elements may only be retrieved using___, whereas vector elements may also be retrieved using:"
            "A.indexes, iterators":
                play sound "click.mp3"
                $right += 1
            "B.iterators, indexs":
                play sound "click.mp3"
                $right += 0
            "C.indexes, names":
                play sound "click.mp3"
                $right += 0
        menu:
            "3.1. Consider the following statement which is defined in a class( let's call it class Test). The keyword static : private static int serial = 0;"
            "A.means that serial is a constant.":
                play sound "click.mp3"
                $right += 0
            "B.ensures that only one instance of serial exists and it will be shared by all objects of type Test.":
                play sound "click.mp3"
                $right += 1
            "C.means that serial should be capitalized( e.g. SERIAL )to comply with Java naming conventions.":
                play sound "click.mp3"
                $right += 0
        menu:
            "4.Which of the following statements about constructors in java is true?"
            "A.A class must define at least one constructor.":
                play sound "click.mp3"
                $right += 0
            "B.A class can define more than one constructor.":
                play sound "click.mp3"
                $right += 1
            "C.A constructor must be defined as public.":
                play sound "click.mp3"
                $right += 0
        menu:
            "5.Which of the following catagorizations can be applied to both the data fields and the methods in a java class?"
            "A.native and non-native.":
                play sound "click.mp3"
                $right += 0
            "B.default and non-default.":
                play sound "click.mp3"
                $right += 0
            "C.static and non-static":
                play sound "click.mp3"
                $right += 1
    elif javapaper == 3:
        menu:
            "1.What is used to indicate that a method doesn't return a value?"
            "A.The keyword void":
                play sound "click.mp3"
                $right += 1
            "B.The name of the class to which it belongs":
                play sound "click.mp3"
                $right += 0
            "C.The omission of the return type":
                play sound "click.mp3"
                $right += 0
        menu:
            "2.When a subclass defines an instance method with the same return type and signature as a method in its parent, the parent's method is said to be:"
            "A.hidden":
                play sound "click.mp3"
                $right += 0
            "B.private":
                play sound "click.mp3"
                $right += 0
            "C.overloaded":
                play sound "click.mp3"
                $right += 1
        menu:
            "3.If a class contains a constructor, that constructor will be invoked:"
            "A.each time an object of that class is instantiated.":
                play sound "click.mp3"
                $right += 1
            "B.once the first time an object of that class is instantiated.":
                play sound "click.mp3"
                $right += 0
            "C.each time an object of that class goes out of scope.":
                play sound "click.mp3"
                $right += 0
        menu:
            "4.Which is a java access modifier used to designate that a particular data field will not be inherited by a subclass?"
            "A.final":
                play sound "click.mp3"
                $right += 0
            "B.default":
                play sound "click.mp3"
                $right += 0
            "C.private":
                play sound "click.mp3"
                $right += 1
        menu:
            "5.If the method int sum(int a, int b) is defined in a java class C, which of the following methods cannot coexist as a different method in class C?"
            "A.int sum(float a, int b)":
                play sound "click.mp3"
                $right += 0
            "B.int sum(int x, int y)":
                play sound "click.mp3"
                $right += 1
            "C.float sum(int x, float y)":
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
