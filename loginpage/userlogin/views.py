from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from userlogin.models import Parameters
import json

# Create your views here.
def index(request):
	response=json.dumps(request)
	return HttpResponse(response, content_type='application/json')


def get_user(request,username):
	if request.method== 'GET':
		try:
			user= Parameters.objects.get(title=username)
			response= json.dumps([{'First_Name':user.title,'Last_Name':user.title3,'phone':user.phone,'Email_Id':user.email}])
		except:
			response= json.dumps({'Error': 'No user with this name'})
	return HttpResponse(response, content_type='application/json')

@csrf_exempt
def add_user(request):
	if request.method== 'POST':

		data=json.loads(request.body)
		#print(data)
		username= data['username']
		last_name= data['last_name']
		phone= data['phone']
		email= data['email']
		user= Parameters(title=username, title3=last_name,phone=phone, email=email)
		try:
			user.save()
			response= json.dumps([{'Success': 'User added successfully'}])
		except:
			response=json.dumps([{'Error': 'User could not be added'}])
		return HttpResponse(response, content_type='application/json')


	if request.mehtod== 'PUT':
		# data=Parameters.objects.all()
		print("data")