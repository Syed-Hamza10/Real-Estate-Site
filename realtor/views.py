from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm, AddProperty
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    purpose_filter = request.GET.get('purpose', '')  # Get the purpose filter from the URL

    if purpose_filter:
        properties = Property.objects.filter(purpose=purpose_filter)
    else:
        properties = Property.objects.all()

    user = request.user
    return render(request, 'realtor/home.html', {'properties': properties,'user':user})

def detail(request,property_id):
    user = request.user
    property = Property.objects.get(id=property_id)
    return render(request, 'realtor/detail.html',{'property':property,'user':user})


@login_required
def delete(request,property_id):
    property = Property.objects.get(id = property_id)
    property.delete()
    return redirect('realtor:home')


def ContactView(request):
    user = request.user
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            print(f"Name : {form.cleaned_data['Name']}")
            print(f"Email : {form.cleaned_data['Email']}")
            print(f"Msg : {form.cleaned_data['Message']}")
            
        
    else:
        form = PropertyForm()
        
    return render(request, 'realtor/contact.html', {'form' : form,'user':user})

@login_required
def NewPropertyView(request):

    if request.method == 'POST':
        form = AddProperty(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('realtor:home')
        
    else:
        form = AddProperty()
        
    return render(request, 'realtor/new_property.html', {'form' : form})



