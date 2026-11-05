#!/usr/bin/env python3
"""Comprueba los IDs documentados y genera un reporte de trazabilidad."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
ALCANCE_REQUISITOS = {"REQ-001", "REQ-002", "REQ-007", "REQ-010", "REQ-015"}
ALCANCE_CASOS_USO = {"CU-001", "CU-002", "CU-003", "CU-006"}


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def first_column_ids(path, prefix):
    ids = []
    for line in read(path).splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if line.startswith("|") and re.fullmatch(prefix, cells[0]):
            ids.append(cells[0])
    return ids


def refs(value, prefix):
    return set(re.findall(r"\b" + prefix + r"\b", value))


def main():
    sources = {
        "REQ": first_column_ids("docs/SRS.md", r"REQ-\d{3}"),
        "RNF": first_column_ids("docs/SRS.md", r"RNF-\d{3}"),
        "CU": first_column_ids("docs/CU.md", r"CU-\d{3}"),
        "CLS": re.findall(r'<mxCell id="(CLS-[A-Za-z]+)"', read("modelos/clases.drawio")),
        "PRU": first_column_ids("pruebas/pruebas.md", r"PRU-\d{3}"),
    }
    rows = []
    for line in read("matrices/trazabilidad.md").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and re.fullmatch(r"REQ-\d{3}", cells[0]):
            rows.append((cells[0], refs(cells[2], r"CU-\d{3}"),
                         refs(cells[3], r"CLS-[A-Za-z]+"), refs(cells[4], r"PRU-\d{3}")))

    errors = []
    matrix_reqs = [row[0] for row in rows]
    if len(matrix_reqs) != len(set(matrix_reqs)):
        errors.append("Hay requisitos repetidos en la matriz.")
    for kind, ids in sources.items():
        if len(ids) != len(set(ids)):
            errors.append(f"Hay IDs {kind} repetidos en el artefacto de origen.")
    missing = ALCANCE_REQUISITOS - set(matrix_reqs)
    extra = set(matrix_reqs) - ALCANCE_REQUISITOS
    unknown_reqs = (ALCANCE_REQUISITOS | set(matrix_reqs)) - set(sources["REQ"])
    if missing:
        errors.append("Requisitos del alcance sin fila: " + ", ".join(sorted(missing)))
    if extra:
        errors.append("Requisitos fuera del alcance: " + ", ".join(sorted(extra)))
    if unknown_reqs:
        errors.append("Requisitos sin SRS: " + ", ".join(sorted(unknown_reqs)))

    for i, kind in enumerate(("CU", "CLS", "PRU"), start=1):
        linked = set().union(*(row[i] for row in rows)) if rows else set()
        unknown = linked - set(sources[kind])
        expected = ALCANCE_CASOS_USO if kind == "CU" else set(sources[kind])
        unlinked = expected - linked
        if kind == "CU" and linked - ALCANCE_CASOS_USO:
            errors.append("CU fuera del alcance: " + ", ".join(sorted(linked - ALCANCE_CASOS_USO)))
        if unknown:
            errors.append(f"{kind} sin artefacto: " + ", ".join(sorted(unknown)))
        if unlinked:
            errors.append(f"{kind} sin requisito en matriz: " + ", ".join(sorted(unlinked)))
    for req, cus, classes, tests in rows:
        if not (cus and classes and tests):
            errors.append(f"{req} carece de CU, CLS o PRU en su fila.")

    covered = sum(bool(cus and classes and tests
                       and cus <= set(sources["CU"])
                       and classes <= set(sources["CLS"])
                       and tests <= set(sources["PRU"]))
                  for _, cus, classes, tests in rows)
    total = len(ALCANCE_REQUISITOS)
    lines = [
        "# Reporte de trazabilidad (sesión 12)", "",
        "Generado con `python3 scripts/verificar-trazabilidad.py` a partir de los artefactos del repositorio.", "",
        f"Requisitos del alcance seleccionado con CU, CLS y PRU: **{covered}/{total}**.",
        f"Cobertura del alcance seleccionado: **{covered / total * 100:.0f} %**.",
        f"Catálogo completo: {len(sources['REQ'])} requisitos funcionales, {len(sources['RNF'])} no funcionales y {len(sources['CU'])} casos de uso.",
        f"Artefactos del alcance seleccionado: {total} REQ, {len(ALCANCE_CASOS_USO)} CU, {len(sources['CLS'])} CLS y {len(sources['PRU'])} PRU.",
        "", "| Requisito | Casos de uso | Clases | Pruebas |", "|---|---|---|---|",
    ]
    for req, cus, classes, tests in rows:
        lines.append("| " + " | ".join((req, ", ".join(sorted(cus)),
                                       ", ".join(sorted(classes)), ", ".join(sorted(tests)))) + " |")
    lines += ["", "## Comprobación bidireccional", ""]
    lines += ["Referencias del alcance seleccionado verificadas en ambos sentidos." if not errors else "Inconsistencias encontradas:"]
    lines += [f"- {error}" for error in errors]
    lines += ["", "La cobertura expresa la correspondencia documental de los cinco requisitos seleccionados.", ""]
    output = ROOT / "reportes/trazabilidad-s12.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"{output.relative_to(ROOT)}: {covered}/{total} requisitos vinculados, {len(errors)} inconsistencias")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
