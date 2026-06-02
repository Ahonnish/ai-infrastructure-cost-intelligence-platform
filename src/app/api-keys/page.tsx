import DashboardLayout from "@/components/DashboardLayout";
import ApiKeyCard from "@/components/ApiKeyCard";
import { apiKeys } from "@/data/apiKeys";


export default function ApiKeysPage() {
  return (
    <DashboardLayout>
      <h1 className="text-3xl font-bold mb-8">
        API Keys
      </h1>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {apiKeys.map((key) => (
          <ApiKeyCard
            key={key.provider}
            provider={key.provider}
            status={key.status}
            usage={key.usage}
            limit={key.limit}
            lastUsed={key.lastUsed}
            requests={key.requests}
            monthlySpend={key.monthlySpend}
          />
        ))}
      </div>
    </DashboardLayout>
  );
}