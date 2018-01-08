from django.db import models
import uuid
from django.urls import reverse
from encrypted_model_fields.fields import EncryptedCharField


'''
Customer's model starts
'''

class Customer(models.Model):
    """
    Model representing a Customer.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    mode = models.ForeignKey('Mode', on_delete=models.SET_NULL, null=True, blank=True)
    vertical = models.ForeignKey('Vertical', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True)
    # time_zone TODO: to be added later
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        # return reverse('customers:details', args=[str(self.id)])
        return reverse('directory:update_customer', args=[str(self.id)])


class Mode(models.Model):
    # Required by Customers model
    # Stores customer delivery model - shared, hybrid, dedicated
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name


class Vertical(models.Model):
    # Required by Customers model
    # Stores customer vertical - BFSI, pharma, etc.
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name


class Location(models.Model):
    # Required by Customers model
    # Stores customer location, APAC, US, etc.
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name


'''
Assets model starts
'''


class AssetFunction(models.Model):
    # Required by Asset model
    # Stores Asset's function - firewall, proxy, SIEM, ITSM
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name



class AssetAttribute(models.Model):
    # Required by Asset model
    # Stores Asset's attributes - IP, URL, username
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name


class AssetActionOn(models.Model):
    # Required by AssetAction model
    # Stores subjects for the action - Block, run, fetch report, etc.
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Asset action on"

    def __str__(self):
        return '%s ' % self.name


class AssetAction(models.Model):
    # Required by Asset model
    # Stores action's supported by the Asset - Block, run, fetch report, etc.
    name = models.CharField(max_length=25, unique=True)
    action_on = models.ManyToManyField(AssetActionOn, blank=True) # Action block works on IP, URL, hostname

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name


class AssetType(models.Model):
    # Required by Asset model
    # Stores Asset's type - QRdadar, PaloAlto
    name = models.CharField(max_length=50, unique=True)

    assetFunction = models.ManyToManyField('AssetFunction', verbose_name="Which function does it play", )
    assetAttribute = models.ManyToManyField('AssetAttribute')
    assetAction = models.ManyToManyField('AssetAction')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s ' % self.name






class Asset(models.Model):
    """
    Model representing an Asset.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Asset Name", max_length=50)
    ipAddress = models.GenericIPAddressField("IP address", null=True, blank=True)
    port = models.CharField(max_length=50, null=True, blank=True)
    hostname = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    # https://github.com/lanshark/django-encrypted-model-fields
    password = EncryptedCharField(max_length=100, null=True, blank=True)
    accessKey = EncryptedCharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    assetType = models.ForeignKey('AssetType', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["name"]
        unique_together = ['name', 'customer']


    def __str__(self):
        return '%s ' % self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        # return reverse('customers:details', args=[str(self.id)])
        return reverse('directory:update_asset', args=[str(self.id)])
        pass



