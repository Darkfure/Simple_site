# Generated by Django 4.2 on 2023-04-07 11:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_upload',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]