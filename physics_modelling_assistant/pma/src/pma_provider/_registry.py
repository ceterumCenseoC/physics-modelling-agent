from inspect_ai.model import modelapi

@modelapi(name="pma")
def pma():
    # import inside factory to keep optional deps local
    from ._backend import PMAModelAPI
    return PMAModelAPI
