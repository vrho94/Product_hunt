from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField(max_length=200)
    pub_date=models.DateTimeField()
    votes_total=models.IntegerField(default=1)
    image=models.ImageField(upload_to='products_images/')
    icon=models.ImageField(upload_to='products_icons/')
    body=models.TextField()
    #hunter-gre za uporabika ki je našel in naložil izdelek. Išče se po ForeignKey-u
    #on_delete pa določa kaj se zgodi s tem če je uporabnik odstranjen. CASCADE pa pomeni da z uporabnikom oddidejo vsi izdelki v tem primeru
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    #uporabljen za spremembo imena objekta v pythonu:
    def __str__(self):
        return self.title
    #okrajšan body ze preview(100 znakov):
    def summary(self):
        return self.body[:100]+"..."#vrne prvih 100 znakov
    #popravljena oblika časa za prikaz:
    def pub_date_modded(self):
        return self.pub_date.strftime(' %e. %b  %Y')
