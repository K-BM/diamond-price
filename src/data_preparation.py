from pycaret.regression import *

def initialize_setup(data):
    """
    Initialize the setup for the regression task using pycaret.regression.setup.

    Args:
    - data: The dataset to be used.

    Returns:
    - s: The initialized setup object.
    """
    s = setup(data, target='Price', transform_target=True, log_experiment=True, experiment_name='diamond_experiment')
    return s