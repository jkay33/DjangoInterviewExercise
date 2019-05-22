from django.shortcuts import render, HttpResponse
from .models import Schedule
from .Form import SGenAppForm
from faker import Faker
from faker.generator import random

fake = Faker()
# Create your views here.
# Defining home view to return html file
def home(request):

    class Meta:
        model = Schedule
        fields = '__all__'

    #intake the data being submitted
    if request.method == 'POST':
        form = SGenAppForm(request.POST)
        #if data in form is clean set it to value as int
        if form.is_valid():
            value = int(form.cleaned_data['records'])
            #generate random data using faker "vale" amount of times
            for x in range(value):
                status_type=(
                'scheduled',
                'work in progress',
                'done'
                )
                Schedule_Instance = Schedule(
                name = fake.name(),
                time = fake.time(),
                status = random.choice(status_type),
                date = fake.date(),
                price = fake.random_number(digits=5)
                )
                Schedule_Instance.save()


    #Include form
    form = SGenAppForm()
    #This will be the appointment scheduler at random intervals will live.
    return render(request, 'front/index.html/', {'form': form})
