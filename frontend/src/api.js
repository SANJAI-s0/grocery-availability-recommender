const API_BASE =
  process.env.REACT_APP_API_BASE || "http://localhost:5000/api";

/* -----------------------------
   Domains
------------------------------ */
export async function fetchDomains() {
  const res = await fetch(`${API_BASE}/domains`);
  if (!res.ok) {
    throw new Error("Failed to load domains");
  }
  return res.json();
}

/* -----------------------------
   Products (DOMAIN AWARE)
------------------------------ */
export async function fetchProducts(domain) {
  if (!domain) {
    throw new Error("Domain is required");
  }

  const res = await fetch(`${API_BASE}/products?domain=${domain}`);

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.error || "Failed to load products");
  }

  return res.json();
}

/* -----------------------------
   Availability Prediction
------------------------------ */
export async function predictAvailability({ domain, name, sales, day }) {
  if (!domain || !name) {
    throw new Error("Domain and product name are required");
  }

  const res = await fetch(`${API_BASE}/predict-availability`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      domain,
      name,
      sales,
      day,
    }),
  });

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.error || "Prediction failed");
  }

  return res.json();
}

/* -----------------------------
   Replacement Recommendation
------------------------------ */
export async function getReplacements(domain, productName) {
  if (!domain || !productName) {
    throw new Error("Domain and product name are required");
  }

  const res = await fetch(`${API_BASE}/recommend`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      domain,
      name: productName,
    }),
  });

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.error || "Replacement fetch failed");
  }

  const data = await res.json();
  return data.replacements || [];
}
