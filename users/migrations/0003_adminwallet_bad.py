# Generated by Django 4.0.4 on 2022-05-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_transaction_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminwallet',
            name='bad',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]