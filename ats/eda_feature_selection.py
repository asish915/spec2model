import os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegressionCV

ROOT = os.path.dirname(__file__)
DATA_PATH = os.path.join(ROOT, 'train_A.csv')
TARGET = 'is_late'

def main():
    df = pd.read_csv(DATA_PATH)
    print('Shape:', df.shape)
    print('\nColumns and dtypes:')
    print(df.dtypes.value_counts())
    print('\nMissing values (top 20):')
    print(df.isnull().sum().sort_values(ascending=False).head(20))

    print('\nTarget distribution:')
    print(df[TARGET].value_counts(dropna=False))

    # Separate X/y
    y = df[TARGET].copy()
    X = df.drop(columns=[TARGET])

    # Encode target to binary if needed
    if y.dtype == object or y.dtype.name == 'category':
        le = LabelEncoder()
        y = le.fit_transform(y.astype(str))

    # Identify numeric and categorical
    numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = X.select_dtypes(exclude=[np.number]).columns.tolist()

    print(f'Numeric cols: {len(numeric_cols)}, Categorical cols: {len(cat_cols)}')

    # Impute numeric
    if numeric_cols:
        num_imp = SimpleImputer(strategy='median')
        X_num = pd.DataFrame(num_imp.fit_transform(X[numeric_cols]), columns=numeric_cols)

    # Impute and one-hot categorical (fill missing with 'missing')
    if cat_cols:
        X_cat = X[cat_cols].fillna('missing').astype(str)
        X_cat = pd.get_dummies(X_cat, drop_first=True)

    # Combine
    X_proc = pd.concat([X_num, X_cat], axis=1)
    print('Processed feature matrix shape:', X_proc.shape)

    # Fill any remaining NaNs 
    X_proc = X_proc.fillna(0)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_proc)

    # L1 (Lasso-like) logistic for selection
    print('\nFitting LogisticRegressionCV (L1) for feature selection :')
    try:
        l1_clf = LogisticRegressionCV(cv=5, penalty='l1', solver='saga', scoring='roc_auc', max_iter=5000, n_jobs=-1).fit(X_scaled, y)
        l1_coef = l1_clf.coef_.ravel()
    except Exception as e:
        print('L1 Logistic failed:', e)
        l1_coef = None

    selected_l1 = []
    if l1_coef is not None:
        selected_l1 = [feat for feat, co in zip(X_proc.columns, l1_coef) if abs(co) > 1e-8]
        print(f'L1 selected {len(selected_l1)} features')
        with open(os.path.join(ROOT, 'selected_features_lasso.txt'), 'w', encoding='utf-8') as f:
            for c in selected_l1:
                f.write(c + '\n')

    # L2 (Ridge-like) logistic for ranking coefficients
    print('\nFitting LogisticRegressionCV (L2) for coefficient ranking...')
    try:
        l2_clf = LogisticRegressionCV(cv=5, penalty='l2', solver='lbfgs', scoring='roc_auc', max_iter=5000, n_jobs=-1).fit(X_scaled, y)
        l2_coef = l2_clf.coef_.ravel()
    except Exception as e:
        print('L2 Logistic failed:', e)
        l2_coef = None

    if l2_coef is not None:
        coef_df = pd.DataFrame({'feature': X_proc.columns, 'coef': l2_coef, 'abs_coef': np.abs(l2_coef)})
        coef_df = coef_df.sort_values('abs_coef', ascending=False)
        coef_df.to_csv(os.path.join(ROOT, 'ridge_coefficients.csv'), index=False)
        print('\n\n===== RIDGE COEFFICIENTS (ALL FEATURES, SORTED BY ABS VALUE) =====')
        print(coef_df.to_string(index=False))
        # Suggest removal: very small coefficients (bottom 10%)
        small_thresh = np.percentile(coef_df['abs_coef'], 10)
        to_remove = coef_df[coef_df['abs_coef'] <= small_thresh]['feature'].tolist()
        print(f"\n\n===== FEATURES TO REMOVE (Bottom 10% by abs coefficient) =====")
        print(f"Threshold: {small_thresh:.6f}")
        print(f"Total features to remove: {len(to_remove)}")
        print('\nFeatures marked for removal:')
        for c in to_remove:
            print(f"  - {c}")
        with open(os.path.join(ROOT, 'suggested_remove_ridge.txt'), 'w', encoding='utf-8') as f:
            for c in to_remove:
                f.write(c + '\n')

    # Save preprocessed features (after removing low-coefficient features)
    print(f"\n\n===== SAVING FINAL PREPROCESSED DATASET =====")
    print(f"Original preprocessed shape: {X_proc.shape}")
    
    # Remove low-coefficient features if they exist
    if l2_coef is not None and len(to_remove) > 0:
        X_proc_clean = X_proc.drop(columns=to_remove)
        print(f"Removed {len(to_remove)} low-coefficient features")
        print(f"Final preprocessed shape: {X_proc_clean.shape}")
        print(f"Features removed: {len(to_remove)}, Features kept: {X_proc_clean.shape[1]}")
    else:
        X_proc_clean = X_proc.copy()
        print("No features removed (L2 fitting failed or no low-coefficient features identified)")
    
    # Add target back and save
    X_proc_clean.insert(0, TARGET, y)
    X_proc_clean.to_csv(os.path.join(ROOT, 'preprocessed_for_modeling.csv'), index=False)

    print('\nOutputs written:')
    print('  - selected_features_lasso.txt (features kept by L1)')
    print('  - ridge_coefficients.csv (all features ranked by coefficient)')
    print('  - suggested_remove_ridge.txt (features marked for removal)')
    print(f'  - preprocessed_for_modeling.csv (final cleaned dataset, shape={X_proc_clean.shape})')

if __name__ == '__main__':
    main()
