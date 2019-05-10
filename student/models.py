from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class ProgramAndBranch(models.Model):
    name = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=10)
    usable = models.BooleanField(default=False)

    def __str__(self):
        return self.abbreviation
