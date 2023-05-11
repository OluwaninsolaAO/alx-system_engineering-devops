# 0x19. Postmortem

## Postmortem Report: Nginx Config Inconsistency Causes System Outage


#### Issue Summary:

On May 10, 2023, between 2:00 PM and 4:30 PM Eastern Daylight Time (EDT),
our website was down, and users were unable to access our services.
Approximately 75% of our users were affected. The root cause of the issue
was that Nginx's config was not properly modified, causing the config
inside sites-available to be different from site-enabled, which resulted
in Nginx not serving the appropriate websites.


#### Timeline:

+ `2:00 PM EDT`: Our monitoring system detected that our website was down.

+ `2:01 PM EDT`: The on-call engineer received an alert and began
investigating the issue.

+ `2:10 PM EDT`: The engineer determined that Nginx was not serving the
appropriate websites and began investigating the cause.

+ `2:20 PM EDT`: The engineer discovered that the config inside
sites-available was different from site-enabled, causing Nginx to malfunction.

+ `2:25 PM EDT`: The engineer attempted to restart Nginx but was unsuccessful
in resolving the issue.

+ `2:30 PM EDT`: The engineer escalated the issue to the senior system
administrator.

+ `2:45 PM EDT`: The senior system administrator reviewed the system logs
and confirmed the root cause of the issue.

+ `3:00 PM EDT`: The senior system administrator modified the config files,
restarted Nginx, and verified that the websites were properly served.


+ `4:30 PM EDT`: The issue was fully resolved, and our services were back
online.


#### Root cause and resolution:

The root cause of the issue was that Nginx's config was not properly modified,
causing the config inside sites-available to be different from site-enabled,
which resulted in Nginx not serving the appropriate websites. The resolution
was to modify the config files to ensure they were consistent between
sites-available and site-enabled, restart Nginx, and verify that the websites
were properly served.


#### Corrective and preventative measures:

To prevent similar incidents in the future, we will take the following
corrective and preventative measures:

+ Improve our change management process to ensure that any modifications
to Nginx's config are properly reviewed and tested before being implemented.

+ Implement monitoring tools to alert us if the config files become
inconsistent between sites-available and site-enabled.

+ Provide additional training to our team members on how to properly modify
Nginx's config files.

+ Create a checklist of steps to follow when modifying Nginx's config files
to ensure consistency and prevent errors.

+ Regularly review our Nginx config files to ensure they are up-to-date and
properly configured.


In summary, the outage occurred due to an inconsistency in Nginx's config
files, which prevented Nginx from serving the appropriate websites. The issue
was resolved by modifying the config files and restarting Nginx. To prevent
similar incidents in the future, we will implement measures to improve our
change management process, provide additional training to our team members,
and implement monitoring tools to alert us of any inconsistencies in the
config files.
