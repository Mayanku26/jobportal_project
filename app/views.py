from django.shortcuts import render, HttpResponse, redirect
import re
import json
from .models import singup, login
from .serializers import signupserializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .forms import SignupForm

# Create your views here.


def Candidate_Signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["psw"]
        repeat_password = request.POST["psw-repeat"]
        data = singup(
            email=email,
            password=password,
            repeat_password=repeat_password,
            first_name=first_name,
            last_name=last_name,
        )

        if (
            re.fullmatch(r"\w+[\w\.-]*@\w+[\w\.-]+\.\w{2,}", email)
            and (password == repeat_password)
            and re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", password)
            and re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", repeat_password)
            and password != ""
            and repeat_password != ""
        ):
            print("success")

            # return HttpResponse("successfully signed up")
            data.save()
            return redirect("login")

    return render(request, "candidate_signup.html")


def Candidate_Login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["psw"]
        user_exist = singup.objects.filter(email=email, password=password)
        if user_exist:
            return redirect("candidate", email)
    return render(request, "candidate_login.html")


def Recruiter_Signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["psw"]
        repeat_password = request.POST["psw-repeat"]
        data = singup(
            email=email,
            password=password,
            repeat_password=repeat_password,
            first_name=first_name,
            last_name=last_name,
        )

        if (
            re.fullmatch(r"\w+[\w\.-]*@\w+[\w\.-]+\.\w{2,}", email)
            and (password == repeat_password)
            and re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", password)
            and re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", repeat_password)
            and password != ""
            and repeat_password != ""
        ):
            print("success")

            # return HttpResponse("successfully signed up")
            data.save()
            return redirect("login")

    return render(request, "recruiter_signup.html")


def Recruiter_Login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["psw"]
        user_exist = singup.objects.filter(email=email, password=password)

        if user_exist:
            return redirect("recruiter", email)
    return render(request, "recruiter_login.html")


def Recruiter(request):
    return render(request, "recruiter.html")


def Candidate(request, email):
    content = singup.objects.filter(email=email)
    return render(request, "candidate.html", {"content": content})


def Candidate_profile(request, email):
    context = singup.objects.filter(email=email)
    return render(request, "candidate_profile.html", {"context": context})


def Recruiter_profile(request, email):
    context_1 = singup.objects.filter(email=email)
    return render(request, "recruiter_profile.html", {"context_1": context_1})


def SignupView(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            first_name = fm.cleaned_data["first_name"]
            print(email, password, first_name)
    else:
        fm = SignupForm()
    return render(request, "signup_form.html", {"form": fm})


@api_view(["GET"])
def signup_list(request):
    if request.method == "GET":
        signup_fields = singup.objects.all()
        serializer = signupserializer(signup_fields, many=True)
        return Response({"status": 200, "students": serializer.data})

@api_view(["POST"])
def signup_post(request):
    data = request.data
    serializer = signupserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"status": 200, "payload": serializer.data, "message": "you sent"}
        )
    else:
        print("error")

