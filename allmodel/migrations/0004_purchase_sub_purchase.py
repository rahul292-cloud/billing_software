# Generated by Django 3.0.2 on 2020-04-09 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allmodel', '0003_delete_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('write_use_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('purchase_invoice', models.CharField(max_length=10)),
                ('purchase_date', models.DateTimeField(auto_now=True)),
                ('purchase_address', models.CharField(max_length=10)),
                ('reference_no', models.CharField(max_length=10)),
                ('Final_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allmodel.Client')),
                ('create_user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_allmodel_purchase_related', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_by_allmodel_purchase_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sub_purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('write_use_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('qty', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('product_name', models.CharField(blank=True, max_length=250, null=True)),
                ('product_code', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('create_user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_allmodel_sub_purchase_related', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allmodel.Product')),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allmodel.Purchase')),
                ('tax_per', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allmodel.Tax')),
                ('writer', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_by_allmodel_sub_purchase_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
