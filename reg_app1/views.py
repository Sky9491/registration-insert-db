from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password



from .models import Registration

# Create your views here.

def register(request):
   if request.method=='POST':
      first_name=request.POST.get('firstname')
      last_name=request.POST.get('lastname')
      username=request.POST.get('username')
      email=request.POST.get('email')
      phone_number=request.POST.get('phone-number')
      password=request.POST.get('password')
      confirm_password=request.POST.get('confirm-password')

      errors=[]
      if password!=confirm_password:
         errors.append("Password does not match")
      if Registration.objects.filter(username=username).exists():
         errors.append('Username already exists.')
      if Registration.objects.filter(email=email).exists():
         errors.append('already exists.')
      if errors:
         return render(request,'reg-app1/registration.html',{'errors':errors})
      hashed_password =make_password(password)
      profile=Registration.objects.create(
         first_name=first_name,
         last_name=last_name,
         username=username,
         email=email,
         phone=phone_number,
         password=hashed_password
         )
      profile.save()
      return HttpResponse('Register successfully.')



   return render(request,'reg-app1/registration.html')