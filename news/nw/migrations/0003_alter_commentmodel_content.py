# Generated by Django 5.0 on 2023-12-25 17:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nw', '0002_remove_commentmodel_updated_at_starmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
    ]
