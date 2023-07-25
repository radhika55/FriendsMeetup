from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views.generic import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import SignUpSerializer

# Create your views here.

# class StartingPage(View):
#     template_name = 'demo/signup.html'
#     model = User

#     def get(self, request):
#         return render(request, 'demo/signup.html')

#     def post(self, request):
#         email = request.POST.get('email')
#         first_name = request.POST.get('firstName')
#         last_name = request.POST.get('lastName')
#         password = request.POST.get('password')

#         User = get_user_model()
#         if not User.objects.filter(email=email).exists():
#             user = User(email=email, first_name=first_name,
#                         last_name=last_name, password=password)
#             user.save()
#             return render(request, 'demo/signup.html')
#         return render(request, 'demo/signup.html', {'error_message': 'Email already registered.'})


# class StartingPage():
#     template_name = 'demo/signup.html'


class SignUpView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'demo/signup.html'

    def get(self, request):
        serializer = SignUpSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'errors': serializer.errors})
            # import pdb
            # pdb.set_trace()
        serializer.save()
        return redirect('starting_page')


@api_view
def login(APIView):
    pass


class Profile(APIView):
    pass
