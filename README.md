# Predicting Obesity Levels Using Lifestyle, Eating Habits, and Physical Activity Patterns

## Project Overview
Obesity is a major public health challenge, contributing to an increased risk of chronic diseases such as diabetes, cardiovascular conditions, and metabolic disorders (Centers for Disease Control and Prevention [CDC], 2022; World Health Organization [WHO], 2023). Understanding the key lifestyle and dietary factors that contribute to obesity is crucial for designing effective, data-driven interventions to promote healthier living.

Using the *Estimation of Obesity Levels Based on Eating Habits and Physical Condition* dataset from the UCI Machine Learning Repository, this project aims to develop machine learning models that analyze the relationships between eating habits, physical activity, and lifestyle choices to predict obesity levels based on the NObesity classification system.

By identifying the most influential predictors of obesity, this model can help healthcare professionals, policymakers, and individuals make informed decisions about obesity prevention and intervention strategies.

## Research Question
**Which lifestyle and dietary habits contribute most to obesity?**

## Dataset Information
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)
- **Description:** The dataset contains demographic information, eating habits, and physical condition indicators that help estimate obesity levels.
- **Dataset Features:**
  - Demographics: Age, Gender
  - Physical Conditions: Physical Conditions: Height, Weight, BMI (derived feature), Physical activity frequency (FAF)
  - Eating Habits: High-calorie food consumption (FAVC), Vegetable consumption (FCVC), Number of main meals per day (NCP), Eating between meals (CAEC)
  - Lifestyle Factors: Alcohol consumption frequency (CALC), Smoking (SMOKE), Water intake (CH2O), Screen time/technology usage (TUE), Transportation mode (MTRANS)
  - Health Indicators: Family history of overweight (family_history_with_overweight), Caloric monitoring (SCC)
  - Target Variable:  The NObesity Classification System categorizes obesity into the following levels:
	1.	Underweight
	2.	Normal weight
	3.	Overweight
	4.	Obesity Type I
	5.	Obesity Type II
	6.	Obesity Type III

## Stakeholders & Their Interest
**Primary Stakeholders:**
1. **Healthcare Professionals & Researchers** – Interested in understanding how lifestyle factors contribute to obesity.
2. **Public Health Organizations** – Can use insights to develop better awareness campaigns and preventive healthcare programs.
3. **Insurance & Policy Makers** – Obesity and its related health risks impact healthcare costs, so insights from this project can guide policy decisions.
4. **Fitness & Nutrition Industries** – Businesses in the health sector can leverage findings to develop personalized diet and exercise programs.
5. **Individuals Concerned About Health** – The general public can benefit from personalized risk assessments based on lifestyle habits.

## Can This Dataset Answer Our Research Question?
- **Yes.** The dataset provides demographic information, physical conditions, and lifestyle habits, which are relevant factors for obesity prediction.

## Value to the Industry
- **Healthcare** – Helps identify key lifestyle-related risk factors for obesity and prevention strategies.
- **Public Health & Policy** – Supports better policy-making for obesity-related health risks.
- **Fitness & Nutrition** – Enables data-driven recommendations for healthier living.

## How Will We Answer Our Business Question?
- We will **analyze the relationships** between lifestyle factors (eating habits, physical activity, BMI) and obesity.
- We will **identify key predictors** that correlate with obesity levels.

## Risks & Uncertainties
1. **Self-Reported Data** – Eating habits and physical activity are self-reported, introducing potential bias.
2. **Generalization Issues** – The dataset's population may not be fully representative of all demographics, limiting external validity.
3. **Feature Limitations** – Critical medical factors (e.g., blood pressure, cholesterol) affecting obesity risk are missing.

## Required Libraries & Tools
- **Data Analysis & Preprocessing:** Python (Pandas, NumPy, Scikit-learn)
- **Exploratory Data Analysis (EDA):** 
- **Feature Engineering:** Encoding categorical variables, handling missing data
- **Machine Learning Models:** Logistic Regression, Random Forest, XGBoost
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score
- **Project Management & Collaboration:** GitHub, Jupyter Notebooks

## Methodology
1. **Data Preprocessing**
   - Addressed missing values, outliners and inconsistancies in the dataset. 
   - Converted categorical variables to numerical representations
   - Standardized numerical features
2. **Exploratory Data Analysis (EDA)**
   - Created visualizations of feature distributions including histograms to identify outliers, class imbalances and skewness. 
   - Identified correlations between variables
3. **Feature Engineering**
   - Create new relevant features based on existing data
   - Perform dimensionality reduction (if needed)
4. **Model Selection & Training**
   - Apply classification models (e.g., Logistic Regression, Random Forest, XGBoost, Neural Networks)
   - Tune hyperparameters for optimal performance
   - Evaluate using metrics like Accuracy, Precision, Recall, and F1-Score
5. **Interpretation & Insights**
   - Identify the most significant factors influencing obesity levels
   - Compare model performance
   - Discuss potential real-world applications

## Findings

**Results**

- Our findings indicate that...

**Model Evalution**

## Folder Structure
```
/project_root  
│── data/                  # Raw & processed data  
│── notebooks/             # Jupyter Notebooks for EDA, modeling  
│── src/                   # Scripts (data processing, model training)  
│── reports/               # Visualizations, findings  
│── models/                # Saved models  
│── requirements.txt       # Dependencies  
│── README.md              # Project summary  
│── .gitignore             # Exclude large files  
```

## Dependencies
Install required packages using:
```bash
pip install -r requirements.txt
```

## Next Steps
- Conduct EDA and feature selection
- Train classification models and optimize performance

## Contributors

| Name                | GitHub Account                               | Reflection Video         |
| ------------------- | -------------------------------------------- | ------------------------ |
| **Laura MacKew**    | [@l-mack](https://github.com/l-mack)         | [Video](INPUT LINK HERE) |
| **Mahdi Zargaran**  | [@mxzargaran](https://github.com/mxzargaran) | [Video](INPUT LINK HERE) |
| **Mohsen Ghaffari** | [@mohghaff](https://github.com/mohghaff)     | [Video](INPUT LINK HERE) |
| **Prashant Baisla** | [@pbaisla](https://github.com/pbaisla)       | [Video](INPUT LINK HERE) |
| **Whitney Mak**     | [@wmak-eng](https://github.com/wmak-eng)     | [Video](INPUT LINK HERE) |

## Acknowledgments
- Data sourced from UCI Machine Learning Repository
- University of Toronto Data Science Institute guidance
  

## References
Centers for Disease Control and Prevention. (2022). Adult obesity facts. U.S. Department of Health & Human Services. https://www.cdc.gov/obesity/data/adult.html

World Health Organization. (2023). Obesity and overweight. https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight
