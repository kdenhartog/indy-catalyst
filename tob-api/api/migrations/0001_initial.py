# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InactiveClaimReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('shortReason', models.CharField(blank=True, max_length=255, null=True)),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('effectiveDate', models.DateField()),
                ('expirationDate', models.DateField(blank=True, null=True)),
                ('displayOrder', models.IntegerField()),
            ],
            options={
                'db_table': 'INACTIVE_CLAIM_REASON',
            },
        ),
        migrations.CreateModel(
            name='IssuerOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('issuerOrgTLA', models.CharField(max_length=255)),
                ('issuerOrgURL', models.CharField(blank=True, max_length=255, null=True)),
                ('DID', models.CharField(max_length=255)),
                ('effectiveDate', models.DateField()),
                ('expirationDate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ISSUER_ORG',
            },
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('jurisdictionAbbrv', models.CharField(max_length=25)),
                ('jurisdictionName', models.CharField(max_length=1000)),
                ('displayOrder', models.IntegerField()),
                ('isOnCommonList', models.BooleanField()),
                ('effectiveDate', models.DateField()),
                ('expirationDate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'JURISDICTION',
            },
        ),
        migrations.CreateModel(
            name='VerifiedOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('busId', models.CharField(max_length=255)),
                ('LegalName', models.CharField(max_length=255)),
                ('effectiveDate', models.DateField()),
                ('endDate', models.DateField(blank=True, null=True)),
                ('jurisdictionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VerifiedOrgjurisdictionId', to='api.Jurisdiction')),
            ],
            options={
                'db_table': 'VERIFIED_ORG',
            },
        ),
        migrations.CreateModel(
            name='VOClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('claimJSON', models.CharField(max_length=255)),
                ('effectiveDate', models.DateField()),
                ('endDate', models.DateField()),
                ('inactiveClaimReasonId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VOClaiminactiveClaimReasonId', to='api.InactiveClaimReason')),
                ('verifiedOrgId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VOClaimverifiedOrgId', to='api.VerifiedOrg')),
            ],
            options={
                'db_table': 'V_O_CLAIM',
            },
        ),
        migrations.CreateModel(
            name='VOClaimType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('theType', models.CharField(max_length=255)),
                ('base64Logo', models.CharField(blank=True, max_length=255, null=True)),
                ('issuerURL', models.CharField(max_length=255)),
                ('claimSchemaDefinition', models.CharField(max_length=255)),
                ('issuerOrgId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VOClaimTypeissuerOrgId', to='api.IssuerOrg')),
            ],
            options={
                'db_table': 'V_O_CLAIM_TYPE',
            },
        ),
        migrations.CreateModel(
            name='VODoingBusinessAs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('DBA', models.CharField(max_length=255)),
                ('effectiveDate', models.DateField()),
                ('endDate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'V_O_DOING_BUSINESS_AS',
            },
        ),
        migrations.CreateModel(
            name='VOLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('Addressee', models.CharField(blank=True, max_length=255, null=True)),
                ('AddlDeliveryInfo', models.CharField(blank=True, max_length=255, null=True)),
                ('unitNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('streetAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('municipality', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('latLong', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'V_O_LOCATION',
            },
        ),
        migrations.CreateModel(
            name='VOLocationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('theType', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('effectiveDate', models.DateField()),
                ('expirationDate', models.DateField(blank=True, null=True)),
                ('displayOrder', models.IntegerField()),
            ],
            options={
                'db_table': 'V_O_LOCATION_TYPE',
            },
        ),
        migrations.CreateModel(
            name='VOType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('theType', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('effectiveDate', models.DateField()),
                ('expirationDate', models.DateField(blank=True, null=True)),
                ('displayOrder', models.IntegerField()),
            ],
            options={
                'db_table': 'V_O_TYPE',
            },
        ),
        migrations.AddField(
            model_name='volocation',
            name='voLocationTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VOLocationvoLocationTypeId', to='api.VOLocationType'),
        ),
        migrations.AddField(
            model_name='voclaim',
            name='voClaimType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VOClaimvoClaimType', to='api.VOClaimType'),
        ),
        migrations.AddField(
            model_name='verifiedorg',
            name='orgType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VerifiedOrgorgType', to='api.VOType'),
        ),
        migrations.AddField(
            model_name='verifiedorg',
            name='primaryLocation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VerifiedOrgprimaryLocation', to='api.VOLocation'),
        ),
        migrations.AddField(
            model_name='issuerorg',
            name='jurisdictionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IssuerOrgjurisdictionId', to='api.Jurisdiction'),
        ),
    ]
