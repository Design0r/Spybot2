# Generated by Django 4.1.7 on 2023-02-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spybot', '0010_alter_tsuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
