from django.db import models

# Patient class
class Patient(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)

    birthdate = models.DateField()
    email     = models.CharField(max_length=256)

    def __unicode__(self):
        return self.lastname + ',' + self.firstname

# Visit class
class Visit(models.Model):
    patient   = models.ForeignKey(Patient)
    date      = models.DateField()
    summary   = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.date) + ': ' + self.summary


