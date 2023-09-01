from django.db import models

class MyFormsmodel(models.Model):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]

    NP_CHOICES=[
        ('Yes', "Yes"),
        ('No',"No")
    ]

    OL_CHOICES=[
        ('Downtown - 1040 SW 2nd Ave, Ocala FL 34471',"Downtown - 1040 SW 2nd Ave, Ocala FL 34471"),
        ('Ocala West - 10230 SW 86th Circle, Ocala FL 34481', "Ocala West - 10230 SW 86th Circle, Ocala FL 34481")

    ]

    SP_CHOICES = [
        ('Ram Vasudevan, MD, FACC, FACP, FCCP, ...', "Ram Vasudevan, MD, FACC, FACP, FCCP, ..."),
        ('Punwattie Ramnaraine, FNP-BC',"Punwattie Ramnaraine, FNP-BC"),
        ('Alceha Mayne-Thomas, ARNP',"Alceha Mayne-Thomas, ARNP"),
        ('Junaina Dominic, PA-C',"Junaina Dominic, PA-C"),
        ('Emily Hawkins, APRN, NP-C',"Emily Hawkins, APRN, NP-C"),
        ('Amreen Noorani, ARNP',"Amreen Noorani, ARNP"),
    ]

    SIT_CHOICES =[
        ("No Insurance","No Insurance"),
        ("Other Insurance","Other Insurance"),
        ("Aetna","Aetna"),
        ("Anthem","Anthem"),
        ("Blue Cross Blue Sheld","Blue Cross Blue Sheld"),
        ("Care Plus","Care Plus"),
        ("Cigna","Cigna"),
        ("Humana","Humana"),
        ("Medicaid","Medicaid"),
        ("Medicare","Medicare"),
        ("UnitedHealth Care","UnitedHealth Care"),
    ]

    HDY_CHOICES =[
        ("Insurance Provider","Insurance Provider"),
        ("Google","Google"),
        ("Bing","Bing"),
        ("Yahoo","Yahoo"),
        ("Yelp","Yelp"),
        ("Healthgrades","Healthgrades"),
        ("Friend / Collegue","Friend / Collegue"),
        ("Local Advertisement","Local Advertisement"),
        ("Other","Other"),
    ]

    BD_CHOICES = [        
        (' 8 AM - 10 AM', " 8 AM - 10 AM"),
        ('10 AM - 12 Noon',"10 AM - 12 Noon"),
        (' 12 Noon - 2 PM'," 12 Noon - 2 PM"),
        (' 2 PM - 4 PM'," 2 PM - 4 PM"),
    ]

    new_pas = models.CharField(max_length=3, choices=NP_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    offi_loc = models.CharField(max_length=100, choices=OL_CHOICES)

    sel_pro = models.CharField(max_length=100, choices=SP_CHOICES)
    Avail_date = models.DateField()
    Av_date_best_time = models.CharField(max_length=20, choices=BD_CHOICES)
    Alter_date = models.DateField()
    Al_date_best_time = models.CharField(max_length=20, choices=BD_CHOICES)

    select_insu = models.CharField(max_length=100, choices=SIT_CHOICES)

    insu_mem_id = models.CharField(max_length=20)
    insu_grp_id = models.CharField(max_length=20)
    
    message = models.TextField()
    how_did_you = models.CharField(max_length=100, choices=HDY_CHOICES)
    
    def __str__(self):
        return self.name

