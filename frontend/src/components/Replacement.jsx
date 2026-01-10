// frontend/src/components/Replacement.jsx
import React from "react";

const Replacement = ({ items = [] }) => {
  return (
    <div className="card">
      <h3>🔁 Recommended Replacements</h3>

      {items.length === 0 ? (
        <p>No replacement suggestions yet.</p>
      ) : (
        <ol>
          {items.map((item, index) => (
            <li key={`${item}-${index}`}>{item}</li>
          ))}
        </ol>
      )}
    </div>
  );
};

export default Replacement;
