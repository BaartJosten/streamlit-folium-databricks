# streamlit-folium-databricks

This repository serves as a small getting-started guide to using streamlit with folium on Databricks for data scientists at Port of Rotterdam. There are already many great resources available to help you when you first start using streamlit, folium or both, e.g., have a look here:

1. [Streamlit get started](https://docs.streamlit.io/library/get-started)
2. [Folium quickstart](https://python-visualization.github.io/folium/quickstart.html)
3. [streamlit-folium app](https://folium.streamlit.app/)

But we will first focus on setting everything up, i.e., installing everything locally in a conda virtual environment and connecting that to a databricks PoR cluster in order to work with remote data.

## Conda env

This guide assumes you have conda already [installed](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). The default Python version for Streamlit is 3.9 so that is the version we will be using in our virtual environment as well. After you have cloned this repository and moved to the root of the project run:

```python
conda create -n dbstreamlit python=3.9
conda activate dbstreamlit
```
