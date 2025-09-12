#!/usr/bin/env python3

# Script to recreate database tables with updated schema
from ride_request_app.server.database import Base, engine
from ride_request_app.server import models

print("Dropping existing tables...")
Base.metadata.drop_all(bind=engine)

print("Creating new tables...")
Base.metadata.create_all(bind=engine)

print("✅ Database tables recreated successfully!")
print("New structure:")
print("- ride_requests: id, source, destination, status, driver_id")
print("- drivers: id, name, status")