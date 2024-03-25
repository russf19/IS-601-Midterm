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
        # Checks to see if the record already exists in the DataFrame, this is to avoid duplicates.
        if not ((cls.history_df['Operation'] == operation) & 
                (cls.history_df['Value1'] == a) & 
                (cls.history_df['Value2'] == b) & 
                (cls.history_df['Result'] == result)).any():
       
        # If not, creates a new record
            new_record = pandas.DataFrame({
                'Operation': [operation],
                'Value1': [a],
                'Value2': [b],
                'Result': [result]
            }, columns=['Operation', 'Value1', 'Value2', 'Result'])
            cls.history_df = pandas.concat([cls.history_df, new_record], ignore_index=True)

    @classmethod
    def get_history(cls):
        if cls.history_df.empty:
            return "No calculations are available. Please enter a command."
        return cls.history_df.to_string(index=False)

    @classmethod
    def clear_history(cls):
        cls.history_df = cls.history_df.iloc[0:0]
