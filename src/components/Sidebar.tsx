"use client";

import { usePathname } from "next/navigation";
import Link from "next/link";


import {
  LayoutDashboard,
  BarChart3,
  KeyRound,
  FileText,
} from "lucide-react";


export default function Sidebar() {
  const pathname = usePathname();
  return (
    <aside className="w-64 min-h-screen bg-black text-white p-6">
      <h2 className="text-2xl font-bold mb-10">
        AI Cost IQ
      </h2>

      <nav className="flex flex-col gap-3">
        <Link
          href="/"
          className={`flex items-center gap-3 px-4 py-3 rounded-lg transition ${pathname === "/"
            ? "bg-white text-black font-medium"
            : "hover:bg-gray-800"
            }`}
        >
          <LayoutDashboard size={20} />
          <span>Dashboard</span>
        </Link>

        <Link
          href="/usage-analytics"
          className={`flex items-center gap-3 px-4 py-3 rounded-lg transition ${pathname === "/usage-analytics"
            ? "bg-white text-black font-medium"
            : "hover:bg-gray-800"
            }`}
        >
          <BarChart3 size={20} />
          <span>Usage Analytics</span>
        </Link>

        <Link
          href="/api-keys"
          className={`flex items-center gap-3 px-4 py-3 rounded-lg transition ${pathname === "/api-keys"
            ? "bg-white text-black font-medium"
            : "hover:bg-gray-800"
            }`}
        >
          <KeyRound size={20} />
          <span>API Keys</span>
        </Link>

        <Link
          href="/cost-reports"
          className={`flex items-center gap-3 px-4 py-3 rounded-lg transition ${pathname === "/cost-reports"
            ? "bg-white text-black font-medium"
            : "hover:bg-gray-800"
            }`}
        >
          <FileText size={20} />
          <span>Cost Reports</span>
        </Link>
      </nav>
    </aside>
  );
}