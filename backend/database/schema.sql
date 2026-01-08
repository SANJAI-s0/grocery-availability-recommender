-- backend/database/schema.sql
-- SQL schema for products, inventory_snapshots, replacement_logs

CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  sku VARCHAR(64) UNIQUE NOT NULL,
  name VARCHAR(256) NOT NULL,
  category VARCHAR(128),
  price NUMERIC,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS inventory_snapshots (
  id SERIAL PRIMARY KEY,
  product_id INTEGER REFERENCES products(id),
  store VARCHAR(128),
  stock_level INTEGER NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS replacement_logs (
  id SERIAL PRIMARY KEY,
  original_product_id INTEGER REFERENCES products(id),
  replacement_product_id INTEGER REFERENCES products(id),
  accepted BOOLEAN DEFAULT FALSE,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
