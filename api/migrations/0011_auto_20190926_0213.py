# Generated by Django 2.2.4 on 2019-09-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_course_preview_text_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='image',
            new_name='anons_image',
        ),
        migrations.AddField(
            model_name='course',
            name='detail_image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='mnemocode',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]