##  Probable Algorithm :
 To allocate a nurse Room-> word -> bed hierarchy will maintain 
 We select a nurse for a word 


### Global Constant 
1. MAX_DUTY_TIME
2. MAX_HANDLE_PATIENT
### Consideration :
1. 1 Nurse can handle maximum MAX_HANDLE_PATIENT number of Patient 
2. Measurement of day should be discrete 
3. 1 word can contain maximum MXA_BED no of bed and <br>
MXA_BED == k*MAX_HANDLE_PATIENT ; <br> where k belongs to Natural number 
4. MAX_DUTY_TIME=8 Hours
### Strategy :
1. We will assign nurse such a way so that 1 nurse can take care of MAX_HANDLE_PATIENT no of patient.
2. To improve this task we update the patient in word such a way so that minimum number of nurse can handle maximum number of patient.


### Data Structure or class 
1.  class Word{
        id,
        MAX_BED,
        working_bed
    }
2. Array_of_Word

3. class Nurse {
    id,
    allocated_word,
    shift,
    cost
}
4. Queue_of_Nurse 


### Nurse Scheduling  Algorithm 
``` Algorithm
> Begin    
update(Array_of_Word, new_patient )    
update(available nurse)    
Sort the queue array of nurse respect of no_duty value in ascending order.   
for word in (Array_of_Word):    
    if(word.working_bed%MAX_HANDLE_PATIENT==0)
        no_nurse = word.working_bed/MAX_HANDLE_PATIENT
    else
        no_nurse = word.working_bed/MAX_HANDLE_PATIENT
    End if

    for i=1 to no_nurse: 
        nurse1 <--- Chose nurse from front of queue (delete) 
        nurse2 <--- Chose nurse from front of queue (delete)
        nurse3 <--- Chose nurse from front of queue (delete)
        nurse1.allocated_word <--- word.id
        nurse2.allocated_word <--- word.id
        nurse3.allocated_word <--- word.id
        nurse1.shift <--- duty_time/First_shift
        nurse2.shift <--- duty_time/Second_shift
        nurse3.shift <--- duty_time/Third_shift
        nurse1.cost++
        nurse2.cost++
        nurse3.cost++
        queue.insert(nurse1) // insert at rear
        queue.insert(nurse2) // insert at rear
        queue.insert(nurse3) // insert at rear
    End for  
 End for  
 suppress (queue of nurse)    
 
....End...
```  

  

### Patient Admission Algorithm 
``` Algorithm
Function update:
Begin (input1: Array_of_word, input2 : N -> Number of new patient)
round = 0;
while(N>0):
    if (Round == 0)
        for word in {Array_of_Word} :  
            if( N== 0) break;
            while(word.working_bed % MAX_HANDLE_PATIENT  && N>0)
                word.working_bed++;
                N--;
    else 
        for word in {Array_of_Word} :   
            if( N== 0) break;       
            while(word.working_bed < word.MAX_BED && N>0)
                
                word.working_bed++;                
                N--;
    round ++
....End....
```
