from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Language(models.Model):
    name = models.CharField(_("Name"), max_length=500)

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Language_detail", kwargs={"pk": self.pk})