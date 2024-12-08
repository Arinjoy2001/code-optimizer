import streamlit as st
from ai_analysis import analyze_code_with_ai
from static_analysis import run_static_analysis

# Streamlit UI
st.title("AI-Powered Code Optimization Tool")
st.write("Analyze your code for performance bottlenecks and get optimization suggestions!")

# File upload or text input
uploaded_file = st.file_uploader("Upload a Code File", type=["py", "txt"])
code_input = st.text_area("Or paste your code snippet below:")

if uploaded_file or code_input:
    code = uploaded_file.read().decode("utf-8") if uploaded_file else code_input

    # Display input code
    st.subheader("Your Code:")
    st.code(code, language="python")

    # Perform static analysis
    st.subheader("Static Analysis Results")
    static_results = run_static_analysis(code)
    if static_results:
        st.json(static_results)
    else:
        st.write("No issues found with static analysis.")

    # Perform AI analysis
    st.subheader("AI-Powered Suggestions")
    ai_results = analyze_code_with_ai(code)
    if ai_results:
        st.json(ai_results)
    else:
        st.write("No significant optimizations suggested.")

    # Download option for results
    st.download_button(
        label="Download Results",
        data=f"Static Analysis:\n{static_results}\n\nAI Suggestions:\n{ai_results}",
        file_name="analysis_results.txt",
        mime="text/plain",
    )

