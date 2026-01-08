// frontend/src/components/Replacement.jsx
import React from "react";

export default function Replacement({ items = [] }) {
  return (
    <div className="card">
      <h3>🔁 Recommended Replacements</h3>

      {items.length === 0 ? (
        <p>No replacement suggestions yet.</p>
      ) : (
        <ol>
          {items.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ol>
      )}
    </div>
  );
}
