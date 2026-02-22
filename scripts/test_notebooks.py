"""
Test all notebooks execute without errors.
Run: python scripts/test_notebooks.py
"""
import subprocess
import sys
import os
import glob
import time
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NBCONVERT = os.path.join(REPO, '.venv', 'bin', 'jupyter-nbconvert')

def test_notebook(path):
    """Execute a notebook and return (success, error_msg, duration)."""
    rel = os.path.relpath(path, REPO)
    start = time.time()
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = os.path.join(tmpdir, 'output.ipynb')
            result = subprocess.run(
                [
                    NBCONVERT,
                    '--to', 'notebook',
                    '--execute',
                    '--ExecutePreprocessor.timeout=120',
                    '--ExecutePreprocessor.kernel_name=formacion-bi',
                    '--output', out_path,
                    path
                ],
                capture_output=True,
                text=True,
                timeout=180,
                cwd=os.path.dirname(path)
            )
        duration = time.time() - start
        if result.returncode == 0:
            return True, None, duration
        else:
            stderr = result.stderr
            lines = stderr.strip().split('\n')
            # Find CellExecutionError or last meaningful error
            error_lines = []
            capture = False
            for line in lines:
                if 'CellExecutionError' in line or 'Error' in line or 'Exception' in line:
                    capture = True
                if capture:
                    error_lines.append(line)
            if not error_lines:
                error_lines = lines[-15:]
            return False, '\n'.join(error_lines[-15:]), duration
    except subprocess.TimeoutExpired:
        duration = time.time() - start
        return False, "TIMEOUT (>180s)", duration
    except Exception as e:
        duration = time.time() - start
        return False, str(e), duration

def main():
    # Find all notebooks
    patterns = [
        os.path.join(REPO, 'modulo-*/notebooks/*.ipynb'),
        os.path.join(REPO, 'modulo-*/laboratorios/*soluciones*.ipynb'),
        os.path.join(REPO, 'modulo-04-proyectos-integradores/templates/ejemplo_proyecto_completo.ipynb'),
    ]

    notebooks = []
    for pat in patterns:
        notebooks.extend(sorted(glob.glob(pat)))

    # Skip exercise-only labs (no code to run) and solution labs
    # Only test content notebooks and solution notebooks
    content_nbs = [n for n in notebooks if '/laboratorios/' not in n]
    solution_nbs = [n for n in notebooks if 'soluciones' in n]

    all_nbs = sorted(content_nbs + solution_nbs)

    print(f"Testing {len(all_nbs)} notebooks...\n")
    print(f"{'Notebook':<70} {'Status':>8} {'Time':>8}")
    print("-" * 90)

    passed = 0
    failed = 0
    errors = []

    for nb in all_nbs:
        rel = os.path.relpath(nb, REPO)
        # Truncate long paths
        display = rel if len(rel) <= 68 else '...' + rel[-65:]
        print(f"{display:<70} ", end='', flush=True)

        success, error, duration = test_notebook(nb)

        if success:
            print(f"{'PASS':>8} {duration:>7.1f}s")
            passed += 1
        else:
            print(f"{'FAIL':>8} {duration:>7.1f}s")
            failed += 1
            errors.append((rel, error))

    print("-" * 90)
    print(f"\nResults: {passed} passed, {failed} failed, {len(all_nbs)} total\n")

    if errors:
        print("=" * 90)
        print("FAILURES:\n")
        for rel, error in errors:
            print(f"--- {rel} ---")
            print(error)
            print()

    sys.exit(0 if failed == 0 else 1)

if __name__ == '__main__':
    main()
