from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=20)
    isShareable = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Calendar"

class Event(models.Model):
    eventId = models.BigAutoField(primary_key=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    content_type = models.CharField(max_length=10)
    duration = models.FloatField(default=0)
    note = models.CharField(max_length=100, blank=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Event"

class Account(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Account"

class Membership(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.calendar) + ' - ' + str(self.account)

    class Meta:
        db_table = "Membership"