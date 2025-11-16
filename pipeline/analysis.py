class Analyzer:
    
    def analyze_weekly_kpis(self, merged_df):
        weekly_kpis = merged_df.groupby("week_label").agg(
        total_tickets=("Customer Name", "count"),
        avg_resolution_sla_mins=("Resolution SLA (Mins)", "mean"),
        avg_response_sla_seconds=("Resp SLA (Seconds)", "mean"),
        resolution_pass_rate=("Resolution SLA pass", lambda x: (x == "pass").mean()),
        response_pass_rate=("Response SLA pass", lambda x: (x == "pass").mean())
    ).reset_index()

        # Converting rates to percentages
        weekly_kpis["resolution_pass_rate"] = (weekly_kpis["resolution_pass_rate"] * 100).round(2)
        weekly_kpis["response_pass_rate"] = (weekly_kpis["response_pass_rate"] * 100).round(2)
        
        return weekly_kpis
    
    
    def manager_operator_report(self, merged_df):
        
        manager_operator_report = (
        merged_df.groupby(["Manager", "Operator"])
            .agg(
                total_tickets=("Customer Name", "count"),
                avg_resolution_sla_mins=("Resolution SLA (Mins)", "mean"),
                avg_response_sla_seconds=("Resp SLA (Seconds)", "mean"),
                resolution_pass_rate=("Resolution SLA pass", lambda x: (x == "pass").mean()),
                response_pass_rate=("Response SLA pass", lambda x: (x == "pass").mean())
            ) .reset_index()
            )
        # Converting pass rates to percentages
        manager_operator_report["resolution_pass_rate"] = (manager_operator_report["resolution_pass_rate"] * 100).round(2)

        manager_operator_report["response_pass_rate"] = (manager_operator_report["response_pass_rate"] * 100).round(2)

        # Now we rank best-performing operators under each manager
        manager_operator_report["rank_by_resolution"] = (
            manager_operator_report.groupby("Manager")["resolution_pass_rate"]
            .rank(ascending=False, method="dense")
        )

        manager_operator_report["rank_by_response"] = (
            manager_operator_report.groupby("Manager")["response_pass_rate"]
            .rank(ascending=False, method="dense")
        )
        
        return manager_operator_report
    
    
    def escalations(self, merged_df):
        escalations = merged_df[merged_df["Resolution Catgory"].str.lower() == "critical"].copy()
        
        return escalations