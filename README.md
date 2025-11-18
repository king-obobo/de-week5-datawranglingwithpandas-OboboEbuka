###TODO: 

## Project summary (1 paragraph)
This project analyzes how well Zentel’s customer support centers perform against their Service Level Agreements (SLAs) and identify key areas of improvement using the data provided. Zentel Network Services is an imaginary leading telecommunications provider. Within its customer experience, customers log their different types of complaints across their branches and expect quick responses and resolutions to their queries.

Some of these customers have a Service level agreement with the Network service provider to resolve their daily queries within a particular average duration.

A dataset is provided which contains daily customer service performance records from Zentel Network Services. It consists of multiple related tables describing service tickets, employees, service types, channels, fault types, and locations. The data will be used to assess how efficiently customer issues are handled based on Service Level Agreements (SLAs).
## How to run (install requirements, python main.py)
Clone the repo and create a new environment. Activate the environment and install `uv`
```
pip install uv
```
Then run the command
```
uv sync
```
This command is used to align your current Python environment with the dependencies specified in your project’s pyproject.toml

## Explanation of results and and a very brief summary of your approach
* A look at the **total tickets per week** shows an increase in the number of tickets over week, with the total tickets being the highest on the third week. This is however followed by a sharp decline (possibly due to poor services) during the last week.


* We also see that for the response time, all through the week, we have less than 30% pass rate, with the pass rate peaking at week 2 but getting worst again at week 4. This trend is also similar with resolution sla, peaking at week 2 and getting worst at week 4.


* Most of our complaints are from the **social media** channel (around 30%). This channel also happens to have the highest mean resolutions and the highest response time


**Possible Key Factors Leading to Delay in Ticket Response Time**

* We see that Intrusions inherently take longer time to respond (mean sla being 378 seconds as compared to an ideal 10seconds)

* Operators also show variations in response speed suggesting uneven staff performance.


* On manager performance, there is clearly an uneven distribution of workload. Kerry and Victor with higher workloads still perform amazingly well though. This uneven distribution is also present in the operators.


### Recommendations
1. There should be improvement in workload balancing. Tickets loads should be redistributed from overwhelmed teams to less busy teams
2. Adequate trainings and proper supervisions should be provided for the different operators
3. Escalation protocols should be implemented to ensure critical tickets are prioritized 

## Tests: how to run pytest
-----
