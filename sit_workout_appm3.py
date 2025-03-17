import streamlit as st
import random
import pandas as pd

# Keep your existing exercise_details dictionary exactly as before (no changes needed here)

indoor_sprints = list(exercise_details.keys())[:4]
outdoor_sprints = list(exercise_details.keys())[4:8]
bodyweight_finishers = list(exercise_details.keys())[8:]

def generate_workout_plan():
    plan = []
    for week in range(1, 5):
        for day in ["Day 1", "Day 2"]:
            plan.append({
                "Week": f"Week {week} - {day}",
                "Indoor Sprint": random.choice(indoor_sprints),
                "Outdoor Sprint": random.choice(outdoor_sprints),
                "Bodyweight Finisher": random.choice(bodyweight_finishers)
            })
    return plan

# Streamlit App
def sit_workout_app():
    st.title("🏋️ SIT Workout Generator with Progress Tracker")

    if 'workout_plan' not in st.session_state:
        st.session_state.workout_plan = []

    if st.button("🔄 Generate New Weekly SIT Plan"):
        st.session_state.workout_plan = generate_workout_plan()
        st.session_state.completion_status = [False] * len(st.session_state.workout_plan)

    if st.session_state.workout_plan:
        st.markdown("---")
        st.header("🗓️ Your 4-Week SIT Workout Schedule")

        for idx, session in enumerate(st.session_state.workout_plan):
            st.subheader(session["Week"])
            cols = st.columns(3)

            for col, workout_type in zip(cols, ["Indoor Sprint", "Outdoor Sprint", "Bodyweight Finisher"]):
                exercise_name = session[workout_type]
                exercise = exercise_details[exercise_name]
                with col:
                    st.markdown(f"**{workout_type}: {exercise_name}**")
                    st.markdown(f"⏱️ Duration: {exercise['duration']}")
                    st.markdown(f"🔄 Repeat: {exercise['repeat']}")
                    st.image(exercise["image"], use_column_width=True)
                    st.caption(exercise["summary"])
                    with st.expander("📖 Steps to Perform"):
                        for idx_step, step in enumerate(exercise["steps"], 1):
                            st.markdown(f"{idx_step}. {step}")

            # Checkbox for workout completion
            st.session_state.completion_status[st.session_state.workout_plan.index(session)] = st.checkbox(
                f"✅ Mark '{session['Week']}' as completed",
                key=f"completed_{session['Week']}"
            )

            st.markdown("---")

        # Display Progress Summary
        completed_count = sum(st.session_state.completion_status)
        total_sessions = len(st.session_state.workout_plan)
        completion_percentage = (completion_status.count(True) / len(completion_status)) * 100 if len(completion_status) > 0 else 0

        st.header("📈 Workout Completion Summary")
        st.write(f"You've completed **{completion_percentage:.0f}% ({completion_status.count(True)} of {total_workouts})** sessions this month!")

        st.progress(completion_percentage / 100)

        # Optional detailed summary table
        df_summary = {
            "Workout Session": [s["Week"] for s in st.session_state.workout_plan],
            "Completed": st.session_state.completion_status
        }

        import pandas as pd
        df = pd.DataFrame(df)
        st.table(df)

if __name__ == "__main__":
    sit_workout_app()
