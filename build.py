import glob
import os
from jinja2 import Template
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def get_img_text(image_path):
    try:
        with Image.open(image_path) as image:
            detected_text = pytesseract.image_to_string(image, lang="eng")
    except FileNotFoundError:
        return ""
    return detected_text


def generate_pages(image_names):
    image_dicts = []
    for i in image_names:
        d = {}
        image_base = os.path.basename(i)
        image_name_no_ext, ext = os.path.splitext(image_base)
        image_name = " ".join(image_name_no_ext.split("_"))

        d["page_path"] = image_name_no_ext + ".html"
        d["image_path"] = "../images/" + image_base
        d["name"] = image_name
        image_dicts.append(d)

    for i in image_dicts:
        with open("templates/base.html") as template_fp:
            page = Template(template_fp.read())

        print(i["image_path"])

        image_path = "images/" + os.path.basename(i["image_path"])
        text = get_img_text(image_path)
        # print(text)
        if text:
            text = text.split("\n")
        else:
            text = ["No text detected"]

        built_page = page.render(
            image_names=image_dicts,
            image_path=i["image_path"],
            caption_lines=text
        )

        with open("docs/" + i["page_path"], 'w') as output_fp:
            output_fp.write(built_page)

        if i["name"] == "grace hopper":
            print(i)
            with open("docs/index.html", 'w') as index_fp:
                index_fp.write(built_page)


def main():
    all_images_names = glob.glob("images/*.jpg")
    generate_pages(all_images_names)


if __name__ == "__main__":
    main()
