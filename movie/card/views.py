from django.http import HttpResponse
from django.shortcuts import render, redirect
from card.models import Cards
from card.forms import Cardsform
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
# def home(request):
#     k = Cards.objects.all()
#     return render(request,'home.html',{'c':k})

class MovieList(ListView):     #ListView Displays all objects/records retreieving from model.
    model=Cards
    template_name="home.html"
    context_object_name="c"


# def moviedetail(request,p):
#     c=Cards.objects.get(id=p)
#     return render(request,'movie.html',{'c':c})


class MovieDetail(DetailView):    ##DetailView Displays a particular  retrieving from a model.
    model=Cards
    template_name='movie.html'
    context_object_name="c"



# def addmovie(request):
#     if(request.method =="POST"):  #After submission
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         i=request.FILES['i']
#         c=Cards.objects.create(title=t,desc=d,year=y,image=i)
#         c.save()
#         return redirect("/")
#     return render(request,"addmovie.html")

class Movieadd(CreateView):    #CreateView displays a form for adding new object and handles forms submission.
    model=Cards
    template_name="addmovie.html"
    fields='__all__'
    success_url=reverse_lazy('card:home')


# def movieupdate(request,p):
#     c=Cards.objects.get(id=p)
#        form=Cardsform(instance=c)
#     if (request.method == "POST"):  # After submission
#         form = Cardsform(request.POST,request.FILES,instance=c)  # Creates form object initialized with values inside request.POST
#         if form.is_valid():
#             form.save()  # save the form object inside DB table
#             return redirect("/")
#             return render(request, 'movie.html', {'c': c})
#     else:
#         form = Cardsform(instance=c)
#     return render(request,'update.html',{'form': form})


class Movieupdate(UpdateView):
    model = Cards
    template_name = "update.html"
    fields = '__all__'
    success_url = reverse_lazy('card:home')



# def moviedelete(request,p):
#     if(request.method =="POST"):
#         c= Cards.objects.get(id=p)
#         c.delete()
#         return redirect("/")
#     return render(request,'home.html')


class Moviedelete(DeleteView):
    model=Cards
    success_url=reverse_lazy('card:home')
    template_name = "delete.html"




# def viewmovie(request):
#     k=Cards.objects.all()
#     return render(request,"viewmovie.html",{'c':k})





