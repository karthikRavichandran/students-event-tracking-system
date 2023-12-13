
import pandas as pd
import openai
import random
import os

DashB = pd.DataFrame({"Courses": ['math314', 'lang101', 'phys999', 'math314'],
                      "Description": ['HW1', 'Project Proposal', 'Quiz 3', 'Mid-Term'],
                      "Summary": ['Calculus and partial derivative', 'Understanding language syntax',
                                  'learning about escape velocity', 'Chapter 1 to Chapter 7'],
                      "Due in (days)": [3, 7, 4, 5],
                      "Avg. Scores (%)": ['89', '90', '78', '89'],
                      "Critical Level": ['High', 'Low', 'Very-High', 'Low'],
                      "Grade progress": [[random.randint(50, 100) for _ in range(10)] for _ in range(4)]})


# Set your OpenAI GPT-3.5 API key
# print(os.environ['OPENAI_API_KEY'])
openai.api_key = os.environ['OPENAI_API_KEY']

# Function to generate a summary using OpenAI GPT-3.5 API
def generate_summary(dataframe, prompt_user='Summarize the following Pandas DataFrame'):
    # Convert the DataFrame to a string representation
    dataframe_str = dataframe.to_string()

    # Define the prompt for the GPT-3.5 API
    prompt = f"{prompt_user}:\n{dataframe_str}\nSummary:"

    # Call the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the "text-davinci-003" engine for GPT-3.5
        prompt=prompt,
        max_tokens=250,  # Adjust the max tokens based on your preference
        temperature=0.7,  # Adjust the temperature based on your preference
    )

    # Extract and return the generated summary
    summary = response.choices[0].text.strip()
    return summary

def get_prompts(field='advice'):
    advice=['Advice the student based on each courses from this data. Use Description column as well in your advice',
            'Advice the student based on each courses from this data in just 3 points. Use Description column as well in your advice',
            'group by Courses column and advice the student based on each courses from this data. Use Description column as well in your advice']
    if field == 'advice':
        return advice


# Example usage
# data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
# df = pd.DataFrame(data)

# summary = generate_summary(DashB, prompt_user='Advice the student based on each courses from this data')
# print("Generated Summary:")
# print(summary)

