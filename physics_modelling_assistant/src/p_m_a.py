from .execute import CritPtExpose

def load_model(**kwargs):
    return CritPtExpose(**kwargs)

# REGISTER YOUR MODEL HERE
from inspect_ai.model._registry import register_model

register_model("p_m_a", load_model)