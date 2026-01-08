# backend/database/db.py
# SQLAlchemy DB connection and ORM models
# Python 3.12 compatible

import os
import sys
import datetime

# ------------------------------------------------------------------
# FIX: Ensure backend/ is on Python path so `config.py` is found
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # points to backend/
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from config import DB_URL

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import OperationalError

# ------------------------------------------------------------------
# Engine and session
# ------------------------------------------------------------------
engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

Base = declarative_base()

# ------------------------------------------------------------------
# ORM Models
# ------------------------------------------------------------------
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(64), unique=True, nullable=False)
    name = Column(String(256), nullable=False)
    category = Column(String(128), nullable=True)
    price = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Product id={self.id} name={self.name}>"

class InventorySnapshot(Base):
    __tablename__ = "inventory_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    store = Column(String(128), nullable=True)
    stock_level = Column(Integer, nullable=False, default=0)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    product = relationship("Product", backref="snapshots")

    def __repr__(self):
        return (
            f"<InventorySnapshot product_id={self.product_id} "
            f"stock={self.stock_level}>"
        )

class ReplacementLog(Base):
    __tablename__ = "replacement_logs"

    id = Column(Integer, primary_key=True, index=True)
    original_product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    replacement_product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    accepted = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    original = relationship("Product", foreign_keys=[original_product_id])
    replacement = relationship("Product", foreign_keys=[replacement_product_id])

    def __repr__(self):
        return (
            f"<ReplacementLog {self.original_product_id} "
            f"-> {self.replacement_product_id}>"
        )

# ------------------------------------------------------------------
# DB Initialization
# ------------------------------------------------------------------
def create_tables():
    """
    Create database tables based on ORM models.
    Safe to run multiple times.
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created (or already exist).")
    except OperationalError as e:
        print("Database initialization failed:", e)

# ------------------------------------------------------------------
# Session helper (for Flask)
# ------------------------------------------------------------------
def get_db_session():
    """
    Generator that yields a SQLAlchemy session.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# ------------------------------------------------------------------
# Script entry point
# ------------------------------------------------------------------
if __name__ == "__main__":
    create_tables()
