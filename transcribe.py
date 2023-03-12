import whisper
import inquirer
import os
from colorama import Fore

# get all files in audio folder
audio_file_list = os.listdir('audio')

# early return if no audio files found
if len(audio_file_list) == 0:
    print(Fore.RED + "Error: No audio files found in /audio folder.")
    quit()

if len(audio_file_list) == 1:
    print(Fore.GREEN + f"Found only 1 file in audio folder. Using {audio_file_list[0]} for transcription.")

# wizard questions
questions = [
    inquirer.List('selected_audio_file',
                  message=f"Detected {len(audio_file_list)} audio files in /audio folder. Please select the one you want to transcribe: ",
                  choices=audio_file_list,
                  ignore=lambda x: len(audio_file_list) == 1
                  ),
    inquirer.Text('user_filename_input',
                  message="Please write a name for your file: "),
    inquirer.List('model',
                  message="Which model would you like to use? Larger models are more accurate, but also slower",
                  choices=['Tiny (fastest)', 'Base', 'Small', 'Medium', 'Large (most accurate)'],
                  default='Base',
                  ),
    inquirer.Text('prompt',
                  message="Describe the context of your audio in one sentence for potentially better results (optional)")
]

answers = inquirer.prompt(questions)

if len(audio_file_list) > 1:
    audio_file = answers['selected_audio_file']
else:
    audio_file = audio_file_list[0]

user_selected_model = answers['model'].split(' ')[0].lower()
initial_prompt = answers['prompt']

# TODO: estimate time based on file size or length?
print("📝 Transcribing...")

model = whisper.load_model(user_selected_model)
result = model.transcribe(f"audio/{audio_file}", fp16=False, language="English", initial_prompt=initial_prompt)

print(Fore.GREEN + "✅ Done transcribing")
print("Transcribed text: " + result["text"])

# format filename
formatted_filename_input = answers['user_filename_input'].lower().replace(" ", "_")
text_file_path = f"transcriptions/{formatted_filename_input}.txt"

# save transcription to .txt file
with open(text_file_path, "w+") as f:
    f.write(result["text"])

print(f"File saved to {text_file_path}")
os.system("open " + text_file_path)
