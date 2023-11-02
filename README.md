# Student Event Tracking System
A system for students who can view the critical and non-critical alerts in the form of a one-liner and a short summary. The primary reason for developing this system is to bring events pertaining to each user in various categories into a single view. The project will consist of an interactive UI (an initial design will be developed in Figma) that will developed in JAVA,  a simple database connection that stores user data, and event information (like a one-liner, summary, and raw data), and LLM-based information extraction from the different source such as Mail, Piazza discussion, Grade scope, and Spire. Since it will be difficult to get permission to assess  those APIs, we will synthesize data in those forms and emulate the scenario for our demo.

### Primary Features
Our 5 primary features are: critical deadline alerts, grade summaries, highlighting important piazza posts, providing upcoming exam alerts, and finally producing an LLM-based summary of this information for the user. 
### Architecture Design
Our project will be split into 5 parts, using a basic client-server architecture:
1. The UI will be prototyped and designed in Figma. It will communicate with the server.
2. The server will be written in Java and will compile information from the database to provide to the frontend UI.
3. The LLM-based section will be written in python and will operate independently from the other components. It will communicate with the server layer only.
4. The data access layer will be written using Firebase and store various tables of student information, piazza posts, etc.
5. We will generate synthetic data in JSON files using ChatGPT or some other language model.
### Timeline
Week of 10/30: Finish design
Week of 11/06: Generate synthetic data, implement UI, begin implementation of database, LLM
Week of 11/13: Finish implementation of database, LLM, link with server
Week of 11/20: Refine server, finish implementation of functionality, add security components
Week of 11/27: Testing
Week of 12/04: Testing
