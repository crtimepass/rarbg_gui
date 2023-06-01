import json
import streamlit as st
from streamlit import session_state as state

# Load the JSON data from the file
with open('output.json') as json_file:
    data = json.load(json_file)

# Create a search function
def search(query, tag):
    results = []
    for item in data:
        if query.lower() in item['title'].lower() and (tag is None or tag == item['tag']):
            results.append(item)
        if state.stop:
            break
    return results

# Create the Streamlit web app
def main():
    st.title("Search Rarbg Data")
    query = st.text_input("Enter search query:")
    tag = st.selectbox("Filter by Tag (Optional):", [None] + list(set(item['tag'] for item in data)))
    
    if st.button("Search"):
        state.stop = False
        results = search(query, tag)
        count = len(results)
        st.write("Search Results Count:", count)
        if results:
            st.write("Search Results:")
            for result in results:
                st.write("Title:", result['title'])
                st.markdown(f"Magnet Link: [{result['magnet_link']}]({result['magnet_link']})")
                st.write("Tag:", result['tag'])
                st.write("---")
        else:
            st.write("No results found.")

if __name__ == '__main__':
    main()
