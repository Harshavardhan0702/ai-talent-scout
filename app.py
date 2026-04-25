import streamlit as st
import json
import pandas as pd
from utils import extract_skills, calculate_match_score, simulate_interest

st.set_page_config(page_title="AI Talent Scout", layout="wide")

st.title("🤖 AI-Powered Talent Scouting & Engagement Agent")
st.caption("Automated candidate discovery, matching, engagement, and ranking system")

# Input JD
jd = st.text_area("📄 Enter Job Description", height=200)

if st.button("🔍 Find Candidates"):

    if not jd.strip():
        st.warning("Please enter a Job Description")

    else:
        # Load candidates
        with open("candidates.json") as f:
            candidates = json.load(f)

        # Extract skills
        required_skills = extract_skills(jd)

        st.subheader("🧠 Extracted Skills from JD")
        if required_skills:
            st.success(", ".join(required_skills))
        else:
            st.warning("No relevant skills detected")

        results = []

        # Process candidates
        for candidate in candidates:
            match_score, matched_skills, missing_skills = calculate_match_score(candidate, required_skills)

            response, interest_score = simulate_interest(match_score)

            final_score = round(0.7 * match_score + 0.3 * interest_score, 2)

            results.append({
                "name": candidate["name"],
                "match_score": match_score,
                "interest_score": interest_score,
                "final_score": final_score,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "response": response
            })

        # Sort results
        results = sorted(results, key=lambda x: x["final_score"], reverse=True)

        st.subheader("🏆 Ranked Candidates")

        # Top candidate
        st.success(f"🏆 Top Candidate: {results[0]['name']} (Score: {results[0]['final_score']})")

        # Chart
        df = pd.DataFrame(results)
        st.subheader("📊 Candidate Ranking Chart")
        st.bar_chart(df.set_index("name")["final_score"])

        # Display candidates
        for r in results:
            explanation = f"Matched {len(r['matched_skills'])}/{len(required_skills)} required skills"

            st.markdown(f"""
            ### 👤 {r['name']}
            - ✅ Match Score: {r['match_score']}%
            - 💬 Interest Score: {r['interest_score']}
            - ⭐ Final Score: {r['final_score']}
            - 🧠 Explanation: {explanation}
            - 🧩 Matched Skills: {', '.join(r['matched_skills']) if r['matched_skills'] else 'None'}
            - ❌ Missing Skills: {', '.join(r['missing_skills']) if r['missing_skills'] else 'None'}
            - 🤖 Candidate Response: {r['response']}
            """)
            st.divider()