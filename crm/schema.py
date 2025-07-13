import graphene
from graphene_django.types import DjangoObjectType
from crm.models import Customer

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = "__all__"

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)

    def resolve_all_customers(root, info):
        return Customer.objects.all()

schema = graphene.Schema(query=Query)

import graphene
from crm.models import Product

class ProductType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    stock = graphene.Int()

class UpdateLowStockProducts(graphene.Mutation):
    updated_products = graphene.List(ProductType)
    message = graphene.String()

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        for product in low_stock_products:
            product.stock += 10
            product.save()
        return UpdateLowStockProducts(
            updated_products=low_stock_products,
            message=f"Updated {low_stock_products.count()} low stock products."
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()
