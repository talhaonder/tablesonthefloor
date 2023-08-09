from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    all_members = Member.objects.all()
    return render(request, 'datatables/index.html', {'all_members': all_members})