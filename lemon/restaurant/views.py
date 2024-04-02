from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .forms import BookingForm
# Create your views here.


def about(request):
    return render(request, 'about.html')
def index(request):
    return render(request,'index.html')


@api_view(['GET','POST','PUT','DELET'])
# Create your views here. 
class MenuItemsView(ListCreateAPIView):
      def get(self,request):
         permission_classes=[IsAuthenticated]
         queryset = Menu.objects.all()
         serializer_class = MenuItemSerializer(queryset)
         return Response(serializer_class.data)

#class SingleMenuItemView(RetrieveUpdateAPIView, RetrieveDestroyAPIView):
#queryset = MenuItem.objects.all()
#serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    def get(self,request):
        items = Booking.objects.all()
        serializer= BookingSerializer(items, many=True)
        return Response(serializer.data)
    
def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', main_data)