class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        # The use of the if else statments below is to set both children and props to a blank list
        # and a blank dictionary if they are constructed without inputs
        # This way they always exist as usable objects
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    
    def to_html(self):
        # This is to be overriden by child classes
        raise NotImplementedError("Only subclasses should implement this method.")
    
    
    def props_to_html(self):
        concatenated_string = ""
        """I originally implemented this
        for i in self.props:
            concatenated_string += f' {i}="{self.props[i]}"'
            """
        # These two lines should be more readable
        for key, value in self.props.items():
            concatenated_string += f' {key}="{value}"'
        return concatenated_string
    
    
    def __repr__(self):
        # I originally used this but realized i need to return this not print it
        # print(f"{self.tag}\n{self.value}\n{self.children}\n{self.props}")
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
        
        
  
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    
    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

