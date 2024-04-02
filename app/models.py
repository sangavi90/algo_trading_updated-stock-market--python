from django.db import models
from django.utils import timezone 

import uuid

import uuid

def generate_uuid_pattern():
    """
    Generate a UUID pattern with the first three characters as alphabetic characters and the remaining characters as numeric.

    Returns:
        str: UUID pattern with the first three characters as alphabetic characters and the remaining characters as numeric.
    """
    # Generate a UUID
    uuid_pattern = str(uuid.uuid4())

    # Extract alphanumeric characters only
    uuid_pattern = ''.join(filter(str.isalnum, uuid_pattern))
    
    # Get the first three characters of the UUID and convert them to uppercase
    first_three_chars = uuid_pattern[:3].upper()

    # Get the remaining characters and convert them to numeric
    remaining_chars = ''.join(filter(str.isdigit, uuid_pattern))

    return first_three_chars + remaining_chars

# # Example usage:
# uuid_pattern = generate_uuid_pattern()
# print("UUID Pattern:", uuid_pattern)
import uuid

def strategy_uuid_pattern():
    """
    Generate a UUID pattern with the first four characters as alphabetic characters and the remaining characters as numeric.

    Returns:
        str: UUID pattern with the first four characters as alphabetic characters and the remaining characters as numeric.
    """
    # Generate a UUID
    uuid_pattern = str(uuid.uuid4())

    # Extract alphanumeric characters only
    uuid_pattern = ''.join(filter(str.isalnum, uuid_pattern))
    
    # Get the first four characters of the UUID and convert them to uppercase
    first_four_chars = uuid_pattern[:4].upper()

    # Get the remaining characters and convert them to numeric
    remaining_chars = ''.join(filter(str.isdigit, uuid_pattern))

    return first_four_chars + remaining_chars

def strategy_uuid():
    return 'STA'+str(uuid.uuid4().hex)[:7].upper()

# Example usage
# print(generate_uuid_pattern())





class company_name(models.Model):
    company_name=models.CharField(max_length=200)

    def __str__(self):
        return self.company_name
    
class options(models.Model):
    company_name=models.ForeignKey(company_name,on_delete=models.CASCADE)    
    ce=models.TextField()
    pe=models.TextField()

    def __str__(self):
        return self.company_name.company_name
    
class expirystrikeprice(models.Model):
    company_name=models.ForeignKey(company_name,on_delete=models.CASCADE)
    ce=models.TextField()
    pe=models.TextField()

    def __str__(self):
        return self.company_name.company_name    

class SignInUser(models.Model):
    user_id=models.CharField(max_length=100,default=generate_uuid_pattern())
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self): 
        
        return self.username    
    
class Strategy(models.Model):
    user_id=models.ForeignKey(SignInUser,on_delete=models.CASCADE,blank=True,null=True)
    strategy_id=models.CharField(max_length=100,default=strategy_uuid,unique=True)
    strategy_name=models.CharField(max_length=100)
    status = models.CharField(max_length=50,blank=True, null=True)
    datetime=models.DateTimeField(default=timezone.localtime)
    def __str__(self):
        if self.user_id:
                return str(self.strategy_id)  # Assuming user_id is the field representing the user's ID in SignInUser model
        else:
                return "No user assigned"  
    

class Leg(models.Model):
    id = models.AutoField(primary_key=True)

    strategy_name=models.ForeignKey(Strategy,on_delete=models.CASCADE) 
    name = models.CharField(max_length=255, blank=True, null=True)
    segments = models.CharField(max_length=255, blank=True, null=True)
    optiontype = models.CharField(max_length=255, blank=True, null=True)
    variety = models.CharField(max_length=255, blank=True, null=True)
    tradingsymbol = models.CharField(max_length=255, blank=True, null=True)
    symboltoken = models.CharField(max_length=255, blank=True, null=True)
    transactiontype = models.CharField(max_length=255, blank=True, null=True)
    exchange = models.CharField(max_length=255, blank=True, null=True)
    ordertype = models.CharField(max_length=255, blank=True, null=True)
    producttype = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    stoploss = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    triggerprice = models.CharField(max_length=255, blank=True, null=True)
    expirydate = models.CharField(max_length=255, blank=True, null=True)
    strikeprice = models.CharField(max_length=255, blank=True, null=True)
    totallot = models.IntegerField(blank=True, null=True)
    trailingstoploss = models.CharField(max_length=255, blank=True, null=True)
    #Below fields are to store the Response Data of leg after placing order
    orderid=models.CharField(max_length=255, blank=True, null=True),
    uniqueorderid=models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
         return self.strategy_name.strategy_id

def generate_uuid_pattern():
    """
    Generate a UUID pattern with the first three characters as alphabetic characters and the remaining characters as numeric.

    Returns:
        str: UUID pattern with the first three characters as alphabetic characters and the remaining characters as numeric.
    """
    # Generate a UUID
    uuid_pattern = str(uuid.uuid4())

    # Extract alphanumeric characters only
    uuid_pattern = ''.join(filter(str.isalnum, uuid_pattern))
    
    # Get the first three characters of the UUID and convert them to uppercase
    first_three_chars = uuid_pattern[:3].upper()

    # Get the remaining characters and convert them to numeric
    remaining_chars = ''.join(filter(str.isdigit, uuid_pattern))

    return first_three_chars + remaining_chars

