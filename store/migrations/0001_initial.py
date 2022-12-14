# Generated by Django 4.1 on 2022-08-11 08:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('OrderNumber', models.IntegerField(unique=True)),
                ('TotalAmount', models.DecimalField(decimal_places=15, max_digits=30)),
                ('CustomerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=100)),
                ('ContractName', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Fax', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=100)),
                ('UnitPrice', models.DecimalField(decimal_places=15, max_digits=30)),
                ('SupplierId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnitPrice', models.DecimalField(decimal_places=15, max_digits=30)),
                ('Quantity', models.IntegerField()),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
