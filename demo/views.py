from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.base import TemplateView
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import LogInSerializer, UserSerializer

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
        serializer = UserSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'errors': serializer.errors})
        serializer.save()
        return redirect('starting_page')


@api_view(['GET', 'POST'])
def user_login(request):
    if request.method == 'POST':
        serializer = LogInSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return render(request, 'demo/login.html')


class Profile(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    template_name = 'demo/profile.html'
    serializer = UserSerializer()
