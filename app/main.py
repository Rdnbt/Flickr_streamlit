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

selected_part = st.selectbox("Select the part:", [i for i in range(1, 33)])

data_dir = '../data/Translated/'
df = load_dataset(data_dir, selected_part)

corrected_dir = '../data/corrected/'
corrected_df = load_corrected_dataset(corrected_dir, selected_part)

if corrected_df is not None:
    df = df.merge(corrected_df[['image_name', 'comment_number', 'Translated Comment']], on=['image_name', 'comment_number'], how='left', suffixes=('', '_corrected'))

if 'index' not in st.session_state:
    st.session_state.index = 0

index = st.session_state.index

# Display the image
st.image(os.path.join('/Users/erdnbt/Projects/Research/flickr30k_images/flickr_images', df.iloc[index]['image_name'].strip()))

# Displaying the original caption and corrected/machine translations
st.write(f"Original: {df.iloc[index]['comment'].strip()}")

if 'Translated Comment_corrected' in df.columns and pd.notna(df.iloc[index]['Translated Comment_corrected']):
    corrected_text_color = 'green'
    corrected_translation_display = df.iloc[index]['Translated Comment_corrected'].strip()
else:
    corrected_text_color = 'red'
    corrected_translation_display = df.iloc[index]['Translated Comment'].strip()

st.markdown(f"**Translation:** <span style='color: {corrected_text_color};'>{corrected_translation_display}</span>", unsafe_allow_html=True)

corrected_translation = st.text_area("Correct the translation:", df.iloc[index]['Translated Comment'].strip())

# Buttons: Previous, Submit, Next
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Previous") and index > 0:
        st.session_state.index -= 1

with col2:
    if st.button("Submit"):
        # Update the dataframe with the latest correction
        df.at[index, 'Translated Comment_corrected'] = corrected_translation.strip()

        # Extract only the necessary columns and rename as needed
        corrected_df = df[['image_name', 'comment_number', 'Translated Comment_corrected']]
        corrected_df = corrected_df.rename(columns={"Translated Comment_corrected": "Translated Comment"})

        # Save the dataframe back to the corrected file
        corrected_df.to_csv(os.path.join('../data/corrected/', f'flickr30k_part_{selected_part}_corrected.csv'), sep='|', index=False)

with col3:
    if st.button("Next") and index < len(df) - 1:
        st.session_state.index += 1
