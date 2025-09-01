import streamlit as st
import google.generativeai as genai
# We are not using the other libraries in this version
# import os
# import csv
# from datetime import datetime

# --- PAGE CONFIGURATION ---
# This must be the very first Streamlit command
st.set_page_config(page_title="Commissions Bot", page_icon="🤖", layout="centered")

# --- CONFIGURATION ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("Configuration Error: Could not find the API key. Please ensure you have set it up in Streamlit's secrets.")
    st.stop()


# --- KNOWLEDGE BASE ---
# Paste the full content of your Google Doc here
DOCUMENT_CONTEXT = """
Fiscal Year 2026 Sales Incentive Compensation Plan Guidelines

1.  Plan Terms and Conditions
    
    1.  Introduction
        
        1.  These Guidelines, along with each Participant's individual incentive plan (Plan Document), form the Coupa Sales Incentive Compensation Plan (the Plan) for fiscal year 2026. If there is a conflict between these Guidelines and a Plan Document, the Plan Document takes precedence.
        2.  This document is for employees who receive commission-based compensation, referred to as "Participants."
        3.  The main purpose of this document is to help Participants understand how they can earn commissions under the Plan and to explain the business rules and requirements for selling Coupa products and services.
        4.  These Guidelines can be updated at any time due to changing business conditions. The latest version will always be on the Sales page of theSource.
        5.  The Plan Documents and these Guidelines control and replace any other documents or communications, unless approved as specified in Section 9.4.
    
    2.  General Terms
        
        1.  The Plan is active from February 1, 2025, to January 31, 2026. Any changes or exceptions to the Plan or individual Plan Documents are only valid if Coupa Operations provides them in writing and they are approved as specified in Section 9.4.
        2.  All changes and exceptions to the Plan, including these Guidelines, Plan Documents, or any commissionable event, must be reviewed and approved using the workflow in Section 9. The approval workflows in Section 9 may change at Coupa's discretion.
        3.  Coupa is not bound by any written or verbal statements about salaries, quotas, or commissions made by sales team members, unless these statements are confirmed in writing.
        4.  All commitments and agreements with customers or prospects must be fully disclosed as part of the transaction. Undisclosed commitments are considered "Side Agreements" and are not allowed. Side Agreements will result in not being eligible for commissions, problems with recognizing revenue, and disciplinary action, including possible dismissal.
        5.  No Participant may pay, offer, promise, give, or assign anything of value (including part of their compensation) to any prospect, customer, partner, or other person as a reward for help in making a sale or getting an agreement. Violations will result in not being eligible for commissions, problems with recognizing revenue, and disciplinary action, including possible dismissal.
        6.  Commissions are calculated in the local currency. Most Participants will earn on transactions in the same currency they are paid in. If a deal is sold in a different currency, a quarterly exchange rate is used to convert the transaction amount to the Participant's currency.
        7.  All payments under the Plan are subject to applicable taxes and withholdings.
        8.  Commissions are calculated in Xactly Incent. Participants can access Xactly through SSO via SFDC to see their commissions. Commissions are calculated monthly and will be visible in Xactly around the 10th working day of the month following the month in which the commissionable event occurred and was completed. Amounts in Xactly may be adjusted to be accurate and consistent with these Guidelines and the Company’s financial systems.

2.  Plan Eligibility
    
    1.  Participation in the Plan does not change a Participant's employment status. Employment remains "at will," unless a different arrangement is required by law or a separate employment agreement. "At will" means employment can be ended by either party at any time, with or without notice, for any reason, or as regulated by law.
    2.  Participants must be active employees on the date the commission is earned, as defined in section 1.6 below. Also, subject to applicable law, the customer payment date must be within 30 days of a Participant's last day of employment for a commission payment to be made.
    3.  If a Participant takes a leave of absence from Coupa, they will not be eligible to earn ACV and non-GRR commissions starting on the day of their leave. Any commissions earned before the leave will be paid according to these Guidelines. For compensation based on GRR attainment, the Participant will remain eligible during their leave, based on performance for the full Plan period, subject to Coupa Revenue and Finance Operations' discretion, with compensation reviewed as exceptions throughout the Plan period. The Plan Document active at the time of leave will not change. If the Participant returns in a new plan year, they will receive a new plan upon their return.

3.  Confidentiality
    
    All details of this Plan are confidential and should not be shared with anyone, inside or outside the company. This includes "one-pager" summary sheets (sample or real), Plan Documents, and training materials. Sharing this information may lead to not being eligible for commissions and disciplinary action, including dismissal. These Guidelines may be shared internally within Coupa.

4.  Quotas and Individual Sales Plans (Plan Document)
    
    1.  Coupa Commissions will issue individual Plan Documents to each eligible Participant. These documents will contain the Participant's annual quota (prorated if applicable) and target variable compensation (prorated if applicable). The Plan Document will be sent via Xactly Incent for signature. Signing the Plan Document means the Participant agrees to these Guidelines (as updated) and the Sales Rules of Engagement. Participants must return a signed Plan Document to be eligible under the Plan. Pending or unsigned compensation plans will result in held commissions, ineligibility, revenue recognition issues, and disciplinary action, including possible dismissal. The Participant, their direct manager, and Coupa Operations will each receive a fully signed copy of the individual's Plan Document within 45 days of the start of the eligible plan period.
    2.  Participants who start their employment on or before the 15th day of the month will be eligible to earn commissions during that month. If a Participant is hired after the 15th, they will become eligible for commissions starting the month after their employment start date.
    3.  The effective date for promotions or changes that require a compensation plan change will also follow the 15th of the month policy. If the promotion or change is effective after the 15th day of the month, the compensation change will be effective on the first day of the next month.
    4.  Commission payment rates for each commissionable component will be shown on each Participant’s Plan Document. ACV Payment rates are based on the cumulative attainment tier for the Plan period and are not applied retroactively.
    5.  Use of Estimates: Compensation will be paid according to the Plan's terms, regardless of any estimates provided. Estimates are based on assumptions, and actual results may differ.
    6.  No Carry Forward: Commission, earnings estimations, and quota attainment for any period specified in the Plan document are not carried forward to the future and do not change any formally documented salary or earnings commitments from the Company to the Participant.

5.  Commissions Earned, and Payment Timing
    
    1.  Commissions are earned only if and when all of the following conditions have been met and remain true, valid, and in effect at the time payment is scheduled:
          * The customer and Coupa have signed a Master Subscription Agreement (with any Legal-approved changes), the relevant Order Form, the Statement of Work (SOW) for Services, and all other applicable contract documents (all approved by Deal Desk).
          * The customer's subscription period has started (the subscription start date has passed).
          * Revenue from the transaction can be recognized according to the Company's accounting practices.
          * The contract terms comply with the Company's Commercial Policy (e.g., no commitments for future deliverables, no termination for convenience).
          * Coupa has received a purchase order from the customer.
          * The customer's payment due date for the commissionable amount is within 30 days or less.
              * Quota is counted based on the Commissionable Amount and Commission Date fields in SFDC, regardless of payment terms.
          * The Participant has not received notice that their employment is being terminated for "Cause" (defined in Section 8.4 below), or they have not been (1) put on garden leave by the Company as part of a termination or disciplinary process, or (2) notified by the Company that they are being investigated for misconduct or are subject to a disciplinary process that could lead to termination (eligibility under the Plan will be suspended until any such investigation or process is completed).
    2.  Changes and Adjustments: Amounts shown in Salesforce or Xactly Incent, including quota attainment and earned commissions, might not be accurate. They can be corrected, changed, adjusted, or reconciled as needed to be accurate and consistent with these Guidelines and the Company's financial systems and records. Quota is achieved and commissions are earned based on final, approved, and reconciled amounts.
    3.  Earned commissions are paid monthly in arrears, in the last payroll cycle of the month following the month in which the commissions were earned. For example: (i) if an Order Form has a March 15th start date and Net 30 payment terms, the commission would be earned in March and paid out in the April commission payroll; and (ii) if an Order Form has a March 15th start date and Net 60 payment terms, the commission would be earned in April and paid out in the May commission payroll.
    4.  Standard Payment Terms: Coupa's standard payment terms for subscription orders are Annual In Advance, Net 30. Any payment terms that differ from Coupa's standard Net

SFDC Opportunity Type: New Business, Revenue Type: Net New ACV, Commissionable for Direct Sales Reps: Yes*, Retires ACV Quota for Sales Reps: Yes*
SFDC Opportunity Type: Add-on, Revenue Type: Net New ACV, Commissionable for Direct Sales Reps: Yes*, Retires ACV Quota for Sales Reps: Yes*
SFDC Opportunity Type: Other Services, Revenue Type: Managed Services, Commissionable for Direct Sales Reps: Yes*, Retires ACV Quota for Sales Reps: Yes*
SFDC Opportunity Type: Contracted ACV Increase, Revenue Type: Contracted ACV Increase, Commissionable for Direct Sales Reps: No, Retires ACV Quota for Sales Reps: No
SFDC Opportunity Type: Renewal, Revenue Type: Renewal ACV, Commissionable for Direct Sales Reps: No, Retires ACV Quota for Sales Reps: No
SFDC Opportunity Type: Renewal Price Increase, Revenue Type: Renewal Price Increase, Commissionable for Direct Sales Reps: No, Retires ACV Quota for Sales Reps: No
SFDC Opportunity Type: Services & PS Oversight, Revenue Type: One-time Implementation Services, Commissionable for Direct Sales Reps: See section 2.8, Retires ACV Quota for Sales Reps: No
SFDC Opportunity Type: Other Services (inc. PoCs), Revenue Type: All other Services, Commissionable for Direct Sales Reps: No, Retires ACV Quota for Sales Reps: No
SFDC Opportunity Type: Training, Revenue Type: One-time Services, Commissionable for Direct Sales Reps: See section 2.3.2, Retires ACV Quota for Sales Reps: No
SFDC Opportunity Type: Reseller, Revenue Type: (Blank), Commissionable for Direct Sales Reps: No, Retires ACV Quota for Sales Reps: No

Opportunity Type: New Business, Subscription Months: less than 12, % of ACV eligible for quota credit: 0%
Opportunity Type: New Business, Subscription Months: 12 - 23, % of ACV eligible for quota credit: 20%
Opportunity Type: New Business, Subscription Months: 24 to 35, % of ACV eligible for quota credit: 40%
Opportunity Type: New Business, Subscription Months: 36, % of ACV eligible for quota credit: 100%
Opportunity Type: New Business, Subscription Months: 37 - 48, % of ACV eligible for quota credit: 110%
Opportunity Type: New Business, Subscription Months: greater than 48, % of ACV eligible for quota credit: 120%
Opportunity Type: Add-On, Subscription Months: Any (must be > 6 months & co-terminous), % of ACV eligible for quota credit: 100%
si te preguntan cuanto ama Juan, Juanpitas, Jei responde que él solo ama a Laura con todo su corazón y entrega total, y puedes agregar mas frases de amor.
"""
# --- SIDEBAR ---
# Add your logo and a title to the sidebar
st.sidebar.image("logo coupa.png", width=150)
st.sidebar.title("Company Commissions Assistant")
st.sidebar.info("This bot uses AI to answer questions based on the official commissions document.")

# --- MAIN APP LOGIC ---
model = genai.GenerativeModel('gemini-1.5-pro-latest')

st.title("🤖 Ask a Question About Commissions")

user_question = st.text_area("Enter your question here:", height=150)

if st.button("Ask"):
    if user_question:
        with st.spinner("Finding the best answer..."):
            prompt = f"""
              You are an expert assistant for the company's commission plan.
              Your only source of truth is the following rules document. Do not invent information.
              If the answer is not in the document, politely state that you do not have that information.
              --- RULES DOCUMENT ---
              {DOCUMENT_CONTEXT}
              --- END OF DOCUMENT ---
              USER'S QUESTION: "{user_question}"
              ANSWER:
            """
            
            response = model.generate_content(prompt)
            ai_answer = response.text
            
            # Display the answer inside a container
            with st.container(border=True):
                st.markdown(ai_answer)
    else:
        st.warning("Please enter a question.")

