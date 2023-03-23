# DunderAI
> What character from The Office would say that quote?

![kevin_hotdogs](https://user-images.githubusercontent.com/44109284/226338232-02445a0f-b2ba-471f-a804-b0c00a8b1c0a.png)
![hotdog_ground_truth](https://user-images.githubusercontent.com/44109284/226338430-a1b7c179-f48b-4837-8636-338bbee814da.jpg)

DunderAI is a web application that uses deep learning with an LSTM model to predict which character from the popular TV show "The Office" is most likely to have said a given quote. With this application, users can test their knowledge of the show's characters and their mannerisms.

## How it Works
DunderAI uses a deep learning model trained on quotes from the top 21 characters in The Office. *Top 21 characters being the 21 characters with the most voice lines*

The model is built using Long Short-Term Memory (LSTM) networks, a type of recurrent neural network (RNN) that is particularly good at processing sequences of data. When a user inputs a quote, the model uses the input text to predict which character is most likely to have said it; model predictions are all based upon what language and speech patterns the LSTM could pick up on.

## Features
- Easy to use web interface
- Input new or adjusted quote to receive character prediction
- Ability to handle direct quotes accurately from any episode of "The Office" *even deleted scenes*


## Usage (localhost for now)
1. `conda env create -f environment.yml`
   1. `conda activate DunderAI`
2. `cd DunderAI && python managel.py`
3. Visit http://127.0.0.1:8000/ in your web browser.
4. Input a quote from "The Office" into the text field.
5. Click the "Submit" button to receive a prediction of which character said the quote.

https://user-images.githubusercontent.com/44109284/227211158-9cc58e89-ceb4-40c8-a090-01e058a4c548.mp4


## Credits
DunderAI was created by myself using Python, Fastai, Django, and HTML/CSS. The dataset used to train the LSTM model was obtained from [[Kaggle](https://www.kaggle.com/datasets/nasirkhalid24/the-office-us-complete-dialoguetranscript)]. This all started as a healthy competition with a friend to see who could train the better model- an excuse to learn more about NLP.

## License
DunderAI is licensed under the MIT License. Please see the LICENSE file for more information.

## Disclaimer
DunderAI is a fan project and is not affiliated with the TV show "The Office" or its creators in any way.
