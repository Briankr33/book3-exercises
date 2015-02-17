# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20141007_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unpaidusers',
            name='last_notification',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 1, 5, 11, 92926)),
        ),
        migrations.AlterField(
            model_name='user',
            name='bigCoID',
            field=models.CharField(max_length=50),
        ),
    ]