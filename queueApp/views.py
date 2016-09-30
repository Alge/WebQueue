from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, MakeQueue, AddQueuePlaceForm, DeleteQueueForm, RemoveFromQueueForm
from .models import Queue, QueuePlace
# Create your views here.

def index(request):


    if request.method == 'POST' and request.user.is_authenticated:
        form = MakeQueue(request.POST)
        if form.is_valid():
            q = Queue()
            q.name = form.cleaned_data['name']
            q.save()
            q.admins.add(request.user)
            q.save()



    context = {
        'queues'    :       Queue.objects.order_by('-timestamp'),
        'form'      :       MakeQueue()
    }

    return render(request, 'queueApp/index.html', context)

def viewQueue(request, queue_id):


    if(request.method== 'POST'):

        if("deleteQueue" in request.POST.keys()) and request.user.is_authenticated:

            form = DeleteQueueForm(request.POST)
            if form.is_valid():
                q = Queue.objects.filter(pk=form.cleaned_data['queue_id'])
                q.delete()
                redirect("/")

        elif "addToQueue" in request.POST.keys():
            form = AddQueuePlaceForm(request.POST)
            if form.is_valid():
                queue = form.cleaned_data['queue_id']
                qp = QueuePlace()
                qp.queue = queue
                qp.name = form.cleaned_data['name']
                qp.place = form.cleaned_data['place']
                pq.save()

        elif "placement_id" in request.POST.keys() and request.user.is_authenticated:
            form = RemoveFromQueueForm(request.POST)
            if form.is_valid():
                qp = QueuePlace.objects.filter(pk=form.cleaned_data['placement_id']).first()
                qp.delete()



    queue = Queue.objects.filter(pk=int(queue_id)).first()
    placementList = QueuePlace.objects.filter(queue=queue).order_by('timestamp')


    context = {
        'queue'             :   queue,
        'queuePlacements'   :   placementList,
        'addToQueueForm'    :   AddQueuePlaceForm(),
        'deleteQueueForm'   :   DeleteQueueForm(),
        'removeFromQueueForm':  RemoveFromQueueForm(),

    }

    return render(request, 'queueApp/viewQueue.html', context)

def login(request):
    state = ""
    if request.user.is_authenticated():
        return redirect("/")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    state = "You're successfully logged in!"
                    return redirect("/")
                else:
                    state = "Your account is not active. Please contact the admin"
            else:
                state = "Your username and/or password were incorrect"

    else:
        form = LoginForm()

    context = {'form': form, 'state': state}

    return render(request, 'queueApp/login.html', context)