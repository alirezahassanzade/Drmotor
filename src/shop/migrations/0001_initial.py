# Generated by Django 2.1.5 on 2019-07-01 07:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'Open'), (20, 'Submitted')], default=10)),
            ],
        ),
        migrations.CreateModel(
            name='BasketLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Commentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('family', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'New'), (20, 'Paid'), (30, 'Done')], default=10)),
                ('billing_name', models.CharField(max_length=60)),
                ('billing_address1', models.CharField(max_length=60)),
                ('billing_address2', models.CharField(blank=True, max_length=60)),
                ('billing_zip_code', models.CharField(max_length=12)),
                ('billing_city', models.CharField(max_length=60)),
                ('billing_country', models.CharField(max_length=3)),
                ('shipping_name', models.CharField(max_length=60)),
                ('shipping_address1', models.CharField(max_length=60)),
                ('shipping_address2', models.CharField(blank=True, max_length=60)),
                ('shipping_zip_code', models.CharField(max_length=12)),
                ('shipping_city', models.CharField(max_length=60)),
                ('shipping_country', models.CharField(max_length=3)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'New'), (20, 'Processing'), (30, 'Sent'), (40, 'Cancelled')], default=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=3, max_digits=13)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('vote', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('in_stock', models.BooleanField(default=True)),
                ('stock_count', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(blank=True, to='shop.Category')),
                ('colors', models.ManyToManyField(to='shop.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discount_value', models.DecimalField(decimal_places=3, max_digits=13)),
                ('discount_type', models.IntegerField(choices=[(10, 'Percent'), (20, 'Fixed')], default=10, verbose_name='Sales Type')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('catrgories', models.ManyToManyField(to='shop.Category')),
                ('products', models.ManyToManyField(to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('discount_value', models.DecimalField(decimal_places=3, max_digits=13)),
                ('discount_type', models.IntegerField(choices=[(10, 'Percent'), (20, 'Fixed')], default=10, verbose_name='Sales Type')),
                ('usage_limit', models.IntegerField(verbose_name='Maximum number of times that the code can be used.')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shop.Tag'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.Product'),
        ),
    ]
