import os
from unicodedata import category
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


# import --> functions 
from faker import Faker 
import random
from products.models import Product , Brand ,Category

def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.png','4.jpg','5.png']
    
    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,4)]}"
        Brand.objects.create(
            name = name,
            image = image
        )
    print(f'Successfully Seeded {n} Brands')
        


def seed_category(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.png','4.jpg','5.png','6.png']
    
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0,5)]}"
        Category.objects.create(
            name = name,
            image = image
        )
    print(f'Successfully Seeded {n} Category')


def seed_products(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpeg']
    flag_type = ['New','Feature','Sale']
    
    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,100000)
        subtitle = fake.text(max_nb_chars=300)
        desc = fake.text(max_nb_chars=10000)
        flag =  flag_type[random.randint(0,2)]
        price = round(random.uniform(20.99,99.99),2)
        image = f"products/{images[random.randint(0,8)]}"
        category = Category.objects.get(id=random.randint(1,17))
        brand = Brand.objects.get(id=random.randint(1,10))
        
        Product.objects.create(
            name = name,
            sku = sku,
            subtitle = subtitle,
            desc = desc , 
            flag = flag ,
            price = price , 
            image = image,
            category = category , 
            brand = brand, 
            video_url = "https://youtu.be/JV_twMJbCik"
        )
    print(f'Successfully Seeded {n} Product')



# seed_brand(5)
# seed_category(10)
seed_products(1000)