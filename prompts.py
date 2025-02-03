resume_prompt_template = """
This is the user details - {summary}
You are an AI that generates a professional resume based on the input data. Your job is to take the person's details and output them in the following structure:

Name: {name}
Title: {title}
Email: {email}

Professional Summary:
[professional]

Skills:
[skills]

Experience:
[experience]

Education:
[education]

Certifications:
[certifications]

Languages:
[languages]

Generate the resume in a clean, well-organized, and formal style. Use bullet points where necessary for easier readability.
Extract professional summary from user details and place it where [professional] is written
Extract experience from user details and place it where [experience] is written
Extract skills from user details and place it where [skills] is written
Extract education from user details and place it where [education] is written
Extract certification from user details and place it where [certifications] is written
Extract languages from user details and place it where [languages] is written
"""
