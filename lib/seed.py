#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie 

# Create Companies

google = Company(name="Google", founding_year=2001)
bing = Company(name="Bing", founding_year=2005)
microsoft = Company(name="Microsoft", founding_year=1996)


# Create Devs

tom = Dev(name="Tom")
kevin = Dev(name="Kevin")
gitau = Dev(name="Gitau")


# Create Freebies

freebie1 = Freebie(
    item_name="Laptop Bag",
    value=200,
    company=bing,
    dev=kevin
)

freebie2 = Freebie(
    item_name="Sweater",
    value=150,
    company=google,
    dev=gitau
)

freebie3 = Freebie(
    item_name="Software",
    value=350,
    company=microsoft,
    dev=tom
)

freebie4 = Freebie(
    item_name="Energy drink",
    value=50,
    company=bing,
    dev=gitau
)

# Database connection

engine = create_engine('sqlite:///freebies.db')  
Session = sessionmaker(bind=engine)
session = Session()

# Save to database
session.add_all([
    google, bing, microsoft,
    kevin, gitau, tom,
    freebie1, freebie2, freebie3, freebie4
])

session.commit()