# Generated by Django 3.0.6 on 2020-07-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0006_realme_xiaomi'),
    ]

    operations = [
        migrations.CreateModel(
            name='xaiomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('categories', models.CharField(default='', max_length=60)),
                ('SubCategories', models.CharField(default='', max_length=60)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='image/mobile')),
            ],
        ),
        migrations.DeleteModel(
            name='xiaomi',
        ),
        migrations.RemoveField(
            model_name='realme',
            name='descirption',
        ),
        migrations.RemoveField(
            model_name='realme',
            name='prices',
        ),
        migrations.AlterField(
            model_name='realme',
            name='image',
            field=models.ImageField(default='', upload_to='image/mobile'),
        ),
        migrations.AlterField(
            model_name='realme',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
