import config
import requests
import json


def get_headers():
    return {'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.api_key}'
            }


def get_base_url():
    return 'https://api.openai.com/v1'


def image_input(image_url):
    return {
        "type": "image_url",
        "image_url": {
            "url": image_url
        },
    }


def text_input(user_input):
    return {
        "type": "text",
        "text": user_input
    }


def get_content(user_input, images):
    content = [text_input(user_input)]

    for image in images:
        content.append(image_input(image['src']))

    return content


def get_payload_images(user_input, images):
    images_payload = json.dumps({
        "model": config.openai_model,
        "messages": [
            {
                "role": "user",
                "content":
                    get_content(user_input, images)

            }
        ]
    })

    return images_payload


def get_openai_response_with_image_input(user_input, images):
    response = requests.post(get_base_url() + "/chat/completions", headers=get_headers(),
                             data=get_payload_images(user_input, images))
    response.raise_for_status()
    ai_response = response.json()
    return ai_response['choices'][0]['message']['content']


def get_payload(user_input):
    return json.dumps({
        "model": config.openai_model,
        "messages": [{"role": "user", "content": user_input}]
    })


def get_openai_response(user_input):
    response = requests.post(get_base_url() + "/chat/completions", headers=get_headers(),
                             data=get_payload(user_input))
    response.raise_for_status()
    ai_response = response.json()
    return ai_response['choices'][0]['message']['content']

