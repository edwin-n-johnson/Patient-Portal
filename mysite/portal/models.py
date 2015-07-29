from django.db import models

# Patient class
class Patient(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)

    birthdate = models.DateField()
    email     = models.CharField(max_length=256)

    def __unicode__(self):
        return self.lastname + ',' + self.firstname

class Physician(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)

    DOCTOR    = 'DR'
    PHYSASST  = 'PA'
    NURSEPR   = 'NP'
    PHYSICIAN_TYPE_CHOICES = (
        (DOCTOR,    'Doctor'),
        (PHYSASST,  'Physician Assistant'),
        (NURSEPR,   'Nurse Practitioner'),
        )
    phystype  = models.CharField(max_length=max(len(x[0]) for x in PHYSICIAN_TYPE_CHOICES),
                                 choices=PHYSICIAN_TYPE_CHOICES,
                                 default=DOCTOR)
    
# Visit class
class Appointment(models.Model):
    patient   = models.ForeignKey(Patient)
    physician = models.ForeignKey(Physician)
    date      = models.DateField()
    summary   = models.CharField(max_length=256)
    
    def __unicode__(self):
        return unicode(self.date) + ' with ' + self.physician


class Message(models.Model):
    patient   = models.ForeignKey(Patient)
    date      = models.DateField()
    subject   = models.CharField(max_length=50)
    body      = models.CharField(max_length=2048)
    
