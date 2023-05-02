from django.db import models
from datetime import datetime

class customers(models.Model):
    class meta:
        db_table = "customers"
        verbose_name = "Customers info"

        
    customer_name = models.CharField(verbose_name="Customer name", on_delete=models.RESTRICT)
    customer_adress = models.CharField(verbose_name="adress", on_delete=models.RESTRICT)
    customer_id = models.CharField(verbose_name="Customer ID", on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.customer_name
    
class orders(models.Model):
    class meta:
        db_table = "orders"
        verbose_name = "orders info"

    order_id = models.Charfield(verbose_name="Order ID", on_delete=models.RESTRICT)
    order_description = models.CharField(verbose_name="description for order")
    created_date = models.DateTimeField(verbose_name="order date", auto_now_add=True)
    order_status = models.CharField(verbose_name="order status", validators=[status_validator])
    customer_id = models.ForeignKey(customers, verbose_name="Customer" , on_delete=models.RESTRICT )

    


    

    
