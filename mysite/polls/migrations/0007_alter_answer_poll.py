# Generated by Django 3.2.5 on 2021-09-26 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_add_poll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.poll'),
        ),
    ]