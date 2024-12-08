from radon.complexity import cc_visit
from radon.metrics import mi_visit

def run_static_analysis(code_snippet):
    """
    Perform static analysis on the code snippet using Radon.
    """
    # Cyclomatic Complexity
    complexity_results = cc_visit(code_snippet)
    complexity_analysis = [
        {
            "function_name": item.name,
            "complexity": item.complexity,
            "line": item.lineno
        }
        for item in complexity_results
    ]

    # Maintainability Index
    mi_score = mi_visit(code_snippet, multi=False)

    return {
        "cyclomatic_complexity": complexity_analysis,
        "maintainability_index": mi_score
    }
