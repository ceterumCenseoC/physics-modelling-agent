from inspect_ai.model import modelapi

@modelapi(name="pma")
def pma():
    # import inside factory to keep optional deps local
    from .execute import CritPtExposeAPI
    return CritPtExposeAPI
