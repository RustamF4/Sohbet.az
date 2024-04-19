from django.shortcuts import render # type: ignore
from django.views import View  # type: ignore

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

