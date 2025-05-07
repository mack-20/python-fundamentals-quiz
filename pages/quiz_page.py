import streamlit as st
import traceback

# ----- Quiz Data -----
QUESTIONS = [
    {
        "description": "1. Write a function `add_numbers(a, b)` that returns the sum of `a` and `b`.",
        "function_name": "add_numbers",
        "template": "def add_numbers(a, b):\n    # Your code here\n    return 0",
        "test_code": "assert add_numbers(2, 3) == 5\nassert add_numbers(-1, 1) == 0"
    },
    {
        "description": "2. Write a function `reverse_list(lst)` that returns the reversed list.",
        "function_name": "reverse_list",
        "template": "def reverse_list(lst):\n    # Your code here\n    return lst",
        "test_code": "assert reverse_list([1, 2, 3]) == [3, 2, 1]\nassert reverse_list([]) == []"
    },
    {
        "description": "3. Write a function `is_even(n)` that returns `True` if `n` is even, otherwise `False`.",
        "function_name": "is_even",
        "template": "def is_even(n):\n    # Your code here\n    return False",
        "test_code": "assert is_even(2) == True\nassert is_even(3) == False"
    }
]

# ----- App State -----
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "user_code" not in st.session_state:
    st.session_state.user_code = QUESTIONS[0]['template']

# ----- App UI -----
st.set_page_config(page_title="Python Quiz App", layout="centered")
st.title("🧪 Python Fundamentals Quiz")
st.markdown("Solve each problem by writing the correct function. You must pass the tests to continue!")

q = QUESTIONS[st.session_state.current_question]
st.subheader(q["description"])
code_input = st.text_area("✍️ Write your code here:", value=st.session_state.user_code, height=200)

if st.button("▶️ Submit Code"):
    try:
        local_env = {}
        exec(code_input, {}, local_env)
        exec(q["test_code"], {}, local_env)
        st.success("✅ All tests passed! Moving to next question.")
        st.session_state.feedback = ""
        st.session_state.current_question += 1
        if st.session_state.current_question < len(QUESTIONS):
            st.session_state.user_code = QUESTIONS[st.session_state.current_question]['template']
        else:
            st.balloons()
    except AssertionError:
        st.error("❌ Test failed! Try again.")
        st.session_state.feedback = traceback.format_exc()
    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.session_state.feedback = traceback.format_exc()

# ----- Feedback -----
if st.session_state.feedback:
    with st.expander("🔍 See error details"):
        st.code(st.session_state.feedback, language='python')

# ----- End Screen -----
if st.session_state.current_question >= len(QUESTIONS):
    st.success("🎉 You've completed all questions!")
    st.stop()
