import pandas as pd
import numpy as np

from dataclasses import dataclass


def load_data(filepath: str, filetype: str = "csv", **kwargs) -> pd.DataFrame:
    """Loads data from various file formats and returns a DataFrame.

    Supports 'csv', 'excel', and 'json' file types. Additional arguments can
    be passed to the Pandas loading functions via kwargs.

    Args:
        filepath (str): The path to the file.
        filetype (str): The type of file to load. Options are 'csv', 'excel', and 'json'.
        kwargs: Additional arguments to pass to the Pandas loading functions.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.

    Raises:
        ValueError: If the filetype is not supported.
    """
    if filetype == "csv":
        return pd.read_csv(filepath, **kwargs)
    elif filetype == "excel":
        return pd.read_excel(filepath, **kwargs)
    elif filetype == "json":
        return pd.read_json(filepath, **kwargs)
    else:
        raise ValueError(f"File type '{filetype}' is not supported.")


def data_to_array(data) -> np.ndarray:
    """Converts input data to a NumPy array for consistent processing.

    This function accepts lists, pandas Series, pandas DataFrames, and NumPy arrays.
    Converts DataFrames and Series to a 1D array by flattening.

    Args:
        daten: Input data, which can be a list, pandas Series, pandas DataFrame,
               or a NumPy array.

    Returns:
        A 1D NumPy array with the values of the input data.

    Raises:
        TypeError: If the input data type is unsupported.

    Examples:
        >>> data_to_array([1, 2, 3])
        array([1, 2, 3])
        >>> data_to_array(pd.Series([1, 2, 3]))
        array([1, 2, 3])
        >>> data_to_array(pd.DataFrame({"values": [1, 2, 3]}))
        array([1, 2, 3])
        >>> data_to_array(pd.DataFrame({"values": [1, 2, 3], "otherValues": [4, 5, 6]}))
        array([[1, 4],
               [2, 5],
               [3, 6]])
    """
    if isinstance(data, pd.DataFrame):
        if data.shape[1] == 1:  # Single-column DataFrame
            return data.iloc[:, 0].to_numpy()  # Return a 1D array
        return data.to_numpy()  # For multi-column DataFrames, return a 2D array
    elif isinstance(data, pd.Series):
        return data.to_numpy()
    elif isinstance(data, list):
        return np.array(data)
    elif isinstance(data, np.ndarray):
        return data
    else:
        raise TypeError("The input data must be a list, NumPy array, pandas DataFrame, or Series.")


@dataclass
class SampleSize:
    m: int  # Stichprobengrösse
    n: int  # Anzahl Stichproben


def get_sample_size(data: np.ndarray) -> SampleSize:
    """Returns the sample size (number of columns) and the number of rows (probes)
    for a NumPy array dataset.

    Args:
        data (np.ndarray): 2D NumPy array of numerical values.

    Returns:
        SampleSize: A dataclass containing the sample size (m) and the number of probes (n).

    Examples:
        >>> data = np.array([[10, 12, 14], [15, 16, 17]])
        >>> get_sample_size(data)
        SampleSize(m=3, n=2)
    """
    if isinstance(data, np.ndarray):
        m = data.shape[1]  # Stichprobengrösse
        n = data.shape[0]  # Anzahl Stichproben
        return SampleSize(m=m, n=n)
    else:
        raise TypeError("Input data must be a NumPy array.")
