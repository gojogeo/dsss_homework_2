import random


def Rand_Int(min, max):
    """
    Returns a random number between min and max.

    :param min: The minimum value to return
    :type min: int
    :param max: The maximum value to return
    :type max: int
    :return: A random integer between min and max
    :rtype: int
    
    """
    return random.randint(min, max)


def Math_Operator():
    """
    Returns a random mathematical opertation 
    :return: A random mathematical opertation between '+','-', and '*'
    :rtype: string

    """
    return random.choice(['+', '-', '*'])


def Math_Operation(n1, n2, o):
    """
    Returns a mathematical expression and its result

    :param n1: The first number
    :type n1: int
    :param n2: The second number
    :type n2: int
    :param o: The operator
    :type o: string
    :return p: string of mathematical expression
    :type p: string
    :return a: result of the evaluated mathematical expression
    :type a: int

    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    Math quiz, where user is presented with a mathematical expression t_q times. User is prompted to 
    input the result. The result is compared with the correct answer and points are added to the score.
    In the end of the quiz user is presented with the final score
    """
    s = 0
    t_q = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = Rand_Int(1, 10); n2 = Rand_Int(1, 20); o = Math_Operator()

        PROBLEM, ANSWER = Math_Operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except:
            print ("Invalid Entry. Enter an integer number")
            pass

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
