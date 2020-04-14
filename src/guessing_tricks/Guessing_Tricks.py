"""
 *   Created by PyCharm Professional, 2020
 *   User: nmn-gupta
 *   Date: 14/04/20
 *   Time: 09:30 PM

"""
print("Press 1. if you want me to guess your birth date")
print("Press 2. if you want me to guess your age")
choice = int(input("Enter the choice:"))

arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
arr2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
arr3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
arr4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
arr5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]


def guess_Birth_date(arr1, arr2, arr3, arr4, arr5):
    s = 0

    print(arr1)
    re = input("Now, tell me that the date which is to be guessed is present in this list (yes/no): ")
    if re == "yes":
        s += 1
    else:
        pass

    print(arr2)
    re2 = input("Now, tell me that the date which is to be guessed is present in this list (yes/no): ")
    if re2 == "yes":
        s += 2
    else:
        pass

    print(arr3)
    re3 = input("Now, tell me that the date which is to be guessed is present in this list (yes/no): ")
    if re3 == "yes":
        s += 4
    else:
        pass

    print(arr4)
    re4 = input("Now, tell me that the date which is to be guessed is present in this list (yes/no): ")
    if re4 == "yes":
        s += 8
    else:
        pass

    print(arr5)
    re5 = input("Now, tell me that the date which is to be guessed is present in this list (yes/no): ")
    if re5 == "yes":
        s += 16
    else:
        pass
    print()
    print("Okay, so your birth date is :", s)


def guess_Age():
    print("Tell me the reminders of dividing your age by 3, 5, 7:")
    rem1=int(input())
    rem2 = int(input())
    rem3 = int(input())
    res=(rem1*70+rem2*21+rem3*15)%105
    print("Okay, so your age is :", res)


if choice == 1:
    guess_Birth_date(arr1, arr2, arr3, arr4, arr5)
'''else:
    guess_Age()


'''
