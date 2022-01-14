from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from model_utils import Choices
from model_utils.fields import StatusField

from product.models import CreatedAtModel
User = get_user_model()


class Order (CreatedAtModel):
    STATUS = Choices ('In progress', 'Canceled', 'Finished')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='orders')
    products = models.ManyToManyField('product.Product')
    order_status = StatusField()

    class Meta:
        ordering = ['-created_at']
        db_table= 'order'

    def __str__(self):
        return f'Заказ№{self.id} от {self.created_at.strftime("%d-%m-%Y %H:%M")}'