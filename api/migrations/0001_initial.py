# Generated by Django 2.2.1 on 2019-08-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor', models.CharField(max_length=70, null=True)),
                ('name', models.CharField(default='Не указано название', max_length=70)),
                ('discipline', models.CharField(max_length=70, null=True)),
                ('long_description', models.TextField(null=True)),
                ('price', models.CharField(default='Бесплатно', max_length=20)),
                ('currency', models.CharField(default='null', max_length=10, null=True)),
                ('organization', models.CharField(default='Частный преподаватель', max_length=40)),
                ('key_words', models.CharField(default='auto', max_length=200)),
                ('modules', models.CharField(default='auto', max_length=200)),
                ('modules_number', models.CharField(max_length=10, null=True)),
                ('modules_type', models.CharField(max_length=50, null=True)),
                ('avg_length', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(default='auto', null=True)),
                ('schema', models.TextField(null=True)),
                ('education_type', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(default=0, null=True)),
                ('code', models.IntegerField(default=0)),
                ('terms', models.CharField(max_length=200, null=True)),
                ('test', models.BooleanField(default=False)),
                ('amount_restrictions', models.BooleanField(default=False, null=True)),
                ('level_counts', models.BooleanField(default=False, null=True)),
                ('teachers_present', models.BooleanField(default=False, null=True)),
                ('tutors_present', models.BooleanField(default=False, null=True)),
                ('facilitators_present', models.BooleanField(default=False, null=True)),
                ('feedback', models.BooleanField(default=False, null=True)),
                ('co_ed', models.BooleanField(default=False, null=True)),
                ('practice', models.BooleanField(default=False, null=True)),
                ('forums', models.BooleanField(default=False, null=True)),
                ('individualization', models.BooleanField(default=False, null=True)),
                ('disabled', models.BooleanField(default=False, null=True)),
                ('webinars', models.BooleanField(default=False, null=True)),
                ('analytics', models.BooleanField(default=False, null=True)),
                ('deadlines', models.BooleanField(default=False, null=True)),
                ('post_entrance', models.BooleanField(default=False, null=True)),
                ('training_materials', models.CharField(max_length=200, null=True)),
                ('browsers', models.CharField(max_length=200, null=True)),
                ('technologies', models.CharField(max_length=200, null=True)),
                ('requsites', models.CharField(max_length=200, null=True)),
                ('payment', models.CharField(default='auto', max_length=200)),
                ('os_list', models.CharField(max_length=200, null=True)),
                ('tools', models.CharField(max_length=200, null=True)),
                ('peripherals', models.CharField(max_length=200, null=True)),
                ('authors', models.CharField(default='Не указан автор', max_length=200, null=True)),
                ('author_degree', models.CharField(max_length=200, null=True)),
                ('author_awards', models.CharField(max_length=200, null=True)),
                ('author_position', models.CharField(max_length=200, null=True)),
                ('valued_work', models.CharField(max_length=5, null=True)),
                ('certification', models.BooleanField(default=False, null=True)),
                ('language', models.CharField(default='Не указан язык обучения', max_length=20, null=True)),
                ('org_link', models.URLField(default='AUTO', null=True)),
                ('start_date', models.CharField(max_length=30, null=True)),
                ('end_date', models.CharField(max_length=30, null=True)),
                ('length', models.CharField(default='auto', max_length=100)),
                ('sync', models.CharField(default='auto', max_length=100)),
                ('assessmet', models.CharField(max_length=100, null=True)),
                ('lms', models.CharField(default='auto', max_length=100)),
                ('course_id', models.CharField(max_length=100, null=True, unique=True)),
                ('prerequesetes', models.CharField(default='auto', max_length=100)),
                ('image', models.URLField(null=True)),
                ('video', models.URLField(null=True)),
                ('interests', models.CharField(default='auto', max_length=100)),
                ('skills', models.CharField(default='auto', max_length=100)),
                ('ways', models.CharField(default='auto', max_length=100)),
            ],
        ),
    ]
