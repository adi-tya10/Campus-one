import uuid
from django.db import models

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    usn = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    mobile = models.CharField(max_length=15)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    email = models.EmailField()
    aadhar_no = models.CharField(max_length=12)
    sslc_mark = models.FloatField()
    puc_mark = models.FloatField()
    father_mobile = models.CharField(max_length=15)
    mother_mobile = models.CharField(max_length=15)
    semester_card = models.FileField(upload_to='semester_cards/', blank=True, null=True)

    disability = models.BooleanField(default=False)
    disability_description = models.TextField(blank=True, null=True)

    accommodation = models.CharField(max_length=10, choices=[("Hostel", "Hostel"), ("Travel", "Travel")])
    travel_description = models.CharField(max_length=255, blank=True, null=True)
    
    college_fee_demand = models.FloatField()
    college_fee_balance = models.FloatField()
    hostel_fee_demand = models.FloatField()
    hostel_fee_balance = models.FloatField()
    bus_fee_demand = models.FloatField()
    bus_fee_balance = models.FloatField()

    achievement_status = models.BooleanField(default=False)
    achievement_description = models.TextField(blank=True, null=True)
    aicte_points = models.IntegerField()
    scholarship_status = models.BooleanField(default=False)
    scholarship_name = models.CharField(max_length=100, blank=True, null=True)
    
    attendance = models.FloatField()
    ia_marks = models.FloatField()

    timetable = models.FileField(upload_to='documents/', blank=True, null=True)
    circulars = models.TextField(blank=True, null=True)
    parents_visits = models.TextField(blank=True, null=True)
    participation_permission = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.usn})"
