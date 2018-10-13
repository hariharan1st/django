""" views for blat """
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Blat

# Create your views here.
def home(request):
    """ dummy home page """
    return render(request, 'blat/home.html', {'message' : 'Hello World'})

class IndexView(generic.ListView):# pylint: disable=too-many-ancestors
    """ IndexView for blats """
    template_name = 'blat/home.html'
    context_object = 'blat_list'

    def get_queryset(self):
        """ get query set for generic view """
        return Blat.objects.select_related('created_by')\
                .prefetch_related('like_set').order_by('-created_on')[:20]

class MyView(IndexView):# pylint: disable=too-many-ancestors
    """ MyView for blats """
    template_name = 'blat/home.html'
    context_object = 'blat_list'

    def get_queryset(self):
        """ get query set for generic view """
        return Blat.objects.filter(created_by=self.request.user.id).order_by('-created_on')[:20]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):# pylint: disable=arguments-differ
        return super(MyView, self).dispatch(*args, **kwargs)


class DetailView(generic.DetailView):# pylint: disable=too-many-ancestors
    """ DetailView for a blat """
    model = Blat
    template_name = 'blat/detail.html'
    context_object = 'blat'

class NewBlatView(generic.edit.CreateView):# pylint: disable=too-many-ancestors
    """ CreateView for a new blat """
    model = Blat
    fields = ['via', 'text']
    success_url = '/my/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NewBlatView, self).form_valid(form)

class EditBlatView(generic.edit.UpdateView):# pylint: disable=too-many-ancestors
    """ Edit View for an existing blat """
    model = Blat
    fields = ['via', 'text']
    success_url = '/my/'

    def get_queryset(self):
        blat_set = super(EditBlatView, self).get_queryset()
        return blat_set.filter(created_by=self.request.user)
