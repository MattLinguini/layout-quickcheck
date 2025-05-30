INCLUDE_VALUE_IN_NAME = ["display"]

from lqc.config.config import Config

class StyleMap():
    map = {}

    def __init__(self, map):
        self.map = map
        pass
    
    def removeById(self, id):
        del self.map[id]
    
    def getElementIds(self):
        return set(self.map.keys())
    
    def renameId(self, old_id, new_id):
        if old_id in self.map:
            self.map[new_id] = self.map[old_id]
            del self.map[old_id]

    def all_style_names(self):
        """Return all style names in this style map as a set
        Include style values for certain styles"""
        all_styles = set()
        for _elementid, styles in self.map.items():
            for style_name, style_value in styles.items():
                if style_name in INCLUDE_VALUE_IN_NAME:
                    all_styles.add(f"{style_name}:{style_value}")
                else:
                    all_styles.add(style_name)
        return all_styles
    
    def toJS(self):
        """
        Create a string that will make style changes in javascript

        Example Output: 

            var abeofmwlekrifj = document.getElementById("abeofmwlekrifj");
            if (abeofmwlekrifj) {
                abeofmwlekrifj.style["min-width"] = "200px";
                abeofmwlekrifj.style["margin-left"] = "10em";
            }

            var zomelfjeiwle = document.getElementById("zomelfjeiwle");
            if (zomelfjeiwle) {
                zomelfjeiwle.style["background-color"] = "blue";
            }
            
        """
        ret_string = ""
        for (elementId, styles) in self.map.items():

            elementStyles = list(styles.items())
            elementStyles.sort() # Sort alphabetical order by style name (to enforce the same order every time)

            if elementStyles:
                ret_string += f'var {elementId} = document.getElementById("{elementId}");\n'
                ret_string += 'if (' + elementId + ') {\n'

                for (style_name, style_value) in elementStyles:
                    # Skip properties that are configured to be excluded from being changed in style changes
                    if not Config().isPropertyExcluded(style_name):
                        ret_string += f'  {elementId}.style["{style_name}"] = "{style_value}";\n'
                
                ret_string += '}\n'

        return ret_string