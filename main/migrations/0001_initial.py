# Generated by Django 3.0.3 on 2020-02-15 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Initiator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Инициатор')),
            ],
            options={
                'verbose_name': 'Инициатор',
                'verbose_name_plural': 'Инициаторы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StatusContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TypeDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_contract', models.CharField(db_index=True, default='-', max_length=20, verbose_name='Номер контракта')),
                ('name_object', models.CharField(db_index=True, default='-', max_length=500, verbose_name='Наименование объекта закупки')),
                ('y_contract', models.CharField(default='1970', max_length=4, verbose_name='Год')),
                ('c_contract', models.FloatField(max_length=50, verbose_name='Цена контракта')),
                ('uch_contract', models.CharField(db_index=True, default='-', max_length=200, verbose_name='Участник')),
                ('in_contract', models.CharField(max_length=10, null=True, verbose_name='Дата подписания контракта')),
                ('in_work', models.CharField(max_length=10, null=True, verbose_name='Дата начала работ')),
                ('out_work', models.CharField(max_length=10, null=True, verbose_name='Дата окончания работ')),
                ('work_contract', models.BooleanField(verbose_name='В работе')),
                ('failures', models.BooleanField(verbose_name='Срыв сроков')),
                ('executed', models.BooleanField(verbose_name='Исполнен')),
                ('file_obj', models.FileField(upload_to='files/')),
                ('data_stamp', models.DateTimeField(auto_now_add=True)),
                ('ini_contract', models.ForeignKey(default='-', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Initiator', verbose_name='Инициатор')),
                ('stat_contract', models.ForeignKey(default='-', on_delete=django.db.models.deletion.DO_NOTHING, to='main.StatusContract', verbose_name='Статус')),
                ('type_doc', models.ForeignKey(default='-', on_delete=django.db.models.deletion.DO_NOTHING, to='main.TypeDoc', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Госконтракт',
                'verbose_name_plural': 'Госконтракты',
                'ordering': ('y_contract', 'num_contract'),
            },
        ),
    ]
