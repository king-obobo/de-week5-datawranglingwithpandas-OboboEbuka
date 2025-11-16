import pandas as pd
from pathlib import Path
import numpy as np

class ETL:
    
    def _validate_path_exists_and_file_type(self, file_path):
        if not file_path.endswith(".csv"):
            raise TypeError("File is not a csv File")
        
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError("File not found")
        
        if file_path.stat().st_size == 0:
            raise ValueError("File is empty")
        
        return True
    
    def load(self, file_path):
        self._validate_path_exists_and_file_type(file_path)
        return pd.read_csv(file_path)
        
        
    def transform_time_col(self, time_df):
        todays_date_time = pd.Timestamp.now().strftime("%Y/%m/%d %H:%M:%S")
        for column in time_df.columns:
            if "time" in column.lower():
                time_df[column] = time_df[column].str.strip()
                time_df[column] = pd.to_datetime(time_df[column], format='mixed')
                
        # Fill up the missing value
        time_df["Ticket Close Time"] = time_df["Ticket Close Time"].fillna(todays_date_time)
        return time_df
    
    
    def fillna(self, df_na):
        df_na["Fault Type"] = df_na["Fault Type"].fillna("Uknown")
        return df_na
    
    
    def enrich(self, df):
        bins = [0, 30, 60, 180, float("inf")]
        labels = ["Excellent", "Good", "Fair", "Critical"]
        
        df["Resolution SLA (Mins)"] = round((df["Issue Res Time"] - df["Ticket Resp Time"]).dt.total_seconds() / 60, 2)
        
        df["Resp SLA (Seconds)"] = (df["Ticket Resp Time"] - df["Ticket Open Time"]).dt.total_seconds()
        
        df["Resolution Catgory"] = pd.cut(df["Resolution SLA (Mins)"], bins = bins, labels= labels, right=False)
        
        # All issues must be responded within 10 seconds of ticket initiation
        df["Response SLA pass"] = np.where(df["Resp SLA (Seconds)"] <= 15, "pass", "fail")

        # All issues must be resolved within 3 hours of respons
        df["Resolution SLA pass"] = np.where(df["Resolution SLA (Mins)"] <= 180, "pass", "fail")
        
        # Adding week column
        df['week_label'] = ("week " + df['Ticket Open Time'].dt.isocalendar().week.astype(str))
        
        return df
    