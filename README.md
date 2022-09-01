# Project Hospital Management
This project is given by SBH sir 

## Problem Statement :
In a hospital there are N no of nurse in duty B no of working bed. We need to schedule the nurse in working bed such a way that duty of nurse will be equally distributed. 

### Probable Algorithm : 
> Begin <br>
> update(current_working_bed)  <br>
> update(availabel nurse)  <br>
> Sort the queue array of nurse respect of no_duty value in assending order.  <br>
> for bed in (set of bed):  <br>
> Chose a bed and 3 nurse from front of queue (delete)  <br>
> nurse.bed <--- bed & duity_time  <br>
> Increase the no_duty value of chosen nurse  <br>
> Add those 3 nurse at the rear of the queue.  <br>
> End for <br>
> suppress (queue of nurse) <br>
#### End
(Try to improve it in a seperate branch)

## Class or data model for Database.
> 1. Nurse <br>
> 2. Bed / Patient / both <br>
> 3. Doctor (Not required in here ) <br>
>  ...edit if you find more .... <br>
