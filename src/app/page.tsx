import DashboardLayout from "@/components/DashboardLayout";
import MetricCard from "@/components/MetricCard";
import SectionCard from "@/components/SectionCard";
import OptimizationCard from "@/components/OptimizationCard";
import ActivityItem from "@/components/ActivityItem";
import UsageChart from "@/components/UsageChart";
import ProviderUsageChart from "@/components/ProviderUsageChart";

export default function Home() {

  const metrics = [
    {
      title: "Total Token Usage",
      value: "1.2M",
    },
    {
      title: "Estimated Cost",
      value: "$842",
    },
    {
      title: "API Requests",
      value: "18,420",
    },
    {
      title: "Active Models",
      value: "6",
    },
  ];

  const suggestions = [
    {
      title: "Switch embedding model",
      description:
        "You are using GPT-4 for embeddings. Switching to text-embedding-3-small can reduce embedding costs by 85%.",
    },
    {
      title: "Reduce unused API calls",
      description:
        "18% of requests returned empty responses. Consider adding response caching.",
    },
  ];

  const activities = [
    {
      model: "OpenAI GPT-4",
      cost: "$124",
    },
    {
      model: "Claude Sonnet",
      cost: "$92",
    },
    {
      model: "Embedding Requests",
      cost: "$41",
    },
  ];


  return (
    <DashboardLayout>
      <h2 className="text-3xl font-bold mb-6">
        Dashboard
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {metrics.map((metric) => (
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

            {suggestions.map((suggestion) => (
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
            {activities.map((activity) => (
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