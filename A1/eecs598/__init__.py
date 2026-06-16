import importlib.util as _ilu
import os as _os
import sys as _sys

from .utils import reset_seed, tensor_to_image, visualize_dataset

# The CIFAR10 data loader is shared across all assignments and lives in the
# top-level `datasets/` folder. Load it from there and expose it as
# `eecs598.data` so notebooks can keep calling `eecs598.data.cifar10()`.
_data_path = _os.path.join(_os.path.dirname(__file__), "..", "..", "datasets", "data.py")
_spec = _ilu.spec_from_file_location(__name__ + ".data", _data_path)
data = _ilu.module_from_spec(_spec)
_sys.modules[__name__ + ".data"] = data
_spec.loader.exec_module(data)
