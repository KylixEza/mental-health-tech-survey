import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def build_home_page(df):
    total_respondent = df.shape[0]

    build_table_of_contents()

    build_introduction()
    build_age_chart(df)
    build_categories_chart(
        df,
        'Gender',
        'Exploring the Diversity: A visual representation of the distribution of gender categories, allowing you to see how individuals are grouped based on gender. Toggle between All and specific categories to gain insights into the overall composition or focus on specific groups within the dataset',
        'gender',
        'Gender'
    )

    build_categories_chart(
        df,
        'Self Employment',
        'Whether the respondent is self-employed',
        'self_employed',
        'Self Employment'
    )

    build_categories_chart(
        df,
        'Family History',
        'Whether the respondent has a family history of mental health issues',
        'family_history',
        'Family History'
    )

    build_categories_chart(
        df,
        'Interfered Work',
        'How much work is interfered with due to mental health issues',
        'work_interfere',
        'Frequently'
    )

    build_categories_chart(
        df,
        'Number of Employees',
        'Number of employees at the respondent\'s workplace',
        'no_employees',
        'Number of Employees'
    )

    build_categories_chart(
        df,
        'Remote Work',
        'Whether the respondent works remotely',
        'remote_work',
        'Remote Work'
    )

    build_categories_chart(
        df,
        'Tech Company',
        'Whether the respondent works in a tech company',
        'tech_company',
        'Tech Company'
    )

    build_categories_chart(
        df,
        'Benefits',
        'Whether the respondent\'s workplace offers mental health benefits',
        'benefits',
        'Benefits'
    )

    build_categories_chart(
        df,
        'Care Options',
        'Whether the respondent\'s workplace offers mental health care options',
        'care_options',
        'Care Options'
    )

    build_categories_chart(
        df,
        'Wellness Program',
        'Whether the respondent\'s workplace offers a wellness program',
        'wellness_program',
        'Wellness Program'
    )

    build_categories_chart(
        df,
        'Seek Help',
        'Whether the respondent has sought help for a mental health issue',
        'seek_help',
        'Seek Help'
    )

    build_categories_chart(
        df,
        'Anonymity',
        'Whether the respondent\'s workplace allows for anonymity when seeking help for a mental health issue',
        'anonymity',
        'Anonymity'
    )

    build_categories_chart(
        df,
        'Leave',
        'Whether the respondent\'s workplace offers leave for mental health issues',
        'leave',
        'Leave'
    )

    build_categories_chart(
        df,
        'Mental Health Consequence',
        'Whether the respondent has experienced negative consequences due to discussing mental health issues at work',
        'mental_health_consequence',
        'Mental Health Consequence'
    )

    build_categories_chart(
        df,
        'Physical Health Consequence',
        'Whether the respondent has experienced negative consequences due to discussing physical health issues at work',
        'phys_health_consequence',
        'Physical Health Consequence'
    )

    build_categories_chart(
        df,
        'Coworkers',
        'Whether the respondent has discussed mental health issues with coworkers',
        'coworkers',
        'Coworkers'
    )

    build_categories_chart(
        df,
        'Supervisor',
        'Whether the respondent has discussed mental health issues with their supervisor',
        'supervisor',
        'Supervisor'
    )

def build_table_of_contents():
    st.header('Table Of Contents')
    st.markdown(
        "- <a href='#introduction' style='color: #ff4b4b'>Introduction</a>\n"
        "- <a href='#age-distribution' style='color: #ff4b4b'>Age Distribution</a>\n"
        "- <a href='#gender' style='color: #ff4b4b'>Gender</a>\n"
        "- <a href='#self-employment' style='color: #ff4b4b'>Self Employment</a>\n"
        "- <a href='#family-history' style='color: #ff4b4b'>Family History</a>\n"
        "- <a href='#interfered-work' style='color: #ff4b4b'>Interfered Work</a>\n"
        "- <a href='#number-of-employees' style='color: #ff4b4b'>Number of Employees</a>\n"
        "- <a href='#remote-work' style='color: #ff4b4b'>Remote Work</a>\n"
        "- <a href='#tech-company' style='color: #ff4b4b'>Tech Company</a>\n"
        "- <a href='#benefits' style='color: #ff4b4b'>Benefits</a>\n"
        "- <a href='#care-options' style='color: #ff4b4b'>Care Options</a>\n"
        "- <a href='#wellness-program' style='color: #ff4b4b'>Wellness Program</a>\n"
        "- <a href='#seek-help' style='color: #ff4b4b'>Seek Help</a>\n"
        "- <a href='#anonymity' style='color: #ff4b4b'>Anonymity</a>\n"
        "- <a href='#leave' style='color: #ff4b4b'>Leave</a>\n"
        "- <a href='#mental-health-consequence' style='color: #ff4b4b'>Mental Health Consequence</a>\n"
        "- <a href='#physical-health-consequence' style='color: #ff4b4b'>Physical Health Consequence</a>\n"
        "- <a href='#coworkers' style='color: #ff4b4b'>Coworkers</a>\n"
        "- <a href='#supervisor' style='color: #ff4b4b'>Supervisor</a>\n"
        , unsafe_allow_html=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    

def build_introduction():
    st.header('Introduction')
    st.write('Survey from individuals in the tech industry about their mental health, including questions about treatment, workplace resources, and attitudes towards discussing mental health in the workplace. Mental health is an issue that affects all people of all ages, genders and walks of life. The prevalence of these issues within the tech industry–one that places hard demands on those who work in it–is no exception. By analyzing this dataset, we can better understand how prevalent mental health issues are among those who work in the tech sector.–and what kinds of resources they rely upon to find help–so that more can be done to create a healthier working environment for all.')

    st.markdown("<hr>", unsafe_allow_html=True)

def build_age_chart(df):
    st.header('Age Distribution')

    age_filter = st.slider('Select Age Range', min_value=min(df['age']), max_value=max(df['age']), value=(min(df['age']), max(df['age'])))
    filtered_df = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1])]

    age_fig = px.histogram(filtered_df, x='age', labels={'age': 'Age'}, color_discrete_sequence=['#ff4b4b'])
    st.plotly_chart(age_fig, use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

def build_categories_chart(
    df, 
    header,
    subtitle,
    df_column_name,
    x_label,
):
    st.header(header)
    st.write(subtitle)

    plot_all_categories = st.checkbox('All', value=True, key=df_column_name)

    unique_values = df[df_column_name].unique()

    if plot_all_categories:
        selected_unique_value = [st.checkbox(f'{unique}', value=True, key=f'{df_column_name} {unique}') for unique in unique_values]
    else:
        selected_unique_value = [st.checkbox(f'{unique}', key=f'{df_column_name} {unique}') for unique in unique_values]

    if plot_all_categories:
        filtered_df = df
    else:
        selected_unique_value = [gender for gender, selected in zip(unique_values, selected_unique_value) if selected]
        filtered_df = df[df[df_column_name].isin(selected_unique_value)]
    
    fig = px.histogram(filtered_df, x=df_column_name, labels={df_column_name : x_label}, color_discrete_sequence=['#ff4b4b'])

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    