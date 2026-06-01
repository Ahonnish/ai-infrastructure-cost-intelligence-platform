


type OptimizationRecommendation = {
  title: string;
  savings: string;
  description: string;
  priority: "High" | "Medium" | "Low";
};

export const optimizationRecommendations: OptimizationRecommendation[] = [
  {
    title: "Switch GPT-4o to GPT-4o-mini",
    savings: "$450/month",
    priority: "High",
    description:
      "Move non-critical requests to GPT-4o-mini."
  },
  {
    title: "Enable Redis Caching",
    savings: "$320/month",
    priority: "High",
    description:
      "Cache repeated prompts and responses."
  },
  {
    title: "Reduce Context Window",
    savings: "$140/month",
    priority: "Medium",
    description:
      "Trim unnecessary conversation history."
  },
  {
    title: "Batch Similar Requests",
    savings: "$180/month",
    priority: "Medium",
    description:
      "Group requests to reduce API overhead."
  }
];