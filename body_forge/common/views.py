from django.shortcuts import render
from django.views import View


def index(request):
    template_name = "common/index_auth.html" if request.user.is_authenticated else "common/index_not_auth.html"

    return render(request, template_name)




