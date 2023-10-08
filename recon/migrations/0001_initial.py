# Generated by Django 4.2.5 on 2023-10-08 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReconciliationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, db_column='DATE_TIME', null=True)),
                ('recon_id', models.CharField(blank=True, db_column='RECON_ID', max_length=35, null=True)),
                ('bank_id', models.CharField(blank=True, db_column='BANK_ID', max_length=15, null=True)),
                ('user_id', models.CharField(blank=True, db_column='USER_ID', max_length=35, null=True)),
                ('rq_date_range', models.CharField(blank=True, db_column='RQ_DATE_RANGE', max_length=255, null=True)),
                ('upld_rws', models.CharField(blank=True, db_column='UPLD_RWS', max_length=15, null=True)),
                ('rq_rws', models.CharField(blank=True, db_column='RQ_RWS', max_length=15, null=True)),
                ('recon_rws', models.CharField(blank=True, db_column='RECON_RWS', max_length=15, null=True)),
                ('unrecon_rws', models.CharField(blank=True, db_column='UNRECON_RWS', max_length=15, null=True)),
                ('excep_rws', models.CharField(blank=True, db_column='EXCEP_RWS', max_length=15, null=True)),
                ('feedback', models.TextField(blank=True, db_column='FEEDBACK', null=True)),
            ],
            options={
                'db_table': 'Reconciliationlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('swift_code', models.CharField(max_length=10, unique=True)),
                ('bank_code', models.CharField(max_length=10, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBankMapping',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recon.bank')),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploaded_files')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('tran_date', models.DateTimeField(blank=True, null=True)),
                ('trn_ref', models.CharField(blank=True, max_length=255, null=True)),
                ('batch', models.CharField(blank=True, max_length=255, null=True)),
                ('acquirer_code', models.CharField(blank=True, max_length=255, null=True)),
                ('issuer_code', models.CharField(blank=True, max_length=255, null=True)),
                ('excep_flag', models.CharField(blank=True, max_length=6, null=True)),
                ('acq_flg', models.CharField(blank=True, max_length=6, null=True)),
                ('iss_flg', models.CharField(blank=True, max_length=6, null=True)),
                ('acq_flg_date', models.DateTimeField(blank=True, null=True)),
                ('iss_flg_date', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]