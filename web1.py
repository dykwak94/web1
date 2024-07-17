import streamlit as st
import google.generativeai as genai


def get_recommendations(body_part, workout_type):
    genai.configure(api_key='AIzaSyCvJ1kAUwogUcM1PgTt6E5-92zbdLLLyJk')
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Recommend a workout for {body_part} for {workout_type} training.
    Format your response exactly as follows:
    Exercise: [Name of exercise]
    Sets and Reps: [Number of sets and reps]
    """
    
    try:
        response = model.generate_content(prompt)
        if response.text:
            lines = response.text.strip().split('\n')
            exercise = lines[0].split(': ')[1] if len(lines) > 0 else "No specific recommendation"
            sets_reps = lines[1].split(': ')[1] if len(lines) > 1 else "Consult a fitness professional"
            return exercise, sets_reps
        else:
            st.error("Empty response from Gemini API")
            return "No recommendation", "N/A"
    except Exception as e:
        st.error(f"Error calling Gemini API: {str(e)}")
        return "Error occurred", "Please try again" 

# App layout
st.title("Workout Recommendation")

# Step 1: Choose the part of the body
body_part = st.selectbox("Choose the Part of Body:",["arm","leg","chest","back","shoulder","abs"])


# Step 3: What type of workout are you planning
workout_type = st.selectbox("What type of workout are you planning to?", ["hypertrophy", "strength", "interval"])

# Step 4: Show recommendation
if st.button("Recommended WOD"):
    exercise, sets_reps = get_recommendations(body_part, workout_type)
    st.subheader("Recommended Exercise")
    st.write(f"Exercise: {exercise}")
    st.write(f"Sets and Reps: {sets_reps}")

#if __name__ == "__main__":
    #get_recommendations(body_part,  workout_type)
