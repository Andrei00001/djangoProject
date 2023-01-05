from uuid import uuid1, uuid4

from djongo import models as mongo_models


def generate_random_id():
    return str(uuid1()) + str(uuid4())


class Form(mongo_models.Model):
    class Meta:
        managed = False

    id = mongo_models.CharField(
        max_length=64,
        primary_key=True,
        editable=False,
        verbose_name='ID',
        default=generate_random_id,
    )
    name = mongo_models.CharField(max_length=50, unique=True)
    email = mongo_models.EmailField(max_length=64)
    phone = mongo_models.CharField(max_length=12, unique=True)
    date = mongo_models.DateField(auto_now_add=True, unique=True)
    text = mongo_models.TextField(max_length=1024)

