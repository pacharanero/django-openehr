# Generated by Django 2.0.1 on 2018-02-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_openehr', '0005_auto_20180205_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdverseReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causative_agent', models.CharField(help_text='Details of the agent or medicinal substance believed to be the cause of the adverse reaction or allergy', max_length=255, null=True)),
                ('reaction_snomed_code', models.CharField(blank=True, help_text='An optional pre-coordinated unqualified SNOMED-CT code for the nature of the reaction produced by the drug allergy', max_length=255, null=True)),
                ('date_recorded', models.DateTimeField(blank=True, help_text='The date that the reaction was clinically recorded/asserted. This will often equate to the date of  # onset of the reaction but this may not be wholly clear from source data', null=True)),
                ('reaction_severity', models.CharField(blank=True, help_text='The severity of the reaction', max_length=255, null=True)),
                ('reaction_certainty', models.CharField(blank=True, help_text='The certainty with which the reaction is deemed to be be due to allergy to the agent', max_length=255, null=True)),
                ('reaction_comment', models.CharField(blank=True, help_text='Any additional comment or clarification about the adverse reaction', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalSynopsis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synopsis', models.TextField(help_text='The summary, assessment, conclusions or evaluation of the clinical findings')),
            ],
            options={
                'verbose_name_plural': 'Clinical Synopses',
            },
        ),
        migrations.CreateModel(
            name='ProblemDiagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_diagnosis_name', models.CharField(help_text='Identification of the problem or diagnosis, by name', max_length=255, null=True)),
                ('clinical_description', models.TextField(blank=True, help_text='Narrative description about the problem or diagnosis', null=True)),
                ('body_site_name', models.CharField(blank=True, help_text='The identifier of the body site, using a recognised clinical terminology where possible', max_length=255, null=True)),
                ('onset_date_time', models.DateTimeField(blank=True, help_text='Estimated or actual date/time that signs or symptoms of the problem/diagnosis were first observed', null=True)),
                ('recognition_date_time', models.DateTimeField(blank=True, help_text='Estimated or actual date/time the diagnosis or problem was recognised by a healthcare professional.', null=True)),
                ('severity', models.CharField(blank=True, choices=[('Mild', 'Mild [The problem or diagnosis does not interfere with normal activity or may cause damage to health if left untreated.]'), ('Moderate', 'Moderate [The problem or diagnosis causes interference with normal activity or will damage health if left untreated.]'), ('Severe', 'Severe [The problem or diagnosis prevents normal activity or will seriously damage health if left untreated.]')], help_text='An assessment of the overall severity of the problem or diagnosis', max_length=255, null=True)),
                ('course_description', models.TextField(blank=True, help_text='Narrative description about the course of the problem or diagnosis since onset', null=True)),
                ('resolution_date_time', models.DateTimeField(blank=True, help_text='Estimated or actual date/time of resolution or remission for this problem or diagnosis, as determined by a healthcare professional', null=True)),
                ('diagnostic_certainty', models.CharField(blank=True, choices=[('Suspected', 'Suspected [The diagnosis has been identified with a low level of certainty.]'), ('Probable', 'Probable [The diagnosis has been identified with a high level of certainty.]'), ('Confirmed', 'Confirmed [The diagnosis has been confirmed against recognised criteria.]')], help_text='The level of confidence in the identification of the diagnosis', max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, help_text='The date this problem or diagnosis was last updated', null=True)),
                ('comment', models.CharField(blank=True, help_text="Any random comment you can't fit into one of the other 572 fields in this archetype", max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Problems / Diagnoses',
            },
        ),
        migrations.RemoveField(
            model_name='relevantcontact',
            name='person_name',
        ),
        migrations.RemoveField(
            model_name='relevantcontact',
            name='telecom_details',
        ),
        migrations.RemoveField(
            model_name='symptomsign',
            name='body_site',
        ),
        migrations.AddField(
            model_name='symptomsign',
            name='body_site_name',
            field=models.CharField(blank=True, help_text='The identifier of the body site, using a recognised clinical terminology where possible', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='symptomsign',
            name='previous_episodes',
            field=models.ManyToManyField(blank=True, help_text='Structured details of the symptom or sign during a previous episode', related_name='_symptomsign_previous_episodes_+', to='django_openehr.SymptomSign'),
        ),
        migrations.AlterField(
            model_name='inpatientadmission',
            name='date_of_admission',
            field=models.DateTimeField(blank=True, help_text='Date patient admitted to hospital', null=True),
        ),
        migrations.AlterField(
            model_name='symptomsign',
            name='associated_symptom_sign',
            field=models.ManyToManyField(blank=True, help_text='Structured details about any associated symptoms or signs that are concurrent.', related_name='_symptomsign_associated_symptom_sign_+', to='django_openehr.SymptomSign'),
        ),
        migrations.DeleteModel(
            name='BodySite',
        ),
    ]
