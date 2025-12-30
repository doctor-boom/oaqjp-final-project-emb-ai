''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows the emotional processing,
        including it's dominant emotional score
    '''
    # Retrieve the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the analyzer
    response = emotion_detector(text_to_analyze)

    # Process the response
    a_score = response['anger']
    d_score = response['disgust']
    f_score = response['fear']
    j_score = response['joy']
    s_score = response['sadness']
    dom_emotion = response['dominant_emotion']
    if a_score is not None:
        dom_emotion = dom_emotion[0]

    r_text = f"For the given statement, the system response is 'anger': {a_score}, \
    'disgust': {d_score}, 'fear': {f_score}, 'joy': {j_score} and 'sadness': {s_score}. \
    The dominant emotion is {dom_emotion}"

    # Return a formatted string
    if dom_emotion is None:
        return "Invalid text! Please try again!"

    # no_else return
    return r_text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000

    app.run(host="0.0.0.0", port=5000)
