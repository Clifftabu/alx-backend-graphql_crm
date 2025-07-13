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
