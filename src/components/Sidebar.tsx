export default function Sidebar() {
  return (
    <aside className="w-64 border-r min-h-screen p-4">
      <h2 className="text-lg font-bold mb-6">
        Navigation
      </h2>

      <nav className="flex flex-col gap-4">
        <button className="text-left hover:text-blue-600">
          Dashboard
        </button>

        <button className="text-left hover:text-blue-600">
          Usage Analytics
        </button>

        <button className="text-left hover:text-blue-600">
          API Keys
        </button>

        <button className="text-left hover:text-blue-600">
          Cost Reports
        </button>
      </nav>
    </aside>
  );
}