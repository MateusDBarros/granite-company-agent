# -*- coding: utf-8 -*-
import pandas as pd

def generate_language_school_data():
    file_name = 'company_data.xlsx'
    print(f"Generating synthetic dataset and saving to '{file_name}'...")

    with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
        workbook = writer.book

        methodology = {
            'Topic': [
                'Teaching Philosophy', 'Communicative Approach', 'Blended Learning',
                'Online Platform', 'Cultural Immersion'
            ],
            'Description': [
                'Learning a language is about connecting people and cultures. Focus goes beyond grammar.',
                'Student-centered classes with real-world simulations such as debates and presentations.',
                'Hybrid model with live classes plus a digital platform for self-paced learning.',
                'Interactive platform with exercises, videos, audios, quizzes, and adaptive AI.',
                'Monthly events: movie nights, conversation clubs, cooking workshops, etc.'
            ]
        }
        pd.DataFrame(methodology).to_excel(writer, sheet_name='Methodology', index=False)

        progression = {
            'Level (CEFR)': ['A1 Beginner', 'A2 Elementary', 'B1 Intermediate', 'B2 Upper-Intermediate', 'C1 Advanced'],
            'Skill Description': [
                'Understands and uses familiar expressions, can introduce themselves.',
                'Understands common phrases, communicates in routine tasks.',
                'Understands main points of familiar topics, manages most travel situations.',
                'Understands complex texts, communicates fluently with natives.',
                'Expresses fluently, uses language effectively for social, academic, professional purposes.'
            ],
            'Estimated Duration (months)': ['4-6', '4-6', '6-8', '6-8', '8-10']
        }
        pd.DataFrame(progression).to_excel(writer, sheet_name='Progression', index=False)

        courses = {
            'Course': [
                'Conversational English', 'Business English', 'TOEFL Prep', 'Spanish for Travel',
                'French Beginner', 'German Intensive', 'Italian Basics', 'Japanese for Beginners'
            ],
            'Level': ['B1-C1', 'B2-C2', 'B1+', 'A1-A2', 'A1', 'A1-B1', 'A1', 'A1'],
            'Duration (weeks)': [12, 16, 10, 8, 10, 8, 12, 16],
            'Description': [
                'Focus on fluency for daily situations.',
                'Corporate vocabulary, negotiation, and presentations.',
                'Strategies and mock exams for TOEFL iBT.',
                'Essential phrases for travel in Spanish-speaking countries.',
                'Intro to French language and culture.',
                'Fast-paced beginner German course.',
                'Learn greetings, useful phrases, and culture.',
                'Learn Hiragana/Katakana and basics of Japanese.'
            ],
            'Price ($)': [350, 500, 450, 250, 300, 400, 320, 480]
        }
        pd.DataFrame(courses).to_excel(writer, sheet_name='Courses', index=False)

        teachers = {
            'Teacher': ['Ana Silva', 'Carlos Andrade', 'Sofia Rossi', 'Marco Bianchi', 'Yuki Tanaka'],
            'Languages': ['English', 'Spanish, English', 'French, German', 'Italian', 'Japanese'],
            'Experience': [
                '10+ years experience, MSc in Applied Linguistics, exam prep specialist.',
                'Native from Madrid, Spain. Focus on immersive teaching.',
                'Franco-German background, 8+ years experience, interactive methods.',
                'Native Italian, uses music and cinema as teaching tools.',
                'Native from Osaka, MSc in teaching Japanese, focus on calligraphy and pop culture.'
            ]
        }
        pd.DataFrame(teachers).to_excel(writer, sheet_name='Teachers', index=False)

        testimonials = {
            'Student': ['Mariana Costa', 'João Pereira', 'Fernanda Lima', 'Ricardo Alves', 'Beatriz Endo'],
            'Course': ['Business English', 'Spanish for Travel', 'French Beginner', 'Italian Basics', 'Japanese for Beginners'],
            'Testimonial': [
                '"The course was a game-changer in my career."',
                '"Perfect prep for my backpacking trip in South America."',
                '"French finally felt possible thanks to Sofia’s method."',
                '"Marco’s classes made me feel like I was in Italy."',
                '"Yuki’s patience teaching writing was essential."'
            ]
        }
        pd.DataFrame(testimonials).to_excel(writer, sheet_name='Testimonials', index=False)

        faq = {
            'Question': [
                'What is the class size?', 'Do you offer online classes?', 'How can I enroll?',
                'Is material included?', 'What is your teaching methodology?',
                'How does blended learning work?', 'How long to reach B1?'
            ],
            'Answer': [
                'Max 8 students per class.',
                'Yes, available in-person and online.',
                'Enrollment via website or in-person.',
                'Yes, all digital materials are included.',
                'Communicative approach + blended learning.',
                'Weekly live classes plus 24/7 digital platform.',
                'From beginner, dedicated students usually reach B1 in 10–14 months.'
            ]
        }
        pd.DataFrame(faq).to_excel(writer, sheet_name='FAQ', index=False)

    print(f"File '{file_name}' created successfully.")

if __name__ == "__main__":
    generate_language_school_data()
