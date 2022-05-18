from django.shortcuts import render
from django.db import connection
from bank.models import Subbank, Client, Contact
from django.http import JsonResponse
import json
from testapp.serializer import SubbankSerializer
from django.http import HttpResponse

def ClientSignin(request):
    responce_dict = {'found': False, 'pwd_right': False}

    info_dict = json.loads(request.body)
    client_set = Client.objects.filter(clientid=info_dict['user'])
    
    # user doesn't exist
    if(client_set.count() == 0):
        return JsonResponse(responce_dict)
    
    responce_dict['found'] = True
    clien_obj = Client.objects.get(clientid=info_dict['user'])

    # password wrong
    if(clien_obj.password != info_dict['password']):
        return JsonResponse(responce_dict)
    
    # signin success
    responce_dict['pwd_right'] = True
    return JsonResponse(responce_dict)


def ClientSignup(request):
    info_dict = json.loads(request.body)

    cl = Client(clientid=info_dict['idnum'], contactname=info_dict['contact'], clientname=info_dict['name'], 
                clienttel=info_dict['tel'], clientaddr=info_dict['addr'], password=info_dict['pswd1'])
    cl.save()

    clien_obj = Client.objects.get(clientid=info_dict['idnum'])
    ct = Contact(clientid=clien_obj, contactname=info_dict['contact'], contacttel=info_dict['contact_tel'], 
                email=info_dict['contact_email'], relationship=info_dict['relation'])
    ct.save()
    
    return JsonResponse('', safe=False)