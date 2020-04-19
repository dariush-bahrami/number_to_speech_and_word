def number_to_speech(number, play=True, save=False,
                     save_folder='numbers_mp3_files'):
    from gtts import gTTS
    from playsound import playsound
    import os

    language = 'en'

    speech_object = gTTS(text=str(number), lang=language, slow=False)

    if save:
        if not os.path.isdir(save_folder):
            os.mkdir(save_folder)

        mp3_path = f'{save_folder}/{number}.mp3'

        speech_object.save(mp3_path)

    if play:
        playsound(mp3_path)

    return speech_object

if __name__ == '__main__':
    number = 42
    number_to_speech(number,play=True, save=True)
