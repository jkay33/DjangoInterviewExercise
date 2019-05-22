
from schedule.models import Schedule
from .serializer import scheduleSerializer
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters


# schedule filter variant which defines the filter button
class scheduleFilter(filters.FilterSet):
    #tuple of possible choices
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')

    )

    date = filters.DateFromToRangeFilter()
    #create field to give user choice for ascending or descending order and passes to sorting method
    order = filters.ChoiceFilter(label='Price', choices=CHOICES, method='sorting')


    class Meta:
        model = Schedule
        #dictionary of possible fields, may change to list depending on if any additional fields
        fields = {
            'date'
        }
    #Function to determine how to sort. Function is getting the input value and sorting it accordingly
    def sorting(self, queryset, name, value):
        sort = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(sort)


#Schedule viewset
# this will specify the variety of views.
class scheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all() #this will return all objects from model
    permissions_classes=[
    permissions.AllowAny
    ]
    serializer_class = scheduleSerializer
    # include the filter
    filterset_class = scheduleFilter
