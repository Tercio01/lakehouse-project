"""
Basic test suite for data quality checks.
"""
import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_session():
    """Create Spark session for testing."""
    return SparkSession.builder \
        .appName("DataQualityTests") \
        .master("local[2]") \
        .getOrCreate()

def test_sample_data_quality(spark_session):
    """Test that sample data meets basic quality standards."""
    # Sample test - in real scenario would test actual data
    test_data = [("1", "test"), ("2", "data")]
    df = spark_session.createDataFrame(test_data, ["id", "value"])
    
    assert df.count() == 2
    assert len(df.columns) == 2
    print("✅ Basic data quality test passed!")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
