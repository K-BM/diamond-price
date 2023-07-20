from pycaret.datasets import get_data
from pycaret.regression import *

from pycaret.regression import save_model

# Step 1: Load the dataset
data = get_data('diamond')

# Step 2: Initialize setup
s = setup(data, target='Price', transform_target=True, log_experiment=True, experiment_name='diamond_experiment')

# Step 3: Compare all models
best_model = compare_models()

# Step 4: Check feature importance
plot_model(best_model, plot='feature')

# Step 5: Finalize and save the model
final_best_model = finalize_model(best_model)
save_model(final_best_model, 'diamond-pipeline')

print("Pipeline executed successfully!")