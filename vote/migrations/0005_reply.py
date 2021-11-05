# Generated by Django 3.2.8 on 2021-11-03 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_choice_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replyer', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.topic')),
            ],
        ),
    ]
