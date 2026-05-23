#!/usr/bin/env python3
"""Ejecuta el notebook Colab y guarda salidas (gráficos, tablas)."""
import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "Colab_Piloto_5_Categorias_Riesgo_KKBox.ipynb"


async def run():
    import os

    os.environ.setdefault("MPLBACKEND", "module://matplotlib_inline.backend_inline")

    import nbformat
    from nbclient import NotebookClient

    nb = nbformat.read(NOTEBOOK, as_version=4)
    client = NotebookClient(
        nb,
        timeout=900,
        kernel_name="pdgrado-venv",
        resources={"metadata": {"path": str(ROOT)}},
    )
    # Ejecutar desde la raíz del proyecto
    orig = Path.cwd()
    try:
        import os

        os.chdir(ROOT)
        await client.async_execute()
    finally:
        os.chdir(orig)

    nbformat.write(nb, NOTEBOOK)
    print("Notebook ejecutado y guardado con salidas:", NOTEBOOK)


if __name__ == "__main__":
    # build fresh notebook first
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_colab_notebook

    build_colab_notebook.main()
    asyncio.run(run())
