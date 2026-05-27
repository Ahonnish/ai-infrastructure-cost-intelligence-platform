export default function Sidebar() {
  return (
    <aside className="w-64 min-h-screen bg-black text-white p-6">
      <h2 className="text-2xl font-bold mb-10">
        AI Cost IQ
      </h2>

      <nav className="flex flex-col gap-3">
        <button className="text-left px-4 py-3 rounded-lg bg-white text-black font-medium">
          Dashboard
        </button>

        <button className="text-left px-4 py-3 rounded-lg hover:bg-gray-800 transition">
          Usage Analytics
        </button>

        <button className="text-left px-4 py-3 rounded-lg hover:bg-gray-800 transition">
          API Keys
        </button>

        <button className="text-left px-4 py-3 rounded-lg hover:bg-gray-800 transition">
          Cost Reports
        </button>
      </nav>
    </aside>
  );
}