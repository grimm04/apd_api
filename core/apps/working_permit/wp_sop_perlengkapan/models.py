from django.db import models 
from apps.working_permit.wp_online.models import WP_ONLINE


class WPSOPPerlengkapan(models.Model):  
    id_wp_sop_perlengkapan = models.AutoField(primary_key=True)  
    id_wp_online = models.ForeignKey(
        WP_ONLINE, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='sop_perlengkapan',
        db_column='id_wp_online'
    )   
    id_sop = models.IntegerField(default=None, null=True,blank=True)
    pelindung1 = models.BooleanField(default=False)
    pelindung2 = models.BooleanField(default=False)
    pelindung3 = models.BooleanField(default=False)
    pelindung4 = models.BooleanField(default=False)
    pelindung5 = models.BooleanField(default=False)
    pelindung6 = models.BooleanField(default=False)
    pelindung7 = models.BooleanField(default=False)
    pelindung8 = models.BooleanField(default=False)
    pelindung9 = models.BooleanField(default=False)
    pelindung10 = models.BooleanField(default=False)
    pelindung11 = models.BooleanField(default=False)
    pelindung12 = models.BooleanField(default=False)
    perlengkapan1 = models.BooleanField(default=False)
    perlengkapan2 = models.BooleanField(default=False)
    perlengkapan3 = models.BooleanField(default=False)
    perlengkapan4 = models.BooleanField(default=False)
    perlengkapan5 = models.BooleanField(default=False)
 

    class Meta:
        managed = False
        db_table = 'wp_sop_perlengkapan'

    def __str__(self):
        return self.id_wp_sop_perlengkapan 
