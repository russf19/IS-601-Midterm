import pandas

class History:
    # Define data types explicitly
    dtypes = {
        'Operation': 'str',
        'Value1': 'float',
        'Value2': 'float',
        'Result': 'float'
    }
    history_df = pandas.DataFrame(columns=['Operation', 'Value1', 'Value2', 'Result']).astype(dtypes)

    @classmethod
    def add_history(cls, operation, a, b, result):
        # Create a new DataFrame for the new record with explicit data types
        new_record = pandas.DataFrame({
            'Operation': [operation],
            'Value1': [a],
            'Value2': [b],
            'Result': [result]
        }).astype(cls.dtypes)

        # Use concat to add the new record to the existing DataFrame
        cls.history_df = pandas.concat([cls.history_df, new_record], ignore_index=True)

    @classmethod
    def get_history(cls):
        if cls.history_df.empty:
            print("No calculations are available. Please enter a command.")
        else:
            print(cls.history_df)

    @classmethod
    def clear_history(cls):
        cls.history_df = cls.history_df.iloc[0:0]
