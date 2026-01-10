export default function AvailabilityBadge({ available, confidence }) {
  const color = available ? "#16a34a" : "#dc2626";

  return (
    <div style={{ color, fontWeight: "bold" }}>
      {available ? "🟢 Available" : "🔴 Out of Stock"}
      <div style={{ fontSize: 12 }}>
        Confidence: {(confidence * 100).toFixed(1)}%
      </div>
    </div>
  );
}
