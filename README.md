# Student-grade-analysis-and-prediction

<p>This Streamlit app provides an interactive platform for analyzing student grades and predicting final grades
        based on semester percentages. The app features data visualization, exploratory data analysis (EDA), and a grade
        prediction tool using a Random Forest Classifier.</p>
    <p>
            <a href="http://localhost:8501/">Check out the website here</a>
        <h2>Usage</h2>
        Once you have the app running, you can navigate through different sections using the sidebar.</p> 
    <p>
        <h2>Home</h2>
        <ul>
            <li>Displays a welcome image and an introduction to the app.</li>
        </ul></p>            
    <p>
        <h2>EDA (Exploratory Data Analysis)</h2>
        <ul>
            <li>Shows a detailed analysis of the dataset including gender ratio, scatter plots, and grade distributions.</li>
        </ul>
        </p>  
   <p>
        <h2>Prediction</h2>
        <ul>
            <li>Allows users to input their semester percentages to predict the final grade.</li>
            <li>Provides suggestions based on the predicted grade.</li>
        </ul>
        </p> 
     <p>
    <h2>Featutes</h2>
    <ul>
        <li>
            <h3>Data Visualization:</h3>
            <ul>
                <li>Pie charts for gender distribution and grade distribution.</li>
                <li>Scatter plots for analyzing relationships between different features.</li>
                <li>Count plots for grades by gender.</li>
            </ul>
        </li>
    </ul>
    <ul>
        <li>
            <h3>Grade Prediction:</h3>
            <ul>
                <li>Predicts the final grade based on the average of two semester percentages.</li>
                <li>Provides personalized suggestions based on the predicted grade.</li>
           </ul>
        </li>
    </ul>
    </p>
        <p>
    <h2>Dataset</h2>
    The dataset used in this project is 'datapro.csv', which contains the following columns:
    <ul>
        <li>
            'Average': The average percentage score of the student.
        </li>
        <li>'Gender': The gender of the student.</li>
        <li>Other relevant columns for analysis.</li>
    </ul>
    The dataset also includes a computed column Grades which categorizes scores into grades (A, B, C, D, E).
     </p>
   <p>
    <h2>Model</h2>
    The grade prediction model is a Random Forest Classifier with the following parameters:
    <ul>
        <li>'n_estimators': 100</li>
        <li>'min_samples_split': 5</li>
        <li>'min_samples_leaf': 1</li>
        <li>'max_samples': 0.75</li>
        <li>'max_features': 0.6</li>
        <li>'max_depth': 2</li>
        <li>'bootstrap': True</li>
    </ul>
    The model is trained on 75% of the dataset and tested on the remaining 25%.
    </p>
 <p>
    <h2>Contributing</h2>
    Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
</p>
