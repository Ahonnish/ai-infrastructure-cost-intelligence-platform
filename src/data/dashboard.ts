export const dashboardMetrics = [
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


  export const optimizationSuggestions = [
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



export const recentActivities = [
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