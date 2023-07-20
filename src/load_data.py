from pycaret.datasets import get_data

def load_dataset():
    """
    Load the dataset using pycaret.datasets.get_data.

    Returns:
    - data: The loaded dataset.
    """
    data = get_data('diamond')
    return data
