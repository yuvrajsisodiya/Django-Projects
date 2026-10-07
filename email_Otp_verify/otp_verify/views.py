from django.shortcuts import render
import random
from django.shortcuts import render , redirect
from django.core.mail import send_mail
# Create your views here.

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = random.randint(100000,999999)
        request.session["otp"] = str(otp)
        request.session["email"] = email
        send_mail(
            subject = "OTP Verification",
            message = f"Hello Sir, your OTP is {otp}. Please use this OTP to verify your email .  {email} \nPlease do not share this OTP with anyone.",
            from_email = "yuvrajsisodiyas19@gmail.com",
            recipient_list = [email],
        )
        return redirect("verify_otp")
    return render(request , 'send_otp.html')

def verify_otp(request):

    if request.method == "POST":
        user_otp = request.POST.get("otp")
        saved_otp = request.session.get("otp")

        if user_otp == saved_otp:
            return render(request, "success.html")

        return render(request, "verify_otp.html", {
            "error": "Invalid OTP"
        })

    return render(request, "verify_otp.html")