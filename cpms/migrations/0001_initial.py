# Generated by Django 4.2 on 2023-09-18 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Callm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type_id', models.CharField(max_length=100)),
                ('message_id', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('payload', models.TextField()),
                ('charger_id', models.CharField(default='', max_length=100)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('direction', models.CharField(blank=True, choices=[('C2S', 'Client to Server'), ('S2C', 'Server to Client')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ChargingStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Charging_Station_Name', models.CharField(default='', max_length=200)),
                ('Address', models.CharField(default='', max_length=200)),
                ('City', models.CharField(default='', max_length=200)),
                ('Zip_Code', models.IntegerField(null=True)),
                ('State', models.CharField(default='', max_length=200)),
                ('Country', models.CharField(default='', max_length=200)),
                ('station_type', models.CharField(default='', max_length=100)),
                ('open', models.CharField(default='', max_length=100)),
                ('Phone_Number', models.CharField(default='', max_length=200)),
                ('Socket_URL', models.CharField(default='', max_length=200)),
                ('Charging_Point_Name', models.CharField(default='', max_length=200)),
                ('Charging_Point_ID', models.CharField(default='', max_length=200)),
                ('Connector_Type', models.CharField(default='', max_length=200)),
                ('Charging_Power', models.CharField(default='', max_length=200)),
                ('EV_Compatible', models.CharField(default='', max_length=200)),
                ('Cost_per_Unit', models.CharField(default='', max_length=200)),
                ('LICENSE', models.CharField(default='', max_length=200)),
                ('Change_Availability', models.CharField(default='', max_length=200)),
                ('Online_Status', models.CharField(default='', max_length=200)),
                ('Connectors', models.CharField(default='', max_length=200)),
                ('Food_Drink', models.CharField(max_length=200)),
                ('Things_to_Do', models.CharField(max_length=200)),
                ('Shopping', models.CharField(max_length=200)),
                ('Services', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20)),
                ('otp', models.CharField(max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CallResultm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type_id', models.IntegerField()),
                ('message_id', models.CharField(max_length=36)),
                ('payload', models.TextField()),
                ('charger_id', models.CharField(default='', max_length=100)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('direction', models.CharField(blank=True, choices=[('C2S', 'Client to Server'), ('S2C', 'Server to Client')], max_length=3)),
                ('call_obj', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpms.callm')),
            ],
        ),
        migrations.AddField(
            model_name='callm',
            name='call_result_obj',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpms.callresultm'),
        ),
        migrations.CreateModel(
            name='Addmoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=0, max_length=100, null=True)),
                ('final_amount', models.FloatField(blank=True, default=0, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
