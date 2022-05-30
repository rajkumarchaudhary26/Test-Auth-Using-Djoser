import uuid
from django.db import models
import datetime
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.urls import reverse
from .managers import CustomUserManager
from .constants import USER_TYPES
from staff.models import Language
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
#Year choices

def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year

class GenderChoice(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'

AWARD_TYPES = (
    ('Advertising Award', 'Advertising Award'),
    ('Movie/Drama Award', 'Movie/Drama Award'),
    ('MV Award', 'MV Award'),
    ('Other awards', 'Other awards'),
)


class Award(models.Model):
    name = models.CharField(_("Name"), max_length=500)
    type = models.CharField(choices=AWARD_TYPES, max_length=255, default=AWARD_TYPES[1][0])
    year = models.IntegerField(
        _('year'), choices=year_choices(), default=current_year())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Award_detail", kwargs={"pk": self.pk})

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(choices=USER_TYPES, max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('Joined Date'), auto_now_add=True)

    # authenticate using email instead of the default username
    USERNAME_FIELD = 'email'
    # USERNAME_FIELD, i.e. email along with password are required by default
    REQUIRED_FIELDS = []

    # CustomUserManager manager manages this user model
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})

# Profile model consists a foreign key to User, which is a custom user model (AbstractBaseUser).
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    family_name_in_kanji = models.CharField(_("Family Name in Kanji"), max_length=255, null=True)
    first_name_in_kanji = models.CharField(_("First Name in Kanji"), max_length=255, null=True)
    family_name_in_hiragana = models.CharField(_("Family Name in Hiragana"), max_length=255, null=True)
    first_name_in_hiragana = models.CharField(_("First Name in Hiragana"), max_length=255, null=True)
    family_name_in_english = models.CharField(_("Family Name in English"), max_length=255, null=True)
    first_name_in_english = models.CharField(_("First Name in English"), max_length=255, null=True)
    date_of_birth = models.DateField(_("Date of Birth"), null=True)
    gender = models.CharField(_("Gender"), max_length=10, choices=GenderChoice.choices, null=True)
    profile_pic = VersatileImageField(_("Profile Picture"), upload_to="profile_pic/", ppoi_field = 'profile_picture_ppoi',  null = True, blank = True)
    profile_picture_ppoi = PPOIField()
    birth_city = models.CharField(_("Birth City"), max_length=255, null=True, blank=True)
    current_city = models.CharField(_("Current City"), max_length=255, null=True, blank=True)
    language = models.ManyToManyField(Language, verbose_name=_("Language"), related_name="language_profiles", null=True, blank=True)
    company = models.CharField(_("Company"), max_length=255, null=True, blank=True)
    working_as = models.CharField(_("Working As"), max_length=255, null=True, blank=True)
    position = models.CharField(_("Position"), max_length=255, null=True)
    is_upgraded = models.BooleanField(_("Upgraded"), default=False)
    full_address = models.CharField(_("Full Address"), max_length=255, blank=True, null=True)
    manager_name = models.CharField(_("Manager Name"), max_length=255, null=True, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=16, null=True, blank=True)
    employee = models.CharField(max_length=255, null=True)
    bio = models.TextField(_("Detail"), null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    award = models.ManyToManyField(to = Award, related_name = 'award_profiles', blank = True, null=True)
    verified = models.BooleanField(default=False)
    number_of_login = models.PositiveIntegerField(_("Number of Login"), null = True, blank = True, default = 0)
    password_changed_date = models.DateTimeField(
        _("Password Changed Date"), null=True, blank=True)
    information_agree = models.BooleanField(_("Terms and Conditions"), default=False)

    def __str__(self):
        return str(self.user)
  
class ProfileShare(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_shares')
    passcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email

class BillingDetail(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=500)
    last_name = models.CharField(_("Last Name"), max_length=500)
    company = models.CharField(_("Company"), max_length=500)
    mobile_number = models.CharField(_("Mobile Number"), max_length=500)
    vat_gst_number = models.CharField(_("Vat/Gst Number"), max_length=100)
    city = models.CharField(_("City"), max_length=500)
    state = models.CharField(_("State"), max_length=500)
    country = models.CharField(_("Country"), max_length=100)
    zip_code = models.IntegerField(_("Zip Code"))

    class Meta:
        verbose_name = _("BillingDetail")
        verbose_name_plural = _("BillingDetails")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("BillingDetail_detail", kwargs={"pk": self.pk})