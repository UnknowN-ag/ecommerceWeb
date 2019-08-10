from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=300)
    category = models.CharField(max_length = 50, default="")
    subCategory = models.CharField(max_length = 50, default="")
    price = models.IntegerField(default=0)
    product_publish_date = models.DateField()
    images = models.ImageField(upload_to = "shop/images", default="")

    def __str__(self):
        return self.product_name