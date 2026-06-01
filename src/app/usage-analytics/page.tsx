import DashboardLayout from "@/components/DashboardLayout";
import UsageMetricCard from "@/components/UsageMetricCard";
import UsageChart from "@/components/UsageChart";
import ProviderUsageChart from "@/components/ProviderUsageChart";
import UsageTable from "@/components/UsageTable";
import { usageMetrics } from "@/data/analytics";

export default function UsageAnalyticsPage() {
  return (
    <DashboardLayout>
      <h1 className="text-3xl font-bold mb-8">
        Usage Analytics
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {usageMetrics.map((metric) => (
          <UsageMetricCard
            key={metric.title}
            title={metric.title}
            value={metric.value}
          />
        ))}
      </div>

      <div className="mt-10">
        <UsageChart />
      </div>

      <div className="mt-10">
        <ProviderUsageChart />
      </div>

      <div className="mt-10">
        <UsageTable />
      </div>

    </DashboardLayout>
  );
}