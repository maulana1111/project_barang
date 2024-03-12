import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
def photo_directory_path(filename):
    return 'picture/{}.{}'.format(uuid.uuid4(), filename.split('.')[-1])

def validate_file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')

def validate_file_extension(value):
    ALLOWED_EXT = ('.pdf', '.jpg', '.png', '.jpeg', '.docx', '.doc', '.docm',
                   '.dotx', '.dotm', '.dot', '.odt')
    if not value.name.endswith(ALLOWED_EXT):
        raise ValidationError(u'Incorrect Format!')


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category'

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 'brand'

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    stars = models.FloatField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=False)
    stock_count = models.IntegerField()
    description = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'product'

class ProductPicture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.FileField(upload_to=photo_directory_path, validators=[
                                                    validate_file_size,
                                                    validate_file_extension
                                                    ])
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        db_table = 'product_picture'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + str(self.create_dt)

    class Meta:
        db_table = 'contact'
