import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

type DashboardLayoutProps = {
  children: React.ReactNode;
};

export default function DashboardLayout({
  children,
}: DashboardLayoutProps) {
  return (
    <div className="flex min-h-screen bg-gray-100">
      <Sidebar />

      <main className="flex-1 p-8">

        <div className="max-w-7xl mx-auto">
          <Navbar />
          {children}
        </div>

      </main>
    </div>
  );
}