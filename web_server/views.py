from django.views.generic import TemplateView, ListView
from django.shortcuts import render

class HomePage(TemplateView):
    def get(self,request):
      print('Server is Running')
      return render(request,'index.html')
