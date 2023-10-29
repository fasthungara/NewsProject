from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, name='rubric')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'
class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='rubric')

    def __str__(self):
        return f'{self.name}'