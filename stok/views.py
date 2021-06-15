from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from stok.models import MalzemeGruplari, Projeler, Stok
from django.urls import reverse
from django.http.response import HttpResponse
from river.models import State


def approve_stok(request, stok_id, next_state_id=None):
    stok = get_object_or_404(Stok, pk=stok_id)
    next_state = get_object_or_404(State, pk=next_state_id)
    
    try:
        stok.river.Stok_Talebi.approve(as_user=request.user, next_state=next_state)
        return redirect("http://127.0.0.1:8000/admin/stok/stok")
    except Exception as e:
        return HttpResponse(e)


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


"""INTRANET SITE KODLAR"""
@login_required(login_url='/login') # Giriş yapıldıysa gösterme decoratörü 1-) Detaylandırılacak
def HomePageView(request):
    return render(request,'home.html')


@login_required(login_url='/login')
def StockRequestView(request):
    context= {'MalzemeGruplari': MalzemeGruplari}
    context ={'Projeler': Projeler}
    return render(request, "stock_request.html",context)

""" """
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from stok.serializers import UserSerializer, GroupSerializer

"""REST API """
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

