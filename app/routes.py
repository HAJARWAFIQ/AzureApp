from flask import Blueprint, render_template, request, redirect, url_for, abort
import os

# Définir le Blueprint
bp = Blueprint('main', __name__)

# Données du CV (variables partagées)
cv_data = {
    "name": "Wafiq Hajar",
    "title": "Développeur DevOps et Cloud",
    "experience": [
        {"role": "Stage DevOps", "company": "Company A", "duration": "2023-2024"},
        {"role": "Ingénieur Logiciel", "company": "Company B", "duration": "2022-2023"}
    ],
    "education": [
        {"degree": "Master en Cloud Computing", "university": "Université XYZ", "year": "2024"}
    ],
    "skills": ["Python", "Docker", "Kubernetes", "Flask"]
}

@bp.route('/')
def home():
    """Page d'accueil"""
    return render_template('index.html')

@bp.route('/cv')
def cv():
    """Afficher le CV dynamique"""
    return render_template('cv.html', cv=cv_data)

@bp.route('/cv/edit', methods=['GET', 'POST'])
def edit_cv():
    """Modifier les données du CV"""
    if request.method == 'POST':
        # Récupérer les données du formulaire
        cv_data["name"] = request.form.get('name')
        cv_data["title"] = request.form.get('title')
        cv_data["experience"] = [
            {"role": request.form.get('exp_role1'), "company": request.form.get('exp_company1'), "duration": request.form.get('exp_duration1')},
            {"role": request.form.get('exp_role2'), "company": request.form.get('exp_company2'), "duration": request.form.get('exp_duration2')}
        ]
        cv_data["education"] = [
            {"degree": request.form.get('edu_degree1'), "university": request.form.get('edu_university1'), "year": request.form.get('edu_year1')}
        ]
        cv_data["skills"] = request.form.get('skills').split(',')  # Les compétences séparées par des virgules
        return redirect(url_for('main.cv'))

    return render_template('edit.html', cv=cv_data)
