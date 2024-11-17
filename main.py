import logging

import asyncio

from ragas.testset.graph import Node
from ragas.testset.transforms.extractors import NERExtractor

def document_splitter():
    sample_nodes = [Node(
        properties={"page_content": "Einstein's theory of relativity revolutionized our understanding of space and time. It introduced the concept that time is not absolute but can change depending on the observer's frame of reference."}
    ),Node(
        properties={"page_content": "Time dilation occurs when an object moves close to the speed of light, causing time to pass slower relative to a stationary observer. This phenomenon is a key prediction of Einstein's special theory of relativity."}
    )]
    print(sample_nodes)
    return sample_nodes

async def extract(nodes):
    extractor = NERExtractor()
    output = [await extractor.extract(node) for node in sample_nodes]
    output[0]

if __name__ == '__main__':
    sample_nodes = document_splitter()
    output = asyncio.run(extract(sample_nodes))