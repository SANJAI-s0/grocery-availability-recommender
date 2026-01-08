// frontend/src/components/ProductList.jsx
import React from "react";

/**
 * ProductList
 * products: array of { name, sku, category, price }
 * onSelect: function(name)
 */
export default function ProductList({ products = [], onSelect }) {
  return (
    <div className="card">
      <h3>🛒 Products</h3>

      {products.map((p) => (
        <div key={p.sku} className="product-item">
          <div>
            <div className="product-name">
              {p.name}
              <span className="category">{p.category}</span>
            </div>
            <div className="price">₹{p.price}</div>
          </div>

          <button onClick={() => onSelect(p.name)}>
            Suggest replacement
          </button>
        </div>
      ))}
    </div>
  );
}
