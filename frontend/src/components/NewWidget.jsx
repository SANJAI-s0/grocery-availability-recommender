// frontend/src/components/NewWidget.jsx
import React from "react";

/**
 * NewWidget
 * A reusable dashboard widget for summary / status display.
 *
 * Props:
 * - title: string
 * - value: string | number
 * - description: string (optional)
 */
export default function NewWidget({ title, value, description }) {
  return (
    <div className="widget-card">
      <h4 className="widget-title">{title}</h4>
      <div className="widget-value">{value}</div>
      {description && <p className="widget-desc">{description}</p>}
    </div>
  );
}
