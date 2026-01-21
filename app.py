import streamlit as st
import os
import base64
import time
import pandas as pd
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Reuters Support Intelligence",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS: REUTERS PROFESSIONAL THEME ---
st.markdown("""
    <style>
    /* GLOBAL FONTS & COLORS */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;600;700&display=swap');
    
    .stApp { background-color: #FFFFFF; font-family: 'Noto Sans', sans-serif; color: #2D2D2D; }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] { background-color: #F8F8F8; border-right: 1px solid #E5E5E5; }
    
    /* BUTTON OVERRIDES */
    div.stButton > button:first-child {
        background-color: transparent;
        color: #444;
        border: none;
        text-align: left;
        padding-left: 0;
    }
    div.stButton > button:first-child:hover {
        color: #FF8000;
        background-color: transparent;
    }
    
    /* PRIMARY BUTTON (Start Session & Download) */
    button[kind="primary"], div.stDownloadButton > button {
        background-color: #FF8000 !important;
        border: 1px solid #FF8000 !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 4px !important;
        padding: 0.5rem 1rem !important;
    }
    button[kind="primary"]:hover, div.stDownloadButton > button:hover {
        background-color: #E67300 !important;
        border-color: #E67300 !important;
    }
    
    /* CHAT INTERFACE - Messages */
    .stChatMessage { background-color: #F9F9F9; border: 1px solid #EEE; border-radius: 4px; }
    .stChatMessage[data-testid="stChatMessageUser"] { background-color: #FFF; border-left: 3px solid #FF8000; }
    
    /* AVATAR SIZING */
    [data-testid="stChatMessageAvatar"] { background-color: transparent; border: none; }
    [data-testid="stChatMessageAvatar"] img { width: 32px; height: 32px; object-fit: contain; }

    /* CUSTOM FOOTER LINK */
    .footer-link {
        text-align: center;
        padding: 20px;
        margin-top: 50px;
        border-top: 1px solid #EEE;
        color: #888;
        font-size: 13px;
    }
    .footer-link a { color: #FF8000; text-decoration: none; font-weight: 600; }
    
    /* HIDE STREAMLIT UI */
    #MainMenu, header, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SESSION & NAVIGATION ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "messages" not in st.session_state:
    st.session_state.messages = []
    # INITIAL WELCOME MESSAGE
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Hi, I am Reuters Support Intelligence. How can I help you?"
    })

def navigate(target):
    st.session_state.page = target
    st.rerun()

# --- 4. BACKEND ---
@st.cache_resource
def load_engine():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = None
    if os.path.exists("./chroma_db"):
        db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    try:
        search = DuckDuckGoSearchRun()
    except:
        search = None
    return db, search

db, search_tool = load_engine()

# --- 5. SIDEBAR ---
with st.sidebar:
    # 1. LOGO
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)
    else:
        st.markdown("## REUTERS")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # NAVIGATION
    if st.button("Home"): navigate("home")
    if st.button("Support Intelligence"): navigate("chat")
    if st.button("Contact Support"): navigate("contact")
    
    st.divider()
    
    # === DROPDOWN VAULT ===
    if st.session_state.page == "chat":
        st.markdown("##### 📎 Attachments")
        uploaded_file = st.file_uploader("Upload Screenshot", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
        if uploaded_file:
            st.success("Image attached.")
        
        st.divider()

        st.caption("DOCUMENT VAULT")
        docs_dir = "documents"
        if os.path.exists(docs_dir):
            files = [f for f in os.listdir(docs_dir) if f.endswith('.pdf')]
            if files:
                selected_doc = st.selectbox("Select a technical guide:", files, index=None, placeholder="Choose document...")
                if selected_doc:
                    file_path = os.path.join(docs_dir, selected_doc)
                    with open(file_path, "rb") as file_data:
                        st.download_button(
                            label=f"Download {selected_doc}",
                            data=file_data,
                            file_name=selected_doc,
                            mime="application/pdf"
                        )
            else:
                st.caption("No PDFs available.")

# --- 6. PAGE: HOME ---
if st.session_state.page == "home":
    st.markdown("""
        <div style="padding: 40px; background-color: #111; color: white; margin-bottom: 30px;">
            <div style="font-size: 28px; font-weight: 600; margin-bottom: 10px;">YOUR SERVICE HUB FOR REUTERS NEWS AGENCY & CONTENT SOLUTIONS</div>
            <div style="font-size: 16px; font-weight: 300; color: #CCC;">Content Solutions & Technical Support Intelligence</div>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([0.65, 0.35], gap="large")
    
    with c1:
        st.markdown("""
        Here you can open service requests, submit feedback, find other tool-kits to support content delivery, download guides, and learn about our products.
        
        The team at **Reuters News Agency-Service and Support** make it our mission, and it’s our pleasure, to ensure that your customer experience is second to none.
        """)
        
        st.markdown("#### Solutions & Delivery")
        st.markdown("""
        Our content is delivered over a wide variety of mediums; either by internet or satellite. Our **Reuters Media Delivery Platform** offers solutions ranging from RSS to FTP Push.
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Start Intelligence Session", type="primary"):
            navigate("chat")

    with c2:
        st.info("""
        **Login Required**
        You must be logged in with any of your Reuters credentials to view available reference material.
        """)
    
    st.markdown("""
        <div class="footer-link">
            Visit <a href="https://www.reuters.com" target="_blank">Reuters.com</a> for global news coverage.
        </div>
    """, unsafe_allow_html=True)

# --- 7. PAGE: CONTACT ---
elif st.session_state.page == "contact":
    st.markdown("## Customer Support")
    st.markdown("You can use the following phone numbers to reach Reuters Customer Support or our TV Help Desk 24/7.")
    st.divider()
    
    st.info("""
    **Note on Branding:** With the formal separation of Thomson Reuters and Refinitiv now complete... the call center will begin using the name Refinitiv when answering support calls.
    """)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.button("Login to Live Chat", use_container_width=True)
    with c2: st.button("Email Us", use_container_width=True)
    with c3: st.button("Call Us", use_container_width=True)
    
    st.markdown("### Reuters Customer Support")
    st.table(pd.DataFrame({
        "Region": ["America", "Latin America", "Europe", "Middle East", "Asia Pacific"],
        "Service & Support Number": ["+1 (833) 282 6915", "+55 11 4700 8804", "+44 207 94 94864", "+35 777 788 558", "+81 3 6362 8225"]
    }).set_index("Region"))

# --- 8. PAGE: INTELLIGENCE (SOP CHAT) ---
elif st.session_state.page == "chat":
    st.markdown("### Support Intelligence")
    
    # SUGGESTED INQUIRIES
    if len(st.session_state.messages) <= 1:
        st.markdown("##### *Suggested Inquiries*")
        q1, q2 = st.columns(2)
        q3, q4 = st.columns(2)
        
        with q1:
            if st.button("“What are the Reuters Restrictions?”"):
                st.session_state.messages.append({"role": "user", "content": "What are the Reuters Restrictions for Broadcast?"})
                st.rerun()
        with q2:
            if st.button("“How do I handle an Opt-Out request?”"):
                st.session_state.messages.append({"role": "user", "content": "What is an Opt-Out request and how do I process it?"})
                st.rerun()
        with q3:
            if st.button("“Latest Global News Updates”"):
                st.session_state.messages.append({"role": "user", "content": "What are the latest global news headlines?"})
                st.rerun()
        with q4:
            if st.button("“Connect API Technical Guide”"):
                st.session_state.messages.append({"role": "user", "content": "Where can I find the Connect API technical guide?"})
                st.rerun()
        st.divider()

    # RENDER HISTORY
    for msg in st.session_state.messages:
        role_display = "You" if msg["role"] == "user" else "Reuters Intelligence"
        
        # AVATAR LOGIC
        if msg["role"] == "assistant":
            if os.path.exists("reuters.svg"):
                avatar_icon = "reuters.svg"
            elif os.path.exists("logo.png"):
                avatar_icon = "logo.png"
            else:
                avatar_icon = "🔴"
        else:
            avatar_icon = "👤"
        
        with st.chat_message(msg["role"], avatar=avatar_icon):
            st.caption(role_display)
            if "image" in msg:
                st.image(msg["image"], width=300)
            st.markdown(msg["content"])

    # FIXED INPUT
    if prompt := st.chat_input("Type your technical query..."):
        user_msg = {"role": "user", "content": prompt}
        image_data = None
        
        # CHECK SIDEBAR UPLOADER
        if uploaded_file:
            bytes_data = uploaded_file.getvalue()
            image_data = base64.b64encode(bytes_data).decode('utf-8')
            user_msg["image"] = bytes_data 
        
        st.session_state.messages.append(user_msg)
        st.rerun()

    # GENERATION
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        
        # PREPARE AVATAR
        if os.path.exists("reuters.svg"):
            avatar_gen = "reuters.svg"
        elif os.path.exists("logo.png"):
            avatar_gen = "logo.png"
        else:
            avatar_gen = "🔴"

        with st.chat_message("assistant", avatar=avatar_gen):
            st.caption("Reuters Intelligence")
            message_placeholder = st.empty()
            full_response = ""
            
            # --- 1. GET CONTEXT ---
            last_msg = st.session_state.messages[-1]
            prompt = last_msg["content"]
            
            internal_context = ""
            if db:
                # SAFE CALIBRATION: k=5 chunks @ 8000 chars each = ~10k tokens (Safe for limits)
                docs = db.similarity_search(prompt, k=5) 
                internal_context = "\n\n".join([d.page_content for d in docs])
            
            external_context = ""
            if search_tool and any(w in prompt.lower() for w in ["news", "latest", "today", "headlines"]):
                try: external_context = search_tool.run(f"site:reuters.com {prompt}")
                except: pass

            # --- 2. CONSTRUCT MEMORY ---
            conversation_history = []
            
            sys_msg = f"""
            You are a warm, expert Technical Consultant for Reuters. 
            You are helpful, respectful, and honest.

            ## INSTRUCTIONS:
            - **DO NOT** output headers like "PHASE 1", "PHASE 2".
            - **DO** speak naturally, like a human expert.
            - **DO** use clear paragraphs and bullet points.
            - **DO** maintain context from previous messages.

            ## DEEP DIVE PROTOCOL:
            - You have access to large documentation chunks. Read them fully.
            - If looking for a list (e.g., domains, IPs), extract ALL items found in the text.
            - If data is missing, admit it.

            ## CONTEXT:
            INTERNAL KNOWLEDGE:
            {internal_context}

            EXTERNAL NEWS:
            {external_context}
            """
            
            conversation_history.append(SystemMessage(content=sys_msg))
            
            # ADD HISTORY
            for m in st.session_state.messages[:-1]: 
                if m["role"] == "user":
                    conversation_history.append(HumanMessage(content=m["content"]))
                elif m["role"] == "assistant":
                    conversation_history.append(AIMessage(content=m["content"]))
            
            # ADD CURRENT PROMPT
            image_payload = None
            if "image" in last_msg:
                 image_payload = base64.b64encode(last_msg["image"]).decode('utf-8')
            
            if image_payload:
                conversation_history.append(HumanMessage(content=[
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_payload}"}}
                ]))
            else:
                conversation_history.append(HumanMessage(content=prompt))

            # --- 3. LLM CALL ---
            llm = ChatOpenAI(model_name="gpt-4o", temperature=0.2)
            
            response_stream = llm.stream(conversation_history)
            
            for chunk in response_stream:
                if chunk.content:
                    full_response += chunk.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
