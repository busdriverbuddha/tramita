# tramita/sources/senado/utils.py

from datetime import date

import unicodedata


def _first_present(d: dict, fields: tuple[str, ...] = (
    "id",
)) -> str | None:
    """
    Return the first present, non-null identifier field from `d`,
    normalized as a string. Tries int() cast first to strip
    leading zeros and enforce numeric form when possible.
    """
    for f in fields:
        if f in d and d[f] is not None:
            try:
                return str(int(d[f]))
            except Exception:
                return str(d[f])
    return None


def _year_from(*candidates: str | None, default: int) -> int:
    for v in candidates:
        if isinstance(v, str) and len(v) >= 4 and v[:4].isdigit():
            try:
                return int(v[:4])
            except Exception:
                pass
    return int(default)


def _slugify_natureza(s: str) -> str:
    """
    "Permanente" -> "permanente"
    "Temporária" -> "temporaria"
    "Conselho"   -> "conselho"
    "Mesa"       -> "mesa"
    "Plenário"   -> "plenario"
    "Órgão"      -> "orgao"
    """
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s.strip().lower()


def _year_hits_legislatura(y: int, ini: date, fim: date) -> bool:
    ys, ye = date(y, 1, 1), date(y, 12, 31)
    return not (ye < ini or ys > fim)
