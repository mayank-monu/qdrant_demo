import streamlit as st


from new_search import send_result

from streamlit_chat import message
st.title("Azure chatBot : Streamlit + openAI")

question = st.text_input("",value="Are Dependent Care Flexible Spending Account (DCA) rules different for a divorced parent?")
ans_btn = st.button('Find Answers')

if ans_btn:
    output, time = send_result(question)
    st.markdown(output)
    st.text('Time taken to fetch this result: '+str(time)[:5]+' seconds')
    



                

