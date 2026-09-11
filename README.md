# Automatic Technical Documentation Generator

> **An AI-powered solution for automatically generating technical documentation from Java source code, with an integrated Natural Language Question & Answer assistant.**

## Overview

**Automatic Technical Documentation Generator** is an AI-powered project developed to simplify and automate the documentation of software projects.

The project addresses a common problem in software development: **technical documentation is often written and maintained manually by developers**, making the process time-consuming and difficult to keep synchronized with the source code.

Our solution analyzes **Java source code**, automatically generates meaningful code comments and structured technical documentation, and provides an interactive **Question & Answer interface** that allows developers to ask questions about their code using natural language.

The project was developed as part of our **Licence in Computer Science – Software Engineering & Information Systems** at **ESPRIT**, in collaboration with **Tritux Group**.

---

## Objectives

The main objectives of the project are to:

* ⚡ Automate the generation of technical documentation.
* 📝 Automatically generate meaningful comments for Java source code.
* 📚 Produce structured technical documentation in multiple formats.
* 🔍 Help developers understand existing code more easily.
* 💬 Provide a natural-language Question & Answer assistant for source code.
* 🤖 Leverage Large Language Models (LLMs) for code understanding and generation.
* 🔎 Use Retrieval-Augmented Generation (RAG) to improve the relevance of answers.
* 🚀 Integrate the solution directly into a development environment through an IDE plugin.

---

## Main Features

### Automatic Code Documentation

The system analyzes Java source code and generates structured documentation and explanatory comments automatically.

Instead of manually documenting every class, method, and component, developers can use the tool to generate documentation through a simplified workflow.

### Documentation Generation

The generated documentation can be exported in several formats:

* **HTML**
* **Markdown**
* **ZIP**

This makes the generated documentation easy to share, integrate, and consult.

### AI Question & Answer Assistant

The project also provides an interactive Q&A interface.

Developers can ask questions about their source code using natural language, such as:

> *"What is the role of this class?"*

> *"How does this method work?"*

> *"What are the dependencies of this component?"*

The system retrieves relevant information from the codebase and uses an LLM to generate an understandable answer.

### Retrieval-Augmented Generation (RAG)

A RAG pipeline is used to improve the Q&A process.

The source code is processed, transformed into embeddings, indexed, and retrieved according to the user's question. The relevant information is then provided to the language model to generate a contextual response.

### Fine-Tuned Language Model

The project explores the use of **Large Language Models specialized in code** and fine-tuning techniques to improve their ability to generate documentation and comments for Java code.

Techniques such as **LoRA** and **DeepSpeed** were investigated as part of the model development process.

### IDE Integration

The solution is integrated into a **JetBrains IDE** through a plugin, allowing developers to access the documentation generation workflow directly from their development environment.

---

## System Workflow

The overall workflow can be summarized as follows:

```text
             Java Source Code
                    │
                    ▼
          ┌───────────────────┐
          │   Code Analysis   │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │  AI Documentation │
          │     Generation    │
          └─────────┬─────────┘
                    │
             ┌──────┴──────┐
             ▼             ▼
      Code Comments    Documentation
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                  HTML       Markdown / ZIP


              Java Source Code
                    │
                    ▼
          ┌───────────────────┐
          │ RAG Ingestion &   │
          │ Vectorization     │
          └─────────┬─────────┘
                    │
                    ▼
             Vector Database
                    │
                    ▼
             User Question
                    │
                    ▼
             Relevant Retrieval
                    │
                    ▼
              Language Model
                    │
                    ▼
             Natural Language
                  Answer
```

---

## AI Architecture

The project combines several AI and NLP technologies:

### Large Language Models

LLMs specialized in programming are used to understand source code and generate documentation.

The project particularly investigates **DeepSeek Coder** and other candidate language models for commented Java code generation.

### Fine-Tuning

Fine-tuning is explored to adapt a language model to the specific task of generating technical comments and documentation.

The project uses techniques such as:

* **LoRA (Low-Rank Adaptation)**
* **DeepSpeed**
* Hyperparameter tuning

### Retrieval-Augmented Generation

The Q&A component follows a RAG architecture:

```text
Source Code
    │
    ▼
Document Ingestion
    │
    ▼
Chunking / Processing
    │
    ▼
Embeddings
    │
    ▼
Vector Index
    │
    ▼
User Question
    │
    ▼
Similarity Retrieval
    │
    ▼
Relevant Code Context
    │
    ▼
LLM
    │
    ▼
Generated Answer
```

---

## Technologies

The project combines software engineering, NLP, Deep Learning and Generative AI technologies.

| Category              | Technologies           |
| --------------------- | ---------------------- |
| Programming Language  | Java                   |
| AI / Machine Learning | Deep Learning, NLP     |
| Generative AI         | Large Language Models  |
| Code LLM              | DeepSeek Coder         |
| Fine-Tuning           | LoRA                   |
| Distributed Training  | DeepSpeed              |
| Retrieval             | RAG                    |
| Embeddings            | Text / Code Embeddings |
| IDE Integration       | JetBrains Plugin       |
| Documentation         | HTML, Markdown         |
| Methodology           | CRISP-DM               |

---

## Expected Benefits

The proposed solution aims to provide several benefits to developers and software teams:

* ⏱️ **Save development time** by reducing manual documentation work.
* 📖 **Improve code understanding** through automatically generated explanations.
* 🔄 **Facilitate documentation maintenance**.
* 🤝 **Improve collaboration** between developers.
* 🧩 **Reduce inconsistencies and omissions** in technical documentation.
* 💡 **Provide an intelligent assistant** capable of answering questions about the codebase.
* 🔌 **Integrate naturally into the developer workflow** through the IDE.

---

## Authors

This project was developed by:

**Islem Tellili**

**Manar Elhouda Ben Farhat**

The project was carried out in collaboration with **Tritux Group**.

---

## 📜 License

This repository contains the work developed as part of an academic PFE project.

Please refer to the repository for the applicable source-code and project usage conditions.
