# 0x19-postmortem

## Issue Summary:

- Duration: The outage occurred from 10:00 AM to 12:00 PM (UTC-5).
- Impact: The web service was completely down during the outage, resulting in users being unable to access the website. Approximately 75% of the users were affected.

## Timeline:

- Detection: The issue was first detected at 10:00 AM by the monitoring system, which triggered an alert for high server response time.
- Investigation: The operations team immediately started investigating the issue, focusing on the server infrastructure and network connectivity.
- Assumptions: Initially, the team assumed that the high server response time was due to increased traffic or a network bottleneck.
- Misleading paths: The team spent significant time investigating the network components and scaling up the server infrastructure, which did not resolve the issue.
- Escalation: As the investigation did not yield results, the incident was escalated to the development team and the database administrators for further analysis.
- Resolution: After thorough investigation, it was discovered that the root cause of the issue was a misconfigured database connection pool, causing a bottleneck in handling incoming requests. The misconfiguration led to a depletion of available connections, resulting in the web service becoming unresponsive.
- Fix: The issue was resolved by updating the configuration of the database connection pool to allow for a higher number of concurrent connections, ensuring sufficient capacity to handle incoming requests.

## Root Cause and Resolution:
- Root Cause: The misconfigured database connection pool caused a depletion of available connections, leading to the unresponsiveness of the web service.
- Resolution: The issue was fixed by adjusting the configuration of the database connection pool to allow for a higher number of concurrent connections, effectively resolving the bottleneck issue.

## Corrective and Preventative Measures:
 ### Improvements: 
  - Enhance monitoring capabilities to proactively detect database connection pool issues.
  - Implement automated alerting for abnormal database connection pool behavior, such as low connection availability.
  - Establish regular reviews of critical system configurations to prevent misconfigurations from going unnoticed.

 ### Tasks to Address the Issue:
  - Update the database connection pool configuration to accommodate future growth and avoid connection depletion.
  - Conduct a comprehensive review of the system's configuration settings to identify and rectify any potential misconfigurations.
  - Implement automated testing and validation of critical system configurations to prevent misconfigurations during deployments.
  - Enhance documentation and knowledge sharing regarding best practices for configuring the database connection pool.

In conclusion, the web stack outage was caused by a misconfigured database connection pool, resulting in a depletion of available connections. The issue was resolved by adjusting the configuration to allow for a higher number of concurrent connections. To prevent similar incidents in the future, proactive monitoring, automated alerting, and comprehensive configuration reviews should be implemented, along with enhancing documentation and knowledge sharing practices.
