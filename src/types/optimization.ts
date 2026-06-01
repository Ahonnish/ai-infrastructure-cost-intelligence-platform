export type OptimizationRecommendation = {
  title: string;
  savings: string;
  description: string;
  priority: "High" | "Medium" | "Low";
};