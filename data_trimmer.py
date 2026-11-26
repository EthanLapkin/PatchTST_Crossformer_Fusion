#this is a tiny little python script to cut some unnecessary columns added by claude when it was being "helpful"
import pandas as pd

df = pd.read_csv("nlr_data.csv")
df = df.drop(columns=['split', 'rapl_w_filled', 'sync_offset_ms'])
df.to_csv("nlr_data_cleaned.csv", index=False)