from django.db import models

class EquipmentSupplier(models.Model):
    '''Информация о поставщике'''
    name = models.CharField(max_length=100, verbose_name='Название/Имя')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Улица')
    street = models.CharField(max_length=100, verbose_name='Город')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

class NetworkNode(models.Model):
    '''Абстрактная модель с полями для всех уровней'''
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска')
    supplier = models.ForeignKey(EquipmentSupplier, on_delete=models.CASCADE, verbose_name='Ссылка на поставщика')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

class Factory(NetworkNode):
    '''Модель: завод'''
    level = models.IntegerField(default=0)

class RetailChain(NetworkNode):
    '''Модель: розничная сеть'''
    level = models.IntegerField(default=1)

class IndividualEntrepreneur(NetworkNode):
    '''Модель: индивидуальный предприниматель'''
    level = models.IntegerField(default=2)