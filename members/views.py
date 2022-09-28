from audioop import reverse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from members.models import Members
# Create your views here.


def index(request):
    all_members = Members.objects.all().values()

    context = {
        'members': all_members
    }

    template = loader.get_template('first.html')
    return HttpResponse(template.render(context, request))
    


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    firstname = request.POST['first']
    lastname = request.POST['last']
    member = Members(firstname=firstname, lastname=lastname)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def deleteRecord(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))