def exercise1():
    print("Exercise 1: Начало")
    num1 = 50
    num2 = 70
    print(num1 + num2)
    print("Exercise 1: Конец")
def exercise2():
    print("Exercise 2: Начало")
    str = "Nfactorial"
    print(str[::-1])
    print("Exercise 2: Конец")
def exercise3():
    print("Exercise 3: Начало")
    my_name = "Zhangeldi"
    print(len(my_name))
    print("Exercise 3: Конец")
def exercise4():
    print("Exercise 4: Начало")
    first_name = "Zhangeldi "
    second_name = "Shakimurat"
    print(first_name + second_name)
    print("Exercise 4: Конец")
def exercise5():
    print("Exercise 5: Начало")
    vowel = "z"
    if vowel == "a" or "e" or "i" or "o" or "u":
        print("It is a vowel")
    else:
        print("It is not a vowel")
    print("Exercise 5: Конец")
def exercise6():
    print("Exercise 6: Начало")
    school = "Nfactorial"
    n = len(school)
    print(school[n-1] + school[1:n] + school[0])
    print("Exercise 6: Конец")
def exercise7():
    print("Exercise 7: Начало")
    str1 = "upper"
    print(str1.upper())
    print("Exercise 7: Конец")
def exercise8():
    print("Exercise 8: Начало")
    Width = 5
    Length = 4
    print(Width * Length)
    print("Exercise 8: Конец")
def exercise9():
    print("Exercise 9: Начало")
    even = 10
    if even % 2 == 0:
        print("Of course", even , "is even!")
    else:
        print("Of course", even ,"is not!")
    print("Exercise 9: Конец")
def exercise10():
    print("Exercise 10: Начало")
    first3 = "Nfactorial"
    n = len(first3)
    print(first3[3:n])
    print("Exercise 10: Конец")
def exercise11():
    print("Exercise 11: Начало")
    name = "Zhangeldi"
    age = 19
    print(f"Hello my name is {name}, and i am {age} old. I hope my homework is well written")
    print("Exercise 11: Конец")
def exercise12():
    print("Exercise 12 Начало")
    anotherstr = "Nfactorial"
    print(anotherstr[2:6])
    print("Exercise 12: Конец")
def exercise13():
    print("Exercise 13: Начало")
    num_or_str = "13"
    print(int(num_or_str))
    print("Exercise 13: Конец")
def exercise14():
    print("Exercise 14: Начало")
    str2 = "Nfactorial "
    str3 = str2 * 3
    print(str3)
    print("Exercise 14: Конец")
def exercise15():
    print("Exercise 15: Начало")
    num1 = 15
    num2 = 7
    print(num1 // num2)
    print(num1 % num2)
    print("Exercise 15: Конец")
def exercise16():
    print("Exercise 16: Начало")
    num1 = 7.5
    num2 = 15
    print(num1 / num2)
    print("Exercise 16: Конец")
def exercise17():
    print("Exercise 17: Начало")
    school = "Nfactorial"
    vowel = "a"
    print(school.count(vowel))
    print("Exercise 17: Конец")
def exercise18():
    print("Exercise 18: Начало")
    str = "It is a string with a \"double\" quotes"
    print(str)
    print("Exercise 18: Конец")
def exercise19():
    print("Exercise 19: Начало")
    multi_line = """
    There
    are
    multi lines"""
    print(multi_line)
    print("Exercise 19: Конец")
def exercise20():
    print("Exercise 20: Начало")
    num1 = 2
    num2 = 32
    print(num1 ** num2)
    print("Exercise 20: Конец")
def exercise21():
    print("Exercise 21: Начало")
    palindrome = "wow"
    if palindrome == palindrome[::-1]:
        print(f"Hell yeah {palindrome} is a palindrome")
    else:
        print(f"Hell no {palindrome} is not")
    print("Exercise 21: Конец")
def exercise22():
    print("Exercise 22: Начало")
    str1 = "rasp"
    str2 = "spar"
    str1.lower()
    str2.lower()
    lst1 = []
    lst2 = []
    for i in str1:
        lst1.append(i)
    for i in str2:
        lst2.append(i)

    if sorted(lst1) == sorted(lst2):
        print(f"{str1} and {str2} are the anagrams!")
    else:
        print(f"{str1} and {str2} not the anagrams!")
    print(sorted(lst1), sorted(lst2))
    print("Exercise 22: Конец")

if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
    exercise11()
    exercise12()
    exercise13()
    exercise14()
    exercise15()
    exercise16()
    exercise17()
    exercise18()
    exercise19()
    exercise20()
    exercise21()
    exercise22()