class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def props_to_html(self):
        """Generate the HTML attributes for the node as a string."""
        return ' '.join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        """Return a string representation of the node."""
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        """This method should be overridden by child classes."""
        raise NotImplementedError("to_html() must be implemented by subclasses.")

    