// frontend/src/api.js
// Simple API wrapper for calling backend endpoints

const API_BASE = process.env.REACT_APP_API_BASE || "http://localhost:5000/api";

export async function predictAvailability({ sales, day }) {
  const resp = await fetch(`${API_BASE}/predict-availability`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sales, day })
  });
  if (!resp.ok) {
    throw new Error("Failed to call predict availability");
  }
  const data = await resp.json();
  return data; // { available: true/false }
}

export async function getReplacements(itemName) {
  const resp = await fetch(`${API_BASE}/recommend`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ item: itemName })
  });
  if (!resp.ok) throw new Error("Failed to fetch replacements");
  const data = await resp.json();
  return data.replacements || [];
}
