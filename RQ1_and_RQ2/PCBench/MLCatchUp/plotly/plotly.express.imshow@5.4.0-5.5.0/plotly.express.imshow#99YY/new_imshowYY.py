import plotly.express as px
import numpy as np
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]], [[0, 255, 0], [0, 0, 255], [255, 0, 0]]], dtype=np.uint8)
fig = px.imshow(img_rgb, None, None, None, {}, x=None, y=None, animation_frame=None, facet_col=None, facet_col_wrap=None, facet_col_spacing=None, facet_row_spacing=None, color_continuous_scale=None, text_auto=False)
