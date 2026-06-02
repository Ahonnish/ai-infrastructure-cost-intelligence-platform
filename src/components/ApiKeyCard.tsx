type ApiKeyCardProps = {
  provider: string;
  status: string;
  usage: string;
  limit: string;
  lastUsed: string;
  requests: string;
  monthlySpend: string;
};

export default function ApiKeyCard({
  provider,
  status,
  usage,
  limit,
  lastUsed,
  requests,
  monthlySpend,
}: ApiKeyCardProps) {
  return (
    <div className="bg-white rounded-2xl p-6 border shadow-sm">
      <div className="flex justify-between items-center mb-4">
        <h3 className="font-semibold text-lg">
          {provider}
        </h3>

        <span
          className={`px-3 py-1 rounded-full text-sm ${status === "Active"
            ? "bg-green-100 text-green-700"
            : "bg-red-100 text-red-700"
            }`}
        >
          {status}
        </span>
      </div>

      <p className="text-gray-600">
        Usage: {usage}
      </p>

      <p className="text-gray-600 mt-2">
        Monthly Limit: {limit}
      </p>

      <p className="text-gray-600 mt-2">
        Last Used: {lastUsed}
      </p>

      <p className="text-gray-600 mt-2">
        Requests: {requests}
      </p>

      <p className="text-gray-600 mt-2">
        Monthly Spend: {monthlySpend}
      </p>
    </div>
  );
}