from django.shortcuts import (render, get_object_or_404)
from django.http.response import HttpResponse
from django.views import generic
from .models import User

# Decorators to check login
from django.contrib.auth.decorators import login_required  # for function based views
from django.contrib.auth.mixins import LoginRequiredMixin  # for class based views
# class MyView(LoginRequiredMixin, View): # for class based views


def handler404(request):
    # TODO: to add handler for 404
    # response = render_to_response('404.html', {},
    #                               context_instance=RequestContext(request))
    response = HttpResponse("Error")
    response.status_code = 404
    return response


@login_required
def index(requests):
    return render(requests, 'base_template.html')


class UserListView(generic.ListView):
    model = User
    context_object_name = 'user_list'  # your own name for the list as a template variable
    # queryset = User.objects.filter(email__contains='email') #Get users with word email in their emails
    queryset = User.objects.all()
    template_name = 'core/user_list.html'  # Specify your own template name/location


class UserDetailView(generic.DetailView):
    model = User

    def user_detail_view(request, pk):
        # try:
        #     user_id = User.objects.get(pk=pk)
        # except User.DoesNotExist:
        #     raise Http404("user does not exist")

        user_id=get_object_or_404(User, pk=pk)

        return render(
            request,
            'catalog/user_detail.html',
            context={'user': user_id, }
        )


