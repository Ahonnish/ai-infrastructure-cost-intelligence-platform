import DashboardLayout from "@/components/DashboardLayout";
import MetricCard from "@/components/MetricCard";

export default function Home() {
  return (
    <DashboardLayout>
      <h2 className="text-3xl font-bold mb-6">
        Dashboard
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard
          title="Total Token Usage"
          value="1.2M"
        />

        <MetricCard
          title="Estimated Cost"
          value="$842"
        />

        <MetricCard
          title="API Requests"
          value="18,420"
        />

        <MetricCard
          title="Active Models"
          value="6"
        />
      </div>
    </DashboardLayout>
  );
}