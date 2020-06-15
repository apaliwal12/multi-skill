# Generated by Django 3.0.7 on 2020-06-15 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminview', '0002_auto_20200615_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('question', models.CharField(max_length=500)),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('option_3', models.CharField(max_length=100)),
                ('option_4', models.CharField(max_length=100)),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.TestHeader')),
            ],
        ),
    ]
