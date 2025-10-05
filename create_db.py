from database import Base, engine

# Tables create karna
Base.metadata.create_all(bind=engine)
print(" Tables created successfully!")
