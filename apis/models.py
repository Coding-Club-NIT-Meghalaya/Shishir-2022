from django.db import models
# Create your models here.
from froala_editor.fields import FroalaField


class Year(models.Model):
    festival_name=models.CharField(max_length=50)
    year = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.year)


class Event(models.Model):
    TYPE_CHOICES = (
        ("Main", "Main"),
        ("Departmental", "Departmental"),
        ("Gaming", "Gaming"),
        ("Other", "Other"),
    )
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(
        max_length=200, choices=TYPE_CHOICES, default='Coding')
    duration = models.CharField(max_length=100)
    total_prize = FroalaField()
    registration_link = models.CharField(max_length=100)
    year = models.ForeignKey(
        Year, on_delete=models.PROTECT, related_name='event_year')
    description = FroalaField()
    image = models.CharField(max_length=200)
    live_link = models.CharField(max_length=100)
    doc_link = models.CharField(max_length=100)
    rules=FroalaField()

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    POSITION_CHOICES = (
        ("Head","Head"),
        ("Coordinator", "Coordinator"),
        ("Co-Coordinator", "Co-Coordinator"),
        ("General Secretary", "General Secretary"),
        ("Publicity and Core Team Head",
         "Publicity and Core Team Head"),
        ("Publicity and Core Team Coordinator",
         "Publicity and Core Team Coordinator"),
        ("Publicity and Core Team Co-Coordinator",
         "Publicity and Core Team Co-Coordinator"),
         ("Designing Team Head", "Designing Team Head"),
        ("Designing Team Coordinator", "Designing Team Coordinator"),
        ("Designing Team Co-Coordinator", "Designing Team Co-Coordinator"),
        ("Sponsor and Marketing Team Head",
         "Sponsor and Marketing Team Head"),
        ("Sponsor and Marketing Team Coordinator",
         "Sponsor and Marketing Team Coordinator"),
        ("Sponsor and Marketing Team Co-Coordinator",
         "Sponsor and Marketing Team Co-Coordinator"),
        ("Web Development Team Head",
         "Web Development Team Head"),
        ("Web Development Team Coordinator",
         "Web Development Team Coordinator"),
        ("Web Development Team Co-Coordinator",
         "Web Development Team Co-Coordinator"),
        ("App Development Team Head",
         "App Development Team Head"),
        ("App Development Team Coordinator",
         "App Development Team Coordinator"),
        ("App Development Team Co-Coordinator",
         "App Development Team Co-Coordinator"),

    )
    member_name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100, choices=POSITION_CHOICES, default='Coordinator')
    email = models.EmailField(max_length=100)
    image = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    event_name = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name='team_members', blank=True, null=True)


class Gallery(models.Model):
    event_name=models.CharField(max_length=30)
    image = models.CharField(max_length=200)


class Notification(models.Model):
    notification = models.CharField(max_length=500)