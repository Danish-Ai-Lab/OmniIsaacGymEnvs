import math
import carb

from typing import Optional

import numpy as np
import torch
from omni.isaac.core.robots.robot import Robot
from omni.isaac.core.utils.stage import add_reference_to_stage

class Moonbot(Robot):
    def __init__(
        self,
        prim_path: str,
        name: Optional[str] = "Moonbot",
        usd_path: Optional[str] = None,
        translation: Optional[np.ndarray] = None,
        orientation: Optional[np.ndarray] = None,
    ) -> None:
        """[summary]"""

        self._usd_path = usd_path
        self._name = name
        assert usd_path is None, "Need to specify usd file."
        add_reference_to_stage(usd_path, prim_path)
        super().__init__(
            prim_path=prim_path,
            name=name,
            translation=translation,
            orientation=orientation,
            articulation_controller=None,
        )

        self._dof_names = [
            "joint1_1",
            "joint2_1",
            "joint3_1",
            "joint4_1",
            "joint1_2",
            "joint2_2",
            "joint3_2",
            "joint4_2",
            "joint1_3",
            "joint2_3",
            "joint3_3",
            "joint4_3",
        ]

    @property
    def dof_names(self):
        return self._dof_names