from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    @property
    def get_discount(self):
        return "122"

    def __str__(self):
        return self.title