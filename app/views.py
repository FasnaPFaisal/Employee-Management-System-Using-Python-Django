from django.shortcuts import render, redirect
from .models import AddEmployee

def index(request):     
    registrations = AddEmployee.objects.all() 
    return render(request, "index.html", {'registrations': registrations})

def addemp(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')        
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        date_of_joining = request.POST.get('date_of_joining')
        role = request.POST.get('role')
        AddEmployee.objects.create(employee_id=employee_id, name=name, address=address, email=email,
                                   contact_number=contact_number, date_of_joining=date_of_joining, role=role)
        return redirect("home")
    return render(request, "addemp.html")

def update(request, id):
    registration = AddEmployee.objects.get(id=id)
    if request.method == 'POST':
        registration.employee_id = request.POST.get('employee_id')
        registration.name = request.POST.get('name')        
        registration.email = request.POST.get('email')
        registration.contact_number = request.POST.get('contact_number')
        registration.address = request.POST.get('address')
        registration.date_of_joining = request.POST.get('date_of_joining')
        registration.role = request.POST.get('role')
        registration.save()
        return redirect("home")
    return render(request, "update.html", {'registration': registration})

def delete(request, id):
    registration = AddEmployee.objects.get(id=id)
    registration.delete()
    return redirect("home")
