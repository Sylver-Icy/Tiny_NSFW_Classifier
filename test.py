import streamlit as st
import pandas as pd
import os

DATA_FILE = "nsfw_sex_reddit.csv"
LABELED_FILE = "nsfw_sex_reddit_labelled.csv"

if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv(DATA_FILE)
    st.session_state.index = 0

df = st.session_state.df
i = st.session_state.index

st.title("NSFW Text Labeler (Streamlit)")

if i >= len(df):
    st.success("✅ All samples labeled!")
    st.stop()

current_text = df.at[i, "text"]
st.markdown(f"### Entry {i+1}/{len(df)}")
st.write(current_text)

col1, col2, col3 = st.columns(3)

def label_and_save(label):
    df.at[i, "label"] = label
    df.iloc[[i]].to_csv(LABELED_FILE, mode='a', header=not os.path.exists(LABELED_FILE), index=False)
    df.drop(index=i, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(DATA_FILE, index=False)
    st.session_state.df = df
    st.session_state.index = i

def skip():
    df.drop(index=i, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(DATA_FILE, index=False)
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