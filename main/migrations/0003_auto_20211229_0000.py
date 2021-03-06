# Generated by Django 3.2.8 on 2021-12-28 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cap_created_cap_updated_alter_brand_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imege', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand')),
            ],
        ),
        migrations.RenameModel(
            old_name='Size',
            new_name='Category',
        ),
        migrations.DeleteModel(
            name='Cap',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]
