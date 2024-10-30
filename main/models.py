from django.db import models

# Create your models here.
class Ownpr(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(verbose_name='Наименование товара', max_length=150, null=True)
    material = models.IntegerField(verbose_name='Материальные затраты', null=True)
    work = models.IntegerField(verbose_name='Оплата труда', null=True)
    social = models.IntegerField(verbose_name='Социальные мероприятия', null=True)
    amort = models.IntegerField(verbose_name='Амортизация средств', null=True)

    class Meta:
        verbose_name = 'Себестоимость'
        verbose_name_plural = 'Себестоимости'

class Others(models.Model):
    def __str__(self):
        return self.name
    cons = models.ForeignKey(Ownpr, verbose_name='Общие расходы', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование расхода', max_length=100, null=True)
    money = models.IntegerField(verbose_name='Кол-во расходов', null=True)

    class Meta:
        verbose_name = 'Прочие расходы'
        verbose_name_plural = 'Прочие расходы'


class Consumptions(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField('Промежуток расходов', max_length=70, null=True)

    class Meta:
        verbose_name = 'Подсчёт расходов'
        verbose_name_plural = 'Подсчёты расходов'

class Subcons(models.Model):
    def __str__(self):
        return self.name
    con = models.ForeignKey(Consumptions, verbose_name='Промежуток', on_delete=models.CASCADE)
    name = models.CharField('Наименование расхода', max_length=70, null=True)
    date = models.DateTimeField(verbose_name='Время', null=True)
    total = models.IntegerField(verbose_name='Потрачено', null=True)

    class Meta:
        verbose_name = 'Часть расхода'
        verbose_name_plural = 'Части расхода'