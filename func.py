import openai
client = openai.AzureOpenAI(
    azure_endpoint = "https://neocentrailopenai202511.openai.azure.com/openai/deployments/Resumeevalutors-GPT-4O/chat/completions?api-version=2024-02-15-preview",
    api_key = "7MGSGMYxydjX4zq5frYyugqUvIDb71ZAvrJziiGEVFRXyFcFJsqdJQQJ99BCACHYHv6XJ3w3AAABACOGCO3N",
    api_version = "2024-05-01-preview")

def get_completion(prompt, model="gpt-35-turbo"): 
    messages = [{"role": "user", "content": prompt}]
    res = client.chat.completions.create(
        model="Resumeevalutors-GPT-4O",
        messages=messages,
        temperature=0.8   
    )
    return res.choices[0].message.content


def generate_jd(Location, Mode_of_work, Years_of_experience,Role_title, Key_skills, specific_requirements,job_responsibilities):
    
    prompt = f"""
    You are a job description generator tasked with creating detailed and compelling job descriptions for various roles within Neostats Analytics.

    About Neostats Analytics:
    NeoStats is a new-age, Data & Analytics firm offering contemporary solutions and infinite 
    possibilities. Our mission is to create lasting competitive advantage for our clients by transforming 
    them into world-class, data-driven organizations. Established in 2022 to provide End to End Data & 
    Analytics Services, we are headquartered out of UAE, with bases in India & UK. Comprising of 
    industry veterans, we enable structural transformations in Analytics powered by our expertise, true 
    partnership, and e2e implementation approach.

    What we offer: 
    • Competitive Salary and Benefits
    • Opportunity to be part of a fast paced and growing startup. Grow your career with 
    the company
    • Ownership - You will own your initiative and be given specific responsibilities 
    • Continuous coaching & mentoring – You will have the opportunity to interact and 
    work closely with other senior data scientists and AI experts across the globe. 
    • Dynamic and respectful work environment – we truly value you


    These are the set of rules listed in numbers that you need to follow:

    1) Craft descriptions that effectively communicate the responsibilities, qualifications, and 
    desired skills for each position, with the aim of attracting top-tier candidates. 
    2) Ensure diversity in job descriptions to cover a wide range of positions within the company. 
    3) Incorporate industry-specific terminology and buzzwords where applicable to enhance the appeal of Responsibilities and requirements section.
    4) Make sure you include these sections which are within brackets in the JD: (About Neostats Analytics, About the Job,  Responsibilities, Requirements, What we offer)
    5) Remember, there should be no changes in the About neostats analytics and what we offer section. It should remain same as it is mentioned above.
    6) The Job description should be around 400 words.
    7) The responsibilities section should contain more than 10 technical points related to the job title.
    8) Include more reasonable, industry-specific, job-specific terms related to the job title in the requirements section.
    8) The information within triple quotes is specified by the HR. Craft the JD accordingly. 
    9) If "use your learnings" is written anywhere, or if any information is not provided by the HR, then, fill it yourself.

    '''
    Location of the job - {Location}
    Mode of work (e.g., onsite, remote, hybrid)- {Mode_of_work}
    Years of experience required - {Years_of_experience}
    Role title - {Role_title}
    Key skills required - {Key_skills}
    Any specific requirements or qualifications (e.g., certifications, knowledge of specific software) - {specific_requirements}
    Brief description of the job responsibilities - {job_responsibilities}
    '''

    Default pre-screening questions:
    How many years of experience do you have in the industry? (numeric input)
    What is your current CTC? (numeric input)
    What is your expected CTC? (numeric input)
    What is your notice period in days? (numeric input)
    Are you willing to work from office 5 days a week?

    10) After generating the Job description, Generate some necessary pre-screening questions that can be posted in linkedin according to the JD generated by you. 
    The Rules for generating pre-screening questions include the following:
    10.1) The questions should be either multiple choice or numeric value input type or dichotomous.
    10.2) Mandatory to include questions related to number of years of experience related to key skills required as mentioned.
    10.3) Along with the pre screening questions generated by you, MAKE SURE YOU INCLUDE the default questions also, which are listed above.
    10.4) Give the questions generated by you and the default pre-screening questions listed under one heading as, "pre-screening question".
    10.5) Also, give the available answers along with the question. Incase of skill related question, have them rating their proficiency in that particular skill in a scale of 1 to 5.
    10.6) The total number of questions should be more than 10.
    
    11) Do not miss any of the above mentioned rules. follow everything.
    """

    response = get_completion(prompt)
    return response

