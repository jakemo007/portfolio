from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from  django.core.mail import send_mail
import json



from .forms import SendEmail




# Create your views here.

def home(request):
    sendEmailForm = SendEmail()
    return render(request,'index.html',{'form':sendEmailForm})


@api_view(["POST"])
def sendEmail(request):
    try:
        if request.method == "POST":
            data = parseTheData(request.data)
            send_mail(
                subject="Automatic Reply From Jajati PortFolio", 
                message = formatMessage(data), 
                from_email = None, 
                recipient_list = data["email"])            
        return JsonResponse({"status" : 200})
    except Exception as e:
        return JsonResponse({"status": 404, "error" : e , "message" : "Please contact via Whatsapp"})

def parseTheData(data):
    for key in data:
        return json.loads(key)

def formatMessage(data):
    return f"""
        Hi {data["name"]},

        Your Message "{data["message"]}"
        has reached to Jajati, with below contact details:
        Phone No. {data["phone"]}

        Thank You For Your Email
    """