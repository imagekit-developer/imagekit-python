# Serialization utilities for upload options
# This file handles serialization of upload parameters before sending to ImageKit API

import json
from typing import Any, Dict, Sequence, cast


def serialize_upload_options(upload_options: Dict[str, Any]) -> Dict[str, Any]:
    """
    Serialize upload options to handle proper formatting for ImageKit backend API.

    Special cases handled:
    - tags: converted to comma-separated string
    - response_fields: converted to comma-separated string
    - extensions: JSON stringified
    - custom_metadata: JSON stringified
    - transformation: JSON stringified

    Args:
        upload_options: Dictionary containing upload parameters

    Returns:
        Dictionary with serialized values
    """
    serialized: Dict[str, Any] = {**upload_options}

    for key in list(serialized.keys()):
        if key and serialized[key] is not None:
            value = serialized[key]

            if key == "tags" and isinstance(value, (list, tuple)):
                # Tags should be comma-separated string
                serialized[key] = ",".join(cast(Sequence[str], value))
            elif key == "response_fields" and isinstance(value, (list, tuple)):
                # Response fields should be comma-separated string
                serialized[key] = ",".join(cast(Sequence[str], value))
            elif key == "extensions" and isinstance(value, list):
                # Extensions should be JSON stringified
                serialized[key] = json.dumps(value)
            elif key == "custom_metadata" and isinstance(value, dict):
                # Custom metadata should be JSON stringified
                serialized[key] = json.dumps(value)
            elif key == "transformation" and isinstance(value, dict):
                # Transformation should be JSON stringified
                serialized[key] = json.dumps(value)

    return serialized
