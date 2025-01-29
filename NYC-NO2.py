import os
import pandas as pd
import requests

# Base URL for the data
base_url = "https://azdohv2staticweb.blob.core.windows.net/$web/hist/csv/"

# Start and end years and months
start_year = 2020
start_month = 1
end_year = 2025
end_month = 1

# Output file to store the filtered data
output_file = "filtered_data.csv"

# List to store filtered data
data_frames = []

# Iterate over the years and months
for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        if year == end_year and month > end_month:
            break

        # Construct the file URL
        file_url = f"{base_url}{year}/{month}/hourlyMonitoring.csv"
        print(f"Processing: {file_url}")

        try:
            # Download the CSV file
            response = requests.get(file_url)
            response.raise_for_status()

            # Save to a temporary file
            temp_file = f"temp_{year}_{month}.csv"
            with open(temp_file, "wb") as f:
                f.write(response.content)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(temp_file) 

            # Print column names for debugging
            print(f"Columns in {temp_file}: {df.columns}")

            # Filter for SiteID 36061NY09734
            if "SiteID" in df.columns:
                filtered_df = df[df['SiteID'] == '36061NY09929']
                if not filtered_df.empty:
                    data_frames.append(filtered_df)

            # Remove the temporary file
            os.remove(temp_file)

        except requests.exceptions.RequestException as e:
            print(f"Failed to download {file_url}: {e}")
        except Exception as e:
            print(f"Error processing {file_url}: {e}")

# Combine all filtered data
if data_frames:
    combined_df = pd.concat(data_frames)
    combined_df.to_csv(output_file, index=False)
    print(f"Filtered data saved to {output_file}")
else:
    print("No data found for SiteID 36061NY09734.")
