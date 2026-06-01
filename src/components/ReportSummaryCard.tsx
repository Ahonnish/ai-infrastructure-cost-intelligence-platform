type ReportSummaryCardProps = {
  title: string;
  value: string;
};

export default function ReportSummaryCard({
  title,
  value,
}: ReportSummaryCardProps) {
  return (
    <div className="bg-white rounded-2xl p-6 border shadow-sm">
      <p className="text-gray-500 mb-2">
        {title}
      </p>

      <h3 className="text-3xl font-bold">
        {value}
      </h3>
    </div>
  );
}