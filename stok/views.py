from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import MalzemeGruplari, Projeler


@login_required(login_url='/login') # Giriş yapıldıysa gösterme decoratörü 1-) Detaylandırılacak
def HomePageView(request):
    return render(request,'home.html')

def LoginPageView(request): # Giriş yapılmış mı kontrol etmeye yarıyor.
    if request.user.is_authenticated:
        return redirect(HomePageView)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(HomePageView)
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def StockRequestView(request):
    context= {'MalzemeGruplari': MalzemeGruplari}
    context ={'Projeler': Projeler}
    return render(request, "stock_request.html",context)


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from stok.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
