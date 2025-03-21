# ============================================================
# DATA PREPROCESSING PARAMETERS
# ============================================================

# General parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
TARGET_COLUMN = 'NObeyesdad'
CV_FOLDS = 5
STRATIFIED_CV = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_STATE)

# Feature selection parameters
FEATURE_SELECTION = {
    'method': 'random_forest',  # Options: 'random_forest', 'lasso', etc.
    'threshold': 'mean',  # Options: 'mean', 'median', or a float value
    'n_estimators': 100,
    'plot_top_n': 15
}

# ============================================================
# MODEL CONFIGURATIONS
# ============================================================

# Define model classes, default parameters, and hyperparameter grids
MODELS = {
    'Logistic Regression': {
        'class': LogisticRegression,
        'default_params': {
            'max_iter': 1000,
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'C': [0.001, 0.01, 0.1, 1, 10, 100],
            'solver': ['liblinear', 'saga'],
            'penalty': ['l1', 'l2']
        }
    },
    'Logistic Regression (Balanced)': {
        'class': LogisticRegression,
        'default_params': {
            'max_iter': 1000,
            'class_weight': 'balanced',
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'C': [0.001, 0.01, 0.1, 1, 10, 100],
            'solver': ['liblinear', 'saga'],
            'penalty': ['l1', 'l2']
        }
    },
    'Decision Tree': {
        'class': DecisionTreeClassifier,
        'default_params': {
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'criterion': ['gini', 'entropy']
        }
    },
    'Random Forest': {
        'class': RandomForestClassifier,
        'default_params': {
            'n_estimators': 100,
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
    },
    'KNN (k=5)': {
        'class': KNeighborsClassifier,
        'default_params': {
            'n_neighbors': 5
        },
        'param_grid': {
            'n_neighbors': [3, 5, 7, 9, 11],
            'weights': ['uniform', 'distance'],
            'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
        }
    },
    'KNN (k=7)': {
        'class': KNeighborsClassifier,
        'default_params': {
            'n_neighbors': 7
        },
        'param_grid': {
            'n_neighbors': [3, 5, 7, 9, 11],
            'weights': ['uniform', 'distance'],
            'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
        }
    },
    'SVM': {
        'class': SVC,
        'default_params': {
            'probability': True,
            'random_state': RANDOM_STATE
        },
        'param_grid': {
            'C': [0.1, 1, 10, 100],
            'gamma': ['scale', 'auto', 0.1, 0.01],
            'kernel': ['rbf', 'linear', 'poly']
        }
    }
}

# Default model evaluation metrics
MODEL_METRICS = ['accuracy', 'f1_macro', 'precision_macro', 'recall_macro']

# ============================================================
# VISUALIZATION PARAMETERS
# ============================================================

# Figure sizes
FIG_SIZE_SMALL = (8, 6)
FIG_SIZE_MEDIUM = (10, 8)
FIG_SIZE_LARGE = (12, 8)

# Plot styling
PLOT_STYLE = 'seaborn-v0_8-whitegrid'
COLOR_PALETTE = 'viridis'
DPI = 300

# File formats
FIGURE_FORMAT = 'png'  # Options: 'png', 'pdf', 'svg', 'jpg'

# Specific plot configurations
CLASS_DISTRIBUTION_PLOT = {
    'title': 'Distribution of Obesity Levels',
    'filename': 'class_distribution.png',
    'figsize': FIG_SIZE_MEDIUM,
    'rotate_labels': True,
    'show_counts': True
}

FEATURE_IMPORTANCE_PLOT = {
    'title': 'Top Feature Importances',
    'filename': 'feature_importance.png',
    'figsize': FIG_SIZE_LARGE,
    'top_n': 15,
    'color': 'royalblue'
}

MODEL_COMPARISON_PLOT = {
    'title': 'Model Performance Comparison',
    'filename': 'model_comparison.png',
    'figsize': FIG_SIZE_LARGE,
    'rotate_labels': 45,
    'y_lim': [0, 1]
}

CONFUSION_MATRIX_PLOT = {
    'filename_prefix': 'cm_',
    'figsize': FIG_SIZE_MEDIUM,
    'cmap': 'Blues',
    'annot': True,
    'fmt': 'd'
}

TUNING_COMPARISON_PLOT = {
    'title': 'Model Performance Before and After Tuning',
    'filename': 'tuning_comparison.png',
    'figsize': FIG_SIZE_SMALL,
    'color': ['lightblue', 'darkblue']
}

# ============================================================
# LOGGING CONFIGURATION
# ============================================================

LOG_FILE = os.path.join(LOGS_DIR, 'obesity_model.log')
LOG_LEVEL = 'INFO'  # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# ============================================================
# PREDICTION SETTINGS
# ============================================================

DEFAULT_PREDICTION_OUTPUT = 'predictions.csv'
RETURN_PROBABILITIES = True
CLASS_PROBABILITY_THRESHOLD = 0.5  # For binary classification if needed

# ============================================================
# ETHICAL CONSIDERATIONS
# ============================================================

# Define sensitive attributes for bias checking
SENSITIVE_ATTRIBUTES = ['Gender', 'Age']
BIAS_THRESHOLD = 0.05  # Consider bias significant if accuracy differs by more than 5%

# ============================================================
# PERFORMANCE SETTINGS
# ============================================================

# Multiprocessing settings
N_JOBS = -1  # Use all available cores
VERBOSE = 1  # Level of verbosity for training progress

# Memory management
CLEAN_MEMORY_THRESHOLD = 0.8  # Trigger garbage collection if memory usage exceeds this fraction