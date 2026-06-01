const usageData = [
  {
    date: "2026-05-24",
    provider: "OpenAI",
    tokens: "120K",
    cost: "$42",
  },
  {
    date: "2026-05-25",
    provider: "Claude",
    tokens: "98K",
    cost: "$31",
  },
  {
    date: "2026-05-26",
    provider: "Gemini",
    tokens: "74K",
    cost: "$18",
  },
];

export default function UsageTable() {
  return (
    <div className="bg-white rounded-2xl p-6 border shadow-sm">
      <h3 className="text-xl font-semibold mb-4">
        Recent Usage Activity
      </h3>

      <table className="w-full">
        <thead>
          <tr className="border-b">
            <th className="text-left py-3">Date</th>
            <th className="text-left py-3">Provider</th>
            <th className="text-left py-3">Tokens</th>
            <th className="text-left py-3">Cost</th>
          </tr>
        </thead>

        <tbody>
          {usageData.map((item) => (
            <tr key={item.date + item.provider}>
              <td className="py-3">{item.date}</td>
              <td className="py-3">{item.provider}</td>
              <td className="py-3">{item.tokens}</td>
              <td className="py-3">{item.cost}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}