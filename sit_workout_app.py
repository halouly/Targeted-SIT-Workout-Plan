import streamlit as st
import random
import pandas as pd

# Exercise details dictionary (complete and correct)
exercise_details = {
    "Treadmill Sprint": {
        "image": "Images/treadmill sprint.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Intense treadmill sprint for calorie burn.",
        "steps": [
            "Warm-up jog 1 minute.",
            "Sprint 30 sec at max effort.",
            "Rest 1 min by slow walking.",
            "Repeat 4 rounds."
        ]
    },
    "Bike Sprint": {
        "image": "Images/bike sprint.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Bike sprints for lower-body strength.",
        "steps": [
            "Pedal lightly for warm-up.",
            "Sprint intensely for 30 sec.",
            "Rest gently pedaling for 1 min.",
            "Repeat 4 rounds."
        ]
    },
    "Rowing Sprint": {
        "image": "Images/rowing sprint.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Rowing for full-body cardio.",
        "steps": [
            "Row gently for warm-up.",
            "Row at max intensity for 30 sec.",
            "Rest 1 min at easy pace.",
            "Repeat 4 rounds."
        ]
    },
    "Battle Rope Slams": {
        "image": "Images/battle rope slams.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Upper-body explosive cardio workout.",
        "steps": [
            "Warm-up gently with rope waves.",
            "Perform intense rope slams for 30 sec.",
            "Rest for 1 min.",
            "Repeat 4 rounds."
        ]
    },
    "Flat Sprints": {
        "image": "Images/flat sprints.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Outdoor flat sprints.",
        "steps": [
            "Light jog warm-up.",
            "Sprint at full speed for 30 sec.",
            "Rest for 1 min by walking.",
            "Repeat 4 rounds."
        ]
    },
    "Hill Sprints": {
        "image": "Images/hill sprints.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Strength-focused uphill sprints.",
        "steps": [
            "Jog gently uphill for warm-up.",
            "Sprint uphill at max intensity for 30 sec.",
            "Walk down slowly for 1 min rest.",
            "Repeat 4 rounds."
        ]
    },
    "Stair Sprints": {
        "image": "Images/stair sprints.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Stairs for power and cardio.",
        "steps": [
            "Walk stairs slowly to warm-up.",
            "Sprint upstairs rapidly for 30 sec.",
            "Rest by descending slowly (1 min).",
            "Repeat 4 rounds."
        ]
    },
    "Sand Sprints": {
        "image": "Images/sand sprints.webp",
        "duration": "30 sec",
        "repeat": "4 rounds (Rest 1 min between)",
        "summary": "Sprints on sand to improve agility.",
        "steps": [
            "Light jogging to warm-up.",
            "Sprint at full pace on sand for 30 sec.",
            "Walk slowly to recover (1 min).",
            "Repeat 4 rounds."
        ]
    },
    "Jump Squats": {
        "image": "Images/jump squats.webp",
        "duration": "1 min",
        "repeat": "3 rounds (Rest 1 min between)",
        "summary": "Explosive lower-body exercise.",
        "steps": [
            "Start standing; squat down deeply.",
            "Explode upward into a jump.",
            "Land softly and repeat continuously for 1 min.",
            "Rest 1 min; perform 3 rounds total."
        ]
    },
    "Burpees": {
        "image": "Images/burpees.webp",
        "duration": "1 min",
        "repeat": "3 rounds (Rest 1 min between)",
        "summary": "Full-body intensive burpees.",
        "steps": [
            "From standing, squat and place hands down.",
            "Kick legs back to plank, then jump feet forward.",
            "Jump upward explosively.",
            "Continue for 1 min; rest 1 min; repeat 3 rounds."
        ]
    },
    "Plank Shoulder Taps": {
        "image": "Images/plank shoulder taps.webp",
        "duration": "1 min",
        "repeat": "3 rounds (Rest 1 min between)",
        "summary": "Core and shoulder stability.",
        "steps": [
            "Assume plank position.",
            "Alternate tapping shoulders for 1 min.",
            "Rest 1 min; repeat 3 rounds."
        ]
    },
    "Russian Twists": {
        "image": "Images/russian twists.webp",
        "duration": "1 min",
        "repeat": "3 rounds (Rest 1 min between)",
        "summary": "Core-strengthening rotational exercise.",
        "steps": [
            "Sit, lean back slightly with feet off ground.",
            "Rotate torso side-to-side for 1 min.",
            "Rest 1 min; repeat 3 rounds."
        ]
    }
}


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
                    st.image(exercise["image"], use_container_width=True)
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
