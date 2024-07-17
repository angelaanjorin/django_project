from django.views import generic, View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Jobs, Profile
from .forms import JobsForm, UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class JobsList(generic.ListView):
    """
    Returns all published jobs and displays them in a page of 15 posts.
    """
    queryset = Jobs.objects.filter(status=1)
    template_name = "jobslist.html"
    paginate_by = 15

class JobDetail(View):
    """
    Renders the job detail page
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Jobs.objects.filter(status=1)
        job = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "job_detail.html",
            {
                "job": job,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handle post request for job detail
        """
        queryset = Jobs.objects.filter(status=1)
        job = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "job_detail.html",
            {
                "job": job,
            },
        )

@login_required
def profile_view(request):
    """
    Renders the profile page
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile.html')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)

@login_required
def delete_job(request, job_id):
    """
    Delete job
    """
    job = get_object_or_404(Jobs, id=job_id)
    job.delete()
    messages.success(request, 'The job was deleted successfully')
    return HttpResponseRedirect(reverse('jobslist.html'))

class EditJob(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit job
    """
    model = Jobs
    template_name = 'edit_job.html'
    form_class = JobsForm
    success_message = 'The job was successfully updated'
