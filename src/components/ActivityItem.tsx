type ActivityItemProps = {
  model: string;
  cost: string;
};

export default function ActivityItem({
  model,
  cost,
}: ActivityItemProps) {
  return (
    <div className="flex items-center justify-between border-b pb-3 last:border-none">
      <span>{model}</span>

      <span className="text-sm text-gray-500">
        {cost}
      </span>
    </div>
  );
}