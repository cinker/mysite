# Generated by Django 2.0.3 on 2018-03-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
