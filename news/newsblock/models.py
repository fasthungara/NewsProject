from django.db import models

class News(models.Model):
    title = models.CharField(max_length=40)
    short_description = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, name='rubric')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'New'
class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='rubric')

    def __str__(self):
        return f'{self.name}'