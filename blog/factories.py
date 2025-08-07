import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create()


class UseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.Faker("name")

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("passowrd, None")
        user = super(UseFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence")
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UseFactory)
    status = 0

    class Meta:
        model = Post

    def __str__(self):
        return self.title