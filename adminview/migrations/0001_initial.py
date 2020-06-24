# Generated by Django 3.0.7 on 2020-06-24 16:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=7)),
                ('mobile', models.CharField(max_length=12)),
                ('doj', models.DateField(auto_now_add=True)),
                ('language_preference', models.CharField(default='English', max_length=200)),
                ('is_admin', models.BooleanField(default=True)),
                ('weekly_off', models.CharField(max_length=100)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(default='Some Admin', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ResultHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_obtained', models.FloatField()),
                ('total_marks', models.FloatField()),
                ('status', models.CharField(max_length=4)),
                ('test_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=50)),
                ('skill_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=50)),
                ('current_manpower', models.IntegerField(default=0)),
                ('required_manpower', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_title', models.CharField(max_length=200)),
                ('no_of_questions', models.IntegerField()),
                ('test_time', models.IntegerField()),
                ('max_marks', models.IntegerField()),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Stage')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Station')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainee', models.CharField(max_length=50)),
                ('token', models.IntegerField(default=0)),
                ('training_stage', models.IntegerField(default=0)),
                ('date', models.DateTimeField(blank=True)),
                ('shift_officer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='training_shift_officer', to='adminview.Employee')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Stage')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='training_trainer', to='adminview.Employee')),
            ],
        ),
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
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.TestHeader')),
            ],
        ),
        migrations.CreateModel(
            name='ResultQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.TestQuestions')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.ResultHeader')),
            ],
        ),
        migrations.AddField(
            model_name='resultheader',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.TestHeader'),
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquired_on', models.DateField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Employee')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Stage')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Shift'),
        ),
        migrations.AddField(
            model_name='employee',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminview.Station'),
        ),
    ]
