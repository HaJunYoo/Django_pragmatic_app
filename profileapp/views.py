from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from django.urls import reverse_lazy, reverse

from profileapp.decorators import profile_ownership_required
from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # form 임시 데이터 저장
        temp_profile = form.save(commit = False)
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})



@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})