import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_listing(
    product_name,
    category,
    image_analysis
):

    prompt = f"""
You are an e-commerce copywriter.

Product Name:
{product_name}

Category:
{category}

Azure AI Vision Analysis:
{image_analysis}

Generate:

1. Product Title

2. Short Description

3. Key Selling Points (5 bullet points)

4. Shopee/Lazada Listing Description

5. SEO Keywords

Make the content professional, concise and suitable for Singapore e-commerce marketplaces.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional e-commerce copywriter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content