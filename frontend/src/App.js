// frontend/src/App.js
import React, { useState, useEffect } from "react";
import "./styles/App.css";
import Availability from "./components/Availability";
import ProductList from "./components/ProductList";
import Replacement from "./components/Replacement";
import { getReplacements } from "./api";

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

  async function onSuggest(productName) {
    setSelectedProduct(productName);
    try {
      const recs = await getReplacements(productName);
      setReplacements(recs);
    } catch (err) {
      alert("Error fetching replacements: " + err.message);
    }
  }

  return (
    <div>
      <h1>Grocery Availability Recommender</h1>

      <div className="container">
        <div>
          <ProductList
            products={SAMPLE_PRODUCTS}
            onSelect={onSuggest}
          />

          <Availability onResult={setAvailabilityResult} />
        </div>

        <div>
          <Replacement items={replacements} />

          <div className="card">
            <h4>📊 Availability Result</h4>
            <pre>{JSON.stringify(availabilityResult, null, 2)}</pre>

            <h4>🧾 Selected Product</h4>
            <p>{selectedProduct || "None"}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
