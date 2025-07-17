# Streamlit: coz uhmm I'm lazy?
import streamlit as st
import pandas as pd
import os

def launch_manual_label_app(data_file, labeled_file):
    """
    Launches a Streamlit interface to manually label NSFW/SFW text entries.
    """
    # If first launch, load the data and initialize index
    if 'df' not in st.session_state:
        st.session_state.df = pd.read_csv(data_file)
        st.session_state.index = 0

    df = st.session_state.df
    i = st.session_state.index

    # App title
    st.title("NSFW Text Labeler (Streamlit)") #Most NPC title ever

    # Useless I ain't finishing all entires ever
    if i >= len(df):
        st.success("✅ All samples labeled!")
        st.stop()

    # Show current text entry to label
    current_text = df.at[i, "text"]
    st.markdown(f"### Entry {i+1}/{len(df)}")
    st.write(current_text)

     # Show three labeling buttons
    col1, col2, col3 = st.columns(3)

    def label_and_save(label):
        """
        Assign label, save to output file, and remove it from the queue.
        """
        df.at[i, "label"] = label
        df.iloc[[i]].to_csv(labeled_file, mode='a', header=not os.path.exists(labeled_file), index=False)
        df.drop(index=i, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(data_file, index=False)
        st.session_state.df = df
        st.session_state.index = i

    def skip():
        """
        Skips current entry without labeling — useful for weird, broken, or ambiguous stuff.
        """
        df.drop(index=i, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(data_file, index=False)
        st.session_state.df = df
        st.session_state.index = i

    if col1.button("SFW (0)"):
        label_and_save(0)
        st.rerun()

    if col2.button("NSFW (1)"):
        label_and_save(1)
        st.rerun()

    if col3.button("Drop (F)"):
        skip()
        st.rerun()