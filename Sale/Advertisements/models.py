from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT)


class Rubric(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'