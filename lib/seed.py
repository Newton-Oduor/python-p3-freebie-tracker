#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie 

# Create Companies

facebook = Company(name="Facebook", founding_year=2001)
openAI = Company(name="OpenAI", founding_year=2005)
andela = Company(name="Andela", founding_year=1996)


# Create Devs

tom = Dev(name="Tom")
kevin = Dev(name="Kevin")
gitau = Dev(name="Gitau")


# Create Freebies

freebie1 = Freebie(
    item_name="Mouse Pad",
    value=15,
    company=openAI,
    dev=kevin
)

freebie2 = Freebie(
    item_name="T-Shirt",
    value=30,
    company=facebook,
    dev=gitau
)

freebie3 = Freebie(
    item_name="Coffee Mug",
    value=25,
    company=andela,
    dev=tom
)

freebie4 = Freebie(
    item_name="Gaming Set",
    value=300,
    company=openAI,
    dev=gitau
)

# Database connection

engine = create_engine('sqlite:///freebies.db')  
Session = sessionmaker(bind=engine)
session = Session()

# Save to database
session.add_all([
    facebook, openAI, andela,
    kevin, gitau, tom,
    freebie1, freebie2, freebie3, freebie4
])

session.commit()