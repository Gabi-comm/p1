import os
import glob
import tiktoken
import numpy as np
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sklearn.manifold import TSNE
import plotly.graph_objects as go

#------------------
model= "gpt-4.1-nano"
db_name='vector_db'
load_dotenv(override=True)
openai_api_key=os.getenv("")
if openai_api_key:
    print("The api is working")
else:
    print("Key not set")

#--------------------
 