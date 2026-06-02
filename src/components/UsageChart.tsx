"use client";

import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
    CartesianGrid,
} from "recharts";

const data = [
    {
        day: "Mon",
        cost: 120,
    },
    {
        day: "Tue",
        cost: 210,
    },
    {
        day: "Wed",
        cost: 180,
    },
    {
        day: "Thu",
        cost: 320,
    },
    {
        day: "Fri",
        cost: 260,
    },
    {
        day: "Sat",
        cost: 400,
    },
    {
        day: "Sun",
        cost: 340,
    },
];

export default function UsageChart() {
    return (
        <div className="bg-white rounded-2xl p-6 border shadow-sm">
            <h3 className="text-xl font-semibold mb-6">
                Weekly AI Cost Usage
            </h3>

            <div className="w-full min-w-0 h-80">
                <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={data}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="day" />

                        <YAxis />

                        <Tooltip />

                        <Line
                            type="monotone"
                            dataKey="cost"
                            stroke="#000"
                            strokeWidth={3}
                            dot={{ r: 5 }}
                            activeDot={{ r: 7 }}
                        />
                    </LineChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}