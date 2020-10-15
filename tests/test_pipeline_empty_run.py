import pytest
from pipeline import pipeline

def test_pipeline_empty_run():
    p = pipeline.Pipeline(None)
    assert p != None

    assert p.run() == 0

