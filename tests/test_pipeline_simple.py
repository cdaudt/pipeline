import pytest
from procpipe import pipeline

def test_pipeline_stageless():
    assert pipeline.Pipeline(None) != None

