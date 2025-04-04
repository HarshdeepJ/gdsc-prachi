# import streamlit as st
# # from user_pages.dashboard import dashboard
# # from user_options.forgot_password_pg import show_forgot_password_page
# # from user_options.signup_pg import show_create_account_page
# # from user_options.login_pg import show_login_page
# from auth_functions import *
# from user_options.profile_entry import main_profile


# def rate_us_button():
#     @st.dialog("How do you rate our app?")
#     def rate():
#         sentiment_mapping = ["one", "two", "three", "four", "five"]
#         selected = st.feedback("stars")
#         if selected is not None:
#             st.session_state.rate = {"item": sentiment_mapping[selected]}
#             # st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
#             st.rerun()
#     rate()
#     return


# # Set up the page config
# st.set_page_config(page_title="Financial Agent", page_icon="💰", layout="wide")

# def entry_point():
#     st.title("My main entry point :D")

#     "This is a string written with :violet[***magic***]"


# if 'user_info' in st.session_state:
#     # Define the pages for logged-in users

#     # st.title("Welcome to Financial Agent")
#     # Sidebar with buttons for account selection

#     # nav_login = st.navigation(
#     #     [
#     #         st.Page('account_settings/user_controls.py', title="Profile", default=True),  # Magic works
#     #         st.Page("user_pages/dashboard.py", title="Dashboard"),
#     #         st.Page(sign_out, title="Sign Out"),  # Magic works
#     #         st.Page("user_options/profile_entry.py", title="Set Profile"),
#     #         st.Page("user_pages/money_tracker.py", title="Finanace Tracker"),
#     #         st.Page("user_pages/fraud_detector.py", title="Fraud Alert"),
#     #         st.Page("user_pages/quiz.py", title="Quiz"),
#     #         st.Page("user_pages/news.py", title="News"),
#     #         st.Page("user_pages/govt_schemes.py", title="Govt Schemes"),
#     #     ]
#     # )


#     with st.sidebar:
#         nav_login = st.navigation(
#             [
#                 # st.Page('account_settings/user_controls.py', title="Profile"),  # Magic works
#                 st.Page("user_pages/dashboard.py", title="Dashboard", default=True),
#                 # st.Page(sign_out, title="Sign Out"),  # Magic works
#                 # st.Page("user_options/profile_entry.py", title="Set Profile"),
#                 st.Page("user_pages/money_tracker.py", title="Finanace Tracker"),
#                 st.Page("user_pages/lessons.py", title=" Finance Lessons"),
#                 st.Page("user_pages/advisor.py", title="Finanace Advisor"),
#                 st.Page("user_pages/fraud_detector.py", title="Fraud Alert"),
#                 st.Page("user_pages/quiz.py", title="Quiz"),
#                 st.Page("user_pages/news.py", title="News"),
#                 st.Page("user_pages/govt_schemes.py", title="Govt Schemes"),
#                 st.Page("user_pages/dictionary.py", title="Dictionary"),
#                 st.Page("user_pages/chatbot.py", title="Chatbot"),
#             ]
#         )

#         # # Add empty space to push buttons to the bottom
#         # for _ in range(23):  # Adjust the number of empty lines as needed
#         #     st.write("")

#         # Add buttons at the bottom
#         col1, col2, col3 = st.columns([1, 1, 1])
#         with col1:
#             if st.button("Profile", key="profile_button"):
#                 main_profile()  # Trigger the profile function when the button is pressed
#         with col2:
#             if st.button("Sign Out", key="sign_out_button"):
#                 sign_out()  # Trigger the sign_out function when the button is pressed
#         with col3:
#             if st.button("Rate Us", key="rate_us_button"):
#                 # rate_us_button()
#                 if "rate" not in st.session_state:
#                     rate_us_button()  # Trigger the sign_out function when the button is pressed
#                 else:
#                     f"You gave us {st.session_state.rate['item']} stars!"


        
#         # if st.button("Sign Out", key="sign_out_button"):
#         #     sign_out()  # Trigger the sign_out function when the button is pressed

#         # if st.button("Profile", key="profile_button"):
#         #     main_profile()  # Trigger the sign_out function when the button is pressed

#     nav_login.run()

# else:
#     st.title("Welcome to Financial Agent")
#     # Sidebar with buttons for account selection

#     nav = st.navigation(
#         [
#             st.Page(entry_point, title="Introduction", default=True),  # Magic works
#             st.Page("user_options/login_pg.py", title="Log In"),  # Magic does not work
#             st.Page("user_options/signup_pg.py", title="Sign Up"),  # Magic works
#             # st.Page("user_options/forgot_password_pg.py", title="Reset Password"),  # Magic works
#         ]
#     )
#     nav.run()


'''
import streamlit as st
# from user_pages.dashboard import dashboard
# from user_options.forgot_password_pg import show_forgot_password_page
# from user_options.signup_pg import show_create_account_page
# from user_options.login_pg import show_login_page
from auth_functions import *
# from account_settings.user_controls import main_profile


initialize_firebase_once()

def rate_us_button():
    @st.dialog("How do you rate our app?")
    def rate():
        sentiment_mapping = ["one", "two", "three", "four", "five"]
        selected = st.feedback("stars")
        if selected is not None:
            st.session_state.rate = {"item": sentiment_mapping[selected]}
            # st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
            st.rerun()
    rate()
    return

# st.markdown("""
#     <style>
#         /* Smaller Button */
#         .stButton>button {
#             background: var(--primary);
#             color: white;
#             border-radius: 8px;
#             padding: 10px 20px; /* Reduced from 12px 24px */
#             font-weight: 500;
#             transition: opacity 0.2s ease;
#         }

#         .stButton>button:hover {
#             opacity: 0.9;
#         }
#     </style>""", unsafe_allow_html=True)

# Set up the page config
st.set_page_config(page_title="Financial Agent", page_icon="💰", layout="wide")

def entry_point():
    st.title("My main entry point :D")

    "This is a string written with :violet[***magic***]"


if 'user_info' in st.session_state:
    initialize_firebase()
    user_info = st.session_state.user_info
    user_id = user_info['localId']  # Get the user ID from session state
    st.session_state.user_id = user_id
    # print("USER ID: ",user_id)
    nav_login = []
    # Define the pages for logged-in users

    # st.title("Welcome to Financial Agent")
    # Sidebar with buttons for account selection

    # nav_login = st.navigation(
    #     [
    #         st.Page('account_settings/user_controls.py', title="Profile", default=True),  # Magic works
    #         st.Page("user_pages/dashboard.py", title="Dashboard"),
    #         st.Page(sign_out, title="Sign Out"),  # Magic works
    #         st.Page("user_options/profile_entry.py", title="Set Profile"),
    #         st.Page("user_pages/money_tracker.py", title="Finanace Tracker"),
    #         st.Page("user_pages/fraud_detector.py", title="Fraud Alert"),
    #         st.Page("user_pages/quiz.py", title="Quiz"),
    #         st.Page("user_pages/news.py", title="News"),
    #         st.Page("user_pages/govt_schemes.py", title="Govt Schemes"),
    #     ]
    # )


    with st.sidebar:
        nav_login = st.navigation(
            [
                # st.Page('account_settings/user_controls.py', title="Profile"),  # Magic works
                st.Page("user_pages/dashboard.py", title="Dashboard", default=True),
                # st.Page(sign_out, title="Sign Out"),  # Magic works
                # st.Page("user_options/profile_entry.py", title="Set Profile"),
                # st.Page("user_pages/money_tracker.py", title="Finanace Tracker"),
                st.Page("user_pages/lessons.py", title=" Finance Lessons"),
                st.Page("user_pages/advisor.py", title="Finanace Advisor"),
                st.Page("user_pages/fraud_detector.py", title="Fraud Alert"),
                st.Page("user_pages/quiz.py", title="Quiz"),
                st.Page("user_pages/news.py", title="News"),
                st.Page("user_pages/govt_schemes.py", title="Govt Schemes"),
                st.Page("user_pages/dictionary.py", title="Dictionary"),
                st.Page("user_pages/chatbot.py", title="Chatbot"),
                # st.Page("account_settings/user_controls.py", title="Profile"),
                st.Page("user_pages/discussion_forum.py", title = "Discussion_Forum"),
                st.Page("user_options/profile_entry.py", title="Profile"),
            ]
        )

        # # Add empty space to push buttons to the bottom
        # for _ in range(23):  # Adjust the number of empty lines as needed
        #     st.write("")

        # Add buttons at the bottom
        col1, col2 = st.columns([1, 1])
        # with col1:
        #     if st.button("Profile", key="profile_button"):
        #         main_profile()  # Trigger the profile function when the button is pressed
        with col1:
            if st.button("Sign Out", key="sign_out_button"):
                sign_out()  # Trigger the sign_out function when the button is pressed
        with col2:
            if st.button("Rate Us", key="rate_us_button"):
                # rate_us_button()
                if "rate" not in st.session_state:
                    rate_us_button()  # Trigger the sign_out function when the button is pressed
                else:
                    f"You gave us {st.session_state.rate['item']} stars!"


        
        # if st.button("Sign Out", key="sign_out_button"):
        #     sign_out()  # Trigger the sign_out function when the button is pressed

        # if st.button("Profile", key="profile_button"):
        #     main_profile()  # Trigger the sign_out function when the button is pressed

    nav_login.run()

else:
    st.markdown("<h1 style='text-align: center; font-size: 60px; font-weight: bold;'>Welcome to FinFriend</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p>Discover tools, resources, and advice to make informed financial decisions.</p>
        <p>Explore personalized financial advice, track savings, detect fraud schemes, and much more.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    initialize_firebase()
    # Sidebar with buttons for account selection

    nav = st.navigation(
        [
            st.Page("user_pages/dashboard.py",title="Introduction", default=True),  # Magic works
            st.Page("user_options/login_pg.py", title="Log In"),  # Magic does not work
            st.Page("user_options/signup_pg.py", title="Sign Up"),  # Magic works
            # st.Page("user_options/forgot_password_pg.py", title="Reset Password"),  # Magic works
        ]
    )
    nav.run()

'''

