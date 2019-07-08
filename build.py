import glob
import os
from jinja2 import Template


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

        built_page = page.render(
            image_names=image_dicts,
            image_path=i["image_path"]
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
