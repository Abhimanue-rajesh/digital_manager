from django.db import models


class Creative(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="creatives/")
    posting_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=(
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ),
        default="pending",
    )
    rejection_reason = models.TextField(null=True, blank=True)
    stage_1_approval = models.BooleanField(default=False)
    stage_2_approval = models.BooleanField(default=False)
    final_approval = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.title
