import gradio as gr
import pandas as pd
import pickle

# Loading The Model

with open("RF_Model.pkl", "rb") as file:
    model = pickle.load(file)


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
            [
                Time_spent_Alone,
                Stage_fear,
                Social_event_attendance,
                Going_outside,
                Drained_after_socializing,
                Friends_circle_size,
                Post_frequency,
            ]
        ],
        columns=[
            "Time_spent_Alone",
            "Stage_fear",
            "Social_event_attendance",
            "Going_outside",
            "Drained_after_socializing",
            "Friends_circle_size",
            "Post_frequency",
        ],
    )
    # prediction
    prediction = model.predict(input_df)[0]
    return f"🎉Hurrah...\nBy analyzing your data, We Found that You are an {prediction} Person."


inputs = [
    gr.Slider(0, 11, step=1, label="Average number of Hours Spend Alone in a day"),
    gr.Radio(["Yes", "No"], label="Do you Fear Performing in stage?"),
    gr.Slider(0, 10, step=1, label="Rate your Appearance in Social Events."),
    gr.Slider(
        0, 7, step=1, label="Rate your average number of Going outside in a week."
    ),
    gr.Radio(["Yes", "No"], label="Do you Feel Bad after getting Socialized?"),
    gr.Number(label="Number of Close Friends."),
    gr.Number(label="Frequency of posting in social media per week"),
]

app = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs="text",
    title="Checking Your Personality",
)
app.launch()
