# #!/usr/bin/env python3

# from sqlalchemy import create_engine

# from models import Company, Dev

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///freebies.db')
#     import ipdb; ipdb.set_trace()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    
    # Create a session to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Test 1: Freebie.dev and Freebie.company
    print("\nTEST 1: Freebie Relationships")
    freebie = session.query(Freebie).first()
    print(f"Freebie.dev: {freebie.dev}")  # Should return Dev instance
    print(f"Freebie.company: {freebie.company}")  # Should return Company instance  

    # Test 2: Company.freebies and Company.devs
    print("\nTEST 2: Company Relationships")
    company = session.query(Company).first()
    print(f"Company: {company.name}")
    print(f"Company.freebies: {company.freebies}")  # Should return collection of Freebie instances
    print(f"Company.devs: {company.devs}")  # Should return collection of Dev instances


    
    import ipdb; ipdb.set_trace()