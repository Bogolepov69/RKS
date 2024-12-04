from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vin_number = models.CharField(max_length=20, unique=True)  # VIN-номер полуприцепа
    trailer_type = models.CharField(max_length=50)  # Тип полуприцепа
    assembly_date = models.DateField()  # Дата сборки
    shipping_date = models.DateField(null=True, blank=True)  # Дата отгрузки
    status = models.CharField(max_length=20, choices=[
        ('in_progress', 'В работе'),
        ('ready', 'Готов к отгрузке'),
        ('shipped', 'Отгружен'),
    ], default='in_progress')  # Статус готовности полуприцепа
    order_date = models.DateField()  # Дата заказа
    additional_options = models.TextField(blank=True)  # Дополнительные опции
    specification = models.TextField()  # Спецификация

    def __str__(self):
        return f"Заказ № {self.pk} ({self.vin_number})"


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


def main():
    pass
