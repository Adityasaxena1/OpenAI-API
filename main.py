# import common
# import csv
#
#
# # ai_response = common.get_openai_response("Hello, How are you")
#
#
# def add_data_to_csv(data, file_path):
#     with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(data)
import common
import re
# value = "I want to change the title of my products into an e-commerce website. Here's an example: 0.01 CT Round Lab Grown Diamond Wedding Band. Is changed into some attractive title like Round Lab Grown Diamond Wedding Band in 0.01 CT Stones. Consider the previous example to generate the title for the given title '0.01 CT Round Lab Grown Diamond Necklace'. Your output only contain the title"
# value = f"Here's the title of the product on my online jewelry store {title}.  Using the given title, generate an title for the same product. Title must be descriptive, highlighting the benefits, including keywords, creating a sense of luxury, include size and specification. Your output only contain the title"


# titles = ['0.01 CT Round  Lab Grown Diamond Open Locket Pendant',
#           '0.01 CT Round Lab Grown Diamond Heart Shaped Necklace', '0.01 CT Round Lab Grown Diamond Necklace',
#           '0.01 CT Round Lab Grown Diamond Pendant Necklace', '0.01 CT Round Lab Grown Diamond Wedding Band', '0.2 TCW Round & Marquise Cut Diamonds Studs', '0.2 TCW Round Cut Diamonds Bezel Chain Earrings', '0.2 TCW Round Cut Diamonds Climbers', '0.2 TCW Round Cut Diamonds Heart Shaped Wedding Band', '0.2 TCW Round Cut Diamonds Flower Shaped Studs']
#
# for title in titles:
#     # value = common.get_openai_response(f"I want to change the title of my products into an e-commerce website. Here's an example: 0.01 CT Round Lab Grown Diamond Wedding Band. Is changed into some attractive title like Round Lab Grown Diamond Wedding Band in 0.01 CT Stones. Consider the previous example to generate the title for the given title {title}. Your output only contain the title")
#     value = common.get_openai_response(f"Here's the title of the product on my online jewelry store {title}.  Using the given title, generate an title for the same product. Title must be descriptive, highlighting the benefits, including keywords, creating a sense of luxury, include size and specification. Your output only contain the title")
#
#     # add_data_to_csv([title, value], 'testing_ai.csv')
#     print(value)
value = """Discover timeless elegance with our exquisite pendant, showcasing the epitome of craftsmanship and ethical luxury. At its heart lies a stunning lab-grown diamond, ethically grown and celebrated as the best in class. This round, brilliantly cut diamond, weighing 0.01 carats, captures the light with breathtaking brilliance and sophistication.

The pendant is meticulously crafted, measuring an elegant 15mm, and is available in a spectrum of luxurious gold hues—choose from radiant white, classic yellow, or romantic rose gold. Each piece is expertly fashioned from solid gold, with options for 10KT, 14KT, or 18KT purity, ensuring a lasting and beautiful finish. Feel confident in the authenticity of your piece, as each pendant bears the stamp of genuine craftsmanship.

To make this jewelry uniquely yours, we offer complimentary engraving in your choice of color or black. Every purchase is a comprehensive package, including the pendant, a certificate of authenticity, a beautifully crafted jewelry box, and a specialized jewelry cleaning kit to maintain its luster. Additionally, receive a thoughtful gift card for future purchases, and an enchanting surprise gift. Our commitment to quality is further affirmed by a lifetime limited warranty, offering you the assurance of enduring beauty and style.

Embrace the allure of sustainable luxury with this magnificent pendant, a treasure to cherish for a lifetime."""


def extract_body_content(html_text):

    match = re.search(r'<body>(.*?)</body>', html_text, re.DOTALL)

    # match = re.search(r'```html(.*?)```', html_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return "No body content found."
# ai_output = common.get_openai_response(f"Here is the description of my online jewlry product: {new_data[product_sku]['new_description']}. I want you to format the given description with some stylings in html format and make sure to keep the product details same as the given description. Your output only contain the html description body tag")
ai_output = common.get_openai_response(f"Here is the description of my online jewlry product: {value}. I want you to format the given description with some stylings in html format with some headings and any heading must not be h1. Your output only contain the html description body tag.")
# print(ai_output)

print(extract_body_content(ai_output))


