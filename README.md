# Team-Ovomaltine

## Team members

Saengrawi Gogniat,

Sunita Vijay Shelke,

Divya Sarah Abraham,

Aleksandra Iskrzynska.

## Histopathology department for breast cancer specimen analysis

Aim to improve the process from specimen registration, specimen analysis, and report generation by using digitalization.

## Description

This project focuses on transforming the analysis process within the pathology department, specifically for breast biopsy assessments. We aim to revolutionize the conventional approach by integrating advanced technology to expedite the diagnostic process and enhance accuracy. The project incorporates the utilization of an AFM (Atomic Force Microscopy) measurement device, specifically the Artidis, to assess the stiffness of the biopsy sample. Additionally, an image analysis techniques will be employed to automatically classify histopathology slides, reducing the reliance on manual human analysis.

## Goals

1. Reducing Waiting Time: The prolonged waiting period for biopsy results often causes distress and hampers timely treatment. By integrating AFM measurement and automated image analysis, we aim to significantly reduce the time required for diagnosis and reporting.

2. Enhancing Accuracy: Human analysis of biopsy samples may lead to errors in diagnosis, resulting in potential overtreating of patients due to incorrect assessments. By introducing additional biomarkers like AFM measurements and automated image classification, we aim to improve diagnostic accuracy and minimize the risk of misdiagnosis.

3. Automation of Analysis: The integration of the Artidis AFM device and image analysis tools will facilitate the automation of certain aspects of the analysis process, reducing the burden on pathologists and enabling more efficient workflows.

## Methods

- Implement technology to enhance the analysis process, including Artedis tissue stiffness measurement and machine learning histopathology image recognition. The final result is the integration of all measurements and specimen eligibility status, including the histopathology report from the pathologist, in the final report.
- Integrate Services using HTTP Connector with Python Flask in Deepnote
- Programming language: Python
- Camunda Modeler Platform 7

## Access to prototypes

Deepnote link: https://deepnote.com/workspace/l04-7d15acad-6de9-4091-891f-efd145100106/project/OlaAPI-69eb62be-3c1b-49e2-ac1f-d13d4e0bc6d3/notebook/Own%20API%20(Flask)-0fe27415a1ac4ffca2033f4b1f891436#0a4b4afdab044098a22e78ef8fae926a

Github: https://github.com/DigiBP/Team-Ovomaltine

## Running the process 
Warning: for demo purposes the process can be run for the specimen_IDs from 1 to 20. This restriction is connected to the images of the histopathology slides that are available. 
To run the process:
1. Run the Deepnote Notebook
2. Open the BPMN diagram via Camunda Modeler: BPMN_Diagram_Improvement.bpmn
3. Deploy the model in Camunda
4. Open Camunda Cockpit and navigate to start a new process: SpecimenJourney_experiment
5. Run through all of the steps of Camunda Tasks


## Tools

- Deepnote
- REST API with Flask - http connector
- Camunda Platform 7
- Microsoft Office Tools

## Technical Requirements

All required packages for Deepnote can be found in requirements.txt file in this repository.
