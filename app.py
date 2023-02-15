import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

st.markdown(
    """
# Basic plotting with Altair in Streamlit

> *[Vega-Altair](https://altair-viz.github.io/) is a declarative statistical visualization
library for Python, based on [Vega](http://vega.github.io/vega) and
[Vega-Lite](http://vega.github.io/vega-lite), and the source is available on
[GitHub](http://github.com/altair-viz/altair).*

## Traditional way of plotting

```python
dummy_data = [
    [-0.016, -0.1138, -0.2643],
    [1.0693, -1.3293, -0.7727],
    [-0.838, 1.5766, 0.8363],
    [-0.2015, 1.4798, 0.1008],
    [1.7676, 0.7272, -1.2334],
    [0.5572, -0.8507, 0.0301],
    [0.6012, -0.74, -0.5296],
    [-1.5085, 0.3461, 0.1905],
    [-0.0774, 1.2145, 2.5208],
    [-0.5933, 0.0748, 1.0418],
    [1.9139, -1.19, 0.7212],
    [0.4775, -0.3011, -0.1785],
    [1.2725, -2.5153, -1.3495],
    [-0.7928, 0.1941, 0.5406],
    [0.8676, 1.0484, -1.6456],
    [-1.121, 0.645, -1.4831],
    [0.5776, 1.2034, 0.496],
    [0.7386, 0.1531, -0.3114],
    [-0.0626, 0.4363, -0.327],
    [-0.2725, 2.0151, -2.7512],
]

chart_data = pd.DataFrame(dummy_data, columns=["a", "b", "c"])

st.write(chart_data)

st.line_chart(chart_data)

"""
)

dummy_data = [
    [-0.016, -0.1138, -0.2643],
    [1.0693, -1.3293, -0.7727],
    [-0.838, 1.5766, 0.8363],
    [-0.2015, 1.4798, 0.1008],
    [1.7676, 0.7272, -1.2334],
    [0.5572, -0.8507, 0.0301],
    [0.6012, -0.74, -0.5296],
    [-1.5085, 0.3461, 0.1905],
    [-0.0774, 1.2145, 2.5208],
    [-0.5933, 0.0748, 1.0418],
    [1.9139, -1.19, 0.7212],
    [0.4775, -0.3011, -0.1785],
    [1.2725, -2.5153, -1.3495],
    [-0.7928, 0.1941, 0.5406],
    [0.8676, 1.0484, -1.6456],
    [-1.121, 0.645, -1.4831],
    [0.5776, 1.2034, 0.496],
    [0.7386, 0.1531, -0.3114],
    [-0.0626, 0.4363, -0.327],
    [-0.2725, 2.0151, -2.7512],
]

chart_data = pd.DataFrame(dummy_data, columns=["a", "b", "c"])

st.write(chart_data)

st.line_chart(chart_data)

st.markdown(
    """
## Plotting with Vega-Altair

## [Encodings](https://altair-viz.github.io/user_guide/encoding.html)

> *The key to creating meaningful visualizations is to map properties of the data to
visual properties in order to effectively communicate information. In Altair, this
mapping of visual properties to data columns is referred to as an **encoding**, and
is most often expressed through the `Chart.encode()` method.*

"""
)

# Plot column "a"

st.markdown(
    """
With the data specified above in altair we could do something like this:

```python
alt.Chart(chart_data.reset_index()).mark_line().encode(x="index", y="a")
st.altair_chart(c, use_container_width=True, theme="streamlit")
```
Note the `reset_index()` call.
"""
)

st.markdown(
    """
### :red[Please don't use the] *:red[updating the code via a text area]* :red[trick like the one below in production code. People can execute arbitrary code. DANGER!!]
"""
)

c = alt.Chart(chart_data.reset_index()).mark_line().encode(x="index", y="a")
default_code = (
    'c = alt.Chart(chart_data.reset_index()).mark_line().encode(x="index", y="a")'
)
code = st.text_area("Play around with the encoding", default_code)

exec(code, locals())

st.altair_chart(c, use_container_width=True, theme="streamlit")

st.markdown(
    """
# How to reproduce the first plot?

The key is in the representation of the data, more specifically in many cases the
data has to be in long format. See this [long-form vs. wide-format](https://altair-viz.github.io/user_guide/data.html?highlight=wide#long-form-vs-wide-form-data) discussion.

We can transform the data above to long-form with the pandas `melt()` function:

```python
chart_data_long = pd.melt(
    chart_data.reset_index(), id_vars=["index"], value_vars=["a", "b", "c"]
)

st.write(chart_data_long)
"""
)

# Plot all lines
chart_data_long = pd.melt(
    chart_data.reset_index(), id_vars=["index"], value_vars=["a", "b", "c"]
)

st.write(chart_data_long)

st.markdown(
    """
Now we can reuse the plot code but with a different encoding:

```python
c = (
    alt.Chart(chart_data_long)
    .mark_line()
    .encode(x="index", y="value", color="variable:N", tooltip=["variable", "value"])
)  # .interactive()

st.altair_chart(c, use_container_width=True, theme="streamlit")
"""
)

c = (
    alt.Chart(chart_data_long)
    .mark_line()
    .encode(x="index", y="value", color="variable:N", tooltip=["variable", "value"])
)  # .interactive()

st.altair_chart(c, use_container_width=True, theme="streamlit")

st.markdown(
    """
Something more advanced:

```python
hover = alt.selection_single(
    fields=["index"],
    nearest=True,
    on="mouseover",
    empty="none",
)

lines = (
    alt.Chart(chart_data_long)
    .mark_line()
    .encode(x="index", y="value", color="variable:N")
)

points = lines.transform_filter(hover).mark_circle(size=65)

ruler = (
    alt.Chart(chart_data_long)
    .mark_rule()
    .encode(
        x="index",
        y="value",
        opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
        tooltip=["variable", "value"],
    )
).add_selection(hover)

st.altair_chart(
    (lines + points + ruler).interactive(), use_container_width=True, theme="streamlit"
)

"""
)

hover = alt.selection_single(
    fields=["index"],
    nearest=True,
    on="mouseover",
    empty="none",
)

lines = (
    alt.Chart(chart_data_long)
    .mark_line()
    .encode(x="index", y="value", color="variable:N")
)

points = lines.transform_filter(hover).mark_circle(size=65)

ruler = (
    alt.Chart(chart_data_long)
    .mark_rule()
    .encode(
        x="index",
        y="value",
        opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
        tooltip=["variable", "value"],
    )
).add_selection(hover)

st.altair_chart(
    (lines + points + ruler).interactive(), use_container_width=True, theme="streamlit"
)

st.markdown(
    """
Different representation

```python
c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
"""
)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.altair_chart(c, use_container_width=True, theme="streamlit")
