from pathlib import Path
import matplotlib.pyplot as plt


class Plot:
    def save_weekly_charts(self, df, output_folder):
        """
        Plots all weekly SLA charts and saves them as PNG files
        in the specified output folder using pathlib.Path.
        """

        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

        charts = {
            "total_tickets": "Total Tickets per Week",
            "avg_resolution_sla_mins": "Average Resolution SLA (Minutes)",
            "avg_response_sla_seconds": "Average Response SLA (Seconds)",
            "resolution_pass_rate": "Resolution SLA Pass Rate (%)",
            "response_pass_rate": "Response SLA Pass Rate (%)"
        }

        for column, title in charts.items():
            plt.figure(figsize=(8, 4))
            df[column].plot(kind="line", marker="o")
            plt.title(title)
            plt.xlabel("Week")
            plt.ylabel(column.replace("_", " ").title())
            plt.grid(True)

            # Build full path using Path
            file_path = output_folder / f"{column}.png"

            # Save file
            plt.savefig(file_path, dpi=300, bbox_inches="tight")
            plt.close()

        print(f"Charts saved successfully to: {output_folder.resolve()}")