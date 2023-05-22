from django.urls import path, include
from .views import *

urlpatterns = [
    path("candidate/signup", Candidate_Signup, name="signup"),
    path("candidate/login", Candidate_Login, name="login"),
    path("recruiter/signup", Recruiter_Signup, name="r_signup"),
    path("recruiter/login", Recruiter_Login, name="r_login"),
    path("candidate/<str:email>", Candidate, name="candidate"),
    path("recruiter", Recruiter, name="recruiter"),
    path("signup_list", signup_list, name="signup_list"),
    path("signup_list/<int:id>", signup_list, name="xyz"),
    path("candidate_profile/<str:email>", Candidate_profile, name="candidate_profile"),
    path("signup_form", SignupView),
    path("signup_post/", signup_post),
]
