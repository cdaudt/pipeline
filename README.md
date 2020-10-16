![Python package](https://github.com/cdaudt/pipeline/workflows/Python%20package/badge.svg)

# Simple data processing pipelines

Create simple data pipelines with sink/source modules that can 
process or drop elements. Each pipeline step receives a dictionary
of metadata+data for the element, and it can add/remove fields
to the element, or terminate processing of the element.

An example pipeline would be a generator (the **source**) which reads image files from a directory, followed by a pipe that resizes each image, followed by a pipe that saves each image. 
# Stages

Each stage can contain a **source**, a **sink**, or both. Sources generate elements, while sinks process and optionally drop elements from the pipeline.




# Elements

Elements are the units of data passed through the processing pipeline. An element is a dictionary that can contain any number of fields. Both data and meta-data about the data unit can be contained in the element.

# TODO: Add Example


