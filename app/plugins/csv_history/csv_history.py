import pandas
from app.commands.command.command import Command
from app.plugins.history.history import History

class CSVHistoryCommand(Command):
    def execute(self, action, filepath):
        if action == 'export':
            return self.export_to_csv(filepath)
        elif action == 'import':
            return self.import_from_csv(filepath)
        else:
            return "Invalid action. Please specify 'export' or 'import'."
    
    def export_to_csv(self, filepath):
        try:
            History.history_df.to_csv(filepath, index=False)
            return f"History exported to {filepath}"
        except Exception as e:
            return f"Failed to export history to CSV: {str(e)}"
    
    def import_from_csv(self, filepath):
        try:
            # Load new history
            new_history = pandas.read_csv(filepath)

            # Check columns
            if set(new_history.columns) == {'Operation', 'Value1', 'Value2', 'Result'}:
                # Standardize and clean data
                new_history = new_history.astype(History.dtypes)
                new_history['Operation'] = new_history['Operation'].str.strip()

                print("New history before merging:")
                print(new_history)

                # Check for pre-existing duplication
                if not new_history.duplicated(subset=['Operation', 'Value1', 'Value2', 'Result']).any():
                    print("No duplicates in the new history.")
                else:
                    print("Duplicates detected in the new history.")

                # Combine with existing history and remove duplicates
                combined_history = pandas.concat([History.history_df, new_history], ignore_index=True)
                combined_history = combined_history.drop_duplicates(subset=['Operation', 'Value1', 'Value2', 'Result'])

                # Assign the combined history
                History.history_df = combined_history

                print("History after merging:")
                print(History.history_df)

                return f"History successfully imported from {filepath}"
            else:
                return "Invalid CSV format. Ensure the columns are 'Operation', 'Value1', 'Value2', and 'Result'."
        except Exception as e:
            return f"Failed to import history from CSV: {str(e)}"
        