import DashboardLayout from "@/components/DashboardLayout";
import ReportSummaryCard from "@/components/ReportSummaryCard";
import ProviderUsageChart from "@/components/ProviderUsageChart";
import { reportMetrics } from "@/data/reports";

export default function CostReportsPage() {
  return (
    <DashboardLayout>
      <h1 className="text-3xl font-bold mb-8">
        Cost Reports
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {reportMetrics.map((report) => (
          <ReportSummaryCard
            key={report.title}
            title={report.title}
            value={report.value}
          />
        ))}
      </div>

      <div className="mt-8">
        <button className="bg-black text-white px-5 py-3 rounded-xl hover:opacity-90">
          Export Report
        </button>
      </div>

      <div className="mt-10">
        <ProviderUsageChart />
      </div>
    </DashboardLayout>
  );
}