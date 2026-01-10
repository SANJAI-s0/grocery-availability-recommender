// frontend/src/components/ProductList.jsx
import React from "react";

/**
 * ProductList
 * props:
 * - products: array of { id, name, sales?, day?, available? }
 * - onSelect: function(product)
 */
export default function ProductList({ products = [], onSelect }) {
  if (!products || products.length === 0) {
    return <div style={{ padding: 12, color: "#64748b" }}>No products available for this domain.</div>;
  }

  return (
    <div>
      {products.map((p) => (
        <div key={p.id || p.name} className="product-item" style={{ alignItems: "center" }}>
          <div style={{ flex: 1 }}>
            <div className="product-name">
              {p.name}{" "}
              {p.available !== undefined && (
                <span style={{ marginLeft: 8, fontSize: 12, color: p.available ? "#16a34a" : "#dc2626" }}>
                  {p.available ? "In stock" : "Out"}
                </span>
              )}
            </div>
            <div style={{ color: "#0ea5a4", fontWeight: 600 }}>
              {p.sales !== undefined ? `Sales: ${p.sales}` : ""}
              {p.day !== undefined ? `  •  Day: ${p.day}` : ""}
            </div>
          </div>

          <div style={{ marginLeft: 12 }}>
            <button onClick={() => onSelect(p)}>Suggest replacement</button>
          </div>
        </div>
      ))}
    </div>
  );
}
