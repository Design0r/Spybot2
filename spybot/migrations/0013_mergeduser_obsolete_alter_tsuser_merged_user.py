# Generated by Django 4.1.7 on 2023-07-02 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spybot', '0012_mergeduser_tsuser_merged_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mergeduser',
            name='obsolete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tsuser',
            name='merged_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tsusers', to='spybot.mergeduser'),
        ),
    ]
