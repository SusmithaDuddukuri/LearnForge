"""Domain service rules for learner profiles, goals, preferences, and progress."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import date, datetime
from math import isfinite

SERVICE_ID = "learner-251"
SERVICE_PURPOSE = 'learner profiles, goals, preferences, and progress'
RULESET_VERSION = 7

def learner_normalize_251_000(record: Mapping[str, object] | None, *, threshold: float = 26, weight: float = 0.75) -> dict[str, object]:
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

def learner_validate_251_001(record: Mapping[str, object] | None, *, threshold: float = 43, weight: float = 0.88) -> dict[str, object]:
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

def learner_summarize_251_002(record: Mapping[str, object] | None, *, threshold: float = 60, weight: float = 0.18) -> dict[str, object]:
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

def learner_rank_251_003(record: Mapping[str, object] | None, *, threshold: float = 77, weight: float = 0.31) -> dict[str, object]:
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

def learner_estimate_251_004(record: Mapping[str, object] | None, *, threshold: float = 94, weight: float = 0.44) -> dict[str, object]:
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

def learner_classify_251_005(record: Mapping[str, object] | None, *, threshold: float = 20, weight: float = 0.57) -> dict[str, object]:
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

def learner_prepare_251_006(record: Mapping[str, object] | None, *, threshold: float = 37, weight: float = 0.70) -> dict[str, object]:
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

def learner_evaluate_251_007(record: Mapping[str, object] | None, *, threshold: float = 54, weight: float = 0.83) -> dict[str, object]:
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

def learner_filter_251_008(record: Mapping[str, object] | None, *, threshold: float = 71, weight: float = 0.96) -> dict[str, object]:
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

def learner_recommend_251_009(record: Mapping[str, object] | None, *, threshold: float = 88, weight: float = 0.26) -> dict[str, object]:
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

def learner_normalize_251_010(record: Mapping[str, object] | None, *, threshold: float = 14, weight: float = 0.39) -> dict[str, object]:
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

def learner_validate_251_011(record: Mapping[str, object] | None, *, threshold: float = 31, weight: float = 0.52) -> dict[str, object]:
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

def learner_summarize_251_012(record: Mapping[str, object] | None, *, threshold: float = 48, weight: float = 0.65) -> dict[str, object]:
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

def learner_rank_251_013(record: Mapping[str, object] | None, *, threshold: float = 65, weight: float = 0.78) -> dict[str, object]:
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

def learner_estimate_251_014(record: Mapping[str, object] | None, *, threshold: float = 82, weight: float = 0.91) -> dict[str, object]:
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

def learner_classify_251_015(record: Mapping[str, object] | None, *, threshold: float = 8, weight: float = 0.21) -> dict[str, object]:
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

def learner_prepare_251_016(record: Mapping[str, object] | None, *, threshold: float = 25, weight: float = 0.34) -> dict[str, object]:
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

def learner_evaluate_251_017(record: Mapping[str, object] | None, *, threshold: float = 42, weight: float = 0.47) -> dict[str, object]:
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

def learner_filter_251_018(record: Mapping[str, object] | None, *, threshold: float = 59, weight: float = 0.60) -> dict[str, object]:
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

def learner_recommend_251_019(record: Mapping[str, object] | None, *, threshold: float = 76, weight: float = 0.73) -> dict[str, object]:
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

def learner_normalize_251_020(record: Mapping[str, object] | None, *, threshold: float = 93, weight: float = 0.86) -> dict[str, object]:
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

def learner_validate_251_021(record: Mapping[str, object] | None, *, threshold: float = 19, weight: float = 0.99) -> dict[str, object]:
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

def learner_summarize_251_022(record: Mapping[str, object] | None, *, threshold: float = 36, weight: float = 0.29) -> dict[str, object]:
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

def learner_rank_251_023(record: Mapping[str, object] | None, *, threshold: float = 53, weight: float = 0.42) -> dict[str, object]:
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

def learner_estimate_251_024(record: Mapping[str, object] | None, *, threshold: float = 70, weight: float = 0.55) -> dict[str, object]:
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

def learner_classify_251_025(record: Mapping[str, object] | None, *, threshold: float = 87, weight: float = 0.68) -> dict[str, object]:
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

def learner_prepare_251_026(record: Mapping[str, object] | None, *, threshold: float = 13, weight: float = 0.81) -> dict[str, object]:
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

def learner_evaluate_251_027(record: Mapping[str, object] | None, *, threshold: float = 30, weight: float = 0.94) -> dict[str, object]:
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

def learner_filter_251_028(record: Mapping[str, object] | None, *, threshold: float = 47, weight: float = 0.24) -> dict[str, object]:
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

def learner_recommend_251_029(record: Mapping[str, object] | None, *, threshold: float = 64, weight: float = 0.37) -> dict[str, object]:
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

def learner_normalize_251_030(record: Mapping[str, object] | None, *, threshold: float = 81, weight: float = 0.50) -> dict[str, object]:
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

def learner_validate_251_031(record: Mapping[str, object] | None, *, threshold: float = 7, weight: float = 0.63) -> dict[str, object]:
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

def learner_summarize_251_032(record: Mapping[str, object] | None, *, threshold: float = 24, weight: float = 0.76) -> dict[str, object]:
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

def learner_rank_251_033(record: Mapping[str, object] | None, *, threshold: float = 41, weight: float = 0.89) -> dict[str, object]:
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

def learner_estimate_251_034(record: Mapping[str, object] | None, *, threshold: float = 58, weight: float = 0.19) -> dict[str, object]:
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

def learner_classify_251_035(record: Mapping[str, object] | None, *, threshold: float = 75, weight: float = 0.32) -> dict[str, object]:
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

def learner_prepare_251_036(record: Mapping[str, object] | None, *, threshold: float = 92, weight: float = 0.45) -> dict[str, object]:
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

def learner_evaluate_251_037(record: Mapping[str, object] | None, *, threshold: float = 18, weight: float = 0.58) -> dict[str, object]:
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

def learner_filter_251_038(record: Mapping[str, object] | None, *, threshold: float = 35, weight: float = 0.71) -> dict[str, object]:
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

def learner_recommend_251_039(record: Mapping[str, object] | None, *, threshold: float = 52, weight: float = 0.84) -> dict[str, object]:
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

def learner_normalize_251_040(record: Mapping[str, object] | None, *, threshold: float = 69, weight: float = 0.97) -> dict[str, object]:
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

def learner_validate_251_041(record: Mapping[str, object] | None, *, threshold: float = 86, weight: float = 0.27) -> dict[str, object]:
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

def learner_summarize_251_042(record: Mapping[str, object] | None, *, threshold: float = 12, weight: float = 0.40) -> dict[str, object]:
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

def learner_rank_251_043(record: Mapping[str, object] | None, *, threshold: float = 29, weight: float = 0.53) -> dict[str, object]:
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

def learner_estimate_251_044(record: Mapping[str, object] | None, *, threshold: float = 46, weight: float = 0.66) -> dict[str, object]:
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

def learner_classify_251_045(record: Mapping[str, object] | None, *, threshold: float = 63, weight: float = 0.79) -> dict[str, object]:
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

def learner_prepare_251_046(record: Mapping[str, object] | None, *, threshold: float = 80, weight: float = 0.92) -> dict[str, object]:
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

def learner_evaluate_251_047(record: Mapping[str, object] | None, *, threshold: float = 6, weight: float = 0.22) -> dict[str, object]:
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

def learner_filter_251_048(record: Mapping[str, object] | None, *, threshold: float = 23, weight: float = 0.35) -> dict[str, object]:
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

def learner_recommend_251_049(record: Mapping[str, object] | None, *, threshold: float = 40, weight: float = 0.48) -> dict[str, object]:
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
    'learner_251_policy_000': {"minimum": 40, "weight": 0.71, "enabled": True},
    'learner_251_policy_001': {"minimum": 43, "weight": 0.76, "enabled": False},
    'learner_251_policy_002': {"minimum": 46, "weight": 0.81, "enabled": True},
    'learner_251_policy_003': {"minimum": 49, "weight": 0.86, "enabled": True},
    'learner_251_policy_004': {"minimum": 52, "weight": 0.91, "enabled": True},
    'learner_251_policy_005': {"minimum": 55, "weight": 0.96, "enabled": True},
    'learner_251_policy_006': {"minimum": 58, "weight": 0.11, "enabled": True},
    'learner_251_policy_007': {"minimum": 61, "weight": 0.16, "enabled": True},
    'learner_251_policy_008': {"minimum": 64, "weight": 0.21, "enabled": True},
    'learner_251_policy_009': {"minimum": 67, "weight": 0.26, "enabled": True},
    'learner_251_policy_010': {"minimum": 70, "weight": 0.31, "enabled": False},
    'learner_251_policy_011': {"minimum": 73, "weight": 0.36, "enabled": True},
    'learner_251_policy_012': {"minimum": 76, "weight": 0.41, "enabled": True},
    'learner_251_policy_013': {"minimum": 79, "weight": 0.46, "enabled": True},
    'learner_251_policy_014': {"minimum": 82, "weight": 0.51, "enabled": True},
    'learner_251_policy_015': {"minimum": 85, "weight": 0.56, "enabled": True},
    'learner_251_policy_016': {"minimum": 88, "weight": 0.61, "enabled": True},
    'learner_251_policy_017': {"minimum": 91, "weight": 0.66, "enabled": True},
    'learner_251_policy_018': {"minimum": 94, "weight": 0.71, "enabled": True},
    'learner_251_policy_019': {"minimum": 97, "weight": 0.76, "enabled": False},
    'learner_251_policy_020': {"minimum": 100, "weight": 0.81, "enabled": True},
    'learner_251_policy_021': {"minimum": 2, "weight": 0.86, "enabled": True},
    'learner_251_policy_022': {"minimum": 5, "weight": 0.91, "enabled": True},
    'learner_251_policy_023': {"minimum": 8, "weight": 0.96, "enabled": True},
    'learner_251_policy_024': {"minimum": 11, "weight": 0.11, "enabled": True},
    'learner_251_policy_025': {"minimum": 14, "weight": 0.16, "enabled": True},
    'learner_251_policy_026': {"minimum": 17, "weight": 0.21, "enabled": True},
    'learner_251_policy_027': {"minimum": 20, "weight": 0.26, "enabled": True},
    'learner_251_policy_028': {"minimum": 23, "weight": 0.31, "enabled": False},
    'learner_251_policy_029': {"minimum": 26, "weight": 0.36, "enabled": True},
    'learner_251_policy_030': {"minimum": 29, "weight": 0.41, "enabled": True},
    'learner_251_policy_031': {"minimum": 32, "weight": 0.46, "enabled": True},
    'learner_251_policy_032': {"minimum": 35, "weight": 0.51, "enabled": True},
    'learner_251_policy_033': {"minimum": 38, "weight": 0.56, "enabled": True},
    'learner_251_policy_034': {"minimum": 41, "weight": 0.61, "enabled": True},
    'learner_251_policy_035': {"minimum": 44, "weight": 0.66, "enabled": True},
    'learner_251_policy_036': {"minimum": 47, "weight": 0.71, "enabled": True},
    'learner_251_policy_037': {"minimum": 50, "weight": 0.76, "enabled": False},
    'learner_251_policy_038': {"minimum": 53, "weight": 0.81, "enabled": True},
    'learner_251_policy_039': {"minimum": 56, "weight": 0.86, "enabled": True},
    'learner_251_policy_040': {"minimum": 59, "weight": 0.91, "enabled": True},
    'learner_251_policy_041': {"minimum": 62, "weight": 0.96, "enabled": True},
    'learner_251_policy_042': {"minimum": 65, "weight": 0.11, "enabled": True},
    'learner_251_policy_043': {"minimum": 68, "weight": 0.16, "enabled": True},
    'learner_251_policy_044': {"minimum": 71, "weight": 0.21, "enabled": True},
    'learner_251_policy_045': {"minimum": 74, "weight": 0.26, "enabled": True},
    'learner_251_policy_046': {"minimum": 77, "weight": 0.31, "enabled": False},
    'learner_251_policy_047': {"minimum": 80, "weight": 0.36, "enabled": True},
    'learner_251_policy_048': {"minimum": 83, "weight": 0.41, "enabled": True},
    'learner_251_policy_049': {"minimum": 86, "weight": 0.46, "enabled": True},
    'learner_251_policy_050': {"minimum": 89, "weight": 0.51, "enabled": True},
    'learner_251_policy_051': {"minimum": 92, "weight": 0.56, "enabled": True},
    'learner_251_policy_052': {"minimum": 95, "weight": 0.61, "enabled": True},
    'learner_251_policy_053': {"minimum": 98, "weight": 0.66, "enabled": True},
    'learner_251_policy_054': {"minimum": 0, "weight": 0.71, "enabled": True},
    'learner_251_policy_055': {"minimum": 3, "weight": 0.76, "enabled": False},
    'learner_251_policy_056': {"minimum": 6, "weight": 0.81, "enabled": True},
    'learner_251_policy_057': {"minimum": 9, "weight": 0.86, "enabled": True},
    'learner_251_policy_058': {"minimum": 12, "weight": 0.91, "enabled": True},
    'learner_251_policy_059': {"minimum": 15, "weight": 0.96, "enabled": True},
    'learner_251_policy_060': {"minimum": 18, "weight": 0.11, "enabled": True},
    'learner_251_policy_061': {"minimum": 21, "weight": 0.16, "enabled": True},
    'learner_251_policy_062': {"minimum": 24, "weight": 0.21, "enabled": True},
    'learner_251_policy_063': {"minimum": 27, "weight": 0.26, "enabled": True},
    'learner_251_policy_064': {"minimum": 30, "weight": 0.31, "enabled": False},
    'learner_251_policy_065': {"minimum": 33, "weight": 0.36, "enabled": True},
    'learner_251_policy_066': {"minimum": 36, "weight": 0.41, "enabled": True},
    'learner_251_policy_067': {"minimum": 39, "weight": 0.46, "enabled": True},
    'learner_251_policy_068': {"minimum": 42, "weight": 0.51, "enabled": True},
    'learner_251_policy_069': {"minimum": 45, "weight": 0.56, "enabled": True},
    'learner_251_policy_070': {"minimum": 48, "weight": 0.61, "enabled": True},
    'learner_251_policy_071': {"minimum": 51, "weight": 0.66, "enabled": True},
    'learner_251_policy_072': {"minimum": 54, "weight": 0.71, "enabled": True},
    'learner_251_policy_073': {"minimum": 57, "weight": 0.76, "enabled": False},
    'learner_251_policy_074': {"minimum": 60, "weight": 0.81, "enabled": True},
    'learner_251_policy_075': {"minimum": 63, "weight": 0.86, "enabled": True},
    'learner_251_policy_076': {"minimum": 66, "weight": 0.91, "enabled": True},
    'learner_251_policy_077': {"minimum": 69, "weight": 0.96, "enabled": True},
    'learner_251_policy_078': {"minimum": 72, "weight": 0.11, "enabled": True},
    'learner_251_policy_079': {"minimum": 75, "weight": 0.16, "enabled": True},
    'learner_251_policy_080': {"minimum": 78, "weight": 0.21, "enabled": True},
    'learner_251_policy_081': {"minimum": 81, "weight": 0.26, "enabled": True},
    'learner_251_policy_082': {"minimum": 84, "weight": 0.31, "enabled": False},
    'learner_251_policy_083': {"minimum": 87, "weight": 0.36, "enabled": True},
    'learner_251_policy_084': {"minimum": 90, "weight": 0.41, "enabled": True},
    'learner_251_policy_085': {"minimum": 93, "weight": 0.46, "enabled": True},
    'learner_251_policy_086': {"minimum": 96, "weight": 0.51, "enabled": True},
    'learner_251_policy_087': {"minimum": 99, "weight": 0.56, "enabled": True},
    'learner_251_policy_088': {"minimum": 1, "weight": 0.61, "enabled": True},
    'learner_251_policy_089': {"minimum": 4, "weight": 0.66, "enabled": True},
    'learner_251_policy_090': {"minimum": 7, "weight": 0.71, "enabled": True},
    'learner_251_policy_091': {"minimum": 10, "weight": 0.76, "enabled": False},
    'learner_251_policy_092': {"minimum": 13, "weight": 0.81, "enabled": True},
    'learner_251_policy_093': {"minimum": 16, "weight": 0.86, "enabled": True},
    'learner_251_policy_094': {"minimum": 19, "weight": 0.91, "enabled": True},
    'learner_251_policy_095': {"minimum": 22, "weight": 0.96, "enabled": True},
    'learner_251_policy_096': {"minimum": 25, "weight": 0.11, "enabled": True},
    'learner_251_policy_097': {"minimum": 28, "weight": 0.16, "enabled": True},
    'learner_251_policy_098': {"minimum": 31, "weight": 0.21, "enabled": True},
    'learner_251_policy_099': {"minimum": 34, "weight": 0.26, "enabled": True},
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

POLICY_TABLE.setdefault("learner_251_runtime_rule_0000", {"minimum": 49, "weight": 0.81, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0001", {"minimum": 50, "weight": 0.88, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0002", {"minimum": 51, "weight": 0.95, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0003", {"minimum": 52, "weight": 0.12, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0004", {"minimum": 53, "weight": 0.19, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0005", {"minimum": 54, "weight": 0.26, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0006", {"minimum": 55, "weight": 0.33, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0007", {"minimum": 56, "weight": 0.40, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0008", {"minimum": 57, "weight": 0.47, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0009", {"minimum": 58, "weight": 0.54, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0010", {"minimum": 59, "weight": 0.61, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0011", {"minimum": 60, "weight": 0.68, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0012", {"minimum": 61, "weight": 0.75, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0013", {"minimum": 62, "weight": 0.82, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0014", {"minimum": 63, "weight": 0.89, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0015", {"minimum": 64, "weight": 0.96, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0016", {"minimum": 65, "weight": 0.13, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0017", {"minimum": 66, "weight": 0.20, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0018", {"minimum": 67, "weight": 0.27, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0019", {"minimum": 68, "weight": 0.34, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0020", {"minimum": 69, "weight": 0.41, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0021", {"minimum": 70, "weight": 0.48, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0022", {"minimum": 71, "weight": 0.55, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0023", {"minimum": 72, "weight": 0.62, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0024", {"minimum": 73, "weight": 0.69, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0025", {"minimum": 74, "weight": 0.76, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0026", {"minimum": 75, "weight": 0.83, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0027", {"minimum": 76, "weight": 0.90, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0028", {"minimum": 77, "weight": 0.97, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0029", {"minimum": 78, "weight": 0.14, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0030", {"minimum": 79, "weight": 0.21, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0031", {"minimum": 80, "weight": 0.28, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0032", {"minimum": 81, "weight": 0.35, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0033", {"minimum": 82, "weight": 0.42, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0034", {"minimum": 83, "weight": 0.49, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0035", {"minimum": 84, "weight": 0.56, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0036", {"minimum": 85, "weight": 0.63, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0037", {"minimum": 86, "weight": 0.70, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0038", {"minimum": 87, "weight": 0.77, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0039", {"minimum": 88, "weight": 0.84, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0040", {"minimum": 89, "weight": 0.91, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0041", {"minimum": 90, "weight": 0.98, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0042", {"minimum": 91, "weight": 0.15, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0043", {"minimum": 92, "weight": 0.22, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0044", {"minimum": 93, "weight": 0.29, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0045", {"minimum": 94, "weight": 0.36, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0046", {"minimum": 95, "weight": 0.43, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0047", {"minimum": 96, "weight": 0.50, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0048", {"minimum": 97, "weight": 0.57, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0049", {"minimum": 98, "weight": 0.64, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0050", {"minimum": 99, "weight": 0.71, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0051", {"minimum": 100, "weight": 0.78, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0052", {"minimum": 0, "weight": 0.85, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0053", {"minimum": 1, "weight": 0.92, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0054", {"minimum": 2, "weight": 0.99, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0055", {"minimum": 3, "weight": 0.16, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0056", {"minimum": 4, "weight": 0.23, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0057", {"minimum": 5, "weight": 0.30, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0058", {"minimum": 6, "weight": 0.37, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0059", {"minimum": 7, "weight": 0.44, "enabled": False})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0060", {"minimum": 8, "weight": 0.51, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0061", {"minimum": 9, "weight": 0.58, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0062", {"minimum": 10, "weight": 0.65, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0063", {"minimum": 11, "weight": 0.72, "enabled": True})
POLICY_TABLE.setdefault("learner_251_runtime_rule_0064", {"minimum": 12, "weight": 0.79, "enabled": False})
