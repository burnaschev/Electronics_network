from django.db import models

NULLABLE = {"null": True, "blank": True}


class Levels(models.IntegerChoices):

    FACTORY = 0, 'Завод'
    RETAIL_NETWORK = 1, 'Розничная сеть'
    IP = 2, 'Индивидуальный предприниматель'


class Node(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='название')
    supplier = models.ForeignKey('self', **NULLABLE, default=None, on_delete=models.SET_NULL, verbose_name='поставщик')
    level = models.IntegerField(choices=Levels.choices, default=Levels.FACTORY, verbose_name='Уровень структуры')
    debt_to_the_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='долг')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата и время создания')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['-level']


class Contact(models.Model):
    member = models.OneToOneField(Node, on_delete=models.CASCADE, verbose_name='поставщик')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='страна')
    city = models.CharField(max_length=50, **NULLABLE, verbose_name='город')
    street = models.CharField(max_length=150, **NULLABLE, verbose_name='улица')
    house_number = models.CharField(max_length=10, **NULLABLE, verbose_name='номер дома')

    def __str__(self):
        return f"{self.member} ({self.email})"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата релиза')
    owner = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='owners', verbose_name="поставщик")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продажи')

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
