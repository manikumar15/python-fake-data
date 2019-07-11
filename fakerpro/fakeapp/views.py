from django.shortcuts import render
from .models import FakeData
from django.http.response import HttpResponse
import faker
fake=faker.Faker()

def insertingdata(request):
	for i in range(100):
		first_name=fake.first_name()
		last_name=fake.first_name()
		email=fake.email()
		job=fake.random_element(elements=("HR","TL","MGR"))
		salary=fake.random_element(elements=(10000,40000,50000))
		city=fake.random_element(elements=("hyderabad","goa","bangalore"))

		data=FakeData(
			first_name=first_name,
			last_name=last_name,
			email=email,
			job=job,
			salary=salary,
			city=city
		)
		data.save()
	return HttpResponse("Data is Saved sucessfully")

def fetchingdata(request):
	fakedata=FakeData.objects.all()
	return render(request,"fakedata.html",{'fakedata':fakedata})
