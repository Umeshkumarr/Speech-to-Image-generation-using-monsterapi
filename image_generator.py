from monsterapi import client

def generate_image(prompt, api_key):
    monster_client = client(api_key)

    input_data = {
        "prompt": prompt,
        "steps": 30,
        "aspect_ratio": "square"
    }

    result = monster_client.generate(
        model="txt2img",
        input=input_data
    )

    return result["output"][0]
