from pipeline.etl import ETL
from pipeline.analysis import Analyzer
from pprint import pprint
import pandas as pd
import numpy as np
from pipeline.plots import Plot

def main():
    # Loading my ETL class
    etl = ETL()

    # Loading in my dataframe
    df_channel_type = etl.load("data/channel_type.csv")
    employee_df = etl.load("data/employee.csv")
    location_df = etl.load("data/location.csv")
    service_data_df = etl.load("data/service_data.csv")
    
    # Handling Missing data in time related cols and transforming it
    service_data_df = etl.transform_time_col(service_data_df)
    
    # Filling up unknown type with "UNKNOWN"
    service_data_df = etl.fillna(service_data_df)
    
    # Merging my Data
    merged_df = pd.merge(pd.merge(service_data_df, location_df, how="left", on="State Key"), df_channel_type, how = "left", left_on= "Report Channel", right_on= "Channel Key")
    
    merged_df = pd.merge(merged_df, employee_df, how="left", left_on= "Operator", right_on="Employee_name")
    
    # Dropping unneeded columns
    merged_df = merged_df.drop(["Report Channel", "Zone", "Manager ID", "Empoyee_ID", "Employee_name", "Report Channel", "Channel Key", "Report ID", "State Key"], axis= 1)
    
    # Enriching my data
    merged_df = etl.enrich(merged_df)
    
    analyzer = Analyzer()
    weekly_kpis = analyzer.analyze_weekly_kpis(merged_df=merged_df)
    manager_operator_report = analyzer.manager_operator_report(merged_df)
    escalations = analyzer.escalations(merged_df)
    
    # Exporting my analysis
    weekly_kpis.to_csv("reports/weekly_kpis.csv", index=False)
    print("Exported my weekly Analysis Successfully")

    
    manager_operator_report.to_json(
        "reports/manager_operator_report.json",
        orient= "records",
        indent= 4
    )
    print("Exported the manager operator report Successfully")
    # pprint(manager_operator_report)
    
    escalations.to_csv("reports/escalations.csv", index=False)
    print("Exported the Escalations Successfully")
    
    plotter = Plot()
    plotter.save_weekly_charts(weekly_kpis, "reports/")


if __name__ == "__main__":
    main()
