import {
  Bell,
  Search,
} from "lucide-react";

export default function Navbar() {
  return (
    <header className="bg-white border border-gray-200 rounded-2xl px-6 py-4 shadow-sm mb-8">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4 w-full max-w-md">
          <div className="relative w-full">
            <Search
              size={18}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
            />

            <input
              type="text"
              placeholder="Search analytics..."
              className="w-full border rounded-xl pl-10 pr-4 py-2 outline-none focus:ring-2 focus:ring-black"
            />
          </div>
        </div>

        <div className="flex items-center gap-5 ml-6">
          <button className="relative">
            <Bell size={22} />

            <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-red-500 rounded-full"></span>
          </button>

          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-black text-white flex items-center justify-center font-semibold">
              A
            </div>

            <div className="hidden md:block">
              <p className="font-medium text-sm">
                Ahonnis
              </p>

              <p className="text-xs text-gray-500">
                Admin
              </p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}