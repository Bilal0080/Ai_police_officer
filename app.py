import streamlit as st
import pandas as pd
import numpy as np
import random

# Set the page config FIRST - this must be the first Streamlit command
st.set_page_config(page_title="A.I.O. - Police Dashboard", layout="wide")

# Main title
st.title("👮‍♂️ A.I.O. - Augmented Intelligence Operator")
st.markdown("**AI-Powered Policing Assistant Demo - Pakistan**")

# Sidebar for navigation
app_mode = st.sidebar.selectbox("Choose Module", 
    ["Dashboard", "Real-Time Analysis", "Report Assistant", "Ethics & Safeguards"])

# 1. DASHBOARD MODULE
if app_mode == "Dashboard":
    st.header("Patrol Command Dashboard - Pakistan")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Patrol Units", "15", "3")
    with col2:
        st.metric("Incidents Today", "22", "-5%")
    with col3:
        st.metric("Avg Response Time", "8.4 min", "1.2 min")
    with col4:
        st.metric("AI Assist Used", "63 times", "18 today")
    
    # Pakistan Map - Centered on Islamabad
    st.subheader("🇵🇰 Live Patrol Map - Pakistan")
    
    # Example patrol data with proper color mapping
    patrol_data = pd.DataFrame({
        'lat': [24.8607, 24.9200, 24.9300, 33.6844, 33.5651, 31.5497, 34.0151, 30.1798],
        'lon': [67.0011, 67.0200, 67.0500, 73.0479, 73.0169, 74.3436, 71.5249, 66.9750],
        'status': ['Active', 'Inactive', 'Busy', 'Active', 'Inactive', 'Busy', 'Active', 'Inactive'],
        'city': ['Karachi', 'Karachi', 'Karachi', 'Islamabad', 'Rawalpindi', 'Lahore', 'Peshawar', 'Quetta']
    })
    
    # Create a color column using hex codes (Streamlit prefers hex over RGB lists)
    status_colors = {
        'Active': '#00FF00',    # Green
        'Inactive': '#FF0000',  # Red
        'Busy': '#FFA500'       # Orange
    }
    
    patrol_data['color'] = patrol_data['status'].map(status_colors)
    patrol_data['size'] = 10  
    
    # Show the map with properly formatted color data
    st.map(patrol_data, size='size', color='color', use_container_width=True)
    
    # Display the patrol data
    with st.expander("View Patrol Details"):
        st.dataframe(patrol_data[['city', 'status', 'lat', 'lon']])
    
    # Pakistan-specific recent activity
    st.subheader("Recent AI-Assisted Activities in Pakistan")
    activity_data = {
        'Time': ['09:30', '11:15', '13:45', '15:20'],
        'City': ['Islamabad', 'Karachi', 'Lahore', 'Rawalpindi'],
        'Activity': ['License Plate Scan', 'Facial Recognition', 'Traffic Monitoring', 'Crowd Analysis'],
        'Result': ['Stolen Car Recovered', 'Wanted Person Identified', 'Traffic Flow Optimized', 'Peaceful Protest Monitored'],
        'Officer': ['ISB-42', 'KHI-15', 'LHR-23', 'RWP-08']
    }
    st.table(pd.DataFrame(activity_data))

# 2. REAL-TIME ANALYSIS MODULE
elif app_mode == "Real-Time Analysis":
    st.header("🔍 Real-Time AI Analysis - Pakistan Context")
    
    # Simulated camera feed analysis
    st.subheader("Live Bodycam Analysis")
    
    # Create two columns for before/after analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Live Camera Feed**")
        # You can replace this with actual Pakistani traffic images if available
        st.image("https://placekitten.com/600/400", caption="Simulated traffic scene in Pakistan")
    
    with col2:
        st.write("**AI Analysis Results**")
        
        # Simulated AI detection results
        with st.expander("Detected Objects", expanded=True):
            detection_data = {
                'Object': ['Motorcycle', 'Car', 'License Plate', 'Person', 'Traffic Sign'],
                'Confidence': ['97%', '95%', '99%', '92%', '98%'],
                'Status': ['Normal', 'Suspicious', 'Verified', 'Normal', 'Stop Sign']
            }
            st.table(pd.DataFrame(detection_data))
        
        # License plate check simulation
        st.success("✅ **License Plate Verified:** LEA 1234")
        st.error("🚨 **Alert:** Vehicle reported in recent incident")
        st.warning("⚠️ **Recommendation:** Proceed with caution and verify documents")

    # Pakistani context features
    st.subheader("Pakistan-Specific Features")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.write("**Language Translation**")
        st.info("Urdu to English: 'میں مدد چاہتا ہوں' → 'I need help'")
        st.info("Punjabi to English: 'ਮੈਨੂੰ ਮਦਦ ਦੀ ਲੋੜ ਹੈ' → 'I need assistance'")
    
    with col4:
        st.write("**Local Database Check**")
        st.success("✅ NADRA Verification: Complete")
        st.success("✅ Police Record: Clear")
        st.success("✅ Vehicle Registration: Valid")

# 3. REPORT ASSISTANT MODULE
elif app_mode == "Report Assistant":
    st.header("📝 AI Report Assistant")
    st.write("Automated report generation for Pakistani police procedures")
    
    # Report form
    with st.form("incident_report"):
        st.subheader("Incident Details")
        
        col1, col2 = st.columns(2)
        with col1:
            officer_id = st.text_input("Officer ID", "ISB-042")
            incident_type = st.selectbox("Incident Type", 
                ["Traffic Violation", "Theft", "Disturbance", "Accident", "Other"])
        with col2:
            location = st.selectbox("City", 
                ["Islamabad", "Karachi", "Lahore", "Rawalpindi", "Peshawar", "Other"])
            severity = st.select_slider("Severity Level", options=["Low", "Medium", "High", "Critical"])
        
        description = st.text_area("Incident Description", "Describe what happened...")
        
        submitted = st.form_submit_button("Generate AI Report")
    
    if submitted:
        st.success("✅ Report Generated Successfully!")
        st.subheader("AI-Generated Report Draft")
        
        report_text = f"""
        **PAKISTAN POLICE DEPARTMENT - INCIDENT REPORT**
        
        **Officer:** {officer_id}
        **Location:** {location}
        **Incident Type:** {incident_type}
        **Severity:** {severity}
        
        **Narrative:**
        Officer responded to a {incident_type.lower()} incident in {location}. {description}
        
        The situation was assessed and handled according to standard operating procedures 
        of the Pakistan Police Department.
        
        **Actions Taken:** Documentation completed, evidence collected, and relevant 
        authorities notified as per protocol.
        
        **AI Assistance:** This report was drafted with A.I.O. assistance to ensure 
        accuracy and compliance with departmental standards.
        """
        
        st.text_area("Report Content", report_text, height=300)
        st.download_button("Download Report", report_text, file_name=f"police_report_{location}.txt")

# 4. ETHICS & SAFEGUARDS MODULE
else:
    st.header("⚖️ Ethical Safeguards - Pakistan Implementation")
    
    st.warning("""
    **Important:** The A.I.O. system operates under strict ethical guidelines 
    tailored for Pakistan's legal and cultural context.
    """)
    
    tab1, tab2, tab3 = st.tabs(["Privacy Protection", "Bias Prevention", "Human Oversight"])
    
    with tab1:
        st.subheader("🇵🇰 Data Privacy Compliance")
        st.write("""
        - **PECA 2016 Compliance:** All data handling complies with Pakistan's Prevention of Electronic Crimes Act
        - **Local Data Storage:** All data remains within Pakistan's borders
        - **Citizen Privacy:** Strict protocols protect civilian privacy rights
        - **Audit Trails:** Complete logging of all system access and queries
        """)
    
    with tab2:
        st.subheader("Bias Mitigation Strategies")
        st.write("""
        - **Pakistan-specific training data** representing diverse demographics
        - **Regular algorithmic audits** for fairness across provinces
        - **Cultural sensitivity training** embedded in AI models
        - **Multi-lingual support** for Urdu, Punjabi, Pashto, and other regional languages
        """)
    
    with tab3:
        st.subheader("Human-in-the-Loop Protocol")
        st.error("""
        ⚠️ **CRITICAL PROTOCOL FOR PAKISTAN DEPLOYMENT** ⚠️
        
        The A.I.O. provides **recommendations only**. 
        The final decision and responsibility for any police action 
        **ALWAYS remains with the trained Pakistani police officer**.
        
        All AI recommendations must be verified and approved by a human officer 
        before any action is taken.
        """)

# Footer
st.markdown("---")
st.caption("A.I.O. - Augmented Intelligence Operator | Pakistan Police Department Simulation")