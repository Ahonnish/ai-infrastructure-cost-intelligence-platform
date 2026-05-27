type MetricCardProps = {
  title: string;
  value: string;
};

export default function MetricCard({
  title,
  value,
}: MetricCardProps) {
  return (
    <div className="bg-white rounded-2xl p-6 shadow-sm border hover:shadow-md transition">
      <h3 className="text-sm text-gray-500 mb-3">
        {title}
      </h3>

      <p className="text-4xl font-bold text-black">
        {value}
      </p>
    </div>
  );
}