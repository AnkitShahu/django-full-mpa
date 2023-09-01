from django import forms

class MyForm(forms.Form):
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
    
    new_pas = forms.ChoiceField( label='Are you a New Patient ?', choices=NP_CHOICES, widget=forms.RadioSelect)
    name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Number',}))
    phone = forms.CharField(max_length=20, label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    offi_loc = forms.ChoiceField( label='Office Location', choices=OL_CHOICES, widget=forms.RadioSelect)
    
    sel_pro = forms.ChoiceField( label='Select Provider', choices=SP_CHOICES, widget=forms.RadioSelect)
    Avail_date = forms.DateField(label='Available Date', widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    
    # forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)
    Av_date_best_time = forms.ChoiceField( label='Best Time', choices=BD_CHOICES, widget=forms.RadioSelect)
    Alter_date = forms.CharField(label='Alternate Date', widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    Al_date_best_time = forms.ChoiceField( label='Best Time', choices=BD_CHOICES, widget=forms.RadioSelect)
    
    #dob = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    select_insu =  forms.ChoiceField( label='Select Insurance Type', choices=SIT_CHOICES, widget=forms.RadioSelect)
   
    # Insurance Member ID
    # Insurance Group ID
    insu_mem_id = forms.CharField(max_length=20, label='Insurance Member ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
    insu_grp_id = forms.CharField(max_length=20, label='Insurance Group ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
   # favorite_color = forms.ChoiceField( label='Your Name', choices=COLOR_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    message = forms.CharField( label='Any other Information? - Please DO NOT inculde your SSN # / Medical Issues / Refill Requests', widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    how_did_you =  forms.ChoiceField( label='How did you hear about us?', choices=HDY_CHOICES, widget=forms.RadioSelect)