import logging
from ragas.testset.graph import Node

def document_splitter():
    sample_nodes = [Node(
        properties={"page_content": "Einstein's theory of relativity revolutionized our understanding of space and time. It introduced the concept that time is not absolute but can change depending on the observer's frame of reference."}
    ),Node(
        properties={"page_content": "Time dilation occurs when an object moves close to the speed of light, causing time to pass slower relative to a stationary observer. This phenomenon is a key prediction of Einstein's special theory of relativity."}
    )]
    print(sample_nodes)
    return sample_nodes

if __name__ == '__main__':
    document_splitter()