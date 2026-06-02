import DashboardLayout from "@/components/DashboardLayout";
import ReportSummaryCard from "@/components/ReportSummaryCard";
import ProviderUsageChart from "@/components/ProviderUsageChart";
import {
  reportMetrics,
  providerCosts,
} from "@/data/reports";


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
        <h2 className="text-xl font-semibold mb-4">
          Cost Breakdown by Provider
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {providerCosts.map((provider) => (
            <div
              key={provider.provider}
              className="bg-white border rounded-2xl p-5 shadow-sm"
            >
              <h3 className="font-semibold text-lg">
                {provider.provider}
              </h3>

              <p className="text-sm text-gray-500 mt-2">
                Current Spend
              </p>

              <p className="text-2xl font-bold mt-3">
                {provider.cost}
              </p>
            </div>
          ))}
        </div>
      </div>

      <div className="mt-10">
        <ProviderUsageChart />
      </div>
    </DashboardLayout>
  );
}