from django.db import models

class Opportunity(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "newsletter_opportunity"
        verbose_name_plural = "Opportunities"
        ordering = ["-created_on"]
        indexes = [models.Index(fields=["email"], name="email_idx")]

    def __str__(self):
        return self.email
