from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Section, Locum
#from .forms import CommentForm

# Create your views here.


class locum_detail(View):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`post_detail.html`
    """
    def get (self, request, slug, *args, **kwargs):
        queryset = Locum.objects.filter(status=1)
        locum = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "locum_detail.html",
            {
                "locum": locum,
                "liked": liked,
            },
        )


class LocumLike(View):
    """
    Toggles like status on submission of like form/button on posts.
    Also sends notification to author
    Login required
    """
    def post(self, request, slug, *args, **kwargs):
        locum = get_object_or_404(Post, slug=slug)
        if locum.likes.filter(id=request.user.id).exists():
            locum.likes.remove(request.user)
        else:
            locum.likes.add(request.user)

        return HttpResponseRedirect(reverse('locum_detail', args=[slug]))


# Category list view
class SecListView(ListView):
    """
     Returns all published posts in :model:`blog.Category`
    and displays them on a page.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``category``
        Group of published posts in :model:`blog.Category`
    displayed on a page.
    """
    template_name = 'locum/section.html'
    context_object_name = 'seclist'

    def get_queryset(self):
        content = {
            'sec': self.kwargs['section'],
            'locum': Locum.objects.filter(section__name=self.kwargs[
                'section']).filter(status=1)
        }
        return content


def section_list(request):
    section_list = Section.objects.exclude(name='other')
    context = {
        "section_list": section_list,
    }
    return context
