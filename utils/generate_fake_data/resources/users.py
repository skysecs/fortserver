from random import choice, sample
import forgery_py

from .base import FakeDataGenerator

from users.models import *


class UserGroupGenerator(FakeDataGenerator):
    resource = 'usergroup'

    def do_generate(self, batch, batch_size):
        groups = []
        for i in batch:
            group_name = forgery_py.name.job_title()
            groups.append(UserGroup(name=group_name, org_id=self.org.id))
        UserGroup.objects.bulk_create(groups, ignore_conflicts=True)


class UserGenerator(FakeDataGenerator):
    resource = 'user'
    roles: list
    group_ids: list

    def pre_generate(self):
        self.group_ids = list(UserGroup.objects.all().values_list('id', flat=True))

    def set_groups(self, users):
        relations = []
        for i in users:
            groups_to_join = sample(self.group_ids, 3)
            _relations = [User.groups.through(user_id=i.id, usergroup_id=gid) for gid in groups_to_join]
            relations.extend(_relations)
        User.groups.through.objects.bulk_create(relations, ignore_conflicts=True)

    def do_generate(self, batch, batch_size):
        users = []
        for i in batch:
            username = forgery_py.internet.user_name(True) + '-' + str(i)
            email = forgery_py.internet.email_address()
            u = User(
                username=username,
                email=email,
                name=username.title(),
                created_by='Faker'
            )
            users.append(u)
        users = User.objects.bulk_create(users, ignore_conflicts=True)
        self.set_groups(users)
