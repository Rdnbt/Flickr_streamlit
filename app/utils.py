import pandas as pd 
import os

def load_dataset(path, corrected_path, part):
    """Load the dataset based on the provided part."""
    filename = os.path.join(path, f'flickr30k_part_{part}_translated.csv')
    corrected_filename = os.path.join(corrected_path, f'flickr30k_part_{part}_corrected.csv')
    
    if os.path.exists(filename):
        df = pd.read_csv(filename, sep='|')
        
        # Load corrected translations if the file exists
        if os.path.exists(corrected_filename):
            corrected_df = pd.read_csv(corrected_filename, sep='|')
            df = df.merge(corrected_df[['image_name', 'comment_number', 'Translated Comment']], on=['image_name', 'comment_number'], how='left', suffixes=('', '_corrected'))
            
        return df
    else:
        return pd.DataFrame()
