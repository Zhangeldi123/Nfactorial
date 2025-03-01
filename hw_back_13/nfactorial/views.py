from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, nfactorial school!")


def two_numbers_view(request, number1, number2):
    return HttpResponse(f"{number1 + number2}")

def upper_case_view(request, text):
    return HttpResponse(text.upper())

def palindrome(request, text):
    if text == text[::-1]:
        return HttpResponse("True")
    else:
        return HttpResponse("False")


def calculator(request, number1, number2, operation):
    if operation == "add":
        return HttpResponse(f"{number1 + number2}")
    elif operation == "sub":
        return HttpResponse(f"{number1 - number2}")
    elif operation == "mul":
        return HttpResponse(f"{number1 * number2}")
    elif operation == "div":
        if number2 == 0:
            return HttpResponse("Division by zero is not allowed")
        return HttpResponse(f"{number1 / number2}")
    else:
        return HttpResponse("Invalid operation")