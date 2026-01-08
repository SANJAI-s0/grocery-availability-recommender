// frontend/src/App.js
import React, { useState, useEffect } from "react";
import "./styles/App.css";

import Availability from "./components/Availability";
import ProductList from "./components/ProductList";
import Replacement from "./components/Replacement";
import NewWidget from "./components/NewWidget";

import { predictAvailability, getReplacements } from "./api";

const SAMPLE_PRODUCTS = [
  { sku: "SKU001", name: "Whole Milk", category: "Dairy", price: 2.5 },
  { sku: "SKU002", name: "Skim Milk", category: "Dairy", price: 2.4 },
  { sku: "SKU003", name: "Almond Milk", category: "Dairy", price: 3.0 },
  { sku: "SKU004", name: "Brown Bread", category: "Bakery", price: 1.8 },
  { sku: "SKU005", name: "White Bread", category: "Bakery", price: 1.5 }
];

function App() {
  const [availabilityResult, setAvailabilityResult] = useState(null);
  const [replacements, setReplacements] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);

  useEffect(() => {
    setReplacements([]);
  }, [selectedProduct]);

  async function onAvailabilityResult(res) {
    setAvailabilityResult(res);
  }

  async function onSuggest(productName) {
    setSelectedProduct(productName);
    try {
      const recs = await getReplacements(productName);
      setReplacements(recs);
    } catch (err) {
      alert("Error: " + err.message);
    }
  }

  return (
    <div className="app-root">
      <h1>Grocery Availability Recommender</h1>

      {/* Dashboard widgets */}
      <div className="widget-grid">
        <NewWidget
          title="Selected Product"
          value={selectedProduct || "None"}
          description="Product currently under analysis"
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
          description="Predicted by ML model"
        />
        <NewWidget
          title="Replacement Count"
          value={replacements.length}
          description="Suggested alternatives"
        />
      </div>

      <div className="container">
        <div>
          <ProductList
            products={SAMPLE_PRODUCTS}
            onSelect={(name) => onSuggest(name)}
          />
          <Availability onResult={onAvailabilityResult} />
        </div>

        <div>
          <Replacement items={replacements} />
          <div className="debug-card">
            <h4>Raw Availability Output</h4>
            <pre>{JSON.stringify(availabilityResult, null, 2)}</pre>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
