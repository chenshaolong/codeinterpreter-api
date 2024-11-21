from codeinterpreterapi.session import CodeInterpreterSession
# import streamlit as st


def main(prompt_text):
    # st.title('Code Interpreter')
    
    # create a session and close it automatically
    with CodeInterpreterSession() as session:
        # generate a response based on user input
        response = session.generate_response(
            prompt_text
        )
        # output the response
        response.show()


if __name__ == "__main__":
    # prompt_text = '请画一个爱心'
    prompt_text = '请实现快排算法'
    # prompt_text = '请实现二分算法'
    # prompt_text = '请找出1000以内的质数，并将结果保存'
    main(prompt_text)