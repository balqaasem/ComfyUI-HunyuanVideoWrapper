from .nodes import NODE_CLASS_MAPPINGS as NODES_CLASS, NODE_DISPLAY_NAME_MAPPINGS as NODES_DISPLAY
from .nodes_rf_inversion import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_RF_INVERSION, NODE_DISPLAY_NAME_MAPPINGS as NODE_DISPLAY_NAME_MAPPINGS_RF_INVERSION

NODE_CLASS_MAPPINGS = {**NODES_CLASS, **NODE_CLASS_MAPPINGS_RF_INVERSION}
NODE_DISPLAY_NAME_MAPPINGS = {**NODES_DISPLAY, **NODE_DISPLAY_NAME_MAPPINGS_RF_INVERSION}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]