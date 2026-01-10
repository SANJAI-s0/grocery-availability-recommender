import React, { useEffect, useState } from "react";
import "./styles/App.css";

import Availability from "./components/Availability";
import ProductList from "./components/ProductList";
import Replacement from "./components/Replacement";
import NewWidget from "./components/NewWidget";
import AvailabilityBadge from "./components/AvailabilityBadge";
import SalesChart from "./components/SalesChart";

import {
  fetchProducts,
  getReplacements,
  fetchDomains,
} from "./api";

function App() {
  const [domains, setDomains] = useState([]);
  const [domain, setDomain] = useState("grocery");

  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);

  const [availabilityResult, setAvailabilityResult] = useState(null);
  const [replacements, setReplacements] = useState([]);

  const [loadingProducts, setLoadingProducts] = useState(false);

  /* -------------------------------------------------
     Load domains (once)
  -------------------------------------------------- */
  useEffect(() => {
    fetchDomains()
      .then((d) => {
        setDomains(d);
        if (d.length > 0 && !d.includes(domain)) {
          setDomain(d[0]);
        }
      })
      .catch(() => {
        setDomains(["grocery"]);
      });
  }, []); // eslint-disable-line

  /* -------------------------------------------------
     Load products when domain changes
  -------------------------------------------------- */
  useEffect(() => {
    if (!domain) return;

    setLoadingProducts(true);
    fetchProducts(domain)
      .then((rows) => {
        setProducts(rows);
        setSelectedProduct(null);
        setAvailabilityResult(null);
        setReplacements([]);
      })
      .catch(() => {
        setProducts([]);
      })
      .finally(() => setLoadingProducts(false));
  }, [domain]);

  /* -------------------------------------------------
     When a product is selected
  -------------------------------------------------- */
  async function handleSelect(product) {
    setSelectedProduct(product);
    setAvailabilityResult(null);
    setReplacements([]);

    try {
      const recs = await getReplacements({
        name: product.name,
        domain,
      });
      setReplacements(recs);
    } catch (err) {
      console.warn("Replacement error:", err);
    }
  }

  return (
    <div className="app-root">
      {/* ---------------- HEADER ---------------- */}
      <header
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 20,
        }}
      >
        <h1>Availability Recommender</h1>

        <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
          <label style={{ fontSize: 14 }}>Domain</label>
          <select
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
          >
            {domains.map((d) => (
              <option key={d} value={d}>
                {d}
              </option>
            ))}
          </select>
        </div>
      </header>

      {/* ---------------- KPI WIDGETS ---------------- */}
      <div className="widget-grid">
        <NewWidget
          title="Selected Product"
          value={selectedProduct ? selectedProduct.name : "None"}
          description="Product under analysis"
        />

        <NewWidget
          title="Availability"
          value={
            availabilityResult
              ? availabilityResult.available
                ? "Available"
                : "Out of Stock"
              : "Not Checked"
          }
          description="ML prediction"
        />

        <NewWidget
          title="Confidence"
          value={
            availabilityResult
              ? `${Math.round(availabilityResult.confidence * 100)}%`
              : "-"
          }
          description="Model certainty"
        />

        <NewWidget
          title="Replacement Count"
          value={replacements.length}
          description="Suggested alternatives"
        />
      </div>

      {/* ---------------- MAIN CONTENT ---------------- */}
      <div className="container">
        {/* LEFT COLUMN */}
        <div>
          <div className="card">
            <h3>🛒 Products</h3>
            {loadingProducts ? (
              <p>Loading products...</p>
            ) : (
              <ProductList
                products={products}
                onSelect={handleSelect}
              />
            )}
          </div>

          <div className="card">
            <Availability
              product={selectedProduct}
              domain={domain}
              onResult={setAvailabilityResult}
            />
          </div>
        </div>

        {/* RIGHT COLUMN */}
        <div>
          <div className="card">
            <Replacement items={replacements} />
          </div>

          {availabilityResult && (
            <div className="card">
              <AvailabilityBadge
                available={availabilityResult.available}
                confidence={availabilityResult.confidence}
              />
            </div>
          )}

          {availabilityResult && (
            <div className="card">
              <h4>📊 Sales vs Availability</h4>
              <SalesChart
                sales={selectedProduct?.sales || 0}
                confidence={availabilityResult.confidence}
              />
            </div>
          )}

          <div className="card debug-card">
            <h4>Raw Availability Output</h4>
            <pre style={{ fontSize: 13 }}>
              {availabilityResult
                ? JSON.stringify(availabilityResult, null, 2)
                : "null"}
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
