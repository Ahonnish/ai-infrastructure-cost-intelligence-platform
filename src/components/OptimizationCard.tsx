type OptimizationCardProps = {
  title: string;
  description: string;
};

export default function OptimizationCard({
  title,
  description,
}: OptimizationCardProps) {
  return (
    <div className="border rounded-xl p-4">
      <p className="font-medium">
        {title}
      </p>

      <p className="text-sm text-gray-600 mt-1">
        {description}
      </p>
    </div>
  );
}