# Predicting Stroke Risk Based on Demographic and Health-Related Factors

## Project Overview
This project aims to analyze demographic and health-related factors to predict the risk of stroke in patients. We use the "Estimation of Obesity Levels Based on Eating Habits and Physical Condition" dataset from the UCI Machine Learning Repository. Our objective is to explore how lifestyle factors such as diet, physical activity, and BMI contribute to stroke risk.

## Research Question
**What demographic and health-related factors significantly predict the occurrence of a stroke in patients?**

## Dataset
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)
- **Description:** The dataset contains demographic information, eating habits, and physical condition indicators that help estimate obesity levels.
- **Key Features:**
  - Age, Gender
  - BMI, Physical Activity Level
  - Eating Habits (Frequency of meals, alcohol consumption, etc.)
  - Health Indicators (Family history of obesity, consumption of high-calorie food)

## Stakeholders & Their Interest
**Primary Stakeholders:**
1. **Healthcare Professionals & Researchers** – Interested in understanding how lifestyle factors contribute to obesity and potential health risks, including stroke.
2. **Public Health Organizations** – Can use insights to develop better awareness campaigns and preventive healthcare programs.
3. **Insurance & Policy Makers** – Obesity and its related health risks (such as stroke) impact healthcare costs, so insights from this project can guide policy decisions.
4. **Fitness & Nutrition Industries** – Businesses in the health sector can leverage findings to develop personalized diet and exercise programs.
5. **Individuals Concerned About Health** – The general public can benefit from personalized risk assessments based on lifestyle habits.

## Can This Dataset Answer Our Research Question?
- **Partially.** The dataset provides demographic information, physical conditions, and lifestyle habits, which are relevant factors for stroke risk.
- However, **stroke occurrence itself is not explicitly included** in the dataset. We may need to **either modify our research question** (e.g., “What factors in this dataset contribute to stroke risk?”) or **supplement it with external stroke-related data.**

## Value to the Industry
- **Healthcare** – Helps identify key lifestyle-related risk factors for obesity and stroke prevention.
- **Public Health & Policy** – Supports better policy-making for obesity-related health risks.
- **Fitness & Nutrition** – Enables data-driven recommendations for healthier living.

## How Will We Answer Our Business Question?
- We will **analyze the relationships** between lifestyle factors (eating habits, physical activity, BMI) and obesity.
- We will **identify key predictors** that correlate with obesity, which is a major risk factor for stroke.
- If needed, we may integrate external datasets containing stroke occurrences to strengthen the analysis.

## Risks & Uncertainties
1. **Lack of Stroke Data** – The dataset does not explicitly include stroke occurrences, which may require modifying the research scope.
2. **Self-Reported Data** – Eating habits and physical activity are self-reported, introducing potential bias.
3. **Generalization Issues** – The dataset's population may not be fully representative of all demographics, limiting external validity.
4. **Feature Limitations** – Critical medical factors (e.g., blood pressure, cholesterol) affecting stroke risk are missing.

## Methods & Technologies
- **Data Analysis & Preprocessing:** Python (Pandas, NumPy, Scikit-learn)
- **Exploratory Data Analysis (EDA):** 
- **Feature Engineering:** Encoding categorical variables, handling missing data
- **Machine Learning Models:** Logistic Regression, Random Forest, XGBoost
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score
- **Project Management & Collaboration:** GitHub, Jupyter Notebooks

## Methodology
1. **Data Preprocessing**
   - Handle missing values (if any)
   - Convert categorical variables to numerical representations
   - Standardize or normalize numerical features
2. **Exploratory Data Analysis (EDA)**
   - Visualize feature distributions
   - Identify correlations between variables
   - Check for class imbalances
3. **Feature Engineering**
   - Create new relevant features based on existing data
   - Perform dimensionality reduction (if needed)
4. **Model Selection & Training**
   - Apply classification models (e.g., Logistic Regression, Random Forest, XGBoost, Neural Networks)
   - Tune hyperparameters for optimal performance
   - Evaluate using metrics like Accuracy, Precision, Recall, and F1-Score
5. **Interpretation & Insights**
   - Identify the most significant factors influencing stroke risk
   - Compare model performance
   - Discuss potential real-world applications

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
- Validate dataset relevance to stroke prediction
- Conduct EDA and feature selection
- Train classification models and optimize performance

## Contributors
| Name       | GitHub Account                        | Email                           | Roles/Responsibilities                     | Reflection Video                    |
|------------|---------------------------------------|---------------------------------|--------------------------------------------|----------------------------------|


## Acknowledgments
- Data sourced from UCI Machine Learning Repository
- University of Toronto Data Science Institute guidance
