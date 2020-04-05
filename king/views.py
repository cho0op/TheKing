from django.shortcuts import render
from .models import King
from .forms import KingForm
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from .forms import KingForm

def home(request):
    king=King.objects.last()
    if request.method == "POST":
        form = KingForm(request.POST)
        pic = request.FILES['pic']
        fs = FileSystemStorage()
        fs.save(pic.name, pic)
        newKing=KingForm(request)
        newKing.save()
        if form.is_valid():
            return redirect('home')
    else:
        form=KingForm()
    return render(request, 'king/home.html', {'form' : form,'king':king})
# Create your views here.
