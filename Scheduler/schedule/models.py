from django.db import models

# defining fields
class Schedule(models.Model):
    status_type=(
    ('scheduled', 'scheduled'),
    ('work in progress', 'work in progress'),
    ('done', 'done')
    )
    # name of customer
    name = models.CharField(max_length=50)
    # time
    time = models.TimeField(auto_now=False, auto_now_add=False)
    # car status
    status = models.CharField(max_length=20, choices=status_type, default='scheduled')
    # appointment date
    date = models.DateField(auto_now=False, auto_now_add=False)
    # price (estimate)
    price = models.DecimalField(max_digits=7, decimal_places=2)
