from django.db import models

class PlaneType(models.Model):

    class Meta:
        verbose_name = ('Модель самолёта')
        verbose_name_plural = ('Модели самолётов')

    choices_style = (
        (1, 'Пассажирский'),
        (2, 'Чартерный'),
        (3, 'Почтовый'),
        (4, 'Военный'),
    )

    name = models.CharField('Модель', max_length=20)
    style = models.PositiveSmallIntegerField(
        'Тип', choices=choices_style)
    seat = models.PositiveSmallIntegerField(
        'Кол-во мест', null=True, blank=True)
    manufacture = models.DateField('Дата выпуска')

    def __str__(self):
        return (self.name)


class Plane(models.Model):

    class Meta:
        verbose_name = ('Самолёт')
        verbose_name_plural = ('Самолёты')

    plane_type = models.ForeignKey(
        PlaneType, verbose_name='Модель самолёта', on_delete=models.CASCADE)
    purchase = models.DateField('Дата покупки')
    reg_numb = models.CharField('Рег. номер', editable=False, max_length=6, unique=True)
    last_refit = models.DateField('Последний осмотр', null=True,
                                  blank=True)
    fly_col = models.PositiveSmallIntegerField('Кол-во полётов', null=True,
                                               blank=True)
    def reg_numb_generation(self):
        import random
        reg_numb = ''
        for x in range(6):
            reg_numb += random.choice(list('123456789QWERTYUIOPASDFGHJKLZXCVBNM'))
        return reg_numb

    def save(self, *args, **kwargs):
        self.reg_numb = self.reg_numb_generation()
        super(Plane, self).save(*args,**kwargs)

    def __str__(self):
        return ((self.plane_type.name) + ' | ' + (self.reg_numb))
