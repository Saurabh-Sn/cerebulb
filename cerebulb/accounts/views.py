from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .serializers import LoginSerializer
from django.contrib.auth.decorators import login_required
from .models import  Category
# Create your views here.


class USerLoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    style = {}

    def get(self, request):
        if request.user.id:
            return redirect('admin:index')
        serializer = LoginSerializer()
        return Response({'serializer': serializer, 'style': self.style })

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(email=serializer.data.get('email'), password=serializer.data.get('password'))
            remember_me = serializer.data.get('remember_me')
            if user:
                if not remember_me:
                    request.session.set_expiry(0)
                login(request, user)
                next_url = request.GET.get('next', None)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('admin:index')
            else:
                messages.error(request, 'Email or Password did not match.')
        return Response({'serializer': serializer, 'style': self.style})


@login_required()
def products(request):
    return render(request, 'product_list.html', )


@login_required()
def add_product(request):
    category = Category.objects.filter(is_deleted=False)
    return render(request, 'add_product.html', {'category': category} )


@login_required()
def edit_product(request, pk=None):

    category = Category.objects.filter(is_deleted=False)
    return render(request, 'edit_product.html', {'category': category} )