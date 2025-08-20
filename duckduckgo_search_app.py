import streamlit as st
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

# Streamlit UI
st.title("DuckDuckGo Search App")
st.write("Search anything from DuckDuckGo")

# User inputs
query = st.text_input("Enter your search query", "")
search_type = st.selectbox(
    "Select search type",
    ["text", "news", "images", "videos"]
)

max_results = st.slider("Number of results", 1, 10, 5)

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching..."):
            # Configure API wrapper dynamically
            api = DuckDuckGoSearchAPIWrapper(source=search_type, max_results=max_results)

            # Configure Tool
            search_tool = DuckDuckGoSearchResults(api_wrapper=api, output_format="list")

            results = search_tool.invoke(query)

        if results:
            st.subheader(f"Top {len(results)} {search_type} results for: {query}")

            # Display results
            for i, item in enumerate(results, start=1):
                if isinstance(item, dict):
                    # Normal results with dict structure
                    st.markdown(f"**{i}. [{item.get('title','')}]({item.get('link','')})**")
                    st.write(item.get("snippet", ""))
                    st.caption(item.get("date", ""))
                    st.write("---")
                else:
                    # Some formats (like images) may return plain strings/URLs
                    st.write(f"{i}. {item}")
        else:
            st.warning("No results found.")
    else:
        st.warning("Please enter a query.")
