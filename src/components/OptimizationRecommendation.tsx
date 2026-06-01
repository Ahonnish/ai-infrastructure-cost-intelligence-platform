
type OptimizationRecommendationProps = {
  title: string;
  savings: string;
  description: string;
  priority: "High" | "Medium" | "Low";
};

export default function OptimizationRecommendation({
  title,
  savings,
  description,
  priority,
}: OptimizationRecommendationProps) {

  const priorityStyles = {
    High: "bg-red-100 text-red-700",
    Medium: "bg-yellow-100 text-yellow-700",
    Low: "bg-green-100 text-green-700",
  };



  return (
    <div className="bg-white border rounded-2xl p-5 shadow-sm">
      <div className="flex justify-between items-start">
        <h3 className="font-semibold text-lg">
          {title}
        </h3>

        <div className="flex gap-2">
          <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
            Save {savings}
          </span>

          <span
            className={`${priorityStyles[priority]} px-3 py-1 rounded-full text-sm`}
          >
            {priority}
          </span>
        </div>
      </div>

      <p className="text-gray-600 mt-3">
        {description}
      </p>
    </div>
  );
}