"use client";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

const data = [
  {
    provider: "OpenAI",
    cost: 420,
  },
  {
    provider: "Claude",
    cost: 280,
  },
  {
    provider: "Gemini",
    cost: 190,
  },
  {
    provider: "Mistral",
    cost: 120,
  },
];

export default function ProviderUsageChart() {
  return (
    <div className="bg-white rounded-2xl p-6 border shadow-sm">
      <h3 className="text-xl font-semibold mb-6">
        AI Provider Cost Comparison
      </h3>

      <div className="w-full h-[320px] min-w-0">
        <ResponsiveContainer width="99%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="provider" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="cost"
              radius={[8, 8, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}