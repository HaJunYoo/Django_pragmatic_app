from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        # request 받은 input의 name key를 통해 해당 value를 가져온다
        temp = request.POST.get('hello_world_input')
        # model에 저장될 수 있도록 모델 호출 => 하지만 모델을 가져온 것이 아니라 저장될 수 있도록 row를 가져온 것
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return redirect(reverse('accountapp:hello_world'))

    else :
        hello_world_list = HelloWorld.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context = {'hello_world_list' : hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # hello world url로 redirect
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') # hello world url로 redirect
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login') # login url로 redirect
    template_name = 'accountapp/delete.html'