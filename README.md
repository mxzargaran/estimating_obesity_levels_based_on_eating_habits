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

## Risks & Uncertainties
1. **Self-Reported Data** – Eating habits and physical activity are self-reported, introducing potential bias.
2. **Generalization Issues** – The dataset's population may not be fully representative of all demographics, limiting external validity.
3. **Feature Limitations** – Critical medical factors (e.g., blood pressure, cholesterol) affecting obesity risk are missing.

## Required Libraries & Tools
•	**Python**: Data processing & modeling.

•	**Pandas, NumPy**: Data handling & numerical operations.

•	**Matplotlib & Seaborn**: Data & results visualization.

•	**Scikit-Learn**:
- Machine learning models (Logistic Regression, Decision Trees, Random Forest, KNN).
- Feature selection (finding the most important predictors). 
- Cross-validation & hyperparameter tuning (improving accuracy).


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


## Results

Our findings indicate that demographic and health-related factors can effectively predict obesity levels with high accuracy. Through comprehensive model evaluation and feature selection, we achieved the following key results:

1. **Model Performance**: Random Forest outperformed all other algorithms, achieving 96.17% accuracy on the test set after feature selection and hyperparameter tuning.

2. **Key Predictors**: The top predictive factors for obesity levels were:
   - Weight (29.52%)
   - Age (9.82%)
   - Height (9.12%)
   - Frequency of consumption of vegetables (8.89%)
   - Gender (6.00%)
   - Number of main meals per day (5.55%)
   - Physical activity frequency (4.96%)
   - Technology usage time (4.69%)
   - Water consumption (4.64%)
   - Family history of overweight (3.12%)

1. **Feature Selection Impact**: Feature selection improved performance for most models, particularly for Decision Trees (+1.20%) and Logistic Regression (+0.72%).

2. **Bias Analysis**: No significant age-related bias was detected in model predictions, with consistent accuracy across age quartiles.

What we see in the below confusion matrix is the model’s performance using all available features in the dataset.  Darker diagonal cells indicate correct classifications, while off-diagonal cells represent misclassifications.  The model is performing well overall but has some misclassifications, particularly in distinguishing Overweight Level I and Normal Weight.

![ ](reports/figures/cm_Random_Forest_all_features.png)

The below confusion matrix here reveals the model’s performance after feature selection, where only the most important features were used.  The performance remains strong, and in some cases, misclassifications are reduced (e.g., Insufficient Weight and Normal Weight have fewer errors). Feature selection has not significantly reduced accuracy, meaning fewer features can achieve comparable results, improving efficiency.

![ ](reports/figures/cm_Random_Forest_selected_features.png)

The following chart shows the most influential factors in predicting obesity levels using our Random Forest model.

![ ](reports/figures/feature_importance.png)

Weight is by far the most important predictor, contributing the most to the model’s decisions.  Age & Height also play a significant role, highlighting the natural relationship between body composition and obesity.  

Eating habits matter: FCVC (Frequency of Vegetable Consumption) and NCP (Number of Meals per Day) are among the top predictors.  

Physical activity is key: FAF (Frequency of Physical Activity) and TUE (Time Using Electronics/Screen Time) both contribute to obesity risk.  Other lifestyle factors, such as water intake (CH2O), family history of overweight, and alcohol consumption habits (CALC, CAEC), also have some influence.


## Model Evaluation

We evaluated six different machine learning models using 5-fold cross-validation, comparing their performance with all features and with selected features.

### Model Performance Comparison

| Model | All Features Accuracy | Selected Features Accuracy | Difference |
|-------|----------------------|---------------------------|------------|
| Random Forest | 95.93% | 96.17% | +0.24% |
| Decision Tree | 92.82% | 94.02% | +1.20% |
| Logistic Regression | 89.47% | 90.19% | +0.72% |
| Logistic Regression (Balanced) | 89.95% | 89.23% | -0.72% |
| KNN (k=5) | 83.97% | 80.14% | -3.83% |
| KNN (k=7) | 81.10% | 78.47% | -2.63% |


### Random Forest Performance (Best Model)

The Random Forest model with selected features achieved:
- Test accuracy: 96.17%
- Excellent performance across all obesity level classes:

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| 0 | 0.98 | 0.98 | 0.98 |
| 1 | 0.91 | 0.91 | 0.91 |
| 2 | 1.00 | 0.97 | 0.99 |
| 3 | 0.98 | 1.00 | 0.99 |
| 4 | 1.00 | 0.98 | 0.99 |
| 5 | 0.91 | 0.91 | 0.91 |
| 6 | 0.93 | 0.97 | 0.95 |

### Hyperparameter Tuning

Hyperparameter tuning for the Random Forest model identified the following optimal parameters:
- n_estimators: 200
- max_depth: None
- min_samples_split: 2
- min_samples_leaf: 1

The tuned model maintained the same test accuracy (96.17%) as the untuned model with selected features.

### Cross-Validation Results

Cross-validation performance for the best model (Random Forest with selected features):
- Mean CV score: 95.33%
- Standard deviation: 1.03%

This indicates strong generalization capability and consistency across different data partitions.

### Ethical Considerations

We also conducted an analysis of ethical factors with the following findings:
1. We did not detect any significant age-related bias (accuracy was consistent across age quartiles).
2. Privacy considerations should be addressed for this dataset as it pertains to people's health information.
3. One should consider the results as a supportive tool and not a replacement for medical advice.

### Conclusion

The Random Forest model with selected features provided a robust tool for predicting obesity levels based on demographic and health-related factors. The model's high accuracy and balanced performance across classes make it suitable for real-world applications in healthcare and wellness programs, with appropriate ethical safeguards.



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

| Name                | GitHub Account                               | Reflection Video                      |
| ------------------- | -------------------------------------------- | ------------------------------------- |
| **Laura MacKew**    | [@l-mack](https://github.com/l-mack)         | [Video](INPUT LINK HERE)              |
| **Mahdi Zargaran**  | [@mxzargaran](https://github.com/mxzargaran) | [Video](INPUT LINK HERE)              |
| **Mohsen Ghaffari** | [@mohghaff](https://github.com/mohghaff)     | [Video](https://youtu.be/mBV62Mfe68w) |
| **Prashant Baisla** | [@pbaisla](https://github.com/pbaisla)       | [Video](INPUT LINK HERE)              |
| **Whitney Mak**     | [@wmak-eng](https://github.com/wmak-eng)     | [Video](INPUT LINK HERE)              |

## Acknowledgments
- Data sourced from UCI Machine Learning Repository
- University of Toronto Data Science Institute guidance

## Presentation
Please find a link to slides used in a presentation of these findings [here](https://docs.google.com/presentation/d/1cOd0nBYNI-o0RPnFu9SHcvhsmV9YmuPeFJKVdAxhK5c/edit?slide=id.g342b201c8ea_0_188#slide=id.g342b201c8ea_0_188). 
  

## References
Centers for Disease Control and Prevention. (2022). Adult obesity facts. U.S. Department of Health & Human Services. https://www.cdc.gov/obesity/data/adult.html

World Health Organization. (2023). Obesity and overweight. https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight
