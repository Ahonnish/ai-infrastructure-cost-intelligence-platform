import Sidebar from "@/components/Sidebar";

export default function Home() {
  return (
    <main className="flex">
      <Sidebar />

      <section className="flex-1 p-6">
        <h2 className="text-3xl font-bold mb-4">
          Dashboard
        </h2>

        <p>
          Welcome to the AI Infrastructure Cost Intelligence Platform.
        </p>
      </section>
    </main>
  );
}