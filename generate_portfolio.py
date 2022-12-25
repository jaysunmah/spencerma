from tornado import template, escape
import sys

from gallery_descriptions import dates

div_template = """<div class=\"col-md-4 col-sm-6\">
    <div class=\"portfolio-item\">
        <a href=\"img/spencer/{spencer_img}.jpeg\" data-lightbox=\"image-1\">
            <div class=\"thumb\">
                <div class=\"hover-effect\">
                    <div class=\"hover-content\">
                        <h1></h1>
                        <p>{date}</p>
                    </div>
                </div>
                <div class=\"image\">
                    <img src=\"img/spencer/{spencer_img}.jpeg\">
                </div>
            </div>
        </a>
    </div>
</div>
"""

def generate_divs(num_pics):
    res = ""
    for i in range(num_pics + 1):
        div_str = div_template.format(
            spencer_img=str(i),
            date=dates[i],
        )
        res += div_str
    return res


def save_index(num_pics):
    div_str = generate_divs(num_pics)
    with open("index.html.template") as inp:
        template_text = inp.read()
        t = template.Template(template_text)
        txt = t.generate(portfolio_body=div_str)

    with open("index.html", "w") as res_f:
        res_f.write(txt)

if __name__ == "__main__":
    num_pics = sys.argv[1]
    save_index(int(num_pics))