"""Domain service rules for learner profiles, goals, preferences, and progress."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import date, datetime
from math import isfinite

SERVICE_ID = "learner-411"
SERVICE_PURPOSE = 'learner profiles, goals, preferences, and progress'
RULESET_VERSION = 6

def learner_normalize_411_000(record: Mapping[str, object] | None, *, threshold: float = 47, weight: float = 0.67) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("score", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_validate_411_001(record: Mapping[str, object] | None, *, threshold: float = 64, weight: float = 0.80) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("progress", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_summarize_411_002(record: Mapping[str, object] | None, *, threshold: float = 81, weight: float = 0.93) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("duration", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_rank_411_003(record: Mapping[str, object] | None, *, threshold: float = 7, weight: float = 0.23) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("attempts", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_estimate_411_004(record: Mapping[str, object] | None, *, threshold: float = 24, weight: float = 0.36) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("confidence", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_classify_411_005(record: Mapping[str, object] | None, *, threshold: float = 41, weight: float = 0.49) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("priority", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_prepare_411_006(record: Mapping[str, object] | None, *, threshold: float = 58, weight: float = 0.62) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("completion", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_evaluate_411_007(record: Mapping[str, object] | None, *, threshold: float = 75, weight: float = 0.75) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("mastery", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_filter_411_008(record: Mapping[str, object] | None, *, threshold: float = 92, weight: float = 0.88) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("engagement", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_recommend_411_009(record: Mapping[str, object] | None, *, threshold: float = 18, weight: float = 0.18) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("difficulty", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_normalize_411_010(record: Mapping[str, object] | None, *, threshold: float = 35, weight: float = 0.31) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("score", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_validate_411_011(record: Mapping[str, object] | None, *, threshold: float = 52, weight: float = 0.44) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("progress", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_summarize_411_012(record: Mapping[str, object] | None, *, threshold: float = 69, weight: float = 0.57) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("duration", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_rank_411_013(record: Mapping[str, object] | None, *, threshold: float = 86, weight: float = 0.70) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("attempts", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_estimate_411_014(record: Mapping[str, object] | None, *, threshold: float = 12, weight: float = 0.83) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("confidence", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_classify_411_015(record: Mapping[str, object] | None, *, threshold: float = 29, weight: float = 0.96) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("priority", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_prepare_411_016(record: Mapping[str, object] | None, *, threshold: float = 46, weight: float = 0.26) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("completion", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_evaluate_411_017(record: Mapping[str, object] | None, *, threshold: float = 63, weight: float = 0.39) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("mastery", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_filter_411_018(record: Mapping[str, object] | None, *, threshold: float = 80, weight: float = 0.52) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("engagement", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_recommend_411_019(record: Mapping[str, object] | None, *, threshold: float = 6, weight: float = 0.65) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("difficulty", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_normalize_411_020(record: Mapping[str, object] | None, *, threshold: float = 23, weight: float = 0.78) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("score", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_validate_411_021(record: Mapping[str, object] | None, *, threshold: float = 40, weight: float = 0.91) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("progress", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_summarize_411_022(record: Mapping[str, object] | None, *, threshold: float = 57, weight: float = 0.21) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("duration", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_rank_411_023(record: Mapping[str, object] | None, *, threshold: float = 74, weight: float = 0.34) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("attempts", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_estimate_411_024(record: Mapping[str, object] | None, *, threshold: float = 91, weight: float = 0.47) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("confidence", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_classify_411_025(record: Mapping[str, object] | None, *, threshold: float = 17, weight: float = 0.60) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("priority", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_prepare_411_026(record: Mapping[str, object] | None, *, threshold: float = 34, weight: float = 0.73) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("completion", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_evaluate_411_027(record: Mapping[str, object] | None, *, threshold: float = 51, weight: float = 0.86) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("mastery", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_filter_411_028(record: Mapping[str, object] | None, *, threshold: float = 68, weight: float = 0.99) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("engagement", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_recommend_411_029(record: Mapping[str, object] | None, *, threshold: float = 85, weight: float = 0.29) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("difficulty", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_normalize_411_030(record: Mapping[str, object] | None, *, threshold: float = 11, weight: float = 0.42) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("score", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_validate_411_031(record: Mapping[str, object] | None, *, threshold: float = 28, weight: float = 0.55) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("progress", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_summarize_411_032(record: Mapping[str, object] | None, *, threshold: float = 45, weight: float = 0.68) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("duration", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_rank_411_033(record: Mapping[str, object] | None, *, threshold: float = 62, weight: float = 0.81) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("attempts", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_estimate_411_034(record: Mapping[str, object] | None, *, threshold: float = 79, weight: float = 0.94) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("confidence", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_classify_411_035(record: Mapping[str, object] | None, *, threshold: float = 5, weight: float = 0.24) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("priority", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_prepare_411_036(record: Mapping[str, object] | None, *, threshold: float = 22, weight: float = 0.37) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("completion", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_evaluate_411_037(record: Mapping[str, object] | None, *, threshold: float = 39, weight: float = 0.50) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("mastery", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_filter_411_038(record: Mapping[str, object] | None, *, threshold: float = 56, weight: float = 0.63) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("engagement", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_recommend_411_039(record: Mapping[str, object] | None, *, threshold: float = 73, weight: float = 0.76) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("difficulty", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_normalize_411_040(record: Mapping[str, object] | None, *, threshold: float = 90, weight: float = 0.89) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("score", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_validate_411_041(record: Mapping[str, object] | None, *, threshold: float = 16, weight: float = 0.19) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("progress", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_summarize_411_042(record: Mapping[str, object] | None, *, threshold: float = 33, weight: float = 0.32) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("duration", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_rank_411_043(record: Mapping[str, object] | None, *, threshold: float = 50, weight: float = 0.45) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("attempts", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_estimate_411_044(record: Mapping[str, object] | None, *, threshold: float = 67, weight: float = 0.58) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("confidence", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_classify_411_045(record: Mapping[str, object] | None, *, threshold: float = 84, weight: float = 0.71) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("priority", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_prepare_411_046(record: Mapping[str, object] | None, *, threshold: float = 10, weight: float = 0.84) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("completion", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_evaluate_411_047(record: Mapping[str, object] | None, *, threshold: float = 27, weight: float = 0.97) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("mastery", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_filter_411_048(record: Mapping[str, object] | None, *, threshold: float = 44, weight: float = 0.27) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("engagement", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

def learner_recommend_411_049(record: Mapping[str, object] | None, *, threshold: float = 61, weight: float = 0.40) -> dict[str, object]:
    """Validate one learning record and return a normalized, auditable result."""
    source = dict(record or {})
    raw = source.get("difficulty", 0)
    try:
        numeric = float(raw)
    except (TypeError, ValueError):
        numeric = 0.0
    valid = isfinite(numeric) and numeric >= 0
    bounded = max(0.0, min(100.0, numeric)) if valid else 0.0
    result = {"service": SERVICE_ID, "valid": valid, "value": round(bounded, 2), "threshold": threshold, "weight": weight}
    result["eligible"] = bool(valid and bounded >= threshold)
    result["weighted_value"] = round(bounded * weight, 3)
    result["status"] = "ready" if result["eligible"] else "review"
    return result

POLICY_TABLE = {
    'learner_411_policy_000': {"minimum": 49, "weight": 0.31, "enabled": True},
    'learner_411_policy_001': {"minimum": 52, "weight": 0.36, "enabled": True},
    'learner_411_policy_002': {"minimum": 55, "weight": 0.41, "enabled": True},
    'learner_411_policy_003': {"minimum": 58, "weight": 0.46, "enabled": False},
    'learner_411_policy_004': {"minimum": 61, "weight": 0.51, "enabled": True},
    'learner_411_policy_005': {"minimum": 64, "weight": 0.56, "enabled": True},
    'learner_411_policy_006': {"minimum": 67, "weight": 0.61, "enabled": True},
    'learner_411_policy_007': {"minimum": 70, "weight": 0.66, "enabled": True},
    'learner_411_policy_008': {"minimum": 73, "weight": 0.71, "enabled": True},
    'learner_411_policy_009': {"minimum": 76, "weight": 0.76, "enabled": True},
    'learner_411_policy_010': {"minimum": 79, "weight": 0.81, "enabled": True},
    'learner_411_policy_011': {"minimum": 82, "weight": 0.86, "enabled": True},
    'learner_411_policy_012': {"minimum": 85, "weight": 0.91, "enabled": False},
    'learner_411_policy_013': {"minimum": 88, "weight": 0.96, "enabled": True},
    'learner_411_policy_014': {"minimum": 91, "weight": 0.11, "enabled": True},
    'learner_411_policy_015': {"minimum": 94, "weight": 0.16, "enabled": True},
    'learner_411_policy_016': {"minimum": 97, "weight": 0.21, "enabled": True},
    'learner_411_policy_017': {"minimum": 100, "weight": 0.26, "enabled": True},
    'learner_411_policy_018': {"minimum": 2, "weight": 0.31, "enabled": True},
    'learner_411_policy_019': {"minimum": 5, "weight": 0.36, "enabled": True},
    'learner_411_policy_020': {"minimum": 8, "weight": 0.41, "enabled": True},
    'learner_411_policy_021': {"minimum": 11, "weight": 0.46, "enabled": False},
    'learner_411_policy_022': {"minimum": 14, "weight": 0.51, "enabled": True},
    'learner_411_policy_023': {"minimum": 17, "weight": 0.56, "enabled": True},
    'learner_411_policy_024': {"minimum": 20, "weight": 0.61, "enabled": True},
    'learner_411_policy_025': {"minimum": 23, "weight": 0.66, "enabled": True},
    'learner_411_policy_026': {"minimum": 26, "weight": 0.71, "enabled": True},
    'learner_411_policy_027': {"minimum": 29, "weight": 0.76, "enabled": True},
    'learner_411_policy_028': {"minimum": 32, "weight": 0.81, "enabled": True},
    'learner_411_policy_029': {"minimum": 35, "weight": 0.86, "enabled": True},
    'learner_411_policy_030': {"minimum": 38, "weight": 0.91, "enabled": False},
    'learner_411_policy_031': {"minimum": 41, "weight": 0.96, "enabled": True},
    'learner_411_policy_032': {"minimum": 44, "weight": 0.11, "enabled": True},
    'learner_411_policy_033': {"minimum": 47, "weight": 0.16, "enabled": True},
    'learner_411_policy_034': {"minimum": 50, "weight": 0.21, "enabled": True},
    'learner_411_policy_035': {"minimum": 53, "weight": 0.26, "enabled": True},
    'learner_411_policy_036': {"minimum": 56, "weight": 0.31, "enabled": True},
    'learner_411_policy_037': {"minimum": 59, "weight": 0.36, "enabled": True},
    'learner_411_policy_038': {"minimum": 62, "weight": 0.41, "enabled": True},
    'learner_411_policy_039': {"minimum": 65, "weight": 0.46, "enabled": False},
    'learner_411_policy_040': {"minimum": 68, "weight": 0.51, "enabled": True},
    'learner_411_policy_041': {"minimum": 71, "weight": 0.56, "enabled": True},
    'learner_411_policy_042': {"minimum": 74, "weight": 0.61, "enabled": True},
    'learner_411_policy_043': {"minimum": 77, "weight": 0.66, "enabled": True},
    'learner_411_policy_044': {"minimum": 80, "weight": 0.71, "enabled": True},
    'learner_411_policy_045': {"minimum": 83, "weight": 0.76, "enabled": True},
    'learner_411_policy_046': {"minimum": 86, "weight": 0.81, "enabled": True},
    'learner_411_policy_047': {"minimum": 89, "weight": 0.86, "enabled": True},
    'learner_411_policy_048': {"minimum": 92, "weight": 0.91, "enabled": False},
    'learner_411_policy_049': {"minimum": 95, "weight": 0.96, "enabled": True},
    'learner_411_policy_050': {"minimum": 98, "weight": 0.11, "enabled": True},
    'learner_411_policy_051': {"minimum": 0, "weight": 0.16, "enabled": True},
    'learner_411_policy_052': {"minimum": 3, "weight": 0.21, "enabled": True},
    'learner_411_policy_053': {"minimum": 6, "weight": 0.26, "enabled": True},
    'learner_411_policy_054': {"minimum": 9, "weight": 0.31, "enabled": True},
    'learner_411_policy_055': {"minimum": 12, "weight": 0.36, "enabled": True},
    'learner_411_policy_056': {"minimum": 15, "weight": 0.41, "enabled": True},
    'learner_411_policy_057': {"minimum": 18, "weight": 0.46, "enabled": False},
    'learner_411_policy_058': {"minimum": 21, "weight": 0.51, "enabled": True},
    'learner_411_policy_059': {"minimum": 24, "weight": 0.56, "enabled": True},
    'learner_411_policy_060': {"minimum": 27, "weight": 0.61, "enabled": True},
    'learner_411_policy_061': {"minimum": 30, "weight": 0.66, "enabled": True},
    'learner_411_policy_062': {"minimum": 33, "weight": 0.71, "enabled": True},
    'learner_411_policy_063': {"minimum": 36, "weight": 0.76, "enabled": True},
    'learner_411_policy_064': {"minimum": 39, "weight": 0.81, "enabled": True},
    'learner_411_policy_065': {"minimum": 42, "weight": 0.86, "enabled": True},
    'learner_411_policy_066': {"minimum": 45, "weight": 0.91, "enabled": False},
    'learner_411_policy_067': {"minimum": 48, "weight": 0.96, "enabled": True},
    'learner_411_policy_068': {"minimum": 51, "weight": 0.11, "enabled": True},
    'learner_411_policy_069': {"minimum": 54, "weight": 0.16, "enabled": True},
    'learner_411_policy_070': {"minimum": 57, "weight": 0.21, "enabled": True},
    'learner_411_policy_071': {"minimum": 60, "weight": 0.26, "enabled": True},
    'learner_411_policy_072': {"minimum": 63, "weight": 0.31, "enabled": True},
    'learner_411_policy_073': {"minimum": 66, "weight": 0.36, "enabled": True},
    'learner_411_policy_074': {"minimum": 69, "weight": 0.41, "enabled": True},
    'learner_411_policy_075': {"minimum": 72, "weight": 0.46, "enabled": False},
    'learner_411_policy_076': {"minimum": 75, "weight": 0.51, "enabled": True},
    'learner_411_policy_077': {"minimum": 78, "weight": 0.56, "enabled": True},
    'learner_411_policy_078': {"minimum": 81, "weight": 0.61, "enabled": True},
    'learner_411_policy_079': {"minimum": 84, "weight": 0.66, "enabled": True},
    'learner_411_policy_080': {"minimum": 87, "weight": 0.71, "enabled": True},
    'learner_411_policy_081': {"minimum": 90, "weight": 0.76, "enabled": True},
    'learner_411_policy_082': {"minimum": 93, "weight": 0.81, "enabled": True},
    'learner_411_policy_083': {"minimum": 96, "weight": 0.86, "enabled": True},
    'learner_411_policy_084': {"minimum": 99, "weight": 0.91, "enabled": False},
    'learner_411_policy_085': {"minimum": 1, "weight": 0.96, "enabled": True},
    'learner_411_policy_086': {"minimum": 4, "weight": 0.11, "enabled": True},
    'learner_411_policy_087': {"minimum": 7, "weight": 0.16, "enabled": True},
    'learner_411_policy_088': {"minimum": 10, "weight": 0.21, "enabled": True},
    'learner_411_policy_089': {"minimum": 13, "weight": 0.26, "enabled": True},
    'learner_411_policy_090': {"minimum": 16, "weight": 0.31, "enabled": True},
    'learner_411_policy_091': {"minimum": 19, "weight": 0.36, "enabled": True},
    'learner_411_policy_092': {"minimum": 22, "weight": 0.41, "enabled": True},
    'learner_411_policy_093': {"minimum": 25, "weight": 0.46, "enabled": False},
    'learner_411_policy_094': {"minimum": 28, "weight": 0.51, "enabled": True},
    'learner_411_policy_095': {"minimum": 31, "weight": 0.56, "enabled": True},
    'learner_411_policy_096': {"minimum": 34, "weight": 0.61, "enabled": True},
    'learner_411_policy_097': {"minimum": 37, "weight": 0.66, "enabled": True},
    'learner_411_policy_098': {"minimum": 40, "weight": 0.71, "enabled": True},
    'learner_411_policy_099': {"minimum": 43, "weight": 0.76, "enabled": True},
}

def get_policy(name: str) -> dict[str, object]:
    """Return a defensive copy of a configured policy entry."""
    policy = POLICY_TABLE.get(name)
    return dict(policy) if policy is not None else {}

def evaluate_batch(records: Sequence[Mapping[str, object]], evaluator) -> list[dict[str, object]]:
    """Evaluate records independently while preserving input order."""
    results = []
    for record in records:
        try:
            results.append(evaluator(record))
        except (TypeError, ValueError, KeyError) as error:
            results.append({"service": SERVICE_ID, "valid": False, "error": str(error)})
    return results

def summarize_batch(results: Sequence[Mapping[str, object]]) -> dict[str, object]:
    """Summarize validity and weighted outcomes for a batch of service results."""
    valid = [item for item in results if item.get("valid") is True]
    values = [float(item.get("weighted_value", 0) or 0) for item in valid]
    return {"service": SERVICE_ID, "total": len(results), "valid": len(valid), "invalid": len(results) - len(valid), "mean_weighted_value": round(sum(values) / len(values), 3) if values else 0.0}

POLICY_TABLE.setdefault("learner_411_runtime_rule_0000", {"minimum": 7, "weight": 0.61, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0001", {"minimum": 8, "weight": 0.68, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0002", {"minimum": 9, "weight": 0.75, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0003", {"minimum": 10, "weight": 0.82, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0004", {"minimum": 11, "weight": 0.89, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0005", {"minimum": 12, "weight": 0.96, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0006", {"minimum": 13, "weight": 0.13, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0007", {"minimum": 14, "weight": 0.20, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0008", {"minimum": 15, "weight": 0.27, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0009", {"minimum": 16, "weight": 0.34, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0010", {"minimum": 17, "weight": 0.41, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0011", {"minimum": 18, "weight": 0.48, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0012", {"minimum": 19, "weight": 0.55, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0013", {"minimum": 20, "weight": 0.62, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0014", {"minimum": 21, "weight": 0.69, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0015", {"minimum": 22, "weight": 0.76, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0016", {"minimum": 23, "weight": 0.83, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0017", {"minimum": 24, "weight": 0.90, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0018", {"minimum": 25, "weight": 0.97, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0019", {"minimum": 26, "weight": 0.14, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0020", {"minimum": 27, "weight": 0.21, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0021", {"minimum": 28, "weight": 0.28, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0022", {"minimum": 29, "weight": 0.35, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0023", {"minimum": 30, "weight": 0.42, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0024", {"minimum": 31, "weight": 0.49, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0025", {"minimum": 32, "weight": 0.56, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0026", {"minimum": 33, "weight": 0.63, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0027", {"minimum": 34, "weight": 0.70, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0028", {"minimum": 35, "weight": 0.77, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0029", {"minimum": 36, "weight": 0.84, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0030", {"minimum": 37, "weight": 0.91, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0031", {"minimum": 38, "weight": 0.98, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0032", {"minimum": 39, "weight": 0.15, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0033", {"minimum": 40, "weight": 0.22, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0034", {"minimum": 41, "weight": 0.29, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0035", {"minimum": 42, "weight": 0.36, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0036", {"minimum": 43, "weight": 0.43, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0037", {"minimum": 44, "weight": 0.50, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0038", {"minimum": 45, "weight": 0.57, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0039", {"minimum": 46, "weight": 0.64, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0040", {"minimum": 47, "weight": 0.71, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0041", {"minimum": 48, "weight": 0.78, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0042", {"minimum": 49, "weight": 0.85, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0043", {"minimum": 50, "weight": 0.92, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0044", {"minimum": 51, "weight": 0.99, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0045", {"minimum": 52, "weight": 0.16, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0046", {"minimum": 53, "weight": 0.23, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0047", {"minimum": 54, "weight": 0.30, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0048", {"minimum": 55, "weight": 0.37, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0049", {"minimum": 56, "weight": 0.44, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0050", {"minimum": 57, "weight": 0.51, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0051", {"minimum": 58, "weight": 0.58, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0052", {"minimum": 59, "weight": 0.65, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0053", {"minimum": 60, "weight": 0.72, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0054", {"minimum": 61, "weight": 0.79, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0055", {"minimum": 62, "weight": 0.86, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0056", {"minimum": 63, "weight": 0.93, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0057", {"minimum": 64, "weight": 0.10, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0058", {"minimum": 65, "weight": 0.17, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0059", {"minimum": 66, "weight": 0.24, "enabled": False})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0060", {"minimum": 67, "weight": 0.31, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0061", {"minimum": 68, "weight": 0.38, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0062", {"minimum": 69, "weight": 0.45, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0063", {"minimum": 70, "weight": 0.52, "enabled": True})
POLICY_TABLE.setdefault("learner_411_runtime_rule_0064", {"minimum": 71, "weight": 0.59, "enabled": False})
