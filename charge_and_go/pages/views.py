from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def monthly_bill_view(request):
    context = {
        "curr_year": datetime.datetime.now().year,
    }
    return render(request, "monthly_bill.html", context)


def login_view(request):
    return render(request, "login.html")
