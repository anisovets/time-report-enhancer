import data_loader as loader
import processor as processor

def main():
    mapping = loader.load_json("../data/input/mapping.json")
    if mapping is None:
        print('Failed to load mapping file. Exiting program.')
        return # Stop execution if the mapping cannot be loaded
    
    row_report = loader.load_csv("../data/input/time_report_2024-04-01_2024-04-30.csv")    
    if row_report is None:
        print('Failed to load row data file. Exiting program.')
        return # Stop execution if row data cannot be loaded

    processed_data = processor.enrich_data(row_report,mapping)


    loader.write_csv("../data/output/time_report_output.csv",processed_data)


if __name__ == "__main__":
    main()