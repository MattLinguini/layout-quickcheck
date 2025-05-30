from functools import reduce
from lqc.model.run_subject import RunSubject
from lqc.generate.web_page.util import formatWithIndent

current_template = """
<{tag} style="{style}" {attributes_string} id="{element_id}">
  {children_string}
</{tag}>
"""

def create(run_subject: RunSubject):

    body = run_subject.html_tree.tree
    styles = run_subject.base_styles.map

    def reduce_children(tree):
        return reduce(generate_element_string, tree, "")

    def generate_element_string(body_string, element):
        tag = element["tag"]
        if tag == "<text>":
            return body_string + element["value"]
        else:
            style = ";".join(
                [
                    f"{name}:{value}"
                    for name, value in styles.get(element["id"], {}).items()
                ]
            )

            attributes_dict = element.get("attributes", {})
            allowed_attributes = ["onclick"]
            attributes_string = " ".join(
                f"{name}='{value}'"
                for name, value in attributes_dict.items() if name in allowed_attributes
            )

            element_id = element["id"]
            children_string = reduce_children(element["children"])
            return body_string + formatWithIndent(current_template,
                tag=tag,
                style=style,
                element_id=element_id,
                attributes_string=attributes_string,
                children_string=children_string,
            )

    return reduce_children(body)