import streamlit as st
from auth_functions import *
# Import your page functions or ensure they are discoverable
# from user_pages.dashboard import show_dashboard # Example import
# from user_options.profile_entry import main_profile # Example import

# --- Initialization ---
initialize_firebase_once() # Ensure Firebase is initialized only once

# --- Page Configuration ---
st.set_page_config(
    page_title="FinFriend - Your Financial Companion",
    page_icon="💰", # Consider using a custom emoji or favicon link
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
# Apply styles inspired by streamlit.io's landing page
st.markdown("""
    <style>
        /* --- General --- */
        html, body, [class*="st-"], button, input, textarea {
            font-family: 'Source Sans Pro', sans-serif; /* Clean sans-serif font */
        }

        /* --- Main Content Area --- */
         .main .block-container {
            padding-top: 3rem; /* More space at the top */
            padding-bottom: 3rem;
            padding-left: 3rem;
            padding-right: 3rem;
            max-width: 1100px; /* Limit max width like many websites */
            margin: auto; /* Center the block container */
        }

        /* --- Hero Section (Introduction Page) --- */
        .hero-section {
            text-align: center;
            padding: 3rem 0; /* Vertical padding */
            margin-bottom: 3rem; /* Space below hero */
        }
        .hero-title {
            font-size: 3.8rem; /* Larger, bolder title */
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 1rem;
            color: #0e1117; /* Streamlit's dark text color */
        }
        
        .hero-subtitle {
            font-size: 1.4rem; /* Larger, bolder title */
            font-weight: 500;
            line-height: 0.9;
            margin-bottom: 1rem;
            color: #555; /* Streamlit's dark text color */
        }
        .hero-cta-text {
            font-size: 1.1rem;
            color: #333;
        }
         /* Style links within CTA text if needed */
        .hero-cta-text a {
            color: var(--primary-color); /* Use Streamlit's primary color */
            text-decoration: none;
            font-weight: 600;
        }
        .hero-cta-text a:hover {
            text-decoration: underline;
        }


        /* --- Feature Highlight Styling (Optional Refinement) --- */
        .feature-section {
            padding: 2rem 0;
        }
        .feature-box {
            background-color: #ffffff; /* White background */
            padding: 25px;
            border-radius: 10px; /* Slightly more rounded */
            text-align: center;
            border: 1px solid #e0e0e0; /* Lighter border */
            height: 100%;
            transition: box-shadow 0.2s ease-in-out, transform 0.2s ease-in-out;
            display: flex; /* Use flexbox for alignment */
            flex-direction: column;
            justify-content: center; /* Center content vertically */
        }
        .feature-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.08); /* Slightly stronger shadow */
        }
        .feature-icon {
            font-size: 2.8rem;
            margin-bottom: 15px;
            color: var(--primary-color); /* Use primary color for icons */
        }
        .feature-title {
            font-size: 1.2rem; /* Larger feature title */
            font-weight: 600;
            margin-bottom: 10px;
            color: #0e1117;
        }
        .feature-desc {
            font-size: 0.95rem;
            color: #333;
            line-height: 1.5;
        }

        /* --- Sidebar Styling --- */
        [data-testid="stSidebar"] {
            /* background-color: #f8f9fa; /* Optional: Light background for sidebar */
            padding-bottom: 2rem; /* Ensure space at bottom */
        }
        .stButton>button[key*='_button'] {
            width: 100%;
            margin-bottom: 8px;
            border-radius: 6px; /* Slightly less rounded buttons */
        }
        .sidebar-footer {
            margin-top: 40px; /* More space above footer */
            border-top: 1px solid #e0e0e0;
            padding-top: 20px;
        }
        [data-testid="stSidebarNav"] ul {
             padding-top: 1rem; /* Add some padding above nav items */
             padding-bottom: 1rem; /* Add some padding below nav items */
        }
         [data-testid="stSidebarNav"] ul li > div[role="button"] {
             padding-top: 0.6rem; /* Adjust vertical padding of nav items */
             padding-bottom: 0.6rem;
             border-radius: 6px; /* Match button radius */
         }

         /* Make Rate Us / Sign Out buttons less prominent */
         .stButton>button[key*='_sidebar'][type='secondary'] {
             background-color: transparent;
             color: #555;
             border: 1px solid #ddd;
         }
         .stButton>button[key*='_sidebar'][type='secondary']:hover {
             color: #000;
             border-color: #bbb;
             background-color: #f0f0f0;
         }

    </style>
""", unsafe_allow_html=True)

# --- Helper Functions ---

def rate_us_dialog():
    """Shows the rating dialog."""
    @st.dialog("How do you rate FinFriend?")
    def rate():
        sentiment_mapping = ["one", "two", "three", "four", "five"]
        selected = st.feedback("stars", key="rating_feedback_stars") # Use a unique key
        if selected is not None:
            st.session_state.user_rating = {"stars": sentiment_mapping[selected - 1]}
            st.success(f"Thank you for rating us {selected} star(s)!")
            st.rerun()
        else:
            st.write("Please select a star rating.")

    rate()

def show_introduction_page():
    """Displays the content for the logged-out introduction page, styled like streamlit.io."""

    # --- Hero Section ---
    st.markdown("""
    <div class='hero-section'>
        <div class='hero-title'>Take Control of Your Financial Future</div>
        <p class='hero-subtitle'>FinFriend provides the tools, insights, and guidance you need to manage your money confidently and achieve your financial goals.</p>
        <p class='hero-cta-text'>
            Ready to get started? Use the sidebar menu to <strong>Sign Up</strong> or <strong>Log In</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider() # Visual separator

    # --- Features Section ---
    st.markdown("<div class='feature-section'>", unsafe_allow_html=True)
    st.subheader("Key Features", anchor=False, help="Explore what FinFriend offers") # Add help tooltip
    st.write("") # Spacer

    col1, col2, col3 = st.columns(3, gap="large") # Increase gap between columns

    with col1:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>💡</div>
            <div class='feature-title'>Personalized Insights</div>
            <p class='feature-desc'>Receive tailored financial advice and track progress towards your unique goals.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>🛡️</div>
            <div class='feature-title'>Stay Secure</div>
            <p class='feature-desc'>Learn to identify potential scams and protect your finances with our fraud detection tips.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
         st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>📚</div>
            <div class='feature-title'>Boost Your Knowledge</div>
            <p class='feature-desc'>Engage with lessons, quizzes, news, and resources to enhance your financial literacy.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# --- Main App Logic --- # Get auth and db objects

if 'user_info' in st.session_state:
    # --- LOGGED-IN VIEW ---
    user_info = st.session_state.user_info
    user_id = user_info['localId']
    st.session_state.user_id = user_id

    user_email = user_info.get('email', 'User')

    with st.sidebar:
        # Simple welcome, could fetch profile name later
        st.subheader(f"Welcome!")
        st.caption(user_email) # Display email smaller
        st.divider()

        pages_logged_in = [
            st.Page("user_pages/dashboard.py", title="Dashboard", icon="📊", default=True),
            #st.Page("user_pages/money_tracker.py", title="Finance Tracker", icon="💸"),
            st.Page("user_pages/lessons.py", title="Finance Lessons", icon="🎓"),
            st.Page("user_pages/advisor.py", title="Finance Advisor", icon="🤖"),
            st.Page("user_pages/fraud_detector.py", title="Fraud Alert", icon="🛡️"),
            st.Page("user_pages/quiz.py", title="Quiz", icon="❓"),
            st.Page("user_pages/news.py", title="News", icon="📰"),
            st.Page("user_pages/govt_schemes.py", title="Govt Schemes", icon="🏦"),
            st.Page("user_pages/dictionary.py", title="Dictionary", icon="📖"),
            st.Page("user_pages/chatbot.py", title="Chatbot", icon="💬"),
            st.Page("user_pages/discussion_forum.py", title="Discussion Forum", icon="🗣️"),
            st.Page("user_options/profile_entry.py", title="My Profile", icon="👤"),
        ]
        nav_selection_logged_in = st.navigation(pages_logged_in)

        # Sidebar Footer Buttons
        st.markdown("<div class='sidebar-footer'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            # Use type="secondary" for less emphasis
            if st.button("Sign Out", key="sign_out_button_sidebar", type="secondary"):
                sign_out()
        with col2:
            if st.button("Rate Us", key="rate_us_button_sidebar", type="secondary"):
                if "user_rating" not in st.session_state:
                    rate_us_dialog()
                # If already rated, clicking might reopen or do nothing based on dialog logic
                # Displaying message below is cleaner

        # Show rating message persistently if rated
        if "user_rating" in st.session_state:
            st.success(f"Thanks for your {st.session_state.user_rating['stars']} star rating!")
            # Consider adding a small button/link to "Change rating?" which could clear session state and call dialog again.
            # if st.button("Change rating?", key="change_rating", type="small"): # Needs custom small button CSS or use link
            #      del st.session_state.user_rating
            #      st.rerun() # Rerun to make Rate Us button active again

        st.markdown("</div>", unsafe_allow_html=True)


    # Run the selected page function
    nav_selection_logged_in.run()

else:
    # --- LOGGED-OUT VIEW ---
    with st.sidebar:
        # Use an emoji or potentially load a small logo image
        st.markdown("### 💰 FinFriend")
        # st.sidebar.title("FinFriend") # Alternative styling
        st.sidebar.divider()

        pages_logged_out = [
            st.Page(show_introduction_page, title="Introduction", icon="👋", default=True),
            st.Page("user_options/login_pg.py", title="Log In", icon="🔑"),
            st.Page("user_options/signup_pg.py", title="Sign Up", icon="📝"),
            # st.Page("user_options/forgot_password_pg.py", title="Reset Password", icon="❓"), # Optional
        ]
        nav_selection_logged_out = st.navigation(pages_logged_out)

    # Run the selected page function (which will be show_introduction_page by default)
    nav_selection_logged_out.run()