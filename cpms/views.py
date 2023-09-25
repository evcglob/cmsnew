# ws
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# app

from django.db.models import Sum
from time import time
from django.core.mail import send_mail
from tokenize import generate_tokens
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from cpms.models import *
from django.contrib.auth.decorators import login_required
from google.auth.transport import requests
from django.conf import settings
import razorpay
from django.http import HttpResponse
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
import json
import requests
import random
from django.utils import timezone
from django.db import IntegrityError
import http.client
from datetime import datetime
import datetime
import pytz


# Create your views here.

def login(request):  
    if request.method == 'POST':
        #input field
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print (username , pass1)
        if username == "admin" and pass1 == "admin":
            return render (request , 'dashboard.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def station(request):
    return render(request, 'station.html')


def newstation(request):
    return render(request, 'newstation.html')


def editstation(request):
    return render(request, 'editstation.html')


def rfid(request):
    return render(request, 'rfid.html')


def role(request):
    return render(request, 'role.html')


def user(request):
    return render(request, 'user.html')


def report(request):
    return render(request, 'report.html')






# # Create your views here.
# #connection


# def station(request):
#     try:
#         if request.method == 'POST':
#             station_name = request.POST['station_name']
#             address = request.POST['address']
#             city = request.POST['city']
#             state = request.POST['state']
#             zip_code = request.POST['zip']
#             station_type = request.POST['Public']
#             open_24_7 = request.POST['Yes']
#             phone = request.POST['phone']
#             print(station_name,address,city,state,zip_code,station_type,open_24_7,phone)

#             charging_station = ChargingStations(
#                 Charging_Station_Name=station_name,
#                 Address=address,
#                 City=city,
#                 State=state,
#                 Zip_Code=zip_code,
#                 station_type=station_type,
#                 open=open_24_7,
#                 Phone_Number=phone
#             )
#             charging_station.save()

#             return render(request, 'station.html')
#     except Exception as e:
#         print(str(e))
#     charging_stations = ChargingStations.objects.all()
#     return render(request, 'station.html', {'charging_stations': charging_stations})


# def logs(request):
#     callm_objects = Callm.objects.order_by('-id')[:500]
#     return render(request, 'logs.html', {'callm_objects': callm_objects})


# def logindash(request):
#     if request.method == 'POST':
#         #input field
#         username = request.POST.get('username')
#         pass1 = request.POST.get('pass')
#         print (username , pass1)
#         if username == "admin" and pass1 == "admin":
#             return render (request , 'dashboard.html')
#         else:
#             return render(request , 'logindash.html')
 
#     return render(request, 'logindash.html')
 
 
 
# def dashboard(request):
#     # Perform the query to get the total counts
#     result = ChargingStations.objects.aggregate(
#         total_charging_points=Sum('Socket_URL'),
#         total_connectors=Sum('Connectors')
#     )
#     # Access the total counts from the result
#     total_charging_points = result['total_charging_points']
#     total_connectors = result['total_connectors']
 
#     # Pass the counts to the template context
#     charging_stations = ChargingStations.objects.all()
#     for charging_station in charging_stations:
#         number_point = charging_station.Charging_Point_Name
  

#     context = {
#         'charging_station_count': ChargingStations.objects.count(),
#         'total_charging_points': total_charging_points,
#         'total_connectors': total_connectors,
#         # 'number_point':number_point,
#     }
 
#     return render(request, 'dashboard.html', context)

 
# def newstation(request):
#     reviews = Review.objects.all().order_by('-id')
#     count = Review.objects.count()


#     callm_objects = Callm.objects.order_by('-id')[:500]
#     if request.method == 'POST':
        
#         #general
#         Charging_Station_Name = request.POST.get('station_name')
#         Address = request.POST.get('address')
#         City = request.POST.get('city')
#         Zip = request.POST.get('zip')
#         State = request.POST.get('state')
#         Country = request.POST.get('country')
#         Station_type = request.POST.getlist('staiontypre')
#         openhr = request.POST.getlist('openn')
#         Phone = request.POST.get('phone')

#         #charging points
#         Socket_URL = request.POST.get('socket_url')
#         Charging_Point_Name = request.POST.get('point_name')
#         Charging_Point_ID = request.POST.get('point_id')
#         Connector_Type = request.POST.get('connector_type')
#         Charging_Power = request.POST.get('charging_power')
#         EV_Compatible = request.POST.get('vehicle_type')
#         Cost_per_Unit = request.POST.get('price')
#         LICENSE = request.POST.get('license')
#         Change_Availability = request.POST.get('change_availability')
        

#         #amenity
#         food_drink = request.POST.getlist('food_drink')
#         Things_to_Do = request.POST.getlist('Things_to_Do')
#         Shopping = request.POST.getlist('Shopping')
#         Services = request.POST.getlist('Services')

#         #saving in databse
#         charging_station = ChargingStations(
#             #general
#             Charging_Station_Name=Charging_Station_Name,
#             Address=Address,
#             City=City,
#             Zip_Code=Zip,
#             State=State,
#             Country=Country,
#             station_type=Station_type,
#             open=openhr,
#             Phone_Number=Phone,

#             #charging point
#             Socket_URL=Socket_URL,
#             Charging_Point_Name=Charging_Point_Name,
#             Charging_Point_ID=Charging_Point_ID,
#             Connector_Type=Connector_Type,
#             Charging_Power=Charging_Power,
#             EV_Compatible=EV_Compatible,
#             Cost_per_Unit=Cost_per_Unit,
#             LICENSE=LICENSE,
#             Change_Availability=Change_Availability,

#             #amenities

#             Food_Drink=food_drink,
#             Things_to_Do=Things_to_Do,
#             Shopping=Shopping,
#             Services=Services,
#             )
#         charging_station.save()
        
#         print(Charging_Station_Name,Services)

#     return render(request, 'newstation.html',{'reviews':reviews, 'count':count, 'callm_objects': callm_objects})
 
# def rfid(request):
#     return render(request, 'rfid.html')
 
# def role(request):
#     return render(request, 'role.html')
 
# def user(request):
#     return render(request, 'user.html')


# # def show(request, id):
# #     mem  =  ChargingStations.objects.get(id=id)
# #     mem.show()
# #     return redirect('station')

# def show(request):

#     return render(request, 'show.html')


# def delete(request, id):
#     mem  =  ChargingStations.objects.get(id=id)
#     mem.delete()
#     return redirect('station')


# def edit(request, id):
#     mem  =  ChargingStations.objects.get(id=id)
#     callm_objects = Callm.objects.order_by('-id')[:500]
#     reviews = Review.objects.all().order_by('-id')
#     print(mem.City)
#     return render(request, 'edit.html', {'mem': mem, 'callm_objects': callm_objects, 'reviews':reviews})

# def update(request, id):
        
#     #general
#     Charging_Station_Name = request.POST.get('station_name')
#     Address = request.POST.get('address')
#     City = request.POST.get('city')
#     Zip = request.POST.get('zip')
#     State = request.POST.get('state')
#     Country = request.POST.get('country')
#     Station_type = request.POST.getlist('staiontypre')
#     openhr = request.POST.getlist('openn')
#     Phone = request.POST.get('phone')

#     #charging points
#     Socket_URL = request.POST.get('socket_url')
#     Charging_Point_Name = request.POST.get('point_name')
#     Charging_Point_ID = request.POST.get('point_id')
#     Connector_Type = request.POST.get('connector_type')
#     Charging_Power = request.POST.get('charging_power')
#     EV_Compatible = request.POST.get('vehicle_type')
#     Cost_per_Unit = request.POST.get('price')
#     LICENSE = request.POST.get('license')
#     Change_Availability = request.POST.get('change_availability')

#     #amenity
#     food_drink = request.POST.getlist('food_drink')
#     Things_to_Do = request.POST.getlist('Things_to_Do')
#     Shopping = request.POST.getlist('Shopping')
#     Services = request.POST.getlist('Services')



#     member = ChargingStations.objects.get(id=id)
#     #general
#     member.Charging_Station_Name = Charging_Station_Name
#     member.Address = Address
#     member.City = City
#     member.Zip_Code = Zip
#     member.State = State
#     member.Country = Country
#     member.station_type = Station_type
#     member.open = openhr
#     member.Phone_Number = Phone
#     #charging point
#     member.Socket_URL = Socket_URL
#     member.Charging_Point_Name = Charging_Point_Name
#     member.Charging_Point_ID = Charging_Point_ID
#     member.Connector_Type = Connector_Type
#     member.Charging_Power = Charging_Power
#     member.EV_Compatible = EV_Compatible
#     member.Cost_per_Unit = Cost_per_Unit
#     member.LICENSE = LICENSE
#     member.Change_Availability = Change_Availability
#     #amenities
#     member.Food_Drink = food_drink
#     member.Things_to_Do = Things_to_Do
#     member.Shopping = Shopping
#     member.Services = Services
#     member.save()
#     return redirect('station')







