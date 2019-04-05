# Generated by Django 2.1.7 on 2019-04-02 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0027_credentialhook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='hook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credential_subscription', to='api_v2.CredentialHook'),
        ),
    ]