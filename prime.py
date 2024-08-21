import streamlit as st 
n=1
n=int(st.number_input("Enter the number to check", value=None, placeholder="Type a number..."))
#n=int(n)
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
if st.button("Check"):
    if(c==2):
        st.success("Prime")
    else:
        st.error("Not Prime")


           
    
