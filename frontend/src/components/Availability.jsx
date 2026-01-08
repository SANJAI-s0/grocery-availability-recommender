// frontend/src/components/Availability.jsx
import React, { useState } from "react";
import { predictAvailability } from "../api";

export default function Availability({ onResult }) {
  const [sales, setSales] = useState(10);
  const [day, setDay] = useState(1);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function handleCheck(e) {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await predictAvailability({
        sales: Number(sales),
        day: Number(day)
      });
      setResult(res);
      onResult(res);
    } catch (err) {
      alert("Error checking availability: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <h3>📦 Check Availability</h3>

      <form onSubmit={handleCheck}>
        <label>
          Recent sales (units)
          <input
            type="number"
            min="0"
            value={sales}
            onChange={(e) => setSales(e.target.value)}
          />
        </label>

        <label>
          Day (1–7)
          <input
            type="number"
            min="1"
            max="7"
            value={day}
            onChange={(e) => setDay(e.target.value)}
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? "Checking..." : "Check"}
        </button>
      </form>

      {result && (
        <p className={result.available ? "status-ok" : "status-bad"}>
          {result.available
            ? "✔ Item is likely available"
            : "✖ Item may be out of stock"}
        </p>
      )}
    </div>
  );
}
