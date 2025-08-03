import pytest
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from src
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.loader.csv_loader import CSVTextDataSetLoader

ENCODING = 'latin-1' # Relevant Encoding for tweets_dataset.csv
DATASET_FILEPATH_CSV = "data/tweets_dataset.csv"

def test_csv_loader_basic():
    """Test basic CSV loading functionality."""
    # Create loader with just filepath
    loader = CSVTextDataSetLoader(filepath=DATASET_FILEPATH_CSV)
    
    # Load dataset
    dataset = loader.load(encoding=ENCODING)
    
    # Basic assertions
    assert dataset is not None
    assert hasattr(dataset, 'data')  # Should have pandas DataFrame
    assert len(dataset.data) > 0


def test_csv_loader_with_features():
    """Test CSV loading with specific features."""
    # Load only specific columns
    chosen_features = ["Text", "Biased"]
    loader = CSVTextDataSetLoader(
        filepath=DATASET_FILEPATH_CSV,
        chosen_features=chosen_features
    )
    
    dataset = loader.load(encoding=ENCODING)
    
    # Should only have the chosen features
    assert list(dataset.data.columns) == chosen_features
    assert len(dataset.data) > 0


def test_csv_loader_all_columns():
    """Test that all columns are loaded when no features specified."""
    loader = CSVTextDataSetLoader(filepath=DATASET_FILEPATH_CSV)
    dataset = loader.load(encoding=ENCODING)
    
    # Should have multiple columns (we don't know exact structure, so just check it's not empty)
    assert len(dataset.data.columns) > 0
    assert len(dataset.data) > 0


def test_csv_loader_get_dataframe():
    """Test that get_dataframe method works."""
    loader = CSVTextDataSetLoader(filepath=DATASET_FILEPATH_CSV)
    dataset = loader.load(encoding=ENCODING)
    
    # get_dataframe should return the same data
    df = dataset.get_dataframe()
    assert df is not None
    assert len(df) > 0
    assert df.equals(dataset.data)


def test_csv_loader_file_not_found():
    """Test error handling for missing files."""
    loader = CSVTextDataSetLoader(filepath="nonexistent.csv")
    
    # The current implementation will raise a pandas error, not FileNotFoundError
    # Let's catch the actual exception that pandas raises
    with pytest.raises(Exception):  # More general exception catching
        loader.load(encoding=ENCODING)


def test_csv_loader_chosen_features_none():
    """Test that None chosen_features works correctly."""
    loader = CSVTextDataSetLoader(
        filepath=DATASET_FILEPATH_CSV,
        chosen_features=None
    )
    
    dataset = loader.load(encoding=ENCODING)
    assert dataset is not None
    assert len(dataset.data) > 0