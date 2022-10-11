from .models import Word, Nurse
import numpy as np

MAX_DUTY_TIME = 8
MAX_HANDLE_PATIENT = 3


def nurse_schedule():
    array_of_nurse = Nurse.objects.all().order_by('cost')
    array_of_nurse = np.array(array_of_nurse)
    array_of_word = Word.objects.all()
    # array_of_word = np.array(array_of_word)

    for word in array_of_word:
        if word.active_bed % MAX_HANDLE_PATIENT == 0:
            no_nurse = word.active_bed//MAX_HANDLE_PATIENT
        else:
            no_nurse = word.active_bed//MAX_HANDLE_PATIENT

        for i in range(0, no_nurse, 3):
            nurse1 = array_of_nurse[i]
            nurse2 = array_of_nurse[i+1]
            nurse3 = array_of_nurse[i+2]
            array_of_nurse = array_of_nurse[3:]
            nurse1.allocated_word = word.id
            nurse2.allocated_word = word.id
            nurse3.allocated_word = word.id

            nurse1.shift = "First_shift"
            nurse2.shift = "Second_shift"
            nurse3.shift = "Third_shift"
            nurse1.cost += 1
            nurse2.cost += 1
            nurse3.cost += 1

            np.append(array_of_nurse, nurse1)
            np.append(array_of_nurse, nurse2)
            np.append(array_of_nurse, nurse3)

    # suppress(queue of nurse)


def generate_bed_no():
    array_of_word = Word.objects.all()
    for word in array_of_word:
        if word.active_bed % MAX_HANDLE_PATIENT:
            word.active_bed += 1
            word.save()
            return word.id
    for word in array_of_word:
        if word.active_bed < word.MAX_BED:
            word.active_bed += 1
            word.save()
            return word.id
