from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'app/index.html', context=None)
