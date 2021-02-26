import matplotlib as mpl
import numpy as np
import os
import shutil
import librosa
from pydub import AudioSegment as seg
def renameFiles():
    fileNum = 0
    for file in os.listdir('dataset/Crema/'):
        newName = ''
        try:
            if 'ANG' in file:
                newName = 'dataset/Crema/ANG{}.wav'.format(fileNum)
                os.rename('dataset/Crema/'+file, newName)
            if 'HAP' in file:
                newName = 'dataset/Crema/HAP{}.wav'.format(fileNum)
                os.rename('dataset/Crema/'+file, newName)
            if 'FEA' in file:
                newName = 'dataset/Crema/FEA{}.wav'.format(fileNum)
                os.rename('dataset/Crema/'+file, newName)
            if 'SAD' in file:
                newName = 'dataset/Crema/SAD{}.wav'.format(fileNum)
                os.rename('dataset/Crema/'+file, newName)
            if 'DIS' in file:
                newName = 'dataset/Crema/DIS{}.wav'.format(fileNum)
                os.rename('dataset/Crema/'+file, newName)
            if 'NEU' in file:
                newName = 'dataset/Crema/NEU{}.wav'.format(fileNum)
                os.rename('dataset/Crema/'+file, newName)
        except FileNotFoundError:
            pass
        fileNum+=1
    for actor in os.listdir('dataset/Ravdess/audio_speech_actors_01-24/'):
        for file in os.listdir('dataset/Ravdess/audio_speech_actors_01-24/{}'.format(actor)):
            newName = ''
            try:
                if file.split('-')[2] == '01':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/NEU{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
                if file.split('-')[2] == '02':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/CAL{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
                if file.split('-')[2] == '03':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/HAP{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
                if file.split('-')[2] == '04':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/SAD{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
                if file.split('-')[2] == '05':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/ANG{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
                if file.split('-')[2] == '06':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/FEA{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
                if file.split('-')[2] == '07':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/DIS{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
                if file.split('-')[2] == '08':
                    newName = 'dataset/Ravdess/audio_speech_actors_01-24/{}/SUP{}.wav'.format(actor, fileNum)
                    os.rename('dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(actor, file), newName)
            except IndexError:
                pass
            fileNum += 1
    for file in os.listdir('dataset/Savee/'):
        try:

            if 'a' in file:
                newName = 'dataset/Savee/ANG{}.wav'.format(fileNum)
                os.rename('dataset/Savee/{}'.format(file), newName)
            if 'd' in file:
                newName = 'dataset/Savee/DIS{}.wav'.format(fileNum)
                os.rename('dataset/Savee/{}'.format(file), newName)
            if 'f' in file:
                newName = 'dataset/Savee/FEA{}.wav'.format(fileNum)
                os.rename('dataset/Savee/{}'.format(file), newName)
            if 'h' in file:
                newName = 'dataset/Savee/HAP{}.wav'.format(fileNum)
                os.rename('dataset/Savee/{}'.format(file), newName)
            if 'n' in file:
                newName = 'dataset/Savee/NEU{}.wav'.format(fileNum)
                os.rename('dataset/Savee/{}'.format(file), newName)
            if 'sa' in file and 'su' not in file:
                newName = 'dataset/Savee/SAD{}.wav'.format(fileNum)
                os.rename('dataset/Savee/{}'.format(file), newName)
            if 'su' in file:
                newName = 'dataset/Savee/SUP{}.wav'.format(fileNum)
                os.rename('dataset/Savee/{}'.format(file), newName)
        except FileNotFoundError:
            pass
        fileNum += 1


    for folder in os.listdir('dataset/Tess/'):

            for file in os.listdir('dataset/Tess/{}'.format(folder)):
                try:
                    print('here')
                    print('herehere')
                    if folder=='OAF_angry' or folder=='YAF_angry':
                        newName = 'dataset/Tess/{}/ANG{}.wav'.format(folder, fileNum)
                        os.rename('dataset/Tess/{}/{}'.format(folder, file), newName)

                    if folder=='OAF_disgust' or folder=='YAF_disgust':
                        newName = 'dataset/Tess/{}/DIS{}.wav'.format(folder, fileNum)
                        os.rename('dataset/Tess/{}/{}'.format(folder, file), newName)
                    if folder=='OAF_Fear' or folder=='YAF_fear':
                        newName = 'dataset/Tess/{}/FEA{}.wav'.format(folder, fileNum)
                        os.rename('dataset/Tess/{}/{}'.format(folder, file), newName)
                    if folder=='OAF_happy' or folder=='YAF_happy':
                        newName = 'dataset/Tess/{}/HAP{}.wav'.format(folder, fileNum)
                        os.rename('dataset/Tess/{}/{}'.format(folder, file), newName)
                    if folder=='OAF_neutral' or folder=='YAF_neutral':
                        newName = 'dataset/Tess/{}/NEU{}.wav'.format(folder, fileNum)
                        os.rename('dataset/Tess/{}/{}'.format(folder, file), newName)
                    if folder=='OAF_Pleasant_suprise' or folder=='YAF_pleasant_suprise':
                        newName = 'dataset/Tess/{}/SUP{}.wav'.format(folder, fileNum)
                        os.rename('dataset/Tess/{}/{}'.format(folder, file), newName)
                    if folder=='OAF_Sad' or folder=='YAF_sad':
                        newName = 'dataset/Tess/{}/SAD{}.wav'.format(folder, fileNum)
                        os.rename('dataset/Tess/{}/{}'.format(folder, file), newName)
                    fileNum += 1
                except FileNotFoundError:
                    pass








    fileNum += 1


def createFinalDataDir():
    if 'mergedData' not in os.listdir('dataset/'):
        os.mkdir('dataset/mergedData/')


def moveAllFilesTO_mergedData():
    target_dir = 'dataset/mergedData/'
    try:
        for file in os.listdir('dataset/Crema/'):
            source_dir = 'dataset/Crema/{}'.format(file)
            shutil.move(os.path.join(source_dir), target_dir)
    except FileNotFoundError:
        pass
    try:
        for folder in os.listdir('dataset/Ravdess/audio_speech_actors_01-24/'):
            for file in os.listdir('dataset/Ravdess/audio_speech_actors_01-24/{}'.format(folder)):
                source_dir = 'dataset/Ravdess/audio_speech_actors_01-24/{}/{}'.format(folder, file)
                shutil.move(os.path.join(source_dir), target_dir)

    except FileNotFoundError:
        pass
    try:
        for file in os.listdir('dataset/Savee/'):
            source_dir = 'dataset/Savee/{}'.format(file)
            shutil.move(os.path.join(source_dir), target_dir)
    except FileNotFoundError:
        pass
    try:
        for folder in os.listdir('dataset/Tess/'):
            for file in os.listdir('dataset/Tess/{}'.format(folder)):
                source_dir = 'dataset/Tess/{}/{}'.format(folder, file)
                shutil.move(os.path.join(source_dir), target_dir)
    except FileNotFoundError:
        pass

    dirsToDel = ['Crema', 'Ravdess', 'Savee', 'Tess']
    for dir in dirsToDel:
        removeDir('dataset/{}'.format(dir))



def removeDir(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        print('Path \"{}\" not found'.format(path))


def createLabels():
    labels = []
    path = 'dataset/mergedData/'
    for file in os.listdir(path):
        if 'ANG' in file:
            labels.append(0)
        if 'CAL' in file:
            labels.append(1)
        if 'DIS' in file:
            labels.append(2)
        if 'FEA' in file:
            labels.append(3)
        if 'HAP' in file:
            labels.append(4)
        if 'NEU' in file:
            labels.append(5)
        if 'SAD' in file:
            labels.append(6)
        if 'SUP' in file:
            labels.append(7)



    return labels


def mergedDataExists():
    return os.path.isdir('dataset/mergedData/')


def createNP_arrLabels(labels):
    return np.asarray(labels)



def createNpDataArr():
    path = 'dataset/mergedData/'
    Y_data = []
    for file in os.listdir(path):
        y, sr = librosa.load(path+file)
        Y_data.append(y)
    return Y_data

def toNpArray(data):
    return np.array(data)

def saveNpArray(arr, path):
    np.save(path, arr)

def __main__():
    if not (mergedDataExists()):
        renameFiles()
        createFinalDataDir()
        moveAllFilesTO_mergedData()
    labels = createLabels()
    labels = createNP_arrLabels(labels=labels)
    saveNpArray(labels, 'labels.npy')
    data = createNpDataArr()
    print('here')

    #!works fine until here
    #!need to pad data to the same length before creating it as a numpy array

    data = toNpArray(data)
    print('herehere')
    saveNpArray(data, 'data.npy')




__main__()


#todo: data formatting and labelling
#todo: pad data to largest file
#todo: format data into list corresponding to labels list


