import React, { useState } from "react";
import { predictAvailability } from "../api";

function Availability({ product, onResult }) {
  const [sales, setSales] = useState(10);
  const [day, setDay] = useState(1);
  const [loading, setLoading] = useState(false);

  async function handleCheck() {
    if (!product || !product.name) {
      alert("Please select a product first");
      return;
    }

    setLoading(true);

    try {
      const result = await predictAvailability({
        name: product.name,
        sales: Number(sales),
        day: Number(day),
      });

      onResult(result);
    } catch (err) {
      alert("Error checking availability: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <h3>📦 Check Availability</h3>

      <label>Recent sales (units)</label>
      <input type="number" min="0" value={sales} onChange={(e) => setSales(e.target.value)} />

      <label>Day (1–7)</label>
      <input type="number" min="1" max="7" value={day} onChange={(e) => setDay(e.target.value)} />

      <button onClick={handleCheck} disabled={loading}>
        {loading ? "Checking..." : "Check Availability"}
      </button>
    </div>
  );
}

export default Availability;
