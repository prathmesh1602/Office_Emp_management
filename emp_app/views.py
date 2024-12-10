from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    
    return render(request,'all_emp.html',context)

def add_emp(request):
    departments = Department.objects.all()
    roles=Role.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        new_emp=Employee(first_name = first_name,last_name = last_name,dept_id = dept,role_id=role,salary=salary,bonus=bonus,phone=phone,hire_date=hire_date)
        new_emp.save()
        return HttpResponse("Employe Added Succesfully")  

    return render(request,'add_emp.html',{'departments': departments,'roles': roles})

def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removes Successfully")
        except:
            return HttpResponse('Pls select valid id')
    emps =Employee.objects.all()
    context = {
        'emps' : emps
    }

    return render(request,'remove_emp.html',context)

def filter_emp(request):
    return render(request,'filter_emp.html')