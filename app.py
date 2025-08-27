# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# The main route for the form. It handles both GET and POST requests.
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the user submits the form
    if request.method == 'POST':
        # Collect data from the form
        personal_data = {
            'full_name': request.form.get('full_name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'linkedin': request.form.get('linkedin'),
            'portfolio': request.form.get('portfolio'),
            'address': request.form.get('address')
        }

        summary = request.form.get('summary')

        # Collect multiple work experiences
        work_experiences = []
        for i in range(1, 5): # Allow up to 4 work experiences
            if request.form.get(f'job_title_{i}'):
                experience = {
                    'job_title': request.form.get(f'job_title_{i}'),
                    'company': request.form.get(f'company_{i}'),
                    'location': request.form.get(f'job_location_{i}'),
                    'start_date': request.form.get(f'job_start_date_{i}'),
                    'end_date': request.form.get(f'job_end_date_{i}'),
                    'responsibilities': request.form.get(f'responsibilities_{i}').split('\n')
                }
                work_experiences.append(experience)

        # Collect multiple education entries
        education_list = []
        for i in range(1, 5): # Allow up to 4 education entries
            if request.form.get(f'degree_{i}'):
                education = {
                    'degree': request.form.get(f'degree_{i}'),
                    'institution': request.form.get(f'institution_{i}'),
                    'location': request.form.get(f'edu_location_{i}'),
                    'grad_date': request.form.get(f'grad_date_{i}'),
                    'gpa': request.form.get(f'gpa_{i}')
                }
                education_list.append(education)

        # Collect skills and projects
        skills = request.form.get('skills').split(',') if request.form.get('skills') else []
        skills = [s.strip() for s in skills]

        projects = []
        for i in range(1, 5): # Allow up to 4 projects
            if request.form.get(f'project_title_{i}'):
                project = {
                    'title': request.form.get(f'project_title_{i}'),
                    'description': request.form.get(f'project_description_{i}'),
                    'technologies': request.form.get(f'project_technologies_{i}').split(',')
                }
                projects.append(project)

        # Combine all data into a single dictionary
        resume_data = {
            'personal': personal_data,
            'summary': summary,
            'experience': work_experiences,
            'education': education_list,
            'skills': skills,
            'projects': projects
        }

        # Render the resume template with the collected data
        return render_template('resume.html', data=resume_data)

    # If it's a GET request, just render the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
