from pycaret.regression import *

def compare_all_models():
    """
    Compare all the available models using pycaret.regression.compare_models.

    Returns:
    - best: The best performing model.
    """
    best = compare_models()
    return best

def check_feature_importance(best_model):
    """
    Plot the feature importance of the best model using pycaret.regression.plot_model.

    Args:
    - best_model: The best performing model obtained from compare_models.
    """
    plot_model(best_model, plot='feature')

def finalize_and_save_model(best_model, save_path):
    """
    Finalize the best model using pycaret.regression.finalize_model and save it to disk.

    Args:
    - best_model: The best performing model obtained from compare_models.
    - save_path: The path where the model will be saved.
    """
    final_best = finalize_model(best_model)
    save_model(final_best, save_path)