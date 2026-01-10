import { Line } from "react-chartjs-2";

export default function SalesChart({ sales, confidence }) {
  return (
    <Line
      data={{
        labels: ["Low", "Medium", "High"],
        datasets: [
          {
            label: "Availability Confidence",
            data: [confidence * 0.6, confidence * 0.8, confidence],
          },
        ],
      }}
    />
  );
}
