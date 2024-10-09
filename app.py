import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_csv('results.csv')
    return df

def main():
    st.title("Student Exam Results Exploration")

    
    df = load_data()

    
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Select a Section:", 
                                ["Introduction",
                                 "Descriptive Statistics", 
                                 "Histograms", 
                                 "Box Plots", 
                                 "Correlation Matrix", 
                                 "Conclusion"])

   
    if options == "Introduction":
        st.markdown(""" 
        ### Introduction
        
        This dataset contains exam marks for **1000 students** in six subjects: Hindi, English, Science, Maths, History, and Geography. It also includes three additional columns: Total Marks, Results, and Division.

        - **Total Marks**: The sum of marks across all subjects.
        - **Results** indicate whether a student passed (1) or failed (0).
        - **Division** categorizes students based on their overall performance:
          - **0**: Failed
          - **1**: First Division (High marks)
          - **2**: Second Division (Satisfactory performance)
          - **3**: Third Division (Just passed)

        This dataset, sourced from Kaggle, can be used for both binary classification (pass/fail) and multi-class classification (division categories). 

        ### Purpose of Exploration

        The purpose of this exploration is to analyze the performance of students across different subjects, identify trends in their results, and assess the factors that may contribute to their success or failure. Insights gained from this analysis could be beneficial for educators and policymakers to improve educational outcomes.
        """)


        if st.checkbox("Show Raw Data"):
            st.subheader("Raw Data")
            st.write(df)

  
    elif options == "Descriptive Statistics":
        st.subheader("Descriptive Statistics")
        st.write(df[['Student no.', 'Hindi', 'English', 'Science', 'Maths', 'History', 'Geography', 'Total', 'Results', 'Div']].describe())

    # Histograms Section
    elif options == "Histograms":
        st.subheader("Histograms of Exam Scores")
        subjects = ['Hindi', 'English', 'Science', 'Maths', 'History', 'Geography']
        
        # Session state for keeping track of current index
        if 'hist_index' not in st.session_state:
            st.session_state.hist_index = 0

        # Display the current subject's histogram
        subject = subjects[st.session_state.hist_index]
        fig, ax = plt.subplots(figsize=(12, 8))
        df[subject].hist(bins=20, ax=ax)
        plt.title(f'Histogram of {subject} Scores')
        plt.xlabel('Scores')
        plt.ylabel('Frequency')
        st.pyplot(fig)

        # Navigation buttons for histograms
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Previous"):
                if st.session_state.hist_index > 0:
                    st.session_state.hist_index -= 1
        with col2:
            if st.button("Next"):
                if st.session_state.hist_index < len(subjects) - 1:
                    st.session_state.hist_index += 1

    # Box Plots Section
    elif options == "Box Plots":
        st.subheader("Box Plots of Exam Scores")
        subjects = ['Hindi', 'English', 'Science', 'Maths', 'History', 'Geography']
        
        # Session state for keeping track of current box plot index
        if 'box_index' not in st.session_state:
            st.session_state.box_index = 0

        # Display the current subject's box plot
        subject = subjects[st.session_state.box_index]
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.boxplot(y=df[subject], ax=ax)
        plt.title(f'Box Plot of {subject} Scores')
        plt.ylabel('Scores')
        st.pyplot(fig)

        # Navigation buttons for box plots
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Previous"):
                if st.session_state.box_index > 0:
                    st.session_state.box_index -= 1
        with col2:
            if st.button("Next"):
                if st.session_state.box_index < len(subjects) - 1:
                    st.session_state.box_index += 1

    # Correlation Matrix Section
    elif options == "Correlation Matrix":
        st.subheader("Correlation Matrix")
        correlation_matrix = df[['Hindi', 'English', 'Science', 'Maths', 'History', 'Geography']].corr()
        
        # Plot heatmap for Correlation Matrix
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
        plt.title('Correlation Matrix of Exam Scores')
        st.pyplot(fig)

    # Conclusion Section
    elif options == "Conclusion":
        st.title("Conclusion")
        st.subheader("Subject Difficulty:")
        st.markdown(""" Maths appears to be the subject with the highest struggles while Hindi and History appear to be doing relatively better.""")
        st.subheader("Possible Knowledge /Skill Gaps:")
        st.markdown(""" The bimodal distribution for English suggests a potential extreme divergence of language abilities in the student population. This could potentially require more tailor-made teaching strategies.""")
        st.subheader("Outliers & Performance Gaps:")
        st.markdown("""In some subjects, there is such a wide range of scores - for example, Geography and Science - that it would seem that most children are performing reasonably well but one or two must be lagging behind and requiring additional support.""")

# Run the app
if __name__ == "__main__":
    main()
