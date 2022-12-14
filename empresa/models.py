from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

class Company(models.Model):
    owner = models.OneToOneField(
        User, 
        related_name='company',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        )
    name = models.CharField(
        'name', 
        max_length=200,
        null=False,
        blank=False,
        unique=True,
        primary_key=True,
        )
    email = models.EmailField('email', null=True, blank=True)
    total_billing  = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']

class TypeProdutChoices(models.TextChoices):
    GENERIC = 'generic'
    FOOD = 'food'
    DRUG = 'drug'
    OTHER = 'other'
class Product(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='products'
    )
    name = models.CharField('name', max_length=200, unique=True)
    description = models.TextField('description', max_length=200)
    price = models.FloatField(
        validators=[MinValueValidator(0.1)],
        null=False,
        blank=False,
        default=1,
    )
    product_type = models.CharField(
        max_length=10,
        choices=TypeProdutChoices.choices,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='inventory',
    )
    quantity = models.PositiveIntegerField(
        'quantity', 
        blank=True,
        default=0
        )


class RegistrySituation(models.TextChoices):
    APPROVED = 'approved'
    REJECTED = 'rejjected'
    PENDING = 'pending'
class Registry(models.Model):
    company = models.ForeignKey(
        Company, 
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='registrys',
        )
    product = models.ForeignKey(
        Product, 
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        )
    product_price = models.FloatField(
        validators=[MinValueValidator(0.1)], # Implement GreaterThanZeroValueValidator
        null=True,
        blank=True,
    )
    product_quantity = models.IntegerField(
        validators=[MinValueValidator(1)]
        )

    # total_price = models.FloatField()
    
    created_at = models.DateTimeField('created at', auto_now_add=True)

    situation = models.CharField(
        'situation',
        max_length=15,
        blank=True,
        null=False,
        choices=RegistrySituation.choices,
        default=RegistrySituation.PENDING
    )

    def total_price(self):
        return self.product_price * self.product_quantity


    class Meta:
        ordering = ['-id']