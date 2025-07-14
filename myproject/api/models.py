from django.db import models

# Create your models here.
class WheelForm(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()

    def __str__(self):
        return self.formNumber

class WheelField(models.Model):
    form = models.OneToOneField(WheelForm, related_name='fields', on_delete=models.CASCADE)

    treadDiameterNew = models.CharField(max_length=50)
    lastShopIssueSize = models.CharField(max_length=50)
    condemningDia = models.CharField(max_length=50)
    wheelGauge = models.CharField(max_length=50)
    variationSameAxle = models.CharField(max_length=50)
    variationSameBogie = models.CharField(max_length=50)
    variationSameCoach = models.CharField(max_length=50)
    wheelProfile = models.CharField(max_length=100)
    intermediateWWP = models.CharField(max_length=50)
    bearingSeatDiameter = models.CharField(max_length=100)
    rollerBearingOuterDia = models.CharField(max_length=100)
    rollerBearingBoreDia = models.CharField(max_length=100)
    rollerBearingWidth = models.CharField(max_length=100)
    axleBoxHousingBoreDia = models.CharField(max_length=100)
    wheelDiscWidth = models.CharField(max_length=100)