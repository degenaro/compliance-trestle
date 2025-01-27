# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Validate by confirming no duplicate items."""

import logging
import re

from trestle.core.base_model import OscalBaseModel
from trestle.core.validator import Validator
from trestle.oscal.__init__ import OSCAL_VERSION_REGEX

logger = logging.getLogger(__name__)


class OSCALVersionValidator(Validator):
    """Validator to confirm the OSCAL version is the one supported."""

    def model_is_valid(self, model: OscalBaseModel) -> bool:
        """Test if the model is valid."""
        try:
            oscal_version = model.metadata.oscal_version
            if type(oscal_version) is not str:
                oscal_version = oscal_version.__root__
        except Exception as err:
            logger.warn(f'Model has improper metadata or oscal version, error: {err}')
            return False
        p = re.compile(OSCAL_VERSION_REGEX)
        matched = p.match(oscal_version)
        return matched is not None
