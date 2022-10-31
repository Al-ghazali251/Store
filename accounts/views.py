from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import user_profile_form, LoginForm
from .models import user_profile, User

class register(APIView):
    def post(self, request):
        if not User.objects.get(email = request.POST['email']).exists():
            if not user_profile.objects.filter(phone = request.POST['phone']).exists():
                if not User.objects.filter(username = request.POST['username']).exists():
                
                    
                    form = user_profile_form(request.POST)
                    if form.is_valid():
                        
                        user = User.objects.create(username = form.cleaned_data['username'], first_name = form.cleaned_data['firstname'], email=form.cleaned_data['email'])

                        user.set_password(form.cleaned_data['password'])
                        user.save()
                        user_extra = user_profile.objects.create(user = user,phone = form.cleaned_data['phone'], gender = form.cleaned_data['gender'], dob = form.cleaned_data['dob'], user_type = form.cleaned_data['user_type'])
                        user_extra.save()
                        return Response({                   
                                            "message": "Account was created successfully.",
                                            # "user": {
                                            #     "id": user.id,
                                            #     "first_name": user.first_name,
                                            #     "last_name": user.last_name,
                                            #     "email": user.email,
                                            #     "phone": user_profile.phone
                                            # },
                                            "status_code": 200
                                        })
                    else:
                        return Response({"message": "Invalid registration details"})
                else:
                    return Response({"message": "username exists"})
            else:
                return Response({
                        "message": "The given data was invalid.",
                        "errors": {
                            "phone": [
                                "The phone number is already in use."
                            ]
                        },
                        "status_code": 422
                    })
        else:
            return Response({
                        "message": "The given data was invalid.",
                        "errors": {
                            "email": [
                                "The email has already been taken."
                            ]
                        },
                        "status_code": 422
                    })
        
        
            
    
    def get(self,request):
        form = user_profile_form()
        
        
class user_login(APIView):
    
    def post(self,request):

        form = LoginForm(request.POST)
        if form.is_valid():
            if User.objects.get(email = form.cleaned_data['email']).exists():
                username = User.objects.get(email = form.cleaned_data['email']).username
            else:
                return Response({"message" : "email does not exist"})
            user = authenticate(request,username=username,password=form.cleaned_data['password'])
            if user is not None:
                    login(request, user)
                    return Response('Authenticated '\
                    'successfully')
                
            else:
                return HttpResponse('Invalid login')
            
    def get(self,request):
        form = LoginForm()
        return Response({"status_code" : 200})
    
    
class user_logout(APIView):
    def get(self,request):
        logout(request)
        # messages.info(request, "You have successfully logged out.") 
        return Response({"message":"Logged out successfully"})

   
