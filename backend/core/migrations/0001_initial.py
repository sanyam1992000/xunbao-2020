# Generated by Django 3.0.3 on 2020-03-12 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HappyHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=2000)),
                ('hint', models.CharField(max_length=1000)),
                ('no', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['no'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=70, null=True)),
                ('pic', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('score', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
                ('submission_count', models.IntegerField(default=0)),
                ('fid', models.SlugField(default=None, max_length=100, unique=True)),
            ],
            options={
                'ordering': ['-score', '-level', 'submission_count'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('fid', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('answer', models.CharField(max_length=100)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Correct', 'Correct'), ('Wrong', 'Wrong')], default='Wrong', max_length=10)),
                ('hintviewed', models.BooleanField(default=False)),
                ('ques', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Question')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='HintModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('hintviewed', models.BooleanField(default=True)),
                ('ques', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Question')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Question')),
            ],
        ),
    ]
