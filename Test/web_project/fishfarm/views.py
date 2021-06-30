from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    p =products.objects.all()
    sp=sproducts.objects.all()
    return render(request, 'index.html',{'product':p, 'sproduct':sp,})

def contact(request):
    if request.method == "POST":  
        Name= request.POST['NAME']
        Email= request.POST['EMAIL']
        Subject = request.POST['SUBJECT']
        Message = request.POST['MESSAGE']
        ins=contact(names=Name,email=Email,subject=Subject,message=Message)
        ins.save()
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def band_listing(request):
    logins = models.login.objects.all()
    return render(request, 'login/login.html', {'logins': logins})
def myaccount(request):
    return render(request, 'myAccount.html')
def pricing(request):
    return render(request, 'pricing.html')
def about(request):
    return render(request, 'about.html')
def team(request):
    return render(request, 'team-member.html')
def ourteam(request):
    return render(request, 'our-team.html')
def services(request):
    return render(request, 'services.html')
def maintenance(request):
    return render(request, 'maintenance.html')
def button(request):
    return render(request, 'features-buttons.html')
def form(request):
    return render(request, 'features-forms.html')
def table(request):
    return render(request, 'features-tables.html')
def accountbilling(request):
    return render(request, 'myAccount-billing-address.html')
def error(request):
    return render(request, '404.html')

