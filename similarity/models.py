from django.db import models

# Create your models here.

class EntityTypes(models.Model):
    """
    Defines the kinds of entities to be examimed 
    """
    type_name = models.CharField(max_length=20,
                                 unique= True, 
                                 )
    source = models.ForeignKey("DataSources", 
                               on_delete=models.PROTECT, 
                               related_name="source",
                               unique= True
                               )
    fields = models.JSONField()
    formula = models.CharField(max_length=20)
    url_query_suffix = models.CharField(max_length=20)


class DataSources(models.Model):
    """
    External data sources, APIs
    """
    name = models.CharField(max_length=20,
                            unique=True, 
                            null=None, 
                            )
    base_url = models.URLField(max_length=20,
                               unique=True, 
                               null=False, 
                               )

class EntitiesConnections(models.Model):
    """
    Points relationships between fields on two different types of entities
    """
    entity_a = models.ForeignKey(EntityTypes, on_delete=models.RESTRICT, related_name="related_to")
    field_entity_a = models.CharField(max_length=20)
    entity_b = models.ForeignKey(EntityTypes, on_delete=models.RESTRICT)
    field_entity_b = models.CharField(max_length=20)
    relation = models.CharField(max_length=20)  ## to be converted into choices
