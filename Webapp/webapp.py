import pandas as pd
import streamlit as st

#Pandas Work
df2=pd.read_csv('df2.csv')
description=pd.read_csv("symptom_Description.csv")
precaution=pd.read_csv("symptom_precaution.csv")
#Streamlit Work

edges=[['fatigue', 'vomiting', 0], ['fatigue', 'loss_of_appetite', 1], ['vomiting', 'skin_rash', 0], ['vomiting', 'nausea', 1], ['loss_of_appetite', 'irritability', 0], ['loss_of_appetite', 'malaise', 1], ['skin_rash', 'headache', 0], ['skin_rash', 'itching', 1], ['nausea', 'abdominal_pain', 0], ['nausea', 'muscle_pain', 1], ['irritability', 'chest_pain', 0], ['irritability', 'slurred_speech', 1], ['malaise', 'stomach_bleeding', 0], ['malaise', 'yellowing_of_eyes', 1], ['headache', 'swelling_joints', 0], ['headache', 'loss_of_balance', 1], ['itching', 'yellow_crust_ooze', 0], ['itching', 'stomach_pain', 1], ['abdominal_pain', 'diarrhoea', 0], ['abdominal_pain', 'yellowish_skin', 1], ['muscle_pain', 'unsteadiness', 0], ['muscle_pain', 'mild_fever', 1], ['chest_pain', 'high_fever', 0], ['chest_pain', 'throat_irritation', 1], ['slurred_speech', 'swollen_extremeties', 0], ['slurred_speech', 'yellow_urine', 1], ['stomach_bleeding', 'joint_pain', 0], ['stomach_bleeding', 'weight_loss', 1], ['yellowing_of_eyes', 'pain_behind_the_eyes', 0], ['yellowing_of_eyes', 'swelled_lymph_nodes', 1], ['swelling_joints', 'dizziness', 0], ['swelling_joints', 'stiff_neck', 1], ['loss_of_balance', 'visual_disturbances', 0], ['loss_of_balance', 'spinning_movements', 1], ['yellow_crust_ooze', 'small_dents_in_nails', 0], ['yellow_crust_ooze', 'weight_gain', 1], ['stomach_pain', 'spotting_ urination', 0], ['stomach_pain', 'weakness_of_one_body_side', 1], ['diarrhoea', 'cough', 0], ['diarrhoea', 'sweating', 1], ['yellowish_skin', 'swelling_of_stomach', 0], ['yellowish_skin', 'dark_urine', 1], ['unsteadiness', 'palpitations', 0], ['unsteadiness', 'weakness_in_limbs', 1], ['mild_fever', 'red_spots_over_body', 0], ['mild_fever', 'watering_from_eyes', 1], ['high_fever', 'polyuria', 0], ['high_fever', 'chills', 1], ['throat_irritation', 'ulcers_on_tongue', 0], ['throat_irritation', 'ulcers_on_tongue', 1], ['swollen_extremeties', 'toxic_look_(typhos)', 0], ['swollen_extremeties', 'toxic_look_(typhos)', 1], ['yellow_urine', 'swollen_legs', 0], ['yellow_urine', 'swollen_legs', 1], ['joint_pain', 'family_history', 0], ['joint_pain', 'back_pain', 1], ['weight_loss', 'swollen_blood_vessels', 0], ['weight_loss', 'swollen_blood_vessels', 1], ['pain_behind_the_eyes', 'sunken_eyes', 0], ['pain_behind_the_eyes', 'sunken_eyes', 1], ['swelled_lymph_nodes', 'skin_peeling', 0], ['swelled_lymph_nodes', 'skin_peeling', 1], ['dizziness', 'burning_micturition', 0], ['dizziness', 'puffy_face_and_eyes', 1], ['stiff_neck', 'muscle_weakness', 0], ['stiff_neck', 'sinus_pressure', 1], ['visual_disturbances', 'altered_sensorium', 0], ['visual_disturbances', 'silver_like_dusting', 1], ['spinning_movements', 'shivering', 0], ['spinning_movements', 'shivering', 1], ['small_dents_in_nails', 'nodal_skin_eruptions', 0], ['small_dents_in_nails', 'scurring', 1], ['weight_gain', 'rusty_sputum', 0], ['weight_gain', 'rusty_sputum', 1], ['spotting_ urination', 'lethargy', 0], ['spotting_ urination', 'runny_nose', 1], ['weakness_of_one_body_side', 'restlessness', 0], ['weakness_of_one_body_side', 'restlessness', 1], ['cough', 'breathlessness', 0], ['cough', 'phlegm', 1], ['sweating', 'redness_of_eyes', 0], ['sweating', 'redness_of_eyes', 1], ['swelling_of_stomach', 'red_sore_around_nose', 0], ['swelling_of_stomach', 'red_sore_around_nose', 1], ['dark_urine', 'history_of_alcohol_consumption', 0], ['dark_urine', 'receiving_unsterile_injections', 1], ['palpitations', 'coma', 0], ['palpitations', 'receiving_blood_transfusion', 1], ['weakness_in_limbs', 'pus_filled_pimples', 0], ['weakness_in_limbs', 'pus_filled_pimples', 1], ['red_spots_over_body', 'prominent_veins_on_calf', 0], ['red_spots_over_body', 'prominent_veins_on_calf', 1], ['watering_from_eyes', 'patches_in_throat', 0], ['watering_from_eyes', 'patches_in_throat', 1], ['polyuria', 'obesity', 0], ['polyuria', 'passage_of_gases', 1], ['chills', 'mucoid_sputum', 0], ['chills', 'painful_walking', 1], ['ulcers_on_tongue', 'pain_during_bowel_movements', 0], ['ulcers_on_tongue', 'pain_during_bowel_movements', 1], ['toxic_look_(typhos)', 'muscle_wasting', 0], ['toxic_look_(typhos)', 'muscle_wasting', 1], ['swollen_legs', 'mood_swings', 0], ['swollen_legs', 'mood_swings', 1], ['family_history', 'loss_of_smell', 0], ['family_history', 'loss_of_smell', 1], ['back_pain', 'lack_of_concentration', 0], ['back_pain', 'lack_of_concentration', 1], ['swollen_blood_vessels', 'irritation_in_anus', 0], ['swollen_blood_vessels', 'irritation_in_anus', 1], ['sunken_eyes', 'internal_itching', 0], ['sunken_eyes', 'internal_itching', 1], ['skin_peeling', 'inflammatory_nails', 0], ['skin_peeling', 'inflammatory_nails', 1]]
le=len(edges)
st.title("Welcome to Disease Predictor!")
st.write("You have to tell about your symptoms in increasing order for getting proper results.")
st.write("Warning:- Changing any value in between may result in wrong prediction.")
now='fatigue'
ansli=[]

