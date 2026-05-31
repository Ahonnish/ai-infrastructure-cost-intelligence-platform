type SectionCardProps = {
  title: string;
  children: React.ReactNode;
};

export default function SectionCard({
  title,
  children,
}: SectionCardProps) {
  return (
    <div className="bg-white rounded-2xl p-6 border shadow-sm">
      <h3 className="text-xl font-semibold mb-4">
        {title}
      </h3>

      {children}
    </div>
  );
}