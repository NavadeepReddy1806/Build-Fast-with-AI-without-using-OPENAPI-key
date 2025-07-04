EduChain MCP Server (Internship Assignment):

It builds an MCP-compatible server using Flask that:
 Generates Multiple-Choice Questions (MCQs)
 Generates Lesson Plans
 Accepts POST requests from Claude Desktop or Postman
 Returns formatted JSON educational content

 Features:
 `/tool/mcqs` → POST → Generates MCQs for a given topic
 `/resource/lessonplan` → POST → Generates a lesson plan for a given subject


How to Run: Install dependencies
```bash
pip install -r requirements.txt


Note: The questions are just smaple ones.
Note:
Claude Desktop integration was not tested as it now requires a Claude Pro subscription. 
However, all MCP endpoints were tested successfully using Postman and return correct results.
