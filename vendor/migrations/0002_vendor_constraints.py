from django.db import migrations, models
from django.db.models import Q


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="vendor",
            constraint=models.CheckConstraint(
                condition=Q(delivery_rating__gte=1, delivery_rating__lte=5),
                name="vendor_delivery_rating_range",
            ),
        ),
        migrations.AddConstraint(
            model_name="vendor",
            constraint=models.CheckConstraint(
                condition=Q(quality_rating__gte=1, quality_rating__lte=5),
                name="vendor_quality_rating_range",
            ),
        ),
        migrations.AddConstraint(
            model_name="vendor",
            constraint=models.CheckConstraint(
                condition=Q(price_rating__gte=1, price_rating__lte=5),
                name="vendor_price_rating_range",
            ),
        ),
        migrations.AddConstraint(
            model_name="vendor",
            constraint=models.CheckConstraint(
                condition=Q(communication_rating__gte=1, communication_rating__lte=5),
                name="vendor_communication_rating_range",
            ),
        ),
    ]
