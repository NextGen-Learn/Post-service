from django.db import models

class Order(models.Model):
    customer = models.IntegerField()
    performer = models.IntegerField()
    requirements = models.JSONField()
    notes = models.TextField(blank=True)
    matched_tutors = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id} by {self.customer.username}'
