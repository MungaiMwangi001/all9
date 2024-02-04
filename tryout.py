import django
from django.db import models

# Define a Django model
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

# Perform operations with the Django model
def create_model_instance():
    instance = MyModel(name='John Doe', age=25)
    instance.save()

def get_model_instances():
    instances = MyModel.objects.all()
    for instance in instances:
        print(instance.name, instance.age)

# Call the functions to execute the operations
create_model_instance()
get_model_instances()
