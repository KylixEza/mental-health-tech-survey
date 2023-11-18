import streamlit as st
import joblib

def build_prediction_page(clean_df, empty_df):
    age = st.text_input('Your Age:')
    gender = create_drop_down(clean_df, 'gender', 'Gender')
    self_employed = create_drop_down(clean_df, 'self_employed', 'Are you self employed?')
    family_history = create_drop_down(clean_df, 'family_history', 'Does your family have a history of mental health issues?')
    work_interfere = create_drop_down(clean_df, 'work_interfere', 'How often is your work interrupted due to mental health issues?')
    no_employees = create_drop_down(clean_df, 'no_employees', 'How many employees work at your workplace?')
    remote_works = create_drop_down(clean_df, 'remote_work', 'Do you work remotely?')
    tech_company = create_drop_down(clean_df, 'tech_company', 'Do you work for a tech company?')
    benefits = create_drop_down(clean_df, 'benefits', 'Does your workplace offer mental health benefits?')
    care_options = create_drop_down(clean_df, 'care_options', 'Does your workplace offer mental health care options?')
    wellness_program = create_drop_down(clean_df, 'wellness_program', 'Does your workplace offer a wellness program?')
    seek_help = create_drop_down(clean_df, 'seek_help', 'Have you ever sought help for mental health issues?')
    anonymity = create_drop_down(clean_df, 'anonymity', 'Does your workplace allow anonymity when seeking help for mental health issues?')
    leave = create_drop_down(clean_df, 'leave', 'Does your workplace offer time off for mental health issues?')
    mental_health_consequence = create_drop_down(clean_df, 'mental_health_consequence', 'Have you ever experienced negative consequences for discussing mental health issues at work?')
    physical_health_cosequnce = create_drop_down(clean_df, 'phys_health_consequence', 'Have you ever experienced negative consequences for discussing physical health issues at work?')
    coworkers = create_drop_down(clean_df, 'coworkers', 'Have you discussed mental health issues with your coworkers?')
    supervisor = create_drop_down(clean_df, 'supervisor', 'Have you discussed mental health issues with your supervisor?')

    if st.button('Submit'):
        if age:
            try:
                age = int(age)
            except ValueError:
                st.warning("Please enter a valid integer.")
        else:
            st.warning("Please enter a value.")
        
        predict(
            clean_df,
            empty_df,
            age,
            gender,
            self_employed,
            family_history,
            work_interfere,
            no_employees,
            remote_works,
            tech_company,
            benefits,
            care_options,
            wellness_program,
            seek_help,
            anonymity,
            leave,
            mental_health_consequence,
            physical_health_cosequnce,
            coworkers,
            supervisor
        )

def create_drop_down(
    df,
    column,
    question,
):
    unique_values = df[column].unique()
    selected_category = st.selectbox(question, unique_values)
    return selected_category

def predict(
    clean_df,
    empty_df,
    age,
    gender,
    self_employed,
    family_history,
    work_interfere,
    no_employees,
    remote_works,
    tech_company,
    benefits,
    care_options,
    wellness_program,
    seek_help,
    anonymity,
    leave,
    mental_health_consequence,
    physical_health_cosequnce,
    coworkers,
    supervisor
):
    empty_df['age'] = standard_scale(age, clean_df['age'].min(), clean_df['age'].max())
    empty_df = transform_df(empty_df, 'gender', gender)
    empty_df = transform_df(empty_df, 'self_employed', self_employed)
    empty_df = transform_df(empty_df, 'family_history', family_history)
    empty_df = transform_df(empty_df, 'work_interfere', work_interfere)
    empty_df = transform_df(empty_df, 'no_employees', no_employees)
    empty_df = transform_df(empty_df, 'remote_work', remote_works)
    empty_df = transform_df(empty_df, 'tech_company', tech_company)
    empty_df = transform_df(empty_df, 'benefits', benefits)
    empty_df = transform_df(empty_df, 'care_options', care_options)
    empty_df = transform_df(empty_df, 'wellness_program', wellness_program)
    empty_df = transform_df(empty_df, 'seek_help', seek_help)
    empty_df = transform_df(empty_df, 'anonymity', anonymity)
    empty_df = transform_df(empty_df, 'leave', leave)
    empty_df = transform_df(empty_df, 'mental_health_consequence', mental_health_consequence)
    empty_df = transform_df(empty_df, 'phys_health_consequence', physical_health_cosequnce)
    empty_df = transform_df(empty_df, 'coworkers', coworkers)
    empty_df = transform_df(empty_df, 'supervisor', supervisor)

    model = joblib.load('rf_model.joblib')
    predicted_class = model.predict(empty_df)
    
    st.title("Result")
    
    if (predicted_class == 1):
        st.header('You need to take a treatment 😔')
        st.write('Taking care of our mental health is just as important as caring for our physical health. Just as we would seek medical attention for a physical ailment, it\'s crucial to recognize the importance of addressing our mental and emotional struggles. Seeking treatment for mental health is not a sign of weakness, but rather a courageous step towards healing and personal growth.')
    else:
        st.header('You are so fine! 😊')
        st.write('Your mental well-being radiates positivity, not only benefiting you but creating a ripple effect in the lives of those fortunate enough to be connected with you. The resilience you\'ve shown in navigating life\'s complexities is a testament to your inner strength and the efficacy of the strategies you\'ve employed to foster mental health.')

def standard_scale(value, min, max):
    if (value > max):
        return 1
    elif (value < min):
        return -1
    mean = (max + min) / 2
    std = (max - min) / 2
    z = (value - mean) / std
    return z

def transform_df(
    df,
    column_start,
    column_value,
):
    matching_column = [col for col in df.columns if f'{column_start}_{column_value}' in col]
    df[matching_column] = 1
    return df


