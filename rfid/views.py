from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core import serializers
import datetime
from datetime import datetime

def index(request):
    name = "Jung"
    the_time = datetime.now()
    return render_to_response('index.html' , locals() )

