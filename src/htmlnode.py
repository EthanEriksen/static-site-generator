class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props_list = []

        for prop in self.props:
            props_list.append(f" {prop}=\"{self.props[prop]}\"")

        return "".join(props_list)
    
    def __repr__(self):
        return {
            "tag": self.tag,
            "value": self.value,
            "children": self.children,
            "properties": self.props
        }
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError()
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"