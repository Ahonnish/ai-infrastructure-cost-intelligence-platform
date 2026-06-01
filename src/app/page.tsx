import DashboardLayout from "@/components/DashboardLayout";
import MetricCard from "@/components/MetricCard";
import SectionCard from "@/components/SectionCard";
import OptimizationCard from "@/components/OptimizationCard";
import ActivityItem from "@/components/ActivityItem";
import UsageChart from "@/components/UsageChart";
import ProviderUsageChart from "@/components/ProviderUsageChart";


import {
  dashboardMetrics,
  optimizationSuggestions,
  recentActivities,
} from "@/data/dashboard";

export default function Home() {


  return (
    <DashboardLayout>
      <h2 className="text-3xl font-bold mb-6">
        Dashboard
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {dashboardMetrics.map((metric) => (
          <MetricCard
            key={metric.title}
            title={metric.title}
            value={metric.value}
          />
        ))}
      </div>

      <div className="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <SectionCard title="Cost Optimization Suggestions">
          <div className="space-y-4">

            {optimizationSuggestions.map((suggestion) => (
              <OptimizationCard
                key={suggestion.title}
                title={suggestion.title}
                description={suggestion.description}
              />
            ))}

          </div>

        </SectionCard>

        <SectionCard title="Recent API Activity">
          <div className="space-y-4">
            {recentActivities.map((activity) => (
              <ActivityItem
                key={activity.model}
                model={activity.model}
                cost={activity.cost}
              />
            ))}
          </div>
        </SectionCard>
      </div>

      <div className="mt-10">
        <UsageChart />
      </div>

      <div className="mt-10">
        <ProviderUsageChart />
      </div>
    </DashboardLayout>
  );
}