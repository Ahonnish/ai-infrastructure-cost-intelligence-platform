import DashboardLayout from "@/components/DashboardLayout";
import OptimizationRecommendation from "@/components/OptimizationRecommendation";
import { optimizationRecommendations } from "@/data/optimization";

export default function OptimizationPage() {
  return (
    <DashboardLayout>
      <h1 className="text-3xl font-bold mb-8">
        Optimization Center
      </h1>

      <div className="space-y-6">
        {optimizationRecommendations.map((recommendation) => (
          <OptimizationRecommendation 
          key={recommendation.title}
            {...recommendation}
          />
        ))}
      </div>
    </DashboardLayout>
  );
}