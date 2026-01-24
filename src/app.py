import gradio as gr
import pandas as pd
import pickle


# Main Fuction
def predict(
    Time_spent_Alone,
    Stage_fear,
    Social_event_attendance,
    Going_outside,
    Drained_after_socializing,
    Friends_circle_size,
    Post_frequency,
):
    input_df = pd.DataFrame(
        [
            Time_spent_Alone,
            Stage_fear,
            Social_event_attendance,
            Going_outside,
            Drained_after_socializing,
            Friends_circle_size,
            Post_frequency,
        ]
    )
    columns = [
        "Time_spent_Alone",
        "Stage_fear",
        "Social_event_attendance",
        "Going_outside",
        "Drained_after_socializing",
        "Friends_circle_size",
        "Post_frequency",
    ]
    # prediction
    with open("RF_Model.pkl", "rb") as file:
        model = pickle.load(file)
    prediction = model.predict(input_df)[0]
    return prediction
