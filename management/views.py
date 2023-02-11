from django.shortcuts import render, redirect
from .models import TeamMember

# Create your views here.
def list(request):
    return render(request, 'list.html', {'team_members': TeamMember.objects.all()})

def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        role = request.POST['role']
        team_member = TeamMember(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, role=role)
        team_member.save()
        return redirect('list')
    return render(request, 'add.html')

def edit(request, pk):
    member = TeamMember.objects.get(pk=pk)
    if request.method == 'POST':
        if 'delete' in request.POST:
            member.delete()
            return redirect('list')
        else:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            role = request.POST.get('role')

            member.first_name = first_name
            member.last_name = last_name
            member.email = email
            member.phone_number = phone_number
            member.role = role
            member.save()

            return redirect('list')
    return render(request, 'edit.html', {'member': member})
