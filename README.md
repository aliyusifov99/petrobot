# PetroBot 🤖

## Overview

PetroBot is an advanced chatbot tailored for the petroleum industry, combining the power of machine learning with detailed industry-specific insights. This project utilizes OpenAI's cutting-edge technology to transform the way professionals access information, making user interaction with complex manuals as simple as asking a question. Click here to check out the [PetroBot](https://aliyusifov99-petrobot-main-c8vpla.streamlit.app/)

🎥 Check out a demo of PetroBot in action:
https://github.com/aliyusifov99/petrobot/assets/72607596/ce24a3c7-d50a-4c6f-87c0-4e9a302519e7

## Inspiration 💡

The concept of PetroBot was born from a desire to simplify the cumbersome process of navigating extensive software applications within the petroleum industry. During my final year, the inefficiency of manual search methods became clear, leading to the development of a chatbot that improves professional interaction with technology in the petroleum sector.

## Features 🌟

- **Interactive Q&A**: Instant, accurate responses to user inquiries, eliminating the need to consult extensive manuals.
- **Advanced AI Integration**: Incorporates OpenAI's sophisticated AI models for high-quality, contextually aware interactions.
- **User-Friendly Interface**: A simple, intuitive design facilitating ease of use and quick information retrieval.

## Installation 🔧

You can download the project using git clone git@github.com:aliyusifov99/petrobot.git

## Usage 🚀

The bot boasts a straightforward user interface, where users pose their queries in a chat format. It then retrieves the answers by consulting the manual and utilizing the GPT-4 model, employing a sophisticated question-answering technique.

## Technical Details 🔍

### Data Extraction

The data extraction process is pivotal in converting raw data from PDFs into a structured format suitable for further analysis. Using the `pdfplumber` library, text is efficiently extracted from PDF documents, with special emphasis on identifying section headers based on text case heuristics. The extracted text, potentially vast and unwieldy, is then segmented into smaller, more manageable pieces, ensuring they meet the constraints of APIs in subsequent steps.

The entire workflow benefits significantly from the `pandas` library, instrumental in handling and organizing data. Its robust data manipulation capabilities facilitate a seamless transition from raw text extraction to a structured format, ready for advanced operations like text embedding or deeper textual analysis.

### OpenAI API Integration

The integration phase with the OpenAI API was marked by rigorous testing, specifically evaluating the API's prowess in question-answering scenarios. Through methodical experimentation, we assessed the API's understanding and response accuracy, providing invaluable insights. These findings were crucial in refining our development approach, ensuring that the API's advanced AI capabilities were fully leveraged for high-quality, context-aware interactions in subsequent phases of the project.

### Interface Creation

The initial user interface, a critical point of interaction for users, was crafted using the `streamlit` library, known for its efficiency and ease of use in creating interactive web applications. The intuitive design simplifies user engagement with the system, allowing for straightforward information input and retrieval, as evident in the screenshot provided. This practical and user-friendly approach underscores the project's commitment to enhancing user experience.

### Word Embedding

During the text embedding phase, the "text-embedding-ada-002" model from OpenAI was employed to transform pre-processed text data into meaningful numerical representations or embeddings. This procedure, often challenged by the extensive nature of the text data, was conducted in batches to meet the API's operational constraints and maintain efficient data processing.

A strategy of careful batch size determination and robust error handling was implemented to ensure smooth communication with the OpenAI API and the integrity of the data exchange process. The `pandas` library played a crucial role in this phase as well, aiding in the systematic organization of the text embeddings in alignment with their corresponding text sections, essential for maintaining consistency and data integrity.

### Enhanced Text Inquiry

The project ventured into sophisticated text inquiry functionalities with the introduction of the `OpenAIInquirer` class, designed to process user queries using advanced OpenAI models. This class, initializing with specific user-related parameters, serves as a conduit between user inquiries and the deep learning models, ensuring custom-tailored interactions.

Internally, the class operates through several private methods, each contributing to the inquiry process's efficiency and precision. These include functions for retrieving texts based on relevance through cosine similarity calculations, understanding and managing query length concerning GPT model constraints, and carefully constructing the queries to be sent to the model, maintaining the structural and contextual integrity.

The culmination of these processes is the `inquire` method, which executes the inquiry, adhering to token limitations, and retrieves comprehensive, contextually relevant responses from the GPT model, enhancing the system's overall AI-human interaction quality.

## Contributions 👥

Warmly welcome and value contributions from the community to help the project grow. Here's how you can participate:

1. **Submit New Manuals**: Expand the repository by contributing manuals I haven't covered yet. By providing new content, you help diversify the information available and enhance the tool's usefulness.

2. **Enhance Query Responses**: Help me refine the system's interactions by improving how it responds to queries, especially by integrating images from manuals. Your insights into making responses more intuitive and informative will significantly enrich user experience.

3. **Financial Support**: The use of OpenAI APIs incurs costs. Your financial backing will support the scalability and continuous improvement of services, ensuring the project remains sustainable and accessible to everyone.


## References 📚

- [OpenAI Cookbook - Question Answering](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb)
- [Embedding Wikipedia Articles for Search](https://github.com/openai/openai-cookbook/blob/12f7c13b61cbe6703cbe7d5038eb9ed522f84141/examples/Embedding_Wikipedia_articles_for_search.ipynb)
- [Vectoring Words (Word Embeddings) - Computerphile](https://www.youtube.com/watch?v=gQddtTdmG_8)

## Connect with me

Feel free to reach out or follow my work through the following platforms:

- [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aliyusifov99)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ali-yusifov/)
- [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/aliyusifovpy)
- [![Portfolio](https://img.shields.io/badge/Personal_Website-4CAF50?style=for-the-badge&logo=google-earth&logoColor=white)](https://www.datascienceportfol.io/aliyusifov)
- [![Support](https://img.shields.io/badge/Buy_Me_A_Coffee-F7DF1E?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/aliyusifov)