#1st symptom prediction
selectbox = st.selectbox(
    "Do yo have "+now,
    ["Yes", "No"],
    key=1
)

if selectbox=="Yes":
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==1:
            ansli.append(now)
            now=edges[j][1]
            break
else:
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==0:
                # ansli.append(now)
            now=edges[j][1]
            break


#2nd symptom prediction
selectbox = st.selectbox(
    "Do yo have "+now,
    ["Yes", "No"],
    key=2
)
if selectbox=="Yes":
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==1:
            ansli.append(now)
            now=edges[j][1]
            break
else:
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==0:
                # ansli.append(now)
            now=edges[j][1]
            break

#3rd symptom prediction
selectbox = st.selectbox(
    "Do yo have "+now,
    ["Yes", "No"],
    key=3
)
if selectbox=="Yes":
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==1:
            ansli.append(now)
            now=edges[j][1]
            break
else:
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==0:
                # ansli.append(now)
            now=edges[j][1]
            break

#4th symptom prediction
selectbox = st.selectbox(
    "Do yo have "+now,
    ["Yes", "No"],
    key=4
)
if selectbox=="Yes":
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==1:
            ansli.append(now)
            now=edges[j][1]
            break
else:
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==0:
                # ansli.append(now)
            now=edges[j][1]
            break

#5th symptom prediction
selectbox = st.selectbox(
    "Do yo have "+now,
    ["Yes", "No"],
    key=5
)
if selectbox=="Yes":
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==1:
            ansli.append(now)
            now=edges[j][1]
            break
else:
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==0:
                # ansli.append(now)
            now=edges[j][1]
            break

#6th symptom prediction
selectbox = st.selectbox(
    "Do yo have "+now,
    ["Yes", "No"],
    key=6
)
if selectbox=="Yes":
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==1:
            ansli.append(now)
            now=edges[j][1]
            break
else:
    for j in range(le):
        if edges[j][0]==now and edges[j][2]==0:
                # ansli.append(now)
            now=edges[j][1]
            break

#7th symptom prediction
selectbox = st.selectbox(
    "Do yo have "+now,
    ["Yes", "No"],
    key=7
)
if selectbox=="Yes":
    ansli.append(now)

# st.write(ansli)
le=len(ansli)
# print(le)
if le==0:
  st.write("You are completely fit")
  st.write("Keep exercising at the same pace for better health.")
else:
  c=0
  anli=[0]*le
  for i in range(le):
    anli[i]=7-i
  dise_list=[]
  for i in df2.index:
    ans=0
    for j in range(le):
      if df2.iloc[i][ansli[j]]==1:
        ans+=df2.iloc[i][ansli[j]]
    dise_list.append([ans,df2.iloc[i]['Disease']])
  # print(c)
  # print(ansli)
  # print(anli)
  dise_list.sort()
  dise_list.reverse()
  disease=dise_list[0][1]
  st.write("You have disease ",disease)
  st.write("What is ",disease," ?")
  for i in description.index:
    if description.iloc[i]['Disease']==disease:
        st.write(description.iloc[i]['Description'])
  st.write("You must take the following precautions to prevent ",disease)
  for i in precaution.index:
    if precaution.iloc[i]['Disease']==disease:
        pre1=precaution.iloc[i]['Precaution_1']
        if type(pre1)!=float:
            st.write(pre1)
        pre2=precaution.iloc[i]['Precaution_2']
        if type(pre2)!=float:
            st.write(pre2)
        pre3=precaution.iloc[i]['Precaution_3']
        if type(pre3)!=float:
            st.write(pre3)
        pre4=precaution.iloc[i]['Precaution_4']
        if type(pre4)!=float:
            st.write(pre4)
        break
    st.write("Wish you good health . Take care of your health")