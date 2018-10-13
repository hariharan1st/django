""" messages view """
#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create(request):
    """ create message for user with given user_id """
    message, user_id = 'test message', 1
    if 'message' in request.GET:
        message = request.GET['message']
    if 'user_id' in request.GET:
        user_id = request.GET['user_id']
    return HttpResponse("method : " + str(request.method) + " message " \
        + str(message) + " saved successfully for " + str(user_id) + " !!! ")
