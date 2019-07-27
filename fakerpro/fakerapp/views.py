from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import FakerData
import faker

# Create your views here.
fake = faker.Faker()
def savefakeData(request):
    for i in range(25):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        job = fake.random_element(elements = ("HR","PM","Admin","Manager"))
        salary = fake.random_element(elements = (50000,55000,560000,54000))
        city = fake.random_element(elements = ('Hyd','Bang','Pune','Mumbai'))
        state = fake.state()
        address = fake.address()

        data = FakerData(first_name=first_name,last_name=last_name,email=email,
                  job=job,salary=salary,city=city,state=state,address=address)
        data.save()
    # return HttpResponse('Data Saved!')
    return redirect('/fetchingdata/')


from django.db.models import Q
def fetchingData(request):
    # data = FakerData.objects.all()
    # data = FakerData.objects.all()
    # data = FakerData.objects.filter(Q(job__exact='Manager')|Q(city__exact='Bang')|Q(salary__exact=54000))
    # data = FakerData.objects.order_by('-salary')# Descending order
    # data = FakerData.objects.filter(~Q(city__exact='Hyd')& Q(salary__exact=55000))
    # data = FakerData.objects.filter(id =1)
    # data = FakerData.objects.all()[0:1]
    data = FakerData.objects.all()

    return render(request,'index.html',{'data':data})

