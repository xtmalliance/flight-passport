# Generated by Django 3.2.3 on 2021-05-31 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authprofiles', '0009_auto_20210322_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='passportapplication',
            name='algorithm',
            field=models.CharField(blank=True, choices=[('', 'No OIDC support'), ('RS256', 'RSA with SHA-2 256'), ('HS256', 'HMAC with SHA-2 256')], default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='passportapplication',
            name='authorization_grant_type',
            field=models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials'), ('openid-hybrid', 'OpenID connect hybrid')], max_length=32),
        ),
    ]