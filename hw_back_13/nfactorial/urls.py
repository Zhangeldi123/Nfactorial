from django.urls import path
from .views import hello_view, two_numbers_view, upper_case_view, palindrome, calculator

urlpatterns = [
    path("", hello_view),
    path("<int:number1>/add/<int:number2>/", two_numbers_view),
    path("transform/<str:text>/", upper_case_view),
    path("palindrome/<str:text>/", palindrome),
    path("calc/<int:number1>/<str:operation>/<int:number2>/", calculator),
]
