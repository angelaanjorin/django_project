from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Job, Speciality
from .forms import JobForm
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class JobsList(generic.ListView):
    
    queryset = Job.objects.filter(status=1)
    template_name = "jobs/jobs_list.html"
    paginate_by = 6



def job_detail(request, slug):
    """
    """
    queryset = Job.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "job_detail.html",
        {"jobs": jobs,
         },
    )


class AddJob(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add Job
    """
    model = Job
    form_class = JobForm
    template_name = 'jobas/add_job.html'
    success_message = """Your jobpost was sent successfully <br>
    and is awaiting approval!"""

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditJob(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit Job
    """
    model = Job
    form_class = JobForm
    template_name = 'jobs/add_job.html'
    success_message = 'The jobpost was successfully updated'


def delete_job(request, job_id):
    """
    Delete job
    """
    job = get_object_or_404(Book, id=job_id)
    job.delete()
    messages.success(request, 'The jobpost was deleted successfully')
    return redirect('jobs')


# Speciality list view
class SpecialityListView(ListView):
    """
     Returns all published jobs in :model:`jobs.Speciality`
    and displays them on a page.

    **Context**

    ``post``
        An instance of :model:`jobs.Addjob`.
    ``category``
        Group of published jobs in :model:`jobs.Speciality`
    displayed on a page.
    """
    template_name = 'speciality.html'
    context_object_name = 'speclist'

    def get_queryset(self):
        content = {
            'spec': self.kwargs['speciality'],
            'post': Job.objects.filter(speciality__name=self.kwargs[
                'speciality']).filter(status=1)
        }
        return content


def speciality_list(request):
    speciality_list = Speciality.objects.exclude(name='other')
    context = {
        "speciality_list": speciality_list,
    }
    return context