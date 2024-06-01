import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pyautogui

data = pd.read_csv("data//datapro.csv")
def determine_grade(scores):
    if scores >= 85 and scores <= 100:
        return 'Grade A'
    elif scores >= 70 and scores < 85:
        return 'Grade B'
    elif scores >= 55 and scores < 70:
        return 'Grade C'
    elif scores >= 35 and scores < 55:
        return 'Grade D'
    elif scores >= 0 and scores < 35:
        return 'Grade E'
data['Grades']=data['Average'].apply(determine_grade)
X = data[['Average']]
y = data['Grades']
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.25,random_state = 99)

params={
    'min_samples_split': 5,
    'min_samples_leaf': 1,
    'max_samples': 0.75,
    'max_features': 0.6,
    'max_depth': 2,
    'bootstrap': True
}

params['n_estimators'] = 100
clf = RandomForestClassifier(**params)
clf.fit(X_train,y_train)
predictions=clf.predict(X_test)

st.title("Student Grade Prediction & Analysis")

nav = st.sidebar.radio("Navigation",["Home","EDA","Prediction"])
if nav == "Home":
    st.image("data//Home.jpeg",width=621)

if nav == "EDA":
    st.image("data//EDA.jpg")
    if st.checkbox("**Show Dataset**"):
        st.dataframe(data)

    # Create a DataFrame from the dataset
    df = pd.DataFrame(data)
    # Streamlit ap
    st.header('Student Gender Ratio')
    # Calculate gender count
    gender_counts = df['Gender'].value_counts()
    # Create a pie char
    figg, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # Display the pie chart in Streamli
    st.pyplot(figg)  


    # Streamlit sidebar to customize the plot
    st.header("Customize Scatter Plot")
    x_axis = st.selectbox("Select X-axis:", data.columns)
    y_axis = st.selectbox("Select Y-axis:", data.columns)

    # Scatter plot with Seaborn
    st.write(f"### Scatter Plot: {x_axis} vs {y_axis}")
    ffig, ax = plt.subplots()
    sns.scatterplot(x=x_axis, y=y_axis, data=data, ax=ax,hue=data["Gender"])
    st.pyplot(ffig)

    st.header("Student's Grade")
    # Calculate gender count
    gender_counts = df['Grades'].value_counts()
    # Create a pie char
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # Display the pie chart in Streamli
    st.pyplot(fig)

    # Streamlit app
    st.title('Grade and Gender Count Plot')

# Count plot
    fiig, ax = plt.subplots()
    sns.countplot(x='Grades', hue='Gender', data=df, ax=ax)
    ax.set_title('Count Plot of Grades by Gender')
    ax.set_xlabel('Grades')
    ax.set_ylabel('Count')

# Show the plot in Streamlit
    st.pyplot(fiig)

if nav == "Prediction":
    st.header("Predict Your Grade")
    val1 = st.number_input("1st Semester Percentage",0,100,step=1)
    val2 = st.number_input("2nd Semester Percentage",0,100,step=1)
    val3 = (val1+val2)/2
    input_data = pd.DataFrame({'Average':[val3]})
    predicted_grade = clf.predict(input_data)[0]
    
    if st.button("Predict"):
        if val3 >= 85 and val3 <= 100:
            st.success('Your final grade is {}'.format(predicted_grade))
            st.write('Suggestion')
            st.write('*Maintain your performance')
            st.write('*Try to be not casual on studies')
        if val3 >= 70 and val3 <= 85:
            st.info('Your final grade is {}'.format(predicted_grade))
            st.write('Suggestion')
            st.write('*Concentrate well on each subject')
            st.write('*Schedule study time everyday')
        if val3 >= 55 and val3 <= 70:
            st.warning('Your final grade is {}'.format(predicted_grade))
            st.write('Suggestion')
            st.write('*Get Faculty feedback ')
            st.write('*Improve time management and study skills')
        if val3 >= 35 and val3 <= 55:
            st.error('Your final grade is {} '.format(predicted_grade))
            st.write('Suggestion')
            st.write('*Learn from your mistakes')
            st.write('*Schedule study time everyday')
        if val3 >= 0 and val3 <= 35:
            st.error('Your final grade is E ')
            st.write('Suggestion')
            st.write('*Donot skip classes')
            st.write('*Ask doubts from concern')

            

    if st.button("Reset"):
        pyautogui.hotkey("ctrl","F5")        
       

