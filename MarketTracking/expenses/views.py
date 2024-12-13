from django.shortcuts import render, redirect
from django.http.response import HttpResponse

def show_expenses(request):
    return render(request, "expenses/goruntule.html")