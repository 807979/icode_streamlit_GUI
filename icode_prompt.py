def get_prompt(code_snippet):
      if not code_snippet:
        return "Error: No code snippet provided. Please provide a valid code snippet for analysis."
      prompt=f"""I’m providing a legacy code snippet or file. Please analyze it thoroughly and generate a detailed documentation using the structure below.
Assume the documentation is for new developers trying to understand this legacy system and maintain or modernize it.
{code_snippet}
Follow this step-by-step thought process to generate a clear and useful output:

1. Introduction
	State the likely project name, version, and a brief objective based on code behavior.
2. Overall Code Explanation
	Summarize what the code does at a high level.
	Mention technologies used or assumed from the syntax (e.g., COBOL, Python, etc.).
	Identify the purpose or intended business logic.
3. Code Structure Overview
	For each line or block in the code, add a one-line explanation.
	Use inline commenting style if possible.
4. Flow Diagram or Algorithm
	Either provide a step-by-step breakdown of the logic,
	Or describe a conceptual flow or algorithm if flowcharting isn’t possible.
5. Module Description
	Identify logical modules or sections within the code.
	For each module, write: module name, what it does, and key functions involved.
6. Input/Output Specification
	What inputs are required (variables, files, user input)?
	What is the expected output or final result of execution?
7. Core Logic Explanation
	Describe the most important part of the code and how it achieves the business logic.
8. Error Handling Analysis
	How are errors managed, if at all?
	Are there try-catch blocks, error codes, or silent failures?
9. Concurrency and Threading
	If applicable, describe how parallelism or multithreading is handled.
	Mention risks of race conditions or locking.
10. External Dependencies
	List libraries, packages, or external files accessed or required.
11. Potential Bugs
	Identify any suspicious code, outdated logic, or known error-prone areas.
12. Potential Improvements
	Suggest where the code could be modernized, refactored, or better organized.
13. Comparison with Best Practices
	Compare the code’s design, structure, and logic against standard best practices for that language or domain.
	Point out any violations or poor patterns.

Format the response strictly using the markdown rules for accurate documentation generation.
 -Use # for main heading , ## for subheadings, and ### for sub-subheadings.
 -Use bullet points for lists and code blocks for code snippets.
If the language is uncommon (like COBOL or Fortran), explain any domain-specific behaviors. 
Be concise but thorough — the goal is clarity for new developers working with legacy systems.


""" 
      return prompt