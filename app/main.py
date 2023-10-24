import os
import pandas as pd
import streamlit as st

# Function to load the dataset
def load_dataset(data_dir, selected_part):
    return pd.read_csv(os.path.join(data_dir, f'flickr30k_part_{selected_part}_translated.csv'), delimiter='|', skipinitialspace=True)

# Function to load the corrected dataset, if exists
def load_corrected_dataset(data_dir, selected_part):
    try:
        return pd.read_csv(os.path.join(data_dir, f'flickr30k_part_{selected_part}_corrected.csv'), delimiter='|', skipinitialspace=True)
    except FileNotFoundError:
        return None

st.title("Translation Checker App")

# Sidebar for file and sentence number selection
selected_part = st.sidebar.selectbox("Select the part:", [i for i in range(1, 33)])

data_dir = '../data/Translated/'
df_original = load_dataset(data_dir, selected_part)

corrected_dir = '../data/corrected/'
corrected_df = load_corrected_dataset(corrected_dir, selected_part)

if corrected_df is not None:
    df = corrected_df
else:
    df = df_original.copy()
    df['corrected_comment'] = None

# Display sentence numbers along with correction status for selection
sentence_numbers = [f"{num + 1} - {'Corrected' if not pd.isna(df.iloc[num]['corrected_comment']) else 'Not Corrected'}" for num in range(len(df))]

# Sidebar selector for sentence number
selected_sentence_number = st.sidebar.selectbox("Select the sentence number:", sentence_numbers)

# Extract the sentence number from the selected option
selected_sentence_number = int(selected_sentence_number.split(" - ")[0])

# Determine the index based on the selected sentence number
index = selected_sentence_number - 1

# Display the image corresponding to the selected sentence
st.image(os.path.join('/Users/erdnbt/Projects/Research/flickr30k_images/flickr_images', df.iloc[index]['image_name'].strip()))

# Displaying the original caption
st.write(f"Original: {df.iloc[index]['comment'].strip()}")

# Check for the existence of 'Translated Comment' column before accessing
if 'Translated Comment' in df.columns:
    machine_translation = df.iloc[index]['Translated Comment'].strip()
else:
    machine_translation = ""

# Display machine translation
st.write(f"Machine Translation: {machine_translation}")

# Displaying the corrected translation if it exists
corrected_comment = df.iloc[index]['corrected_comment'] if 'corrected_comment' in df.columns else machine_translation

if not pd.isna(corrected_comment):
    st.markdown(f"**Corrected Translation (green):** <span style='color: green;'>{corrected_comment.strip()}</span>", unsafe_allow_html=True)

# Text area and Submit button
corrected_translation = st.text_area(
    "Correct the translation:",
    corrected_comment
)

if st.button("Submit"):
    # Update the dataframe with the latest correction
    df.at[index, 'corrected_comment'] = corrected_translation.strip()
    
    # Save the dataframe back to the corrected file
    df[['image_name', 'comment_number', 'comment', 'corrected_comment']].to_csv(os.path.join('../data/corrected/', f'flickr30k_part_{selected_part}_corrected.csv'), sep='|', index=False)
