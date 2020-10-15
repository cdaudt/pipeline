import pytest
from pipeline import pipeline

def test_pipeline_stageless():
    assert pipeline.Pipeline(None) != None

