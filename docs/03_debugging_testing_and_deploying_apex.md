
# Debugging, Testing, and Deploying Apex

```apex
// Now search the database looking for duplicates
for(Lead[] leadsCheck:[SELECT Id, duplicate_key__c FROM Lead WHERE
duplicate_key__c IN :leadMap.keySet()]) {
for(Lead lead:leadsCheck) {
// If there's a duplicate, add the error.
```

```apex
if(leadMap.containsKey(lead.Duplicate_Key__c))
leadMap.get(lead.Duplicate_Key__c).email.addError('Duplicate found
```

```apex
in salesforce(Id: ' + lead.Id + ')');
}
}
}
}
```

Apex Reference Guide : Pattern Class Apex Reference Guide : Matcher Class

## Debugging, Testing, and Deploying Apex

Develop your Apex code in a sandbox and debug it with the Developer Console and debug logs. Unit-test your code, then distribute it to customers using packages. Debugging Apex Apex provides debugging support. You can debug your Apex code using the Developer Console and debug logs. Testing Apex Apex provides a testing framework that allows you to write unit tests, run your tests, check test results, and have code coverage results. Deploying Apex You can't develop Apex in your Salesforce production org. Your development work is done in a sandbox, in a scratch org, or in a Developer Edition org. Apex in Managed Packages Learn how to develop, distribute, and use managed Apex. Apex in managed packages can behave differently than Apex in unmanaged packages or Apex deployed directly to an org. Managed package developers and subscribers must understand these differences so that they can safely evolve their packages and integrations.

## Debugging Apex

Apex provides debugging support. You can debug your Apex code using the Developer Console and debug logs. To aid debugging in your code, Apex supports exception statements and custom exceptions. Also, Apex sends emails to developers for unhandled exceptions. 1. Debug Log 2. Exceptions in Apex Exceptions note errors and other events that disrupt the normal flow of code execution. `throw` statements are used to generate exceptions, while `try` , `catch` , and `finally` statements are used to gracefully recover from exceptions.

### Debug Log

A debug log can record database operations, system processes, and errors that occur when executing a transaction or running unit tests. Debug logs can contain information about: Database changes HTTP callouts Apex errors Resources used by Apex Automated workflow processes, such as: Workflow rules Assignment rules Approval processes Validation rules The debug log doesn’t include information from actions triggered by time-based workflows. It also doesn’t include information from standard or custom controllers used in Visualforce email templates. You can retain and manage debug logs for specific users, including yourself, and for classes and triggers. Setting class and trigger trace flags doesn’t cause logs to be generated or saved. Class and trigger trace flags override other logging levels, including logging levels set by user trace flags, but they don’t cause logging to occur. If logging is enabled when classes or triggers execute, logs are generated at the time of execution. To view a debug log from Setup, enter `Debug` `Logs` in the `Quick` `Find` box, then select **Debug Logs** . Then click **View** next to the debug log that you want to examine. Click **Download** to download the debug log as a log file.

#### Debug Log Limits

Debug logs have the following limits. Each debug log must be 20 MB or smaller. Debug logs that are larger than 20 MB are reduced in size by removing older log lines, such as log lines for earlier `System.debug` statements. The log lines can be removed from any location, not just the start of the debug log. System debug logs are retained for 24 hours. Monitoring debug logs are retained for seven days. If you generate more than 1,000 MB of debug logs in a 15-minute window, your trace flags are disabled. We send an email to the users who last modified the trace flags, informing them that they can re-enable the trace flag in 15 minutes. If the debug log trace flag is enabled on a frequently accessed Apex class or for a user executing requests often, the request can result in failure, regardless of the time window and the size of the debug logs. When your org accumulates more than 1,000 MB of debug logs, we prevent users in the org from adding or editing trace flags. To add or edit trace flags so that you can generate more logs after you reach the limit, delete some debug logs.

#### Inspecting the Debug Log Sections

After you generate a debug log, the type and amount of information listed depends on the filter values you set for the user. However, the format for a debug log is always the same. Session IDs are replaced with "SESSION_ID_REMOVED" in Apex debug logs A debug log has the following sections. **Header** The header contains the following information. The version of the API used during the transaction. The log category and level used to generate the log. For example: The following is an example of a header.

```apex
67.0
APEX_CODE,DEBUG;APEX_PROFILING,INFO;CALLOUT,INFO;DB,INFO;SYSTEM,DEBUG;VALIDATION,INFO;VISUALFORCE,INFO;
WORKFLOW,INFO
```

In this example, the API version is 67.0, and the following debug log categories and levels have been set. DEBUG Apex Code INFO Apex Profiling INFO Callout INFO Database DEBUG System INFO Validation INFO Visualforce INFO Workflow If the Apex Code log level is set to FINEST, the debug log includes details of all Apex variable assignments. Ensure that the Apex Code being traced doesn’t handle sensitive data. Before enabling FINEST log level, be sure to understand the level of sensitive data your organization's Apex handles. Be careful with processes such as community users self-registration where user passwords can be assigned to an Apex string variable. **Execution Units** An execution unit is equivalent to a transaction. It contains everything that occurred within the transaction. `EXECUTION_STARTED` and `EXECUTION_FINISHED` delimit an execution unit. **Code Units** A code unit is a discrete unit of work within a transaction. For example, a trigger is one unit of code, as is a `webservice` method or a validation rule. A class isn’t a discrete unit of code. `CODE_UNIT_STARTED` and `CODE_UNIT_FINISHED` delimit units of code. Units of work can embed other units of work. For example:

```apex
EXECUTION_STARTED
CODE_UNIT_STARTED|[EXTERNAL]execute_anonymous_apex
CODE_UNIT_STARTED|[EXTERNAL]MyTrigger on Account trigger event BeforeInsert for
[new]|__sfdc_trigger/MyTrigger
CODE_UNIT_FINISHED <-- The trigger ends
CODE_UNIT_FINISHED <-- The executeAnonymous ends
EXECUTION_FINISHED
```

Units of code include, but aren’t limited to, the following: Triggers Workflow invocations and time-based workflow Validation rules Approval processes Apex lead convert `@future` method invocations Web service invocations `executeAnonymous` calls Visualforce property access on Apex controllers Visualforce actions on Apex controllers Execution of the batch Apex `start` and `finish` methods, and each execution of the `execute` method Execution of the Apex `System.Schedule` `execute` method Incoming email handling **Log Lines** Log lines are included inside units of code and indicate which code or rules are being executed. Log lines can also be messages written to the debug log. Log lines are made up of a set of fields, delimited by a pipe ( `|` ). The format is: timestamp : Consists of the time when the event occurred and a value between parentheses. The time is in the user’s time zone and in the format `HH:mm:ss.SSS` . The value in parentheses represents the time elapsed in nanoseconds since the start of the request. The elapsed time value is excluded from logs reviewed in the Developer Console when you use the Execution Log view. However, you can see the elapsed time when you use the Raw Log view. To open the Raw Log view, from the Developer Console’s Logs tab, right-click the name of a log and select **Open Raw Log** . event identifier : Specifies the event that triggered the debug log entry (such as `SAVEPOINT_RESET` or `VALIDATION_RULE` ). Also includes additional information logged with that event, such as the method name or the line and character number where the code was executed. If a line number can’t be located, `[EXTERNAL]` is logged instead. For example, `[EXTERNAL]` is logged for built-in Apex classes or code that’s in a managed package. For some events ( `CODE_UNIT_STARTED` , `CODE_UNIT_FINISHED` , `VF_APEX_CALL_START` , `VF_APEX_CALL_END` , `CONSTRUCTOR_ENTRY` , and `CONSTRUCTOR_EXIT` ), the end of the event identifier includes a pipe ( `|` ) followed by a typeRef for an Apex class or trigger. For a trigger, the typeRef begins with the SFDC trigger prefix `__sfdc_trigger/` . For example, `__sfdc_trigger/` `YourTriggerName` or `__sfdc_trigger/` `YourNamespace` `/` `YourTriggerName` . For a class, the typeRef uses the format `YourClass` , `YourClass` `$` `YourInnerClass,` , or `YourNamespace` `/` `YourClass` `$` `YourInnerClass` . **More Log Data** In addition, the log contains the following information. Cumulative resource usage is logged at the end of many code units. Among these code units are triggers, `executeAnonymous` , batch Apex message processing, `@future` methods, Apex test methods, Apex web service methods, and Apex lead convert. Cumulative profiling information is logged once at the end of the transaction and contains information about DML invocations, expensive queries, and so on. “Expensive” queries use resources heavily. Heap usage is accurately reported in the debug log and an exception is thrown whenever an Apex Heap Size error occurs. At other times, the heap size shown in the debug log is the largest heap size that was calculated during the transaction. To reduce the overhead on small transactions, minimal heap usage doesn’t warrant an accurate calculation and is reported as 0(zero). The following is an example debug log.

```apex
37.0 APEX_CODE,FINEST;APEX_PROFILING,INFO;CALLOUT,INFO;DB,INFO;SYSTEM,DEBUG;
VALIDATION,INFO;VISUALFORCE,INFO;WORKFLOW,INFO
Execute Anonymous: System.debug('Hello World!');
16:06:58.18 (18043585)|USER_INFO|[EXTERNAL]|005D0000001bYPN|devuser@example.org|
Pacific Standard Time|GMT-08:00
16:06:58.18 (18348659)|EXECUTION_STARTED
16:06:58.18 (18383790)|CODE_UNIT_STARTED|[EXTERNAL]|execute_anonymous_apex
16:06:58.18 (23822880)|HEAP_ALLOCATE|[72]|Bytes:3
16:06:58.18 (24271272)|HEAP_ALLOCATE|[77]|Bytes:152
16:06:58.18 (24691098)|HEAP_ALLOCATE|[342]|Bytes:408
16:06:58.18 (25306695)|HEAP_ALLOCATE|[355]|Bytes:408
16:06:58.18 (25787912)|HEAP_ALLOCATE|[467]|Bytes:48
16:06:58.18 (26415871)|HEAP_ALLOCATE|[139]|Bytes:6
16:06:58.18 (26979574)|HEAP_ALLOCATE|[EXTERNAL]|Bytes:1
16:06:58.18 (27384663)|STATEMENT_EXECUTE|[1]
16:06:58.18 (27414067)|STATEMENT_EXECUTE|[1]
16:06:58.18 (27458836)|HEAP_ALLOCATE|[1]|Bytes:12
16:06:58.18 (27612700)|HEAP_ALLOCATE|[50]|Bytes:5
16:06:58.18 (27768171)|HEAP_ALLOCATE|[56]|Bytes:5
16:06:58.18 (27877126)|HEAP_ALLOCATE|[64]|Bytes:7
16:06:58.18 (49244886)|USER_DEBUG|[1]|DEBUG|Hello World!
16:06:58.49 (49590539)|CUMULATIVE_LIMIT_USAGE
16:06:58.49 (49590539)|LIMIT_USAGE_FOR_NS|(default)|
Number of SOQL queries: 0 out of 100
Number of query rows: 0 out of 50000
Number of SOSL queries: 0 out of 20
Number of DML statements: 0 out of 150
Number of DML rows: 0 out of 10000
Maximum CPU time: 0 out of 10000
Maximum heap size: 0 out of 6000000
Number of callouts: 0 out of 100
Number of Email Invocations: 0 out of 10
Number of future calls: 0 out of 50
Number of queueable jobs added to the queue: 0 out of 50
Number of Mobile Apex push calls: 0 out of 10
```

```apex
16:06:58.49 (49590539)|CUMULATIVE_LIMIT_USAGE_END
```

```apex
16:06:58.18 (52417923)|CODE_UNIT_FINISHED|execute_anonymous_apex
16:06:58.18 (54114689)|EXECUTION_FINISHED
```

#### Setting Debug Log Filters for Apex Classes and Triggers

To debug complex Apex logic, you can set Apex class and trigger trace flags, also known as debug log filters. For example, you can raise the log verbosity for a given class while turning off logging for other classes or triggers. These trace flags have the debug log type `CLASS_TRACING` and override the debug log levels of the `USER_DEBUG` and `DEVELOPER_LOG` trace flags. For an explanation and an example of how Apex class and trigger trace flags work, see Debug Log Filtering for Apex Classes and Apex Triggers in Salesforce Help . For concrete instructions about how to configure debug log filters, see Set Up Apex Class and Trigger Trace Flags in Salesforce Help . Working with Logs in the Developer Console Use the Logs tab in the Developer Console to open debug logs. Debugging Apex API Calls Debug Log Order of Precedence Which events are logged depends on various factors. These factors include your trace flags, the default logging levels, your API header, user-based system log enablement, and the log levels set by your entry points. Salesforce Help : Set Up Debug Logging Salesforce Help : View Debug Logs Salesforce Help : Delete Debug Logs

#### Working with Logs in the Developer Console

Use the Logs tab in the Developer Console to open debug logs. Logs open in Log Inspector. Log Inspector is a context-sensitive execution viewer in the Developer Console. It shows the source of an operation, what triggered the operation, and what occurred next. Use this tool to inspect debug logs that include database events, Apex processing, workflow, and validation logic. To learn more about working with logs in the Developer Console, see Log Inspector in the Salesforce online help. When using the Developer Console or monitoring a debug log, you can specify the level of information that gets included in the log. **Log category** The type of information logged, such as information from Apex or workflow rules. **Log level** The amount of information logged. **Event type** The combination of log category and log level that specify which events get logged. Each event can log additional information, such as the line and character number where the event started, fields associated with the event, and duration of the event. Each debug level includes a debug log level for each of these log categories. The amount of information logged for each category depends on the log level. Includes information about database activity, including every data manipulation language (DML) statement or inline SOQL or SOSL query. `Database` Logs rules and policy information for objects accessed from the UI, which can be used to determine why an object isn’t accessible. `Database` `Access` Includes information for workflow rules, flows, and processes, such as the rule name and the actions taken. `Workflow` Includes information about Einstein Next Best Action activity, including strategy execution details from Strategy Builder. `NBA` Includes information about validation rules, such as the name of the rule and whether the rule evaluated true or false. `Validation` Includes the request-response XML that the server is sending and receiving from an external web service. Useful when debugging issues related to using Lightning Platform web service API calls or troubleshooting user access to external objects via Salesforce Connect.

```apex
Callout
```

Includes information about Apex code. Can include information such as log messages generated by DML statements, inline SOQL or SOSL queries, the start and completion of any triggers, and the start and completion of any test method.

```apex
Apex Code
```

Includes cumulative profiling information, such as the limits for your namespace and the number of emails sent. `Apex` `Profiling` Includes information about Visualforce events, including serialization and deserialization of the view state or the evaluation of a formula field in a Visualforce page. `Visualforce` Includes information about calls to all system methods such as the `System.debug` method. `System` Each debug level includes one of these log levels for each log category. The levels are listed from lowest to highest. Specific events are logged based on the combination of category and levels. Most events start being logged at the INFO level. The level is cumulative, that is, if you select FINE, the log also includes all events logged at the DEBUG, INFO, WARN, and ERROR levels. Not all levels are available for all categories. Only the levels that correspond to one or more events are available. `NONE` `ERROR` `WARN` `INFO` `DEBUG` `FINE` `FINER` `FINEST` Before running a deployment, verify that the Apex Code log level isn’t set to FINEST. Otherwise, the deployment is likely to take longer than expected. If the Developer Console is open, the log levels in the Developer Console affect all logs, including logs created during a deployment. This example shows what is written to the debug log. The event is `USER_DEBUG` . The format is `timestamp` | `event` `identifier` . This example shows a debug log line. **Debug Log Line Example** timestamp : Consists of the time when the event occurred and a value between parentheses. The time is in the user’s time zone and in the format `HH:mm:ss.SSS` . The value in parentheses represents the time elapsed in nanoseconds since the start of the request. The elapsed time value is excluded from logs reviewed in the Developer Console when you use the Execution Log view. However, you can see the elapsed time when you use the Raw Log view. To open the Raw Log view, from the Developer Console’s Logs tab, right-click the name of a log and select **Open Raw Log** . event identifier : Specifies the event that triggered the debug log entry, such as `SAVEPOINT_RESET` or `VALIDATION_RULE` . Also includes additional information logged with that event, such as the method name or the line and character number where the code was executed. If a line number can’t be located, `[EXTERNAL]` is logged instead. For example, `[EXTERNAL]` is logged for built-in Apex classes or code that’s in a managed package. For some events, such as `CODE_UNIT_STARTED` , `CODE_UNIT_FINISHED` , `VF_APEX_CALL_START` , `VF_APEX_CALL_END` , `CONSTRUCTOR_ENTRY` , and `CONSTRUCTOR_EXIT` , the end of the event identifier includes a pipe ( `|` ) followed by a typeRef for an Apex class or trigger. For a trigger, the typeRef begins with the SFDC trigger prefix `__sfdc_trigger/` . For example, `__sfdc_trigger/` `YourTriggerName` or `__sfdc_trigger/` `YourNamespace` `/` `YourTriggerName` . For a class, the typeRef uses the format `YourClass` , `YourClass` `$` `YourInnerClass,` or `YourNamespace` `/` `YourClass` `$` `YourInnerClass` . In this example, the event identifier consists of: Event name:

```apex
USER_DEBUG
```

Line number of the event in the code:

```apex
[2]
```

Logging level the `System.Debug` method was set to:

```apex
DEBUG
```

User-supplied string for the `System.Debug` method:

```apex
Hello world!
```

This code snippet triggers this example log line. **Debug Log Line Code Snippet** This log line is recorded when the test reaches line 5 in the code.

```apex
15:51:01.071 (55856000)|DML_BEGIN|[5]|Op:Insert|Type:Invoice_Statement__c|Rows:1
```

In this example, the event identifier consists of: Event name:

```apex
DML_BEGIN
```

Line number of the event in the code:

```apex
[5]
```

DML operation type— `Insert` :

```apex
Op:Insert
```

Object name:

```apex
Type:Invoice_Statement__c
```

Number of rows passed into the DML operation:

```apex
Rows:1
```

These event types are logged. The table lists which fields or other information are logged with each event, and which combination of log level and category causes an event to be logged. FINEST Apex Code Number of bytes allocated `BULK_HEAP_ALLOCATE` INFO and above Callout Line number and request headers `CALLOUT_REQUEST` INFO and above Callout External endpoint and method `CALLOUT_REQUEST` (External object access via cross-org and OData adapters for Salesforce Connect) INFO and above Callout Line number and response body `CALLOUT_RESPONSE` INFO and above Callout Status and status code `CALLOUT_RESPONSE` (External object access via cross-org and OData adapters for Salesforce Connect) ERROR and above Apex Code Line number, code unit name, such as `MyTrigger` `on` `Account` `trigger` `event` `BeforeInsert` `for` `[new]` , and:

```apex
CODE_UNIT_FINISHED
```

For Apex methods, the namespace (if applicable), class name, and method name; for example, `YourNamespace.YourClass.yourMethod()` or `YourClass.yourMethod()` For Apex triggers, a typeRef; for example, `__sfdc_trigger/YourNamespace.YourTrigger` or `__sfdc_trigger/YourTrigger` ERROR and above Apex Code Line number, code unit name, such as `MyTrigger` `on` `Account` `trigger` `event` `BeforeInsert` `for` `[new]` , and:

```apex
CODE_UNIT_STARTED
```

For Apex methods, the namespace (if applicable), class name, and method name; for example, `YourNamespace.YourClass.yourMethod()` or `YourClass.yourMethod()` For Apex triggers, a typeRef; for example, `__sfdc_trigger/YourTrigger` FINE and above Apex Code Line number, Apex class ID, the string `<init>()` with the types of parameters (if any) between the

```apex
CONSTRUCTOR_ENTRY
```

parentheses, and a typeRef; for example, `YourClass` or `YourClass.YourInnerClass` FINE and above Apex Code Line number, the string `<init>()` with the types of parameters (if any) between the parentheses, and a

```apex
CONSTRUCTOR_EXIT
```

typeRef; for example, `YourClass` or `YourClass.YourInnerClass` INFO and above Apex Profiling None `CUMULATIVE_LIMIT_USAGE` INFO and above Apex Profiling None `CUMULATIVE_LIMIT_USAGE_END` FINE and above Apex Profiling None `CUMULATIVE_PROFILING` FINE and above Apex Profiling None `CUMULATIVE_PROFILING_BEGIN` FINE and above Apex Profiling None `CUMULATIVE_PROFILING_END` INFO and above DB Line number and SOQL query This event occurs when you call `Database.getCursor()` or `Database.getPaginationCursor()` .

```apex
CURSOR_CREATE_BEGIN
```

INFO and above DB Line number, query ID, and number of rows in the result set

```apex
CURSOR_CREATE_END
```

This event occurs when a cursor or pagination cursor is created. INFO and above DB Line number, query ID, cursor offset position, and number of rows fetched

```apex
CURSOR_FETCH
```

This event occurs when you call `Cursor.fetch()` . INFO and above DB Line number, query ID, cursor offset position, and number of rows on the current page

```apex
CURSOR_FETCH_PAGE
```

This event occurs when you call `PaginationCursor.fetchPage()` . FINE Data Access Request and Response for the data access request. Used regardless of the data space or policy being accessed.

```apex
DATA_ACCESS_EVALUATION
```

INFO and above DB Line number, operation (such as `Insert` or `Update` ), record name or type, and number of rows passed into DML operation

```apex
DML_BEGIN
```

INFO and above DB Line number `DML_END` INFO and above Apex Code Line number `EMAIL_QUEUE` FINE and above Apex Code Package namespace `ENTERING_MANAGED_PKG` INFO and above Workflow Event Type `EVENT_SERVICE_PUB_BEGIN` FINER and above Workflow Subscription IDs, ID of the user who published the event, and event message data

```apex
EVENT_SERVICE_PUB_DETAIL
```

INFO and above Workflow Event Type `EVENT_SERVICE_PUB_END` INFO and above Workflow Event type and action (subscribe or unsubscribe) `EVENT_SERVICE_SUB_BEGIN` FINER and above Workflow ID of the subscription, ID of the subscription instance, reference data (such as process API name), ID of the user who activated or deactivated the subscription, and event message data

```apex
EVENT_SERVICE_SUB_DETAIL
```

INFO and above Workflow Event type and action (subscribe or unsubscribe) `EVENT_SERVICE_SUB_END` INFO and above Apex Code Line number, exception type, and message `EXCEPTION_THROWN` ERROR and above Apex Code None `EXECUTION_FINISHED` ERROR and above Apex Code None `EXECUTION_STARTED` ERROR and above Apex Code Exception type, message, and stack trace `FATAL_ERROR` FINER and above Workflow Interview ID, element name, action type, action enum or ID, whether the action call succeeded, and error message

```apex
FLOW_ACTIONCALL_DETAIL
```

FINER and above Workflow Interview ID, reference, operator, and value `FLOW_ASSIGNMENT_DETAIL` FINE and above Workflow Interview ID and element type `FLOW_BULK_ELEMENT_BEGIN` FINER and above Workflow Interview ID, element type, element name, number of records `FLOW_BULK_ELEMENT_DETAIL` FINE and above Workflow Interview ID, element type, element name, number of records, and execution time

```apex
FLOW_BULK_ELEMENT_END
```

FINER and above Workflow Incremented usage toward a limit for this bulk element. Each event displays the usage for one of these limits.

```apex
SOQL queries
SOQL query rows
```

```apex
FLOW_BULK_ELEMENT_LIMIT_USAGE
```

```apex
SOSL queries
DML statements
DML rows
CPU time in ms
Heap size in bytes
Callouts
Email invocations
Future calls
Jobs in queue
Push notifications
```

INFO and above Workflow Operation, element name, and entity name that doesn’t support bulk operations

```apex
FLOW_BULK_ELEMENT_NOT_SUPPORTED
```

INFO and above Workflow Organization ID, definition ID, and version ID `FLOW_CREATE_INTERVIEW_BEGIN` INFO and above Workflow Interview ID and flow name `FLOW_CREATE_INTERVIEW_END` ERROR and above Workflow Message, organization ID, definition ID, and version ID `FLOW_CREATE_INTERVIEW_ERROR` FINE and above Workflow Interview ID, element type, and element name `FLOW_ELEMENT_BEGIN` FINE and above Workflow Element type and element name `FLOW_ELEMENT_DEFERRED` FINE and above Workflow Interview ID, element type, and element name `FLOW_ELEMENT_END` ERROR and above Workflow Message, element type, and element name (flow runtime exception) `FLOW_ELEMENT_ERROR` ERROR and above Workflow Message, element type, and element name (spark not found) `FLOW_ELEMENT_ERROR` ERROR and above Workflow Message, element type, and element name (designer exception) `FLOW_ELEMENT_ERROR` ERROR and above Workflow Message, element type, and element name (designer limit exceeded) `FLOW_ELEMENT_ERROR` ERROR and above Workflow Message, element type, and element name (designer runtime exception) `FLOW_ELEMENT_ERROR` WARNING and above Workflow Message, element type, and element name (fault path taken) `FLOW_ELEMENT_FAULT` FINER and above Workflow Incremented usage toward a limit for this element. Each event displays the usage for one of these limits.

```apex
SOQL queries
SOQL query rows
```

```apex
FLOW_ELEMENT_LIMIT_USAGE
```

```apex
SOSL queries
DML statements
DML rows
CPU time in ms
Heap size in bytes
Callouts
```

```apex
Email invocations
Future calls
Jobs in queue
Push notifications
```

FINER and above Workflow Usage toward a limit when the interview finishes. Each event displays the usage for one of these limits.

```apex
SOQL queries
SOQL query rows
```

```apex
FLOW_INTERVIEW_FINISHED_LIMIT_USAGE
```

```apex
SOSL queries
DML statements
DML rows
CPU time in ms
Heap size in bytes
Callouts
Email invocations
Future calls
Jobs in queue
Push notifications
```

INFO and above Workflow Interview ID, flow name, and why the user paused `FLOW_INTERVIEW_PAUSED` INFO and above Workflow Interview ID and flow name `FLOW_INTERVIEW_RESUMED` FINER and above Workflow Interview ID, index, and value The index is the position in the collection variable for the item that the loop is operating on.

```apex
FLOW_LOOP_DETAIL
```

FINER and above Workflow Interview ID, rule name, and result `FLOW_RULE_DETAIL` INFO and above Workflow Interview ID and flow name `FLOW_START_INTERVIEW_BEGIN` INFO and above Workflow Interview ID and flow name `FLOW_START_INTERVIEW_END` INFO and above Workflow Requests `FLOW_START_INTERVIEWS_BEGIN` INFO and above Workflow Requests `FLOW_START_INTERVIEWS_END` ERROR and above Workflow Message, interview ID, and flow name `FLOW_START_INTERVIEWS_ERROR` FINER and above Workflow Usage toward a limit at the interview’s start time. Each event displays the usage for one of these limits.

```apex
SOQL queries
SOQL query rows
```

```apex
FLOW_START_INTERVIEW_LIMIT_USAGE
```

```apex
SOSL queries
DML statements
DML rows
CPU time in ms
Heap size in bytes
Callouts
Email invocations
Future calls
Jobs in queue
Push notifications
```

INFO and above Workflow Message and number of records that the flow runs for `FLOW_START_SCHEDULED_RECORDS` FINER and above Workflow Interview ID, name, definition ID, and version ID `FLOW_SUBFLOW_DETAIL` FINER and above Workflow Interview ID, key, and value `FLOW_VALUE_ASSIGNMENT` FINER and above Workflow Interview ID, element name, event name, and event type `FLOW_WAIT_EVENT_RESUMING_DETAIL` FINER and above Workflow Interview ID, element name, event name, event type, and whether conditions were met

```apex
FLOW_WAIT_EVENT_WAITING_DETAIL
```

FINER and above Workflow Interview ID, element name, and persisted interview ID `FLOW_WAIT_RESUMING_DETAIL` FINER and above Workflow Interview ID, element name, number of events that the element is waiting for, and persisted interview ID

```apex
FLOW_WAIT_WAITING_DETAIL
```

FINER and above Apex Code Line number and number of bytes `HEAP_ALLOCATE` FINER and above Apex Code Line number and number of bytes deallocated `HEAP_DEALLOCATE` FINEST DB Line number `IDEAS_QUERY_EXECUTE` FINEST Apex Profiling Namespace and these limits:

```apex
Number of SOQL queries
```

```apex
LIMIT_USAGE_FOR_NS
```

```apex
Number of query rows
```

```apex
Number of SOSL queries
```

```apex
Number of DML statements
```

```apex
Number of DML rows
```

```apex
Number of code statements
```

```apex
Maximum heap size
```

```apex
Number of callouts
```

```apex
Number of Email
Invocations
```

```apex
Number of fields
describes
```

```apex
Number of record type
describes
```

```apex
Number of child
relationships
```

```apex
describes
```

```apex
Number of picklist
describes
```

```apex
Number of future calls
```

```apex
Number of find similar
calls
```

```apex
Number of System.runAs()
```

```apex
invocations
```

FINE and above Apex Code Line number, the Lightning Platform ID of the class, and method signature (with namespace, if applicable)

```apex
METHOD_ENTRY
```

FINE and above Apex Code Line number, the Lightning Platform ID of the class, and method signature (with namespace, if applicable) For constructors, this information is logged: line number and class name.

```apex
METHOD_EXIT
```

INFO and above Callout Named Credential Id, Named Credential Name, Endpoint, Method, External Credential Type, Http Header

```apex
NAMED_CREDENTIAL_REQUEST
```

Authorization, Request Size bytes, and Retry on 401. If using an outbound network connection, these fields are also logged: Outbound Network Connection Id, Outbound Network Connection Name, Outbound Network Connection Status, Host Type, Host Region, and Private Connect Outbound Hourly Data Usage Percent. INFO and above Callout Truncated section of the response body that’s returned from the NamedCredential callout.

```apex
NAMED_CREDENTIAL_RESPONSE
```

FINER and above Callout Named Credential Id, Named Credential Name, Status Code, Response Size bytes, Overall Callout Time ms, and Connect Time ms. If using an outbound network connection, these fields are also

```apex
NAMED_CREDENTIAL_RESPONSE_DETAIL
```

logged: Outbound Network Connection Id, Outbound Network Connection Name, and Private Connect Outbound Hourly Data Usage Percent. FINE and above NBA Element name, element type `NBA_NODE_BEGIN` FINE and above NBA Element name, element type, message `NBA_NODE_DETAIL` FINE and above NBA Element name, element type, message `NBA_NODE_END` ERROR and above NBA Element name, element type, error message `NBA_NODE_ERROR` FINE and above NBA Name, ID, reason `NBA_OFFER_INVALID` FINE and above NBA Strategy name `NBA_STRATEGY_BEGIN` FINE and above NBA Strategy name, count of outputs `NBA_STRATEGY_END` ERROR and above NBA Strategy name, error message `NBA_STRATEGY_ERROR` FINER Data Access Condition evaluation response for a policy. Used for identifying conditions that match the policy.

```apex
POLICY_RULE_DEFINITION_CONDITION_EVALUATION_RESPONSE
```

FINE Data Access Request received for the evaluation of access via the policy. `POLICY_RULE_EVALUATION_REQUEST` FINER Data Access Response for the evaluation of access via the policy, including why access is granted or denied.

```apex
POLICY_RULE_EVALUATION_RESPONSE
```

FINER Data Access Object for which the policy evaluation is skipped. If the policy evaluation is skipped, the user is allowed access to the object.

```apex
POLICY_RULE_EVALUATION_SKIPPED
```

FINER Data Access Rule being evaluated. `POLICY_RULE_EVALUATION_START` INFO and above System Line number, the Lightning Platform ID of the class or trigger that has its log levels set and that is going into scope,

```apex
POP_TRACE_FLAGS
```

the name of this class or trigger, and the log level settings that are in effect after leaving this scope ERROR Apex Code App namespace, app name This event occurs when Apex code is trying to send a notification to an app

```apex
PUSH_NOTIFICATION_INVALID_APP
```

that doesn't exist in the org, or isn’t push-enabled. ERROR Apex Code App namespace, app name This event indicates that the certificate is invalid. For example, it’s expired.

```apex
PUSH_NOTIFICATION_INVALID_CERTIFICATE
```

ERROR Apex Code App namespace, app name, service type (Apple or Android GCM), user ID, device, payload (substring), payload length. This event occurs when a notification payload is too long.

```apex
PUSH_NOTIFICATION_INVALID_NOTIFICATION
```

DEBUG Apex Code App namespace, app name This event occurs when none of the users we’re trying to send notifications to have devices registered.

```apex
PUSH_NOTIFICATION_NO_DEVICES
```

INFO Apex Code This event occurs when push notifications aren’t enabled in your org.

```apex
PUSH_NOTIFICATION_NOT_ENABLED
```

DEBUG Apex Code App namespace, app name, service type (Apple or Android GCM), user ID, device, payload (substring) This event records that a notification was accepted for sending. We don’t guarantee delivery of the notification.

```apex
PUSH_NOTIFICATION_SENT
```

INFO and above System Line number, the Salesforce ID of the class or trigger that has its log levels set and that is going out of scope, the

```apex
PUSH_TRACE_FLAGS
```

name of this class or trigger, and the log level settings that are in effect after entering this scope INFO and above DB Line number `QUERY_MORE_BEGIN` INFO and above DB Line number `QUERY_MORE_END` INFO and above DB Line number and the number of `queryMore` iterations `QUERY_MORE_ITERATIONS` INFO and above DB Line number and Savepoint name `SAVEPOINT_ROLLBACK` INFO and above DB Line number and Savepoint name `SAVEPOINT_SET` INFO and above Workflow Number of cases, load time, processing time, number of case milestones to insert, update, or delete, and new trigger

```apex
SLA_END
```

INFO and above Workflow Milestone ID `SLA_EVAL_MILESTONE` INFO and above Workflow None `SLA_NULL_START_DATE` INFO and above Workflow Case ID `SLA_PROCESS_CASE` INFO and above DB Line number, number of aggregations, and query source `SOQL_EXECUTE_BEGIN` INFO and above DB Line number, number of rows, and duration in milliseconds `SOQL_EXECUTE_END` FINEST DB Query Plan details for the executed SOQL query. To get feedback on query `SOQL_EXECUTE_EXPLAIN` performance, see Get Feedback on Query Performance . INFO and above DB Line number and query source `SOSL_EXECUTE_BEGIN` INFO and above DB Line number, number of rows, and duration in milliseconds `SOSL_EXECUTE_END` FINE and above Apex Profiling Frame number and variable list of the form: `Variable` `number` | `Value` . For example:

```apex
var1:50
```

```apex
var2:'Hello World'
```

```apex
STACK_FRAME_VARIABLE_LIST
```

FINER and above Apex Code Line number `STATEMENT_EXECUTE` FINE and above Apex Profiling Variable list of the form: `Variable` `number` | `Value` . For example:

```apex
var1:50
```

```apex
var2:'Hello World'
```

```apex
STATIC_VARIABLE_LIST
```

FINE and above System Line number and the string `<init>()` with the types of parameters, if any, between the parentheses

```apex
SYSTEM_CONSTRUCTOR_ENTRY
```

FINE and above System Line number and the string `<init>()` with the types of parameters, if any, between the parentheses

```apex
SYSTEM_CONSTRUCTOR_EXIT
```

FINE and above System Line number and method signature `SYSTEM_METHOD_ENTRY` FINE and above System Line number and method signature `SYSTEM_METHOD_EXIT` INFO and above System Mode name `SYSTEM_MODE_ENTER` INFO and above System Mode name `SYSTEM_MODE_EXIT` INFO and above Apex Profiling None `TESTING_LIMITS` FINE and above Apex Profiling Number of emails sent `TOTAL_EMAIL_RECIPIENTS_QUEUED` DEBUG and Apex Code Line number, logging level, and user-supplied string `USER_DEBUG` above by default. If the user sets the log level for the `System.Debug` method, the event is logged at that level instead. ERROR and above Apex Code Line number, user ID, username, user timezone, and user timezone in GMT `USER_INFO` INFO and above Validation Error message `VALIDATION_ERROR` INFO and above Validation None `VALIDATION_FAIL` INFO and above Validation Formula source and values `VALIDATION_FORMULA` INFO and above Validation None `VALIDATION_PASS` INFO and above Validation Rule name `VALIDATION_RULE` FINEST Apex Code Line number, variable name (including the variable’s namespace, if applicable), a string representation of

```apex
VARIABLE_ASSIGNMENT
```

the variable’s value, and the variable’s address FINEST Apex Code Line number, variable name (including the variable’s namespace, if applicable), type, a value that indicates

```apex
VARIABLE_SCOPE_BEGIN
```

whether the variable can be referenced, and a value that indicates whether the variable is static FINEST Apex Code None `VARIABLE_SCOPE_END` INFO and above Apex Code Element name, method name, return type, and the typeRef for the Visualforce controller (for example, `YourApexClass` )

```apex
VF_APEX_CALL_START
```

INFO and above Apex Code Element name, method name, return type, and the typeRef for the Visualforce controller (for example, `YourApexClass` )

```apex
VF_APEX_CALL_END
```

INFO and above Visualforce View state ID `VF_DESERIALIZE_VIEWSTATE_BEGIN` INFO and above Visualforce None `VF_DESERIALIZE_VIEWSTATE_END` FINER and above Visualforce View state ID and formula `VF_EVALUATE_FORMULA_BEGIN` FINER and above Visualforce None `VF_EVALUATE_FORMULA_END` INFO and above Apex Code Message text `VF_PAGE_MESSAGE` INFO and above Visualforce View state ID `VF_SERIALIZE_VIEWSTATE_BEGIN` INFO and above Visualforce None `VF_SERIALIZE_VIEWSTATE_END` INFO and above Workflow Action description `WF_ACTION` INFO and above Workflow Task subject, action ID, rule name, rule ID, owner, and due date `WF_ACTION_TASK` INFO and above Workflow Summary of actions performed `WF_ACTIONS_END` INFO and above Workflow Transition type, `EntityName:` `NameField` `Id` , and process node name

```apex
WF_APPROVAL
```

INFO and above Workflow `EntityName:` `NameField` `Id` `WF_APPROVAL_REMOVE` INFO and above Workflow `EntityName:` `NameField` `Id` `WF_APPROVAL_SUBMIT` INFO and above Workflow Submitter ID, submitter full name, and error message `WF_APPROVAL_SUBMITTER` INFO and above Workflow Owner and assignee template ID `WF_ASSIGN` INFO and above Workflow `EntityName:` `NameField` `Id` , rule name, rule ID, and (if rule respects trigger types) trigger type and recursive count

```apex
WF_CRITERIA_BEGIN
```

INFO and above Workflow Boolean value indicating success (true or false) `WF_CRITERIA_END` INFO and above Workflow Action ID, rule name, and rule ID `WF_EMAIL_ALERT` INFO and above Workflow Email template ID, recipients, and CC emails `WF_EMAIL_SENT` INFO and above Workflow Summary of actions enqueued `WF_ENQUEUE_ACTIONS` INFO and above Workflow Case ID and escalation date `WF_ESCALATION_ACTION` INFO and above Workflow None `WF_ESCALATION_RULE` INFO and above Workflow Process name, email template ID, and Boolean value indicating result (true or false)

```apex
WF_EVAL_ENTRY_CRITERIA
```

INFO and above Workflow `EntityName:` `NameField` `Id` and the object or field name `WF_FIELD_UPDATE` INFO and above Workflow ID of flow trigger `WF_FLOW_ACTION_BEGIN` FINE and above Workflow ID of flow trigger, object type and ID of record whose creation or update caused the workflow rule to fire, name

```apex
WF_FLOW_ACTION_DETAIL
```

and ID of workflow rule, and the names and values of flow variables INFO and above Workflow ID of flow trigger `WF_FLOW_ACTION_END` ERROR and above Workflow ID of flow trigger, ID of flow definition, ID of flow version, and flow error message

```apex
WF_FLOW_ACTION_ERROR
```

ERROR and above Workflow Detailed flow error message `WF_FLOW_ACTION_ERROR_DETAIL` INFO and above Workflow Formula source and values `WF_FORMULA` INFO and above Workflow None `WF_HARD_REJECT` INFO and above Workflow Owner, next owner type, and field `WF_NEXT_APPROVER` INFO and above Workflow None `WF_NO_PROCESS_FOUND` INFO and above Workflow `EntityName:` `NameField` `Id` , action ID, rule name, and rule ID `WF_OUTBOUND_MSG` INFO and above Workflow Process definition ID and process label `WF_PROCESS_FOUND` INFO and above Workflow Process name `WF_PROCESS_NODE` INFO and above Workflow `EntityName:` `NameField` `Id` and owner `WF_REASSIGN_RECORD` INFO and above Workflow Notifier name, notifier email, notifier template ID, and reply-to email `WF_RESPONSE_NOTIFY` INFO and above Workflow Integer indicating order `WF_RULE_ENTRY_ORDER` INFO and above Workflow Rule type `WF_RULE_EVAL_BEGIN` INFO and above Workflow None `WF_RULE_EVAL_END` INFO and above Workflow Value `WF_RULE_EVAL_VALUE` INFO and above Workflow Filter criteria `WF_RULE_FILTER` INFO and above Workflow `EntityName:` `NameField` `Id` `WF_RULE_INVOCATION` INFO and above Workflow None `WF_RULE_NOT_EVALUATED` INFO and above Workflow Process name `WF_SOFT_REJECT` INFO and above Workflow Node type `WF_SPOOL_ACTION_BEGIN` INFO and above Workflow `EntityName:` `NameField` `Id` , time action, time action container, and evaluation Datetime

```apex
WF_TIME_TRIGGER
```

INFO and above Workflow None `WF_TIME_TRIGGERS_BEGIN` FINER and above Callout For OData adapters, the POST body and the name and evaluated formula for custom HTTP headers

```apex
XDS_DETAIL
```

(External object access via cross-org and OData adapters for Salesforce Connect) INFO and above Callout External data source, external object, request details, number of returned records, and system usage

```apex
XDS_RESPONSE
```

(External object access via cross-org and OData adapters for Salesforce Connect) FINER and above Callout Truncated response from the external system, including returned records `XDS_RESPONSE_DETAIL` (External object access via cross-org and OData adapters for Salesforce Connect) ERROR and above Callout Error message `XDS_RESPONSE_ERROR` (External object access via cross-org and OData adapters for Salesforce Connect) Salesforce Help : Debug Log Levels Salesforce Help : Partition Your Data with Enhanced Security Data Spaces Salesforce Help : User Access Policies

#### Debugging Apex API Calls

All API calls that invoke Apex support a debug facility that allows access to detailed information about the execution of the code, including any calls to `System.debug()` . The `categories` field of a SOAP input header called `DebuggingHeader` allows you to set the logging granularity according to the levels outlined in this table. Specify the type of information returned in the debug log. Valid values are: LogCategory `category` `Db` `Workflow`

```apex
•
Validation
```

`Callout`

```apex
•
Apex_code
```

```apex
•
Apex_profiling
```

```apex
•
Visualforce
```

`System` `All` Specifies the level of detail returned in the debug log. Valid log levels are (listed from lowest to highest): LogCategoryLevel `level` `NONE` `ERROR` `WARN` `INFO` `DEBUG` `FINE` `FINER` `FINEST` In addition, the following log levels are still supported as part of the `DebuggingHeader` for backwards compatibility. Does not include any log messages. `NONE` Includes lower-level messages, and messages generated by calls to the `System.debug` method. `DEBUGONLY` Includes log messages generated by calls to the `System.debug` method, and every data manipulation language (DML) statement or inline SOQL or SOSL query. `DB` Includes log messages generated by calls to the `System.debug` method, every DML statement or inline SOQL or SOSL query, and the entrance and exit of every user-defined method. `PROFILE` In addition, the end of the debug log contains overall profiling information for the portions of the request that used the most resources. This profiling information is presented in terms of SOQL and SOSL statements, DML operations, and Apex method invocations. These three sections list the locations in the code that consumed the most time, in descending order of total cumulative time. Also listed is the number of times the categories executed. Includes the request-response XML that the server is sending and receiving from an external web service. Useful when debugging issues related to using Lightning Platform web service API calls or troubleshooting user access to external objects via Salesforce Connect.

```apex
CALLOUT
```

Includes all messages generated by the `PROFILE` level and the following. `DETAIL` Variable declaration statements Start of loop executions All loop controls, such as break and continue Thrown exceptions * Static and class initialization code * Any changes in the `with` `sharing` context The corresponding output header, `DebuggingInfo` , contains the resulting debug log. For more information, see `DebuggingHeader` in the SOAP API Developer Guide .

#### Debug Log Order of Precedence

Which events are logged depends on various factors. These factors include your trace flags, the default logging levels, your API header, user-based system log enablement, and the log levels set by your entry points. The order of precedence for debug log levels is: **1.** Trace flags override all other logging logic. The Developer Console sets a trace flag when it loads, and that trace flag remains in effect until it expires. You can set trace flags in the Developer Console or in Setup or by using the `TraceFlag` and `DebugLevel` Tooling API objects. Setting class and trigger trace flags doesn’t cause logs to be generated or saved. Class and trigger trace flags override other logging levels, including logging levels set by user trace flags, but they don’t cause logging to occur. If logging is enabled when classes or triggers execute, logs are generated at the time of execution. **2.** If you don’t have active trace flags, synchronous and asynchronous Apex tests execute with the default logging levels. Default logging levels are: **DB** INFO **APEX_CODE** DEBUG **APEX_PROFILING** INFO **WORKFLOW** INFO **VALIDATION** INFO **CALLOUT** INFO **VISUALFORCE** INFO **SYSTEM** DEBUG **3.** If no relevant trace flags are active, and no tests are running, your API header sets your logging levels. API requests that are sent without debugging headers generate transient logs—logs that aren’t saved—unless another logging rule is in effect. **4.** If your entry point sets a log level, that log level is used. For example, Visualforce requests can include a debugging parameter that sets log levels. If none of these cases apply, logs aren’t generated or persisted.

### Exceptions in Apex

Exceptions note errors and other events that disrupt the normal flow of code execution. `throw` statements are used to generate exceptions, while `try` , `catch` , and `finally` statements are used to gracefully recover from exceptions. There are many ways to handle errors in your code, including using assertions like `System.assert` calls, or returning error codes or Boolean values, so why use exceptions? The advantage of using exceptions is that they simplify error handling. Exceptions bubble up from the called method to the caller, as many levels as necessary, until a `catch` statement is found to handle the error. This bubbling up relieves you from writing error-handling code in each of your methods. Also, by using `finally` statements, you have one place to recover from exceptions, like resetting variables and deleting data.

#### What Happens When an Exception Occurs?

When an exception occurs, code execution halts. Any DML operations that were processed before the exception are rolled back and aren’t committed to the database. Exceptions get logged in debug logs. For unhandled exceptions (exceptions that the code doesn’t catch) Salesforce sends an email that includes the exception information. The end user sees an error message in the Salesforce user interface.

#### Unhandled Exception Emails

Take advantage of free-tier access to Event Monitoring, and track unhandled exceptions in Apex code execution instead of relying only on unhandled exception emails. Troubleshoot your Apex code by analyzing the information captured in the event log files for the Apex Unexpected Exception event type. When unhandled Apex exceptions occur, emails sent contain the Apex stack trace, exception message, customer’s org and user ID, org name, and My Domain name. No other data is returned with the report. Unhandled exception emails are sent by default to the developer specified in the `LastModifiedBy` field on the failing class or trigger. In addition, you can have emails sent to users of your Salesforce org and to arbitrary email addresses. These email recipients can also receive process or flow error emails. To set up these email notifications, from Setup, enter `Apex` `Exception` `Email` in the `Quick` `Find` box, then select **Apex Exception Email** . The entered email addresses then apply to all managed packages in the customer's org. You can also configure Apex exception emails using Tooling API object ApexEmailNotification. If duplicate exceptions occur in Apex code that runs synchronously or asynchronously, subsequent exception emails are suppressed and only the first email is sent. This email suppression prevents flooding of the developer’s inbox with emails about the same error. Emails aren’t sent for exceptions encountered with anonymous Apex executions or with Apex methods accessed by Aura components and Lightning web components via the @AuraEnabled annotation. Apex exception emails are limited to 10 emails per hour, per application server. Because this limit isn’t on a per-org basis, email delivery to a particular org can be unreliable.

#### Unhandled Exceptions in the User Interface

If an end user runs into an exception that occurred in Apex code while using the standard user interface, an error message appears. The error message includes text similar to the notification shown here. Exception Statements Exception Handling Example Learn how exception handling works in Apex. Built-In Exceptions and Common Methods Catching Different Exception Types Create Custom Exceptions

#### Exception Statements

Apex uses exceptions to note errors and other events that disrupt the normal flow of code execution. `throw` statements can be used to generate exceptions, while `try` , `catch` , and `finally` can be used to gracefully recover from an exception. A `throw` statement allows you to signal that an error has occurred. To throw an exception, use the `throw` statement and provide it with an exception object to provide information about the specific error. For example:

```apex
throw exceptionObject;
```

The `try` , `catch` , and `finally` statements can be used to gracefully recover from a thrown exception: The `try` statement identifies a block of code in which an exception can occur. The `catch` statement identifies a block of code that can handle a particular type of exception. A single `try` statement can have zero or more associated `catch` statements. Each `catch` statement must have a unique exception type. Also, once a particular exception type is caught in one `catch` block, the remaining `catch` blocks, if any, aren’t executed. The `finally` statement identifies a block of code that is guaranteed to execute and allows you to clean up your code. A single `try` statement can have up to one associated `finally` statement. Code in the `finally` block always executes regardless of whether an exception was thrown or the type of exception that was thrown. Because the `finally` block always executes, use it for cleanup code, such as for freeing up resources. The syntax of the `try` , `catch` , and `finally` statements is as follows.

```apex
try {
```

```apex
// Try block
code_block
} catch (exceptionType variableName) {
```

```apex
// Initial catch block.
// At least the catch block or the finally block must be present.
code_block
} catch (Exception e) {
```

```apex
// Optional additional catch statement for other exception types.
// Note that the general exception type, 'Exception',
// must be the last catch block when it is used.
code_block
} finally {
```

```apex
// Finally block.
// At least the catch block or the finally block must be present.
code_block
}
```

At least a `catch` block or a `finally` block must be present with a `try` block. The following is the syntax of a try-catch block.

```apex
try {
code_block
} catch (exceptionType variableName) {
code_block
}
// Optional additional catch blocks
```

The following is the syntax of a try-finally block.

```apex
try {
code_block
} finally {
code_block
}
```

This is a skeletal example of a try-catch-finally block.

```apex
try {
```

```apex
// Perform some operation that
//
might cause an exception.
} catch(Exception e) {
```

```apex
// Generic exception handling code here.
} finally {
```

```apex
// Perform some clean up.
}
```

Some special types of built-in exceptions can’t be caught. Those exceptions are associated with critical situations in the Lightning Platform. These situations require the abortion of code execution and don’t allow for execution to resume through exception handling. One such exception is the limit exception ( `System.LimitException` ) that the runtime throws if a governor limit such as heap size or CPU time has been exceeded, when the maximum number of SOQL queries issued has been exceeded, an attempt is made to retrieve more than the maximum number of records, and so on. Other examples are exceptions thrown when assertion statements fail (through `System.assert` methods) or license exceptions. When exceptions are uncatchable, `catch` blocks, as well as `finally` blocks if any, aren’t executed. In API version 41.0 and later, unreachable statements in your code will cause compilation errors. For example, the following code block generates a compile time error in API version 41.0 and later. The third statement can never be reached because the previous statement throws an unconditional exception.

```apex
Boolean x = true;
throw new NullPointerException();
x = false;
```

#### Exception Handling Example

Learn how exception handling works in Apex. To see an exception in action, execute some code that causes a DML exception to be thrown. Execute the following in the Developer Console:

```apex
Merchandise__c m = new Merchandise__c();
insert m;
```

The `insert` DML statement in the example causes a DmlException because we’re inserting a merchandise item without setting any of its required fields. This is the exception error that you see in the debug log.

```apex
System.DmlException: Insert failed. First exception on row 0; first error:
REQUIRED_FIELD_MISSING, Required fields are missing: [Description, Price, Total
Inventory]: [Description, Price, Total Inventory]
```

Next, execute this snippet in the Developer Console. It’s based on the previous example but includes a try-catch block.

```apex
try {
Merchandise__c m = new Merchandise__c();
insert m;
} catch(DmlException e) {
System.debug('The following exception has occurred: ' + e.getMessage());
}
```

Notice that the request status in the Developer Console now reports success. This is because the code handles the exception. Any statements in the try block occurring after the exception are skipped and aren’t executed. For example, if you add a statement after `insert` `m;` , this statement won’t be executed. Execute the following:

```apex
try {
Merchandise__c m = new Merchandise__c();
insert m;
// This doesn't execute since insert causes an exception
System.debug('Statement after insert.');
} catch(DmlException e) {
System.debug('The following exception has occurred: ' + e.getMessage());
}
```

In the new debug log entry, notice that you don’t see a debug message of `Statement` `after` `insert` . This is because this debug statement occurs after the exception caused by the insertion and never gets executed. To continue the execution of code statements after an exception happens, place the statement after the try-catch block. Execute this modified code snippet and notice that the debug log now has a debug message of `Statement` `after` `insert` .

```apex
try {
Merchandise__c m = new Merchandise__c();
insert m;
} catch(DmlException e) {
System.debug('The following exception has occurred: ' + e.getMessage());
}
// This will get executed
System.debug('Statement after insert.');
```

Alternatively, you can include additional try-catch blocks. This code snippet has the `System.debug` statement inside a second try-catch block. Execute it to see that you get the same result as before.

```apex
try {
Merchandise__c m = new Merchandise__c();
insert m;
} catch(DmlException e) {
```

```apex
System.debug('The following exception has occurred: ' + e.getMessage());
}
```

```apex
try {
System.debug('Statement after insert.');
// Insert other records
}
catch (Exception e) {
```

```apex
// Handle this exception here
}
```

The finally block always executes regardless of what exception is thrown, and even if no exception is thrown. Let’s see it used in action. Execute the following:

```apex
// Declare the variable outside the try-catch block
// so that it will be in scope for all blocks.
XmlStreamWriter w = null;
try {
w = new XmlStreamWriter();
w.writeStartDocument(null, '1.0');
w.writeStartElement(null, 'book', null);
w.writeCharacters('This is my book');
w.writeEndElement();
w.writeEndDocument();
```

```apex
// Perform some other operations
String s;
// This causes an exception because
// the string hasn't been assigned a value.
Integer i = s.length();
} catch(Exception e) {
System.debug('An exception occurred: ' + e.getMessage());
} finally {
```

```apex
// This gets executed after the exception is handled
System.debug('Closing the stream writer in the finally block.');
// Close the stream writer
w.close();
}
```

The previous code snippet creates an XML stream writer and adds some XML elements. Next, an exception occurs due to accessing the null String variable `s` . The catch block handles this exception. Then the finally block executes. It writes a debug message and closes the stream writer, which frees any associated resources. Check the debug output in the debug log. You’ll see the debug message `Closing` `the` `stream` `writer` `in` `the` `finally` `block.` after the exception error. This tells you that the finally block executed after the exception was caught. Create Custom Exceptions Salesforce Developers Blog : Error Handling Best Practices for Lightning and Apex

#### Built-In Exceptions and Common Methods

Apex provides a number of built-in exception types that the runtime engine throws if errors are encountered during execution. You've seen the DmlException in the previous example. Here is a sample of some other built-in exceptions. For a complete list of built-in exception types, see Exception Class and Built-In Exceptions . **DmlException** Any problem with a DML statement, such as an `insert` statement missing a required field on a record. This example makes use of DmlException. The `insert` DML statement in this example causes a DmlException because it’s inserting a merchandise item without setting any of its required fields. This exception is caught in the `catch` block and the exception message is written to the debug log using the `System.debug` statement.

```apex
try {
Merchandise__c m = new Merchandise__c();
insert m;
} catch(DmlException e) {
System.debug('The following exception has occurred: ' + e.getMessage());
}
```

**ListException** Any problem with a list, such as attempting to access an index that is out of bounds. This example creates a list and adds one element to it. Then, an attempt is made to access two elements, one at index 0, which exists, and one at index 1, which causes a ListException to be thrown because no element exists at this index. This exception is caught in the catch block. The `System.debug` statement in the catch block writes the following to the debug log: `The` `following` `exception` `has` `occurred:` `List` `index` `out` `of` `bounds:` `1` .

```apex
try {
List<Integer> li = new List<Integer>();
li.add(15);
// This list contains only one element,
// but we're attempting to access the second element
// from this zero-based list.
Integer i1 = li[0];
Integer i2 = li[1]; // Causes a ListException
} catch(ListException le) {
System.debug('The following exception has occurred: ' + le.getMessage());
}
```

**NullPointerException** Any problem with dereferencing a `null` variable. This example creates a String variable named `s` but we don’t initialize it to a value, hence, it is null. Calling the `contains` method on our null variable causes a NullPointerException. The exception is caught in our catch block and this is what is written to the debug log: `The` `following` `exception` `has` `occurred:` `Attempt` `to` `de-reference` `a` `null` `object` .

```apex
try {
```

```apex
String s;
Boolean b = s.contains('abc'); // Causes a NullPointerException
} catch(NullPointerException npe) {
System.debug('The following exception has occurred: ' + npe.getMessage());
}
```

**QueryException** Any problem with SOQL queries, such as assigning a query that returns no records or more than one record to a singleton sObject variable. The second SOQL query in this example causes a QueryException. The example assigns a Merchandise object to what is returned from the query. Note the use of `LIMIT` `1` in the query. This ensures that at most one object is returned from the database so we can assign it to a single object and not a list. However, in this case, we don’t have a Merchandise named XYZ, so nothing is returned, and the attempt to assign the return value to a single object results in a QueryException. The exception is caught in our catch block and this is what you’ll see in the debug log: `The` `following` `exception` `has` `occurred:` `List` `has` `no` `rows` `for` `assignment` `to` `SObject` .

```apex
try {
```

```apex
// This statement doesn't cause an exception, even though
// we don't have a merchandise with name='XYZ'.
// The list will just be empty.
List<Merchandise__c> lm = [SELECT Name FROM Merchandise__c WHERE Name = 'XYZ'];
// lm.size() is 0
System.debug(lm.size());
```

```apex
// However, this statement causes a QueryException because
// we're assiging the return value to a Merchandise__c object
// but no Merchandise is returned.
Merchandise__c m = [SELECT Name FROM Merchandise__c WHERE Name = 'XYZ' LIMIT 1];
} catch(QueryException qe) {
System.debug('The following exception has occurred: ' + qe.getMessage());
}
```

**SObjectException** Any problem with sObject records, such as attempting to change a field in an `update` statement that can only be changed during `insert` . This example results in an SObjectException in the try block, which is caught in the catch block. The example queries an invoice statement and selects only its Name field. It then attempts to get the Description__c field on the queried sObject, which isn’t available because it isn’t in the list of fields queried in the SELECT statement. This results in an SObjectException. This exception is caught in our catch block and this is what you’ll see in the debug log: `The` `following` `exception` `has` `occurred:` `SObject` `row` `was` `retrieved` `via` `SOQL` `without` `querying` `the` `requested` `field:` `Invoice_Statement__c.Description__c` .

```apex
try {
Invoice_Statement__c inv = new Invoice_Statement__c(
Description__c='New Invoice');
insert inv;
```

```apex
// Query the invoice we just inserted
Invoice_Statement__c v = [SELECT Name FROM Invoice_Statement__c WHERE Id = :inv.Id];
```

```apex
// Causes an SObjectException because we didn't retrieve
// the Description__c field.
String s = v.Description__c;
} catch(SObjectException se) {
System.debug('The following exception has occurred: ' + se.getMessage());
}
```

You can use common exception methods to get more information about an exception, such as the exception error message or the stack trace. The previous example calls the `getMessage` method, which returns the error message associated with the exception. There are other exception methods that are also available. Here are descriptions of some useful methods: `getCause` : Returns the cause of the exception as an exception object. `getLineNumber` : Returns the line number from where the exception was thrown. `getMessage` : Returns the error message that displays for the user. `getStackTraceString` : Returns the stack trace of a thrown exception as a string. `getTypeName` : Returns the type of exception, such as DmlException, ListException, MathException, and so on. **Example** To find out what some of the common methods return, try running this example.

```apex
try {
Merchandise__c m = [SELECT Name FROM Merchandise__c LIMIT 1];
// Causes an SObjectException because we didn't retrieve
// the Total_Inventory__c field.
Double inventory = m.Total_Inventory__c;
} catch(Exception e) {
System.debug('Exception type caught: ' + e.getTypeName());
System.debug('Message: ' + e.getMessage());
System.debug('Cause: ' + e.getCause());
// returns null
System.debug('Line number: ' + e.getLineNumber());
System.debug('Stack trace: ' + e.getStackTraceString());
}
```

The output of all `System.debug` statements looks like the following:

```apex
17:38:04:149 USER_DEBUG [7]|DEBUG|Exception type caught: System.SObjectException
```

```apex
17:38:04:149 USER_DEBUG [8]|DEBUG|Message: SObject row was retrieved via SOQL without
querying the requested field: Merchandise__c.Total_Inventory__c
```

```apex
17:38:04:150 USER_DEBUG [9]|DEBUG|Cause: null
```

```apex
17:38:04:150 USER_DEBUG [10]|DEBUG|Line number: 5
```

```apex
17:38:04:150 USER_DEBUG [11]|DEBUG|Stack trace: AnonymousBlock: line 5, column 1
```

The catch statement argument type is the generic Exception type. It caught the more specific SObjectException. You can verify that this is so by inspecting the return value of `e.getTypeName()` in the debug output. The output also contains other properties of the SObjectException, like the error message, the line number where the exception occurred, and the stack trace. You might be wondering why `getCause` returned null. This is because in our sample there was no previous exception (inner exception) that caused this exception. In Create Custom Exceptions , you’ll get to see an example where the return value of `getCause` is an actual exception. Some exception types, such as DmlException, have specific exception methods that apply to only them and aren’t common to other exception types: `getDmlFieldNames(Index` `of` `the` `failed` `record)` : Returns the names of the fields that caused the error for the specified failed record. `getDmlId(Index` `of` `the` `failed` `record)` : Returns the ID of the failed record that caused the error for the specified failed record. `getDmlMessage(Index` `of` `the` `failed` `record)` : Returns the error message for the specified failed record. `getNumDml` : Returns the number of failed records. **Example** This snippet makes use of the DmlException methods to get more information about the exceptions returned when inserting a list of Merchandise objects. The list of items to insert contains three items, the last two of which don’t have required fields and cause exceptions.

```apex
Merchandise__c m1 = new Merchandise__c(
Name='Coffeemaker',
Description__c='Kitchenware',
Price__c=25,
Total_Inventory__c=1000);
// Missing the Price and Total_Inventory fields
Merchandise__c m2 = new Merchandise__c(
Name='Coffeemaker B',
Description__c='Kitchenware');
// Missing all required fields
Merchandise__c m3 = new Merchandise__c();
Merchandise__c[] mList = new List<Merchandise__c>();
mList.add(m1);
mList.add(m2);
mList.add(m3);
```

```apex
try {
```

```apex
insert mList;
} catch (DmlException de) {
```

```apex
Integer numErrors = de.getNumDml();
System.debug('getNumDml=' + numErrors);
for(Integer i=0;i<numErrors;i++) {
System.debug('getDmlFieldNames=' + de.getDmlFieldNames(i));
System.debug('getDmlMessage=' + de.getDmlMessage(i));
}
}
```

Note how the sample above didn’t include all the initial code in the try block. Only the portion of the code that could generate an exception is wrapped inside a `try` block, in this case the `insert` statement could return a DML exception in case the input data is not valid. The exception resulting from the `insert` operation is caught by the `catch` block that follows it. After executing this sample, you’ll see an output of `System.debug` statements similar to the following:

```apex
14:01:24:939 USER_DEBUG [20]|DEBUG|getNumDml=2
```

```apex
14:01:24:941 USER_DEBUG [23]|DEBUG|getDmlFieldNames=(Price, Total Inventory)
```

```apex
14:01:24:941 USER_DEBUG [24]|DEBUG|getDmlMessage=Required fields are missing: [Price,
Total Inventory]
```

```apex
14:01:24:942 USER_DEBUG [23]|DEBUG|getDmlFieldNames=(Description, Price, Total Inventory)
```

```apex
14:01:24:942 USER_DEBUG [24]|DEBUG|getDmlMessage=Required fields are missing:
[Description, Price, Total Inventory]
```

The number of DML failures is correctly reported as two since two items in our list fail insertion. Also, the field names that caused the failure, and the error message for each failed record is written to the output.

#### Catching Different Exception Types

In the previous examples, we used the specific exception type in the catch block. We could have also just caught the generic Exception type in all examples, which catches all exception types. For example, try running this example that throws an SObjectException and has a catch statement with an argument type of Exception. The SObjectException gets caught in the catch block.

```apex
try {
Merchandise__c m = [SELECT Name FROM Merchandise__c LIMIT 1];
// Causes an SObjectException because we didn't retrieve
// the Total_Inventory__c field.
Double inventory = m.Total_Inventory__c;
} catch(Exception e) {
System.debug('The following exception has occurred: ' + e.getMessage());
}
```

Alternatively, you can have several catch blocks—a catch block for each exception type, and a final catch block that catches the generic Exception type. Look at this example. Notice that it has three catch blocks.

```apex
try {
Merchandise__c m = [SELECT Name FROM Merchandise__c LIMIT 1];
// Causes an SObjectException because we didn't retrieve
// the Total_Inventory__c field.
Double inventory = m.Total_Inventory__c;
} catch(DmlException e) {
System.debug('DmlException caught: ' + e.getMessage());
} catch(SObjectException e) {
System.debug('SObjectException caught: ' + e.getMessage());
} catch(Exception e) {
System.debug('Exception caught: ' + e.getMessage());
}
```

Remember that only one catch block gets executed and the remaining ones are bypassed. This example is similar to the previous one, except that it has a few more catch blocks. When you run this snippet, an SObjectException is thrown on this line: `Double` `inventory` `=` `m.Total_Inventory__c;` . Every catch block is examined in the order specified to find a match between the thrown exception and the exception type specified in the catch block argument: **1.** The first catch block argument is of type DmlException, which doesn’t match the thrown exception (SObjectException.) **2.** The second catch block argument is of type SObjectException, which matches our exception, so this block gets executed and the following message is written to the debug log: `SObjectException` `caught:` `SObject` `row` `was` `retrieved` `via` `SOQL` `without` `querying` `the` `requested` `field:` `Merchandise__c.Total_Inventory__c` . **3.** The last catch block is ignored since one catch block has already executed. The last catch block is handy because it catches any exception type, and so catches any exception that was not caught in the previous catch blocks. Suppose we modified the code above to cause a NullPointerException to be thrown, this exception gets caught in the last catch block. Execute this modified example. You’ll see the following debug message: `Exception` `caught:` `Attempt` `to` `de-reference` `a` `null` `object` .

```apex
try {
```

```apex
String s;
Boolean b = s.contains('abc'); // Causes a NullPointerException
} catch(DmlException e) {
System.debug('DmlException caught: ' + e.getMessage());
} catch(SObjectException e) {
System.debug('SObjectException caught: ' + e.getMessage());
} catch(Exception e) {
```

```apex
System.debug('Exception caught: ' + e.getMessage());
}
```

#### Create Custom Exceptions

Custom exceptions enable you to specify detailed error messages and have more custom error handling in your catch blocks. Exceptions can be top-level classes, that is, they can have member variables, methods and constructors, they can implement interfaces, and so on. To create your custom exception class, extend the built-in `Exception` class and make sure your class name ends with the word `Exception` , such as “MyException” or “PurchaseException”. All exception classes extend the system-defined base class `Exception` , and therefore, inherits all common Exception methods. This example defines a custom exception called `MyException` .

```apex
public class MyException extends Exception {}
```

Like Java classes, user-defined exception types can form an inheritance tree, and catch blocks can catch any object in this inheritance tree. For example:

```apex
public class ExceptionExample {
```

```apex
public virtual class BaseException extends Exception {}
public class OtherException extends BaseException {}
```

```apex
public static void testExtendedException() {
```

```apex
try {
```

```apex
Integer i=0;
// Your code here
if (i < 5) throw new OtherException('This is bad');
} catch (BaseException e) {
```

```apex
// This catches the OtherException
System.debug(e.getMessage());
}
}
}
```

Here are some ways you can create your exceptions objects, which you can then throw. You can construct exceptions: With no arguments:

```apex
new MyException();
```

With a single String argument that specifies the error message:

```apex
new MyException('This is bad');
```

With a single Exception argument that specifies the cause and that displays in any stack trace:

```apex
new MyException(e);
```

With both a String error message and a chained exception cause that displays in any stack trace:

```apex
new MyException('This is bad', e);
```

After catching an exception in a catch block, you have the option to rethrow the caught exception variable. This is useful if your method is called by another method and you want to delegate the handling of the exception to the caller method. You can rethrow the caught exception as an inner exception in your custom exception and have the main method catch your custom exception type. The following example shows how to rethrow an exception as an inner exception. The example defines two custom exceptions, `My1Exception` and `My2Exception` , and generates a stack trace with information about both.

```apex
// Define two custom exceptions
public class My1Exception extends Exception {}
public class My2Exception extends Exception {}
```

```apex
try {
```

```apex
// Throw first exception
throw new My1Exception('First exception');
} catch (My1Exception e) {
```

```apex
// Throw second exception with the first
// exception variable as the inner exception
throw new My2Exception('Thrown with inner exception', e);
}
```

This is how the stack trace looks like resulting from running the code above:

```apex
15:52:21:073 EXCEPTION_THROWN [7]|My1Exception: First exception
```

```apex
15:52:21:077 EXCEPTION_THROWN [11]|My2Exception: Throw with inner exception
```

```apex
15:52:21:000 FATAL_ERROR AnonymousBlock: line 11, column 1
```

```apex
15:52:21:000 FATAL_ERROR Caused by
```

```apex
15:52:21:000 FATAL_ERROR AnonymousBlock: line 7, column 1
```

The example in the next section shows how to handle an exception with an inner exception by calling the `getCause` method. Now that you’ve seen how to create a custom exception class and how to construct your exception objects, let’s create and run an example that demonstrates the usefulness of custom exceptions. **1.** In the Developer Console, create a class named `MerchandiseException` and confirm that it has this content.

```apex
public class MerchandiseException extends Exception {
```

```apex
}
```

You’ll use this exception class in the second class that you create. The curly braces at the end enclose the body of your exception class, which we left empty because we get some free code—our class inherits all the constructors and common exception methods, such as `getMessage` , from the built-in `Exception` class. **2.** Next, create a second class named `MerchandiseUtility` .

```apex
public class MerchandiseUtility {
```

```apex
public static void mainProcessing() {
```

```apex
try {
insertMerchandise();
} catch(MerchandiseException me) {
System.debug('Message: ' + me.getMessage());
```

```apex
System.debug('Cause: ' + me.getCause());
System.debug('Line number: ' + me.getLineNumber());
System.debug('Stack trace: ' + me.getStackTraceString());
}
}
```

```apex
public static void insertMerchandise() {
```

```apex
try {
```

```apex
// Insert merchandise without required fields
Merchandise__c m = new Merchandise__c();
insert m;
} catch(DmlException e) {
```

```apex
// Something happened that prevents the insertion
// of Employee custom objects, so throw a more
// specific exception.
throw new MerchandiseException(
```

```apex
'Merchandise item could not be inserted.', e);
}
}
}
```

This class contains the `mainProcessing` method, which calls `insertMerchandise` . The latter causes an exception by inserting a Merchandise without required fields. The catch block catches this exception and throws a new exception, the custom MerchandiseException you created earlier. Notice that we called a constructor for the exception that takes two arguments: the error message, and the original exception object. You might wonder why we are passing the original exception? Because it is useful information—when the MerchandiseException gets caught in the first method, `mainProcessing` , the original exception (referred to as an inner exception) is really the cause of this exception because it occurred before the MerchandiseException. **3.** Now let’s see all this in action to understand better. Execute the following:

```apex
MerchandiseUtility.mainProcessing();
```

**4.** Check the debug log output. You should see something similar to the following:

```apex
18:12:34:928 USER_DEBUG [6]|DEBUG|Message: Merchandise item could not be inserted.
```

```apex
18:12:34:929 USER_DEBUG [7]|DEBUG|Cause: System.DmlException: Insert failed. First
exception on row 0; first error: REQUIRED_FIELD_MISSING, Required fields are missing:
[Description, Price, Total Inventory]: [Description, Price, Total Inventory]
```

```apex
18:12:34:929 USER_DEBUG [8]|DEBUG|Line number: 22
```

```apex
18:12:34:930 USER_DEBUG [9]|DEBUG|Stack trace:
Class.EmployeeUtilityClass.insertMerchandise: line 22, column 1
```

A few items of interest: The cause of MerchandiseException is the DmlException. You can see the DmlException message also that states that required fields were missing. The stack trace is line 22, which is the second time an exception was thrown. It corresponds to the throw statement of MerchandiseException.

```apex
throw new MerchandiseException('Merchandise item could not be inserted.', e);
```

## Testing Apex

Apex provides a testing framework that allows you to write unit tests, run your tests, check test results, and have code coverage results. Let's talk about unit tests, data visibility for tests, and the tools that are available on the Lightning platform for testing Apex. We'll also describe testing best practices and a testing example. To protect the privacy of your data, make sure that test error messages and exception details don’t contain any personal data. The Apex exception handler and testing framework can’t determine if sensitive data is contained in user-defined messages and details. To include personal data in custom Apex exceptions, we recommend that you create an Exception subclass with new properties that hold the personal data. Then, don’t include subclass property information in the exception's message string. Understanding Testing in Apex What to Test in Apex What Are Apex Unit Tests? Understanding Test Data Apex test data is transient and isn’t committed to the database. Run Unit Test Methods To verify the functionality of your Apex code, execute unit tests. You can run Apex test methods in the Developer Console, in Setup, in the Salesforce extensions for Visual Studio Code, or using the API. Testing Best Practices Testing Example Testing and Code Coverage The Apex testing framework generates code coverage numbers for your Apex classes and triggers every time you run one or more tests. Code coverage indicates how many executable lines of code in your classes and triggers have been exercised by test methods. Write test methods to test your triggers and classes, and then run those tests to generate code coverage information. Code Coverage Best Practices Consider the following code coverage tips and best practices. Build a Mocking Framework with the Stub API Apex provides a stub API for implementing a mocking framework. A mocking framework has many benefits. It can streamline and improve testing and help you create faster, more reliable tests. You can use it to test classes in isolation, which is important for unit testing. Building your mocking framework with the stub API can also be beneficial because stub objects are generated at runtime. Because these objects are generated dynamically, you don’t have to package and deploy test classes. You can build your own mocking framework, or you can use one built by someone else. Apex Integration Tests for Agentforce and Data 360 Services (Developer Preview) Use Apex integration tests to write end-to-end tests that exercise real interactions between your Salesforce org and services such as Agentforce and Data 360. Unlike standard Apex unit tests, integration tests relax callout restrictions and transaction rollback semantics, so your tests can make real service calls, commit data mid-transaction, and make assertions on expected outcomes. As a developer preview feature, integration tests are available only in scratch orgs. You can’t run them in production orgs or during metadata deployments.

### Understanding Testing in Apex

Testing is the key to successful long-term development and is a critical component of the development process. We strongly recommend that you use a test-driven development process, that is, test development that occurs at the same time as code development.

#### Why Test Apex?

Testing is key to the success of your application, particularly if your application is to be deployed to customers. If you validate that your application works as expected, that there are no unexpected behaviors, your customers are going to trust you more. There are two ways of testing an application. One is through the Salesforce user interface, important, but merely testing through the user interface will not catch all of the use cases for your application. The other way is to test for bulk functionality: up to 200 records can be passed through your code if it's invoked using SOAP API or by a Visualforce standard set controller. An application is seldom finished. You will have additional releases of it, where you change and extend functionality. If you have written comprehensive tests, you can ensure that a regression is not introduced with any new functionality. Before you can deploy your code or package it for the Salesforce AppExchange, the following must be true. Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully. Note the following. When deploying Apex to a production organization, each unit test in your organization namespace is executed by default. Calls to `System.debug` aren’t counted as part of Apex code coverage. Test methods and test classes aren’t counted as part of Apex code coverage. While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead, make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and single records. This approach ensures that 75% or more of your code is covered by unit tests. Every trigger must have some test coverage. All classes and triggers must compile successfully. Salesforce runs all tests in all organizations that have Apex code to verify that no behavior has been altered as a result of any service upgrades.

### What to Test in Apex

Salesforce recommends that you write tests for the following: **Single action** Test to verify that a single record produces the correct, expected result. **Bulk actions** Any Apex code, whether a trigger, a class or an extension, may be invoked for 1 to 200 records. You must test not only the single record case, but the bulk cases as well. **Positive behavior** Test to verify that the expected behavior occurs through every expected permutation, that is, that the user filled out everything correctly and did not go past the limits. **Negative behavior** There are likely limits to your applications, such as not being able to add a future date, not being able to specify a negative amount, and so on. You must test for the negative case and verify that the error messages are correctly produced as well as for the positive, within the limits cases. **Restricted user** Test whether a user with restricted access to the sObjects used in your code sees the expected behavior. That is, whether they can run the code or receive error messages. Conditional and ternary operators are not considered executed unless both the positive and negative branches are executed. For examples of these types of tests, see Testing Example on page 742.

### What Are Apex Unit Tests?

To facilitate the development of robust, error-free code, Apex supports the creation and execution of unit tests . Unit tests are class methods that verify whether a particular piece of code is working properly. Unit test methods take no arguments, commit no data to the database, and send no emails. Such methods are flagged with the `@IsTest` annotation in the method definition. Unit test methods must be defined in test classes, that is, classes annotated with `@IsTest` . For example:

```apex
@IsTest
private class myClass {
```

```apex
@IsTest
static void myTest() {
```

```apex
// code_block
}
}
```

Use the `@IsTest` annotation to define classes and methods that only contain code used for testing your application. The `@IsTest` annotation can take multiple modifiers within parentheses and separated by blanks. The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a future release. This example of a test class contains two test methods.

```apex
@IsTest
private class MyTestClass {
```

```apex
// Methods for testing
@IsTest
static void test1() {
```

```apex
// Implement test code
}
```

```apex
@IsTest
static void test2() {
```

```apex
// Implement test code
}
```

```apex
}
```

Classes and methods defined as `@IsTest` can be either `private` or `public` . The access level of test classes methods doesn’t matter. You need not add an access modifier when defining a test class or test methods. The default access level in Apex is private. The testing framework can always find the test methods and execute them, regardless of their access level. Classes defined as `@IsTest` must be top-level classes and can't be interfaces or enums. Methods of a test class can only be called from a test method or code invoked by a test method; non-test requests can’t invoke it. This example shows a class to be tested and its corresponding test class. It contains two methods and a constructor.

```apex
public class TVRemoteControl {
```

```apex
// Volume to be modified
Integer volume;
// Constant for maximum volume value
static final Integer MAX_VOLUME = 50;
```

```apex
// Constructor
public TVRemoteControl(Integer v) {
```

```apex
// Set initial value for volume
volume = v;
}
```

```apex
public Integer increaseVolume(Integer amount) {
volume += amount;
if (volume > MAX_VOLUME) {
volume = MAX_VOLUME;
}
return volume;
}
```

```apex
public Integer decreaseVolume(Integer amount) {
volume -= amount;
if (volume < 0) {
volume = 0;
}
return volume;
}
```

```apex
public static String getMenuOptions() {
```

```apex
return 'AUDIO SETTINGS - VIDEO SETTINGS';
}
```

```apex
}
```

This example contains the corresponding test class with four test methods. Each method in the previous class is called. Although there’s sufficient test coverage, the test methods in the test class perform extra testing to verify boundary conditions.

```apex
@IsTest
class TVRemoteControlTest {
```

```apex
@IsTest
static void testVolumeIncrease() {
TVRemoteControl rc = new TVRemoteControl(10);
Integer newVolume = rc.increaseVolume(15);
System.assertEquals(25, newVolume);
}
```

```apex
@IsTest
static void testVolumeDecrease() {
TVRemoteControl rc = new TVRemoteControl(20);
Integer newVolume = rc.decreaseVolume(15);
System.assertEquals(5, newVolume);
}
```

```apex
@IsTest
static void testVolumeIncreaseOverMax() {
TVRemoteControl rc = new TVRemoteControl(10);
Integer newVolume = rc.increaseVolume(100);
System.assertEquals(50, newVolume);
}
```

```apex
@IsTest
```

```apex
static void testVolumeDecreaseUnderMin() {
TVRemoteControl rc = new TVRemoteControl(10);
Integer newVolume = rc.decreaseVolume(100);
System.assertEquals(0, newVolume);
}
```

```apex
@IsTest
static void testGetMenuOptions() {
```

```apex
// Static method call. No need to create a class instance.
String menu = TVRemoteControl.getMenuOptions();
System.assertNotEquals(null, menu);
System.assertNotEquals('', menu);
}
}
```

#### Unit Test Considerations

Here are some things to note about unit tests. Starting with Salesforce API 28.0, test methods can no longer reside in non-test classes and must be part of classes annotated with `IsTest` . See the `TestVisible` annotation to learn how you can access private class members from a test class. Test methods can’t be used to test Web service callouts. Instead, use mock callouts. See Test Web Service Callouts and Testing HTTP Callouts . You can’t send email messages from a test method. Since test methods don’t commit data created in the test, you don’t have to delete test data upon completion. If the value of a static member variable in a test class is changed in a testSetup or test method, the new value isn’t preserved. Other test methods in this class get the original value of the static member variable. This behavior also applies when the static member variable is defined in another class and accessed in test methods. For some sObjects that have fields with unique constraints, inserting duplicate sObject records results in an error. For example, inserting CollaborationGroup sObjects with the same names results in an error because CollaborationGroup records must have unique names. Tracked changes for a record (FeedTrackedChange records) in Chatter feeds aren't available when test methods modify the associated record. FeedTrackedChange records require the change to the parent record they're associated with to be committed to the database before they're created. Since test methods don't commit data, they don't result in the creation of FeedTrackedChange records. Similarly, field history tracking records can't be created in test methods because they require other sObject records to be committed first. For example, AccountHistory records can’t be created in test methods because Account records must be committed first. If your tests include DML, make sure that you don’t exceed the MAX_DML_ROWS limit. See “Miscellaneous Apex Limits” in Execution Governors and Limits 1. Accessing Private Test Class Members IsTest Annotation

#### Accessing Private Test Class Members

Test methods are defined in a test class, separate from the class they test. This can present a problem when having to access a private class member variable from the test method, or when calling a private method. Because these are private, they aren’t visible to the test class. You can either modify the code in your class to expose public methods that will make use of these private class members, or you can simply annotate these private class members with `TestVisible` . When you annotate private or protected members with this annotation, they can be accessed by test methods and only code running in test context. This example shows how `TestVisible` is used with private member variables, a private inner class with a constructor, a private method, and a private custom exception. All these can be accessed in the test class because they’re annotated with `TestVisible` . The class is listed first and is followed by a test class containing the test methods.

```apex
public class VisibleSampleClass {
```

```apex
// Private member variables
@TestVisible private Integer recordNumber = 0;
@TestVisible private String areaCode = '(415)';
// Public member variable
public Integer maxRecords = 1000;
```

```apex
// Private inner class
@TestVisible class Employee {
```

```apex
String fullName;
String phone;
```

```apex
// Constructor
@TestVisible Employee(String s, String ph) {
fullName = s;
phone = ph;
}
}
```

```apex
// Private method
@TestVisible private String privateMethod(Employee e) {
System.debug('I am private.');
recordNumber++;
String phone = areaCode + ' ' + e.phone;
String s = e.fullName + '\'s phone number is ' + phone;
System.debug(s);
return s;
}
```

```apex
// Public method
public void publicMethod() {
maxRecords++;
System.debug('I am public.');
}
```

```apex
// Private custom exception class
@TestVisible private class MyException extends Exception {}
}
```

```apex
// Test class for VisibleSampleClass
@isTest
private class VisibleSampleClassTest {
```

```apex
// This test method can access private members of another class
// that are annotated with @TestVisible.
static testmethod void test1() {
VisibleSampleClass sample = new VisibleSampleClass ();
```

```apex
// Access private data members and update their values
sample.recordNumber = 100;
sample.areaCode = '(510)';
```

```apex
// Access private inner class
VisibleSampleClass.Employee emp =
```

```apex
new VisibleSampleClass.Employee('Joe Smith', '555-1212');
```

```apex
// Call private method
String s = sample.privateMethod(emp);
```

```apex
// Verify result
System.assert(
s.contains('(510)') &&
s.contains('Joe Smith') &&
s.contains('555-1212'));
}
```

```apex
// This test method can throw private exception defined in another class
static testmethod void test2() {
```

```apex
// Throw private exception.
try {
```

```apex
throw new VisibleSampleClass.MyException('Thrown from a test.');
} catch(VisibleSampleClass.MyException e) {
```

```apex
// Handle exception
}
}
```

```apex
static testmethod void test3() {
```

```apex
// Access public method.
// No @TestVisible is used.
VisibleSampleClass sample = new VisibleSampleClass ();
sample.publicMethod();
}
```

```apex
}
```

The `TestVisible` annotation can be handy when you upgrade the Salesforce API version of existing classes containing mixed test and non-test code. Because test methods aren’t allowed in non-test classes starting in API version 28.0, you must move the test methods from the old class into a new test class (a class annotated with `isTest` ) when you upgrade the API version of your class. You might run into visibility issues when accessing private methods or member variables of the original class. In this case, just annotate these private members with `TestVisible` .

### Understanding Test Data

Apex test data is transient and isn’t committed to the database. This means that after a test method finishes execution, the data inserted by the test doesn’t persist in the database. As a result, there is no need to delete any test data at the conclusion of a test. Likewise, all the changes to existing records, such as updates or deletions, don’t persist. This transient behavior of test data makes the management of data easier as you don’t have to perform any test data cleanup. At the same time, if your tests access organization data, this prevents accidental deletions or modifications to existing records. By default, existing organization data isn’t visible to test methods, with the exception of certain setup objects. You should create test data for your test methods whenever possible. However, test code saved against Salesforce API version 23.0 or earlier has access to all data in the organization. Data visibility for tests is covered in more detail in the next section. Isolation of Test Data from Organization Data in Unit Tests Using the isTest(SeeAllData=True) Annotation Annotate your test class or test method with `IsTest(SeeAllData=` `true` `)` to open up data access to records in your organization. The IsTest(SeeAllData=true) annotation applies to data queries but doesn't apply to record creation or changes, including deletions. New and changed records are still rolled back in Apex tests even when using the annotation. Loading Test Data Using the `Test.loadData` method, you can populate data in your test methods without having to write many lines of code. Common Test Utility Classes for Test Data Creation Common test utility classes are public test classes that contain reusable code for test data creation. Using Test Setup Methods Use test setup methods (methods that are annotated with `@testSetup` ) to create test records once and then access them in every test method in the test class. Test setup methods can be time-saving when you need to create reference or prerequisite data for all test methods, or a common set of records that all test methods operate on.

#### Isolation of Test Data from Organization Data in Unit Tests

By default, Apex test methods (API version 24.0 and later) can’t access pre-existing org data such as standard objects, custom objects, and custom settings data. They can only access data that they create. However, objects that are used to manage your organization or metadata objects can still be accessed in your tests. These are some examples of such objects. User Profile Organization CronTrigger RecordType ApexClass ApexTrigger ApexComponent ApexPage Whenever possible, create test data for each test. You can disable this restriction by annotating your test class or test method with the `IsTest(SeeAllData=` `true` `)` annotation. Test code saved using Salesforce API version 23.0 or earlier continues to have access to all data in the organization and its data access is unchanged. **Data Access Considerations** When working with data silo Apex tests, cross-object field references using the `Owner` relationship aren’t supported. Due to this limitation, `SELECT` `Owner.IsActive` `FROM` `Account` returns null when run within a data silo Apex test. If a new test method saved using Salesforce API version 24.0 or later calls a method in another class saved using version 23.0 or earlier, the data access restrictions of the caller are enforced in the called method. The called method can’t access organization data because the caller can’t access it, even though it was saved in an earlier version. The `IsTest(SeeAllData=` `true` `)` annotation has no effect when added to Apex code saved using Salesforce API version 23.0 and earlier. This access restriction to test data applies to all code running in test context. For example, if a test method causes a trigger to execute and the test can’t access organization data, the trigger won’t be able to either. If a test makes a Visualforce request, the executing test stays in test context but runs in a different thread. Therefore, test data isolation is no longer enforced. In this case, the test will be able to access all data in the organization after initiating the Visualforce request. However, if the Visualforce request performs a callback, such as a JavaScript remoting call, any data inserted by the callback isn’t visible to the test. The VLOOKUP validation rule function, in API version 27.0 and earlier, always looks up org data in addition to test data when fired by a running Apex test. Starting with version 28.0, the VLOOKUP validation rule function no longer accesses organization data from a running Apex test. The function looks up only data created by the test, unless the test class or method is annotated with `IsTest(SeeAllData=` `true` `)` . There can be some cases where you can’t create certain types of data from your test method because of specific limitations. Here are some examples of such limitations. Some standard objects aren’t creatable. For more information on these objects, see the Object Reference for Salesforce . For some sObjects that have fields with unique constraints, inserting duplicate sObject records results in an error. For example, inserting CollaborationGroup sObjects with the same names results in an error because CollaborationGroup records must have unique names. This error occurs whether your test is annotated with `IsTest(SeeAllData=` `true` `)` , or not. Records that are created only after related records are committed to the database, like tracked changes in Chatter. Tracked changes for a record (FeedTrackedChange records) in Chatter feeds aren't available when test methods modify the associated record. FeedTrackedChange records require the change to the parent record they're associated with to be committed to the database before they're created. Since test methods don't commit data, they don't result in the creation of FeedTrackedChange records. Similarly, field history tracking records can't be created in test methods because they require other sObject records to be committed first. For example, AccountHistory records can’t be created in test methods because Account records must be committed first. When working with data silo Apex tests, Salesforce recommends that you don’t share record IDs between test data and org data, thereby preventing test data from accessing pre-existing org data.

#### Using the isTest(SeeAllData=True) Annotation

Annotate your test class or test method with `IsTest(SeeAllData=` `true` `)` to open up data access to records in your organization. The IsTest(SeeAllData=true) annotation applies to data queries but doesn't apply to record creation or changes, including deletions. New and changed records are still rolled back in Apex tests even when using the annotation. By annotating your class with `@isTest(SeeAllData=true)` , you allow test methods to access all org records. The best practice, however, is to run Apex tests with data silo using `@isTest(SeeAllData=false)` . For data access considerations in Salesforce API version 23.0 and earlier, see Isolation of Test Data from Organization Data in Unit Tests on page 726. This example shows how to define a test class with the `@IsTest(SeeAllData=true)` annotation. All the test methods in this class have access to all data in the organization.

```apex
// All test methods in this class can access all data.
@IsTest(SeeAllData=true)
public class TestDataAccessClass {
```

```apex
// This test accesses an existing account.
// It also creates and accesses a new test account.
@IsTest
```

```apex
static void myTestMethod1() {
```

```apex
// Query an existing account in the organization.
Account a = [SELECT Id, Name FROM Account WHERE Name='Acme' LIMIT 1];
System.assert(a != null);
```

```apex
// Create a test account based on the queried account.
Account testAccount = a.clone();
testAccount.Name = 'Acme Test';
insert testAccount;
```

```apex
// Query the test account that was inserted.
Account testAccount2 = [SELECT Id, Name FROM Account
WHERE Name='Acme Test' LIMIT 1];
System.assert(testAccount2 != null);
}
```

```apex
// Like the previous method, this test method can also access all data
// because the containing class is annotated with @IsTest(SeeAllData=true).
@IsTest
static void myTestMethod2() {
```

```apex
// Can access all data in the organization.
}
```

```apex
}
```

This second example shows how to apply the `@IsTest(SeeAllData=true)` annotation on a test method. Because the test method’s class isn’t annotated, you have to annotate the method to enable access to all data for the method. The second test method doesn’t have this annotation, so it can access only the data it creates. In addition, it can access objects that are used to manage your organization, such as users.

```apex
// This class contains test methods with different data access levels.
@IsTest
private class ClassWithDifferentDataAccess {
```

```apex
// Test method that has access to all data.
@IsTest(SeeAllData=true)
static void testWithAllDataAccess() {
```

```apex
// Can query all data in the organization.
}
```

```apex
// Test method that has access to only the data it creates
// and organization setup and metadata objects.
@IsTest
static void testWithOwnDataAccess() {
```

```apex
// This method can still access the User object.
// This query returns the first user object.
User u = [SELECT UserName,Email FROM User LIMIT 1];
System.debug('UserName: ' + u.UserName);
System.debug('Email: ' + u.Email);
```

```apex
// Can access the test account that is created here.
Account a = new Account(Name='Test Account');
insert a;
```

```apex
// Access the account that was just created.
Account insertedAcct = [SELECT Id,Name FROM Account
WHERE Name='Test Account'];
System.assert(insertedAcct != null);
}
}
```

**Considerations for the** `@IsTest(SeeAllData=true)` **Annotation** If a test class is defined with the `@IsTest(SeeAllData=true)` annotation, the `SeeAllData=` `true` applies to all test methods that don’t explicitly set the `SeeAllData` keyword. The `@IsTest(SeeAllData=true)` annotation is used to open up data access when applied at the class or method level. However, if the containing class has been annotated with `@IsTest(SeeAllData=true)` , annotating a method with `@IsTest(SeeAllData=false)` is ignored for that method. In this case, that method still has access to all the data in the organization. Annotating a method with `@IsTest(SeeAllData=true)` overrides, for that method, an `@IsTest(SeeAllData=false)` annotation on the class. `@IsTest(SeeAllData=true)` and `@IsTest(IsParallel=true)` annotations can’t be used together on the same Apex method.

#### Loading Test Data

Using the `Test.loadData` method, you can populate data in your test methods without having to write many lines of code. Follow these steps: **1.** Add the data in a .csv file. **2.** Create a static resource for this file. **3.** Call `Test.loadData` within your test method and passing it the sObject type token and the static resource name. For example, for Account records and a static resource name of `myResource` , make the following call:

```apex
List<sObject> ls = Test.loadData(Account.sObjectType, 'myResource');
```

The `Test.loadData` method returns a list of sObjects that correspond to each record inserted. You must create the static resource prior to calling this method. The static resource is a comma-delimited file ending with a .csv extension. The file contains field names and values for the test records. The first line of the file must contain the field names and subsequent lines are the field values. To learn more about static resources, see “Defining Static Resources” in the Salesforce online help. Once you create a static resource for your .csv file, the static resource will be assigned a MIME type. Supported MIME types are: text/csv application/vnd.ms-excel application/octet-stream text/plain `Test.loadData` The following are steps for creating a sample .csv file and a static resource, and calling `Test.loadData` to insert the test records. **1.** Create a .csv file that has the data for the test records. This sample .csv file has three account records. You can use this sample content to create your .csv file.

```apex
Name,Website,Phone,BillingStreet,BillingCity,BillingState,BillingPostalCode,BillingCountry
sForceTest1,http://www.sforcetest1.com,(415) 901-7000,The Landmark @ One Market,San
```

```apex
Francisco,CA,94105,US
sForceTest2,http://www.sforcetest2.com,(415) 901-7000,The Landmark @ One Market Suite
300,San Francisco,CA,94105,US
sForceTest3,http://www.sforcetest3.com,(415) 901-7000,1 Market St,San
Francisco,CA,94105,US
```

**2.** Create a static resource for the .csv file: **a.** From Setup, enter `Static` `Resources` in the `Quick` `Find` box, then select **Static Resources** . **b.** Click **New** . **c.** Name your static resource `testAccounts` . **d.** Choose the file you created. **e.** Click **Save** . **3.** Call `Test.loadData` in a test method to populate the test accounts.

```apex
@isTest
private class DataUtil {
```

```apex
static testmethod void testLoadData() {
```

```apex
// Load the test accounts from the static resource
List<sObject> ls = Test.loadData(Account.sObjectType, 'testAccounts');
// Verify that all 3 test accounts were created
System.assert(ls.size() == 3);
```

```apex
// Get first test account
Account a1 = (Account)ls[0];
String acctName = a1.Name;
System.debug(acctName);
```

```apex
// Perform some testing using the test records
}
}
```

#### Common Test Utility Classes for Test Data Creation

Common test utility classes are public test classes that contain reusable code for test data creation. Public test utility classes are defined with the `IsTest` annotation, and as such, are excluded from the organization code size limit and execute in test context. They can be called by test methods but not by non-test code. The methods in the public test utility class are defined the same way methods are in non-test classes. They can take parameters and can return a value. The methods must be declared as public or global to be visible to other test classes. These common methods can be called by any test method in your Apex classes to set up test data before running the test. While you can create public methods for test data creation in a regular Apex class, without the `IsTest` annotation, you don’t get the benefit of excluding this code from the organization code size limit. This is an example of a test utility class. It contains one method, `createTestRecords` , which accepts the number of accounts to create and the number of contacts per account. The next example shows a test method that calls this method to create some data.

```apex
@IsTest
public class TestDataFactory {
```

```apex
public static void createTestRecords(Integer numAccts, Integer numContactsPerAcct) {
List<Account> accts = new List<Account>();
```

```apex
for(Integer i=0;i<numAccts;i++) {
Account a = new Account(Name='TestAccount' + i);
accts.add(a);
}
insert accts;
```

```apex
List<Contact> cons = new List<Contact>();
for (Integer j=0;j<numAccts;j++) {
Account acct = accts[j];
// For each account just inserted, add contacts
for (Integer k=numContactsPerAcct*j;k<numContactsPerAcct*(j+1);k++) {
cons.add(new Contact(firstname='Test'+k,
lastname='Test'+k,
AccountId=acct.Id));
}
}
// Insert all contacts for all accounts
insert cons;
}
}
```

The test method in this class calls the test utility method, `createTestRecords` , to create five test accounts with three contacts each.

```apex
@IsTest
private class MyTestClass {
```

```apex
static testmethod void test1() {
TestDataFactory.createTestRecords(5,3);
// Run some tests
}
}
```

#### Using Test Setup Methods

Use test setup methods (methods that are annotated with `@testSetup` ) to create test records once and then access them in every test method in the test class. Test setup methods can be time-saving when you need to create reference or prerequisite data for all test methods, or a common set of records that all test methods operate on. Test setup methods can reduce test execution times especially when you’re working with many records. Test setup methods enable you to create common test data easily and efficiently. By setting up records once for the class, you don’t need to re-create records for each test method. Also, because the rollback of records that are created during test setup happens at the end of the execution of the entire class, the number of records that are rolled back is reduced. As a result, system resources are used more efficiently compared to creating those records and having them rolled back for each test method. If a test class contains a test setup method, the testing framework executes the test setup method first, before any test method in the class. Records that are created in a test setup method are available to all test methods in the test class and are rolled back at the end of test class execution. If a test method changes those records, such as record field updates or record deletions, those changes are rolled back after each test method finishes execution. The next executing test method gets access to the original unmodified state of those records. Similarly, if you create a static variable in a test setup method, and then modify that variable in a test method, the change doesn’t persist to other test methods. Every test method, including the test setup method, runs as a separate transaction. The static context of the test class is reinitialized before each transaction begins. Therefore, static variable initializers and static blocks are executed fresh at the start of every test method. Any change to a static variable within a test setup method is confined to that specific transaction. After the transaction completes, those in-memory changes are discarded. Test setup methods are defined in a test class, take no arguments, and return no value. The following is the syntax of a test setup method.

```apex
@testSetup static void methodName() {
```

```apex
}
```

This example shows how to create test records once and then access them in multiple test methods. Also, the example shows how changes that are made in the first test method are rolled back and are not available to the second test method.

```apex
@isTest
private class CommonTestSetup {
```

```apex
@testSetup static void setup() {
```

```apex
// Create common test accounts
List<Account> testAccts = new List<Account>();
for(Integer i=0;i<2;i++) {
testAccts.add(new Account(Name = 'TestAcct'+i));
}
insert testAccts;
}
```

```apex
@isTest static void testMethod1() {
```

```apex
// Get the first test account by using a SOQL query
Account acct = [SELECT Id FROM Account WHERE Name='TestAcct0' LIMIT 1];
// Modify first account
acct.Phone = '555-1212';
// This update is local to this test method only.
update acct;
```

```apex
// Delete second account
Account acct2 = [SELECT Id FROM Account WHERE Name='TestAcct1' LIMIT 1];
// This deletion is local to this test method only.
delete acct2;
```

```apex
// Perform some testing
}
```

```apex
@isTest static void testMethod2() {
```

```apex
// The changes made by testMethod1() are rolled back and
// are not visible to this test method.
// Get the first account by using a SOQL query
Account acct = [SELECT Phone FROM Account WHERE Name='TestAcct0' LIMIT 1];
// Verify that test account created by test setup method is unaltered.
System.assertEquals(null, acct.Phone);
```

```apex
// Get the second account by using a SOQL query
Account acct2 = [SELECT Id FROM Account WHERE Name='TestAcct1' LIMIT 1];
```

```apex
// Verify test account created by test setup method is unaltered.
System.assertNotEquals(null, acct2);
```

```apex
// Perform some testing
}
```

```apex
}
```

Test setup methods are supported only with the default data isolation mode for a test class. If the test class or a test method has access to organization data by using the `@isTest(SeeAllData=true)` annotation, test setup methods aren’t supported in this class. Because data isolation for tests is available for API versions 24.0 and later, test setup methods are also available for those versions only. You can have only one test setup method per test class. If a fatal error occurs during the execution of a test setup method, such as an exception that’s caused by a DML operation or an assertion failure, the entire test class fails, and no further tests in the class are executed. If a test setup method calls a non-test method of another class, no code coverage is calculated for the non-test method.

### Run Unit Test Methods

To verify the functionality of your Apex code, execute unit tests. You can run Apex test methods in the Developer Console, in Setup, in the Salesforce extensions for Visual Studio Code, or using the API. You can run these groupings of unit tests. Some or all methods in a specific class Some or all methods in a set of classes A predefined suite of classes, known as a test suite All unit tests in your org To run a test, use any of the following: Salesforce user interface Salesforce extensions for Visual Studio Code and Code Builder Developer Console The API All Apex tests that are started from the Salesforce user interface (including the Developer Console) run asynchronously and in parallel. Apex test classes are placed in the Apex job queue for execution. The maximum number of test classes that you can run per 24-hour period is the greater of 500 or 10 multiplied by the number of test classes in the org. For sandbox and Developer Edition organizations, this limit is higher and is the greater of 500 or 20 multiplied by the number of test classes in the org. Apex tests that run as part of a deployment always run synchronously and serially.

#### Running Tests Through the Salesforce User Interface

You can run unit tests on the Application Test Execution page. Tests started on this page run asynchronously, that is, you don't have to wait for a test class execution to finish. The Application Test Execution page refreshes the status of a test and displays the results after the test completes. **1.** From Setup, enter `Application` `Test` `Execution` in the `Quick` `Find` box, then select **Application Test Execution** . **2.** Click **Select Tests...** . If you have Apex classes that are installed from a managed package, you must compile these classes first by clicking **Compile all classes** on the Apex Classes page so that they appear in the list. **3.** Select the tests to run. The list of tests includes only classes that contain test methods. To select tests from an installed managed package, select the managed package’s corresponding namespace from the dropdown list. Only the classes of the managed package with the selected namespace appear in the list. To select tests that exist locally in your organization, select **[My Namespace]** from the dropdown list. Only local classes that aren't from managed packages appear in the list. To select any test, select **[All Namespaces]** from the dropdown list. All the classes in the organization appear, even those in a managed package. Classes with tests currently running don't appear in the list. **4.** To opt out of collecting code coverage information during test runs, select **Skip Code Coverage** . **5.** Click **Run** . After you run tests using the Application Test Execution page, you can view code coverage details in the Developer Console. From Setup, enter `Application` in the `Quick` `Find` box, select **Application Test Execution** , then click **View Test History** to view all test results for your organization, not just tests that you have run. Test results are retained for 30 days after they finish running, unless cleared.

#### Running Tests Using the Salesforce Extensions for Visual Studio Code

You can execute tests with Visual Studio Code. See Salesforce Extensions for Visual Studio Code and Code Builder .

#### Running Tests Using the Developer Console

In the Developer Console, you can execute some or all tests in specific test classes, set up and run test suites, or run all tests. The Developer Console runs tests asynchronously in the background, unless your test run includes only one class and you’ve not chosen **Always Run** **Asynchronously** in the Test menu. Running tests asynchronously lets you work in other areas of the Developer Console while tests are running. After the tests execute, you can inspect the test results in the Developer Console. Also, you can inspect the overall code coverage for classes covered by the tests. For more information, see the Developer Console documentation in Salesforce Help.

#### Running Tests Using the API

You can use the `runTests()` call from SOAP API to run tests synchronously.

```apex
RunTestsResult[] runTests(RunTestsRequest ri)
```

This call allows you to run the following, as specified in the RunTestsRequest object: All tests in all classes All tests in a specific namespace All tests in a subset of classes in a specific namespace It returns the following: Total number of tests that ran Code coverage statistics Error information for each failed test Information for each test that succeeds Time it took to run the test For more information on `runTests()` , see `runTests()` in the SOAP API Developer Guide . You can also run tests using the Tooling REST API. Use the `/runTestsAsynchronous/` and `/runTestsSynchronous/` endpoints to run tests asynchronously or synchronously. For usage details, see Tooling API : REST Resources .

#### Running Tests Using ApexTestQueueItem

You can run tests asynchronously using `ApexTestQueueItem` and `ApexTestResult` . These objects let you add tests to the Apex job queue and check the results of the completed test runs. This process enables you to not only start tests asynchronously but also schedule your tests to execute at specific times by using the Apex scheduler. See Apex Scheduler for more information. Insert an `ApexTestQueueItem` object to place its corresponding Apex class in the Apex job queue for execution. The Apex job executes the test methods in the class. After the job executes, `ApexTestResult` contains the result for each single test method executed as part of the test. `ApexTestResult` rows are also generated for Apex tests run with the `@testSetup` annotation. The `IsTestSetup` field is set to `true` for these annotated tests to distinguish them from other test methods. The `TestSetupTime` field on `ApexTestRunResult` tracks the cumulative time of all setup methods for the given `ApexTestRunResult` . To abort a class that is in the Apex job queue, perform an update operation on the ApexTestQueueItem object and set its `Status` field to `Aborted` . If you insert multiple Apex test queue items in a single bulk operation, the queue items share a parent job and a test run can execute tests for several classes. The maximum number of test queue items, and hence classes, that you can insert in the Apex job queue is the greater of 500 or 10 multiplied by the number of test classes in the org. For sandbox and Developer Edition organizations, this limit is higher and is the greater of 500 or 20 multiplied by the number of test classes in the org. You may observe slower async test execution time when compilation is required, for example when tests are run after altering an Apex class. This is because parallel test execution is restricted to one job until compilation is completed. If you have Apex code in your org that is referenced by queued tests and fails to compile, you will be limited to the one concurrent job. You must ensure that Apex code in your org compiles successfully. This example uses DML operations to insert and query the `ApexTestQueueItem` and `ApexTestResult` objects. The `enqueueTests` method inserts queue items for all classes that end with Test. It then returns the parent job ID of one queue item, which is the same for all queue items because they were inserted in bulk. The `checkClassStatus` method retrieves all queue items that correspond to the specified job ID. It then queries and outputs the name, job status, and pass rate for each class. The `checkMethodStatus` method gets information of each test method that was executed as part of the job.

```apex
public class TestUtil {
```

```apex
// Enqueue all classes ending in "Test".
public static ID enqueueTests() {
ApexClass[] testClasses =
[SELECT Id FROM ApexClass
WHERE Name LIKE '%Test'];
if (testClasses.size() > 0) {
ApexTestQueueItem[] queueItems = new List<ApexTestQueueItem>();
for (ApexClass cls : testClasses) {
queueItems.add(new ApexTestQueueItem(ApexClassId=cls.Id));
}
```

```apex
insert queueItems;
```

```apex
// Get the job ID of the first queue item returned.
ApexTestQueueItem item =
[SELECT ParentJobId FROM ApexTestQueueItem
WHERE Id=:queueItems[0].Id LIMIT 1];
return item.parentjobid;
}
return null;
}
```

```apex
// Get the status and pass rate for each class
// whose tests were run by the job.
// that correspond to the specified job ID.
public static void checkClassStatus(ID jobId) {
ApexTestQueueItem[] items =
[SELECT ApexClass.Name, Status, ExtendedStatus
FROM ApexTestQueueItem
WHERE ParentJobId=:jobId];
for (ApexTestQueueItem item : items) {
```

```apex
String extStatus = item.extendedstatus == null ? '' : item.extendedStatus;
System.debug(item.ApexClass.Name + ': ' + item.Status + extStatus);
}
}
```

```apex
// Get the result for each test method that was executed.
public static void checkMethodStatus(ID jobId) {
ApexTestResult[] results =
[SELECT Outcome, ApexClass.Name, MethodName, Message, StackTrace
FROM ApexTestResult
WHERE AsyncApexJobId=:jobId];
for (ApexTestResult atr : results) {
System.debug(atr.ApexClass.Name + '.' + atr.MethodName + ': ' + atr.Outcome);
```

```apex
if (atr.message != null) {
System.debug(atr.Message + '\n at ' + atr.StackTrace);
}
}
}
}
```

1. Using the runAs Method Generally, all Apex code runs in user mode, where the object-level and field-level permissions of the current user are enforced. With the System method `runAs` , you can write test methods that change the user context to an existing user or a new user. Then that user’s sharing rules and object-level and field-level permissions are enforced. 2. Using Limits, startTest , and stopTest 3. Adding SOSL Queries to Unit Tests Testing and Code Coverage Salesforce Help : Open the Developer Console

#### Using the runAs Method

Generally, all Apex code runs in user mode, where the object-level and field-level permissions of the current user are enforced. With the System method `runAs` , you can write test methods that change the user context to an existing user or a new user. Then that user’s sharing rules and object-level and field-level permissions are enforced. The user’s sharing rules and object-level and field-level permissions are enforced within a `runAs` block, regardless of the sharing mode ( `with` `sharing` or `without` `sharing` ) of the test class. If a user-defined method is called in the `runAs` block, the sharing mode enforced is that of the class where the method is defined, not the test class. You can use `runAs` only in test methods. The original current user context is started again after all `runAs` test methods complete. The `runAs` method ignores user license limits. You can create users with `runAs` even if your organization has no additional user licenses. Every call to `runAs` counts against the total number of DML statements issued in the process. In the following example, a new test user is created, then code is run as that user, with that user's record sharing access:

```apex
@isTest
private class TestRunAs {
```

```apex
public static testMethod void testRunAs() {
```

```apex
// Setup test data
// Create a unique UserName
String uniqueUserName = 'standarduser' + DateTime.now().getTime() + '@testorg.com';
```

```apex
// This code runs as the system user
Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];
User u = new User(Alias = 'standt', Email='standarduser@testorg.com',
EmailEncodingKey='UTF-8', LastName='Testing', LanguageLocaleKey='en_US',
```

```apex
LocaleSidKey='en_US', ProfileId = p.Id,
TimeZoneSidKey='America/Los_Angeles',
UserName=uniqueUserName);
```

```apex
System.runAs(u) {
```

```apex
// The following code runs as user 'u'
System.debug('Current User: ' + UserInfo.getUserName());
System.debug('Current Profile: ' + UserInfo.getProfileId());
}
}
}
```

You can nest more than one `runAs` method. For example:

```apex
@isTest
private class TestRunAs2 {
```

```apex
public static testMethod void test2() {
```

```apex
Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];
User u2 = new User(Alias = 'newUser', Email='newuser@testorg.com',
EmailEncodingKey='UTF-8', LastName='Testing', LanguageLocaleKey='en_US',
LocaleSidKey='en_US', ProfileId = p.Id,
TimeZoneSidKey='America/Los_Angeles', UserName='newuser@testorg.com');
```

```apex
System.runAs(u2) {
```

```apex
// The following code runs as user u2.
System.debug('Current User: ' + UserInfo.getUserName());
System.debug('Current Profile: ' + UserInfo.getProfileId());
```

```apex
// The following code runs as user u3.
User u3 = [SELECT Id FROM User WHERE UserName='newuser@testorg.com'];
System.runAs(u3) {
System.debug('Current User: ' + UserInfo.getUserName());
System.debug('Current Profile: ' + UserInfo.getProfileId());
}
```

```apex
// Any additional code here would run as user u2.
}
}
}
```

`runAs` You can also use the `runAs` method to perform mixed DML operations in your test by enclosing the DML operations within the `runAs` block. In this way, you bypass the mixed DML error that is otherwise returned when inserting or updating setup objects together with other sObjects. See sObjects That Cannot Be Used Together in DML Operations . There’s another overload of the `runAs` method ( `runAs(System.Version)` ) that takes a package version as an argument. This method causes the code of a specific version of a managed package to be used. For information on using the `runAs` method and specifying a package version context, see Testing Behavior in Package Versions on page 770. Enforce Sharing Rules Enforce Object and Field Permissions Apex Reference Guide : System.runAs(userSObject)

#### Using Limits, startTest , and stopTest

The Limits methods return the specific limit for the particular governor, such as the number of calls of a method or the amount of heap size remaining. Each method has two versions. The first version returns the amount of the resource that has been used in the current context. The second version contains the word “limit” and returns the total amount of the resource that is available for that context. For example, `getCallouts` returns the number of callouts to an external service that have already been processed in the current context, while `getLimitCallouts` returns the total number of callouts available in the given context. In addition to the Limits methods, use the `startTest` and `stopTest` methods to validate how close the code is to reaching governor limits. The `startTest` method marks the point in your test code when your test actually begins. Each test method is allowed to call this method only once. All of the code before this method should be used to initialize variables, populate data structures, and so on, allowing you to set up everything you need to run your test. Any code that executes after the call to `startTest` and before `stopTest` is assigned a new set of governor limits. The `startTest` method does not refresh the context of the test: it adds a context to your test. For example, if your class makes 98 SOQL queries before it calls `startTest` , and the first significant statement after `startTest` is a DML statement, the program can now make an additional 100 queries. Once `stopTest` is called, however, the program goes back into the original context, and can only make 2 additional SOQL queries before reaching the limit of 100. The `stopTest` method marks the point in your test code when your test ends. Use this method in conjunction with the `startTest` method. Each test method is allowed to call this method only once. Any code that executes after the `stopTest` method is assigned the original limits that were in effect before `startTest` was called. All asynchronous calls made after the `startTest` method are collected by the system. When `stopTest` is executed, all asynchronous processes are run synchronously. An exception encountered during `stopTest` halts the synchronous processing. For example, an unhandled exception in a batch job’s `execute` method will prevent the `finish` method from running in a test context. Test Apex Triggers

#### Adding SOSL Queries to Unit Tests

To ensure that test methods always behave in a predictable way, any Salesforce Object Search Language (SOSL) query that is added to an Apex test method returns an empty set of search results when the test method executes. If you do not want the query to return an empty list of results, you can use the `Test.setFixedSearchResults` system method to define a list of record IDs that are returned by the search. All SOSL queries that take place later in the test method return the list of record IDs that were specified by the `Test.setFixedSearchResults` method. Additionally, the test method can call `Test.setFixedSearchResults` multiple times to define different result sets for different SOSL queries. If you do not call the `Test.setFixedSearchResults` method in a test method, or if you call this method without specifying a list of record IDs, any SOSL queries that take place later in the test method return an empty list of results. The list of record IDs specified by the `Test.setFixedSearchResults` method replaces the results that would normally be returned by the SOSL query if it were not subject to any `WHERE` or `LIMIT` clauses. If these clauses exist in the SOSL query, they are applied to the list of fixed search results. For example:

```apex
@isTest
private class SoslFixedResultsTest1 {
```

```apex
public static testMethod void testSoslFixedResults() {
Id [] fixedSearchResults= new Id[1];
fixedSearchResults[0] = '001x0000003G89h';
Test.setFixedSearchResults(fixedSearchResults);
List<List<SObject>> searchList = [FIND 'test'
```

```apex
IN ALL FIELDS RETURNING
Account(id, name WHERE name = 'test' LIMIT
1)];
}
}
```

SOSL queries for `ContentDocument` (File) or `ContentNote` (Note) entities require using `setFixedSearchResults` with `ContentVersion` IDs to remain consistent with how Salesforce indexes and searches for files and notes. Although the account record with an ID of `001x0000003G89h` may not match the query string in the FIND clause ( `'test'` ), the record is passed into the `RETURNING` clause of the SOSL statement. If the record with ID `001x0000003G89h` matches the `WHERE` clause filter, the record is returned. If it does not match the `WHERE` clause, no record is returned.

### Testing Best Practices

Good tests do the following: Cover as many lines of code as possible. Before you can deploy Apex or package it for AppExchange, the following must be true. Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully. Note the following. When deploying Apex to a production organization, each unit test in your organization namespace is executed by default. Calls to `System.debug` aren’t counted as part of Apex code coverage. Test methods and test classes aren’t counted as part of Apex code coverage. While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead, make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and single records. This approach ensures that 75% or more of your code is covered by unit tests. Tests don’t run in parallel in metadata deployments, package installations, or change set deployments. Every trigger must have some test coverage. All classes and triggers must compile successfully. If code uses conditional logic (including ternary operators), execute each branch. Make calls to methods using both valid and invalid inputs. Complete successfully without throwing any exceptions, unless those errors are expected and caught in a `try` `…` `catch` block. Always handle all exceptions that are caught, instead of merely catching the exceptions. Use the methods of the Assert class to prove that the code behaves properly. Use the `runAs` method to test your application in different user contexts. Exercise bulk trigger functionality—use at least 20 records in your tests. Use the `ORDER` `BY` keywords to ensure that the records are returned in the expected order. Not assume that record IDs are in sequential order. Record IDs aren’t created in ascending order unless you insert multiple records with the same request. For example, if you create an account A, and receive the ID `001D000000IEEmT` , then create account B, the ID of account B need not be sequentially higher. Set up test data: Create the necessary data in test classes, so the tests don’t have to rely on data in a particular organization. Create all test data before calling the `Test.startTest` method. Since tests don't commit, you don't have to delete any data. Write comments stating not only what must be tested, but the assumptions the tester made about the data, the expected outcome, and so on. Test the classes in your application individually. Never test your entire application in a single test. To protect the privacy of your data, make sure that test error messages and exception details don’t contain any personal data. The Apex exception handler and testing framework can’t determine if sensitive data is contained in user-defined messages and details. To include personal data in custom Apex exceptions, we recommend that you create an Exception subclass with new properties that holds the personal data. Then, don’t include subclass property information in the exception's message string. If you’re running many tests, test the classes in your organization individually in the Salesforce user interface instead of using the **Run** **All Tests** button to run them all together.

#### Best Practices for Parallel Test Execution

Tests that are started from the Salesforce user interface (including the Developer Console) run in parallel. Parallel test execution can speed up test run time. Sometimes, parallel test execution results in data contention issues, and you can turn off parallel execution in those cases. In particular, data contention issues and `UNABLE_TO_LOCK_ROW` errors can occur in the following cases: When tests update the same records at the same time. Updating the same records typically occurs when tests don’t create their own data and turn off data isolation to access the organization’s data. When a deadlock occurs in tests that are running in parallel and that try to create records with duplicate index field values. A deadlock occurs when two running tests are waiting for each other to roll back data. Such a wait can happen if two tests insert records with the same unique index field values. You can prevent receiving those errors by turning off parallel test execution in the Salesforce user interface: **1.** From Setup, enter `Apex` `Test` . **2.** Click **Options...** . **3.** In the Apex Test Execution Options dialog, select **Disable Parallel Apex Testing** and then click **OK** . Test classes annotated with `IsTest(IsParallel=` `true` `)` indicate that the test class can run concurrently with more than the default number of concurrent test classes. This annotation overrides default settings. Code Coverage Best Practices

### Testing Example

The following example includes cases for the following types of tests: Positive case with single and multiple records Negative case with single and multiple records Testing with other users The test is used with a simple mileage tracking application. The existing code for the application verifies that not more than 500 miles are entered in a single day. The primary object is a custom object named Mileage__c. The test creates one record with 300 miles and verifies there are only 300 miles recorded. Then a loop creates 200 records with one mile each. Finally, it verifies there are 500 miles recorded in total (the original 300 plus the new ones). Here’s the entire test class. The following sections step through specific portions of the code.

```apex
@isTest
private class MileageTrackerTestSuite {
```

```apex
static testMethod void runPositiveTestCases() {
```

```apex
Double totalMiles = 0;
final Double maxtotalMiles = 500;
final Double singletotalMiles = 300;
final Double u2Miles = 100;
```

```apex
//Set up user
User u1 = [SELECT Id FROM User WHERE Alias='auser'];
```

```apex
//Run As U1
System.RunAs(u1){
```

```apex
System.debug('Inserting 300
miles... (single record validation)');
```

```apex
Mileage__c testMiles1 = new Mileage__c(Miles__c = 300, Date__c = System.today());
```

```apex
insert testMiles1;
```

```apex
//Validate single insert
for(Mileage__c m:[SELECT miles__c FROM Mileage__c
WHERE CreatedDate = TODAY
and CreatedById = :u1.id
and miles__c != null]) {
totalMiles += m.miles__c;
}
```

```apex
Assert.areEqual(singletotalMiles, totalMiles);
```

```apex
//Bulk validation
totalMiles = 0;
System.debug('Inserting 200 mileage records... (bulk validation)');
```

```apex
List<Mileage__c> testMiles2 = new List<Mileage__c>();
for(integer i=0; i<200; i++) {
testMiles2.add( new Mileage__c(Miles__c = 1, Date__c = System.today()) );
}
insert testMiles2;
```

```apex
for(Mileage__c m:[SELECT miles__c FROM Mileage__c
WHERE CreatedDate = TODAY
and CreatedById = :u1.Id
and miles__c != null]) {
totalMiles += m.miles__c;
}
```

```apex
Assert.areEqual(maxtotalMiles, totalMiles);
```

```apex
}//end RunAs(u1)
```

```apex
//Validate additional user:
totalMiles = 0;
//Setup RunAs
User u2 = [SELECT Id FROM User WHERE Alias='tuser'];
System.RunAs(u2){
```

```apex
Mileage__c testMiles3 = new Mileage__c(Miles__c = 100, Date__c = System.today());
```

```apex
insert testMiles3;
```

```apex
for(Mileage__c m:[SELECT miles__c FROM Mileage__c
WHERE CreatedDate = TODAY
and CreatedById = :u2.Id
and miles__c != null]) {
totalMiles += m.miles__c;
}
//Validate
Assert.areEqual(u2Miles, totalMiles);
```

```apex
} //System.RunAs(u2)
```

```apex
} // runPositiveTestCases()
```

```apex
static testMethod void runNegativeTestCases() {
```

```apex
User u3 = [SELECT Id FROM User WHERE Alias='tuser'];
System.RunAs(u3) {
```

```apex
System.debug('Inserting a record with 501 miles... (negative test case)');
```

```apex
Mileage__c testMiles3 = new Mileage__c( Miles__c = 501, Date__c = System.today()
);
```

```apex
try {
```

```apex
insert testMiles3;
Assert.fail('DmlException expected');
} catch (DmlException e) {
```

```apex
//Assert Status Code
Assert.areEqual('FIELD_CUSTOM_VALIDATION_EXCEPTION', e.getDmlStatusCode(0));
```

```apex
//Assert field
Assert.areEqual(Mileage__c.Miles__c, e.getDmlFields(0)[0]);
```

```apex
//Assert Error Message
Assert.isTrue(e.getMessage().contains(
```

```apex
'Mileage request exceeds daily limit(500): [Miles__c]'),
'DMLException did not contain expected validation message:' + e.getMessage()
);
```

```apex
} //catch
} //RunAs(u3)
} // runNegativeTestCases()
```

```apex
} // class MileageTrackerTestSuite
```

#### Positive Test Case

The following steps through the above code, in particular, the positive test case for single and multiple records. **1.** Add text to the debug log, indicating the next step of the code:

```apex
System.debug('Inserting 300 more miles...single record validation');
```

**2.** Create a Mileage__c object and insert it into the database.

```apex
Mileage__c testMiles1 = new Mileage__c(Miles__c = 300, Date__c = System.today() );
insert testMiles1;
```

**3.** Validate the code by returning the inserted records:

```apex
for(Mileage__c m:[SELECT miles__c FROM Mileage__c
WHERE CreatedDate = TODAY
and CreatedById = :createdbyId
and miles__c != null]) {
totalMiles += m.miles__c;
}
```

**4.** Use the `Assert.areEqual` method to verify that the expected result is returned:

```apex
Assert.areEqual(singletotalMiles, totalMiles);
```

**5.** Before moving to the next test, set the number of total miles back to 0:

```apex
totalMiles = 0;
```

**6.** Validate the code by creating a bulk insert of 200 records. First, add text to the debug log, indicating the next step of the code:

```apex
System.debug('Inserting 200 Mileage records...bulk validation');
```

**7.** Then insert 200 Mileage__c records:

```apex
List<Mileage__c> testMiles2 = new List<Mileage__c>();
for(Integer i=0; i<200; i++){
testMiles2.add( new Mileage__c(Miles__c = 1, Date__c = System.today()) );
}
insert testMiles2;
```

**8.** Use `Assert.areEqual` to verify that the expected result is returned:

```apex
for(Mileage__c m:[SELECT miles__c FROM Mileage__c
WHERE CreatedDate = TODAY
and CreatedById = :CreatedbyId
and miles__c != null]) {
totalMiles += m.miles__c;
}
Assert.areEqual(maxtotalMiles, totalMiles);
```

#### Negative Test Case

The following steps through the above code, in particular, the negative test case. **1.** Create a static test method called `runNegativeTestCases` :

```apex
static testMethod void runNegativeTestCases(){
```

**2.** Add text to the debug log, indicating the next step of the code:

```apex
System.debug('Inserting 501 miles... negative test case');
```

**3.** Create a Mileage__c record with 501 miles.

```apex
Mileage__c testMiles3 = new Mileage__c(Miles__c = 501, Date__c = System.today());
```

**4.** Place the `insert` statement within a `try` / `catch` block. This allows you to catch the validation exception and assert the generated error message. Use the `Assert.fail` method to clearly assert that you expect the validation exception.

```apex
try {
```

```apex
insert testMiles3;
Assert.fail('DmlException expected');
} catch (DmlException e) {
```

**5.** Now use the `Assert.areEqual` and `Assert.isTrue` methods to do the testing. Add the following code to the `catch` block you previously created:

```apex
//Assert Status Code
Assert.areEqual('FIELD_CUSTOM_VALIDATION_EXCEPTION', e.getDmlStatusCode(0));
```

```apex
//Assert field
Assert.areEqual(Mileage__c.Miles__c, e.getDmlFields(0)[0]);
```

```apex
//Assert Error Message
Assert.isTrue(e.getMessage().contains(
```

```apex
'Mileage request exceeds daily limit(500): [Miles__c]'),
'DMLException did not contain expected validation message:' + e.getMessage() );
```

#### Testing as a Second User

The following steps through the above code, in particular, running as a second user. **1.** Before moving to the next test, set the number of total miles back to 0:

```apex
totalMiles = 0;
```

**2.** Set up the next user.

```apex
User u2 = [SELECT Id FROM User WHERE Alias='tuser'];
System.RunAs(u2){
```

**3.** Add text to the debug log, indicating the next step of the code:

```apex
System.debug('Setting up testing - deleting any mileage records for ' +
UserInfo.getUserName() +
' from today');
```

**4.** Then insert one Mileage__c record:

```apex
Mileage__c testMiles3 = new Mileage__c(Miles__c = 100, Date__c = System.today());
insert testMiles3;
```

**5.** Validate the code by returning the inserted records:

```apex
for(Mileage__c m:[SELECT miles__c FROM Mileage__c
WHERE CreatedDate = TODAY
and CreatedById = :u2.Id
and miles__c != null]) {
totalMiles += m.miles__c;
}
```

**6.** Use the `Assert.areEqual` method to verify that the expected result is returned:

```apex
Assert.areEqual(u2Miles, totalMiles);
```

### Testing and Code Coverage

The Apex testing framework generates code coverage numbers for your Apex classes and triggers every time you run one or more tests. Code coverage indicates how many executable lines of code in your classes and triggers have been exercised by test methods. Write test methods to test your triggers and classes, and then run those tests to generate code coverage information. **Apex Trigger and Class Covered by Test Methods** In addition to ensuring the quality of your code, unit tests enable you to meet the code coverage requirements for deploying or packaging Apex. To deploy Apex or package it for the Salesforce AppExchange, unit tests must cover at least 75% of your Apex code, and those tests must pass. Code coverage serves as one indication of test effectiveness, but doesn’t guarantee test effectiveness. The quality of the tests also matters, but you can use code coverage as a tool to assess whether you need to add more tests. While you need to meet minimum code coverage requirements for deploying or packaging your Apex code, code coverage shouldn’t be the only goal of your tests. Tests should assert your app’s behavior and ensure the quality of your code.

#### How Is Code Coverage Calculated?

Code coverage percentage is a calculation of the number of covered lines divided by the sum of the number of covered lines and uncovered lines. Only executable lines of code are included. (Comments and blank lines aren’t counted.) `System.debug()` statements and curly brackets are excluded when they appear alone on one line. Multiple statements on one line are counted as one line for the purpose of code coverage. If a statement consists of multiple expressions that are written on multiple lines, each line is counted for code coverage. The following is an example of a class with one method. The tests for this class have been run, and the option to show code coverage was chosen for this class in the Developer Console. The blue lines represent the lines that are covered by tests. The lines that aren’t highlighted are left out of the code coverage calculation. The red lines show the lines that weren’t covered by tests. To achieve full coverage, more tests are needed. The tests must call `getTaskPriority()` with different inputs and verify the returned value. This is the class that is partially covered by test methods. The corresponding test class isn’t shown. Test classes (classes that are annotated with `@isTest` ) are excluded from the code coverage calculation. This exclusion applies to all test classes regardless of what they contain—test methods or utility methods used for testing. The Apex compiler sometimes optimizes expressions in a statement. For example, if multiple string constants are concatenated with the `+` operator, the compiler replaces those expressions with one string constant internally. If the string concatenation expressions are on separate lines, the additional lines aren’t counted as part of the code coverage calculation after optimization. To illustrate this point, a string variable is assigned to two string constants that are concatenated. The second string constant is on a separate line.

```apex
String s = 'Hello'
```

```apex
+ ' World!';
```

The compiler optimizes the string concatenation and represents the string as one string constant internally. The second line in this example is ignored for code coverage.

```apex
String s = 'Hello World!';
```

#### Inspecting Code Coverage

After running tests, you can view code coverage information in the Tests tab of the Developer Console. The code coverage pane includes coverage information for each Apex class and the overall coverage for all Apex code in your organization. Also, code coverage is stored in two Lightning Platform Tooling API objects: ApexCodeCoverageAggregate and ApexCodeCoverage . ApexCodeCoverageAggregate stores the sum of covered lines for a class after checking all test methods that test it. ApexCodeCoverage stores the lines that are covered and uncovered by each individual test method. For this reason, a class can have multiple coverage results in ApexCodeCoverage—one for each test method that has tested it. You can query these objects by using SOQL and the Tooling API to retrieve coverage information. Using SOQL queries with Tooling API is an alternative way of checking code coverage and a quick way to get more details. For example, this SOQL query gets the code coverage for the `TaskUtil` class. The coverage is aggregated from all test classes that exercised the methods in this class.

```apex
SELECT ApexClassOrTrigger.Name, NumLinesCovered, NumLinesUncovered
FROM ApexCodeCoverageAggregate
WHERE ApexClassOrTrigger.Name = 'TaskUtil'
```

This SOQL query requires the Tooling API. You can run this query by using the Query Editor in the Developer Console and checking **Use Tooling API** . Here’s a sample query result for a class that’s partially covered by tests: 2 8 TaskUtil This next example shows how you can determine which test methods covered the class. The query gets coverage information from a different object, ApexCodeCoverage, which stores coverage information by test class and method.

```apex
SELECT ApexTestClass.Name,TestMethodName,NumLinesCovered,NumLinesUncovered
FROM ApexCodeCoverage
WHERE ApexClassOrTrigger.Name = 'TaskUtil'
```

Here’s a sample query result. 3 7 testTaskPriority TaskUtilTest 4 6 testTaskHighPriority TaskUtilTest If a single deployment has over 2,000 Apex classes, ApexCodeCoverage objects for the deployed classes are deleted even if the deployment fails or is rolled back.ApexCodeCoverageAggregate objects aren’t affected. The NumLinesUncovered values in ApexCodeCoverage differ from the corresponding value for the aggregate result in ApexCodeCoverageAggregate because they represent the coverage related to one test method each. For example, test method `testTaskPriority()` covered 7 lines in the entire class out of a total of 10 coverable lines, so the number of uncovered lines with regard to `testTaskPriority()` is 3 lines (10–7). Because the aggregate coverage stored in ApexCodeCoverageAggregate includes coverage by all test methods, the coverage of `testTaskPriority()` and `testTaskHighPriority()` is included, which leaves only 2 lines that are not covered by any test methods.

### Code Coverage Best Practices

Consider the following code coverage tips and best practices.

#### Code Coverage General Tips

Run tests to refresh code coverage numbers. Code coverage numbers aren't refreshed when updates are made to Apex code in the organization unless tests are rerun. If the organization has been updated since the last test run, the code coverage estimate can be incorrect. Rerun Apex tests to get a correct estimate. The overall code coverage percentage in your organization doesn’t include code coverage from package-related tests. The only exception is when package tests cause your triggers to fire. For more information, see Managed and Unlocked Package Tests . Coverage is based on the total number of code lines in the organization. Adding or deleting lines of code changes the coverage percentage. For example, let's say an organization has 50 lines of code covered by test methods. If you add a trigger that has 50 lines of code not covered by tests, the code coverage percentage drops from 100% to 50%. The trigger increases the total code lines in the organization from 50 to 100, of which only 50 are covered by tests.

#### Why Code Coverage Numbers Differ Between Sandbox and Production

When Apex is deployed to production or uploaded as part of a package to the Salesforce AppExchange, Salesforce runs local tests in the destination organization. Sandbox and production environments often don’t contain the same data and metadata, so the code coverage results don’t always match. If code coverage is less than 75% in production, increase the coverage to be able to deploy or upload your code. The following are common causes for the discrepancies in code coverage numbers between your development or sandbox environment and production. This information can help you troubleshoot and reconcile those differences. **Test Failures** If the test results in one environment are different, the overall code coverage percentage doesn’t match. Before comparing code coverage numbers between sandbox and production, make sure that all tests for the code that you’re deploying or packaging pass in your organization first. The tests that contribute to the code coverage calculation must all pass before deployment or a package upload. **Data Dependencies** If your tests access organization data by using the `@IsTest(SeeAllData=true)` annotation, the test results can differ depending on which data is available in the organization. If the records referenced in a test don’t exist or have changed, the test fails or different code paths are executed in the Apex methods. Modify tests so that they create test data instead of accessing organization data. **Metadata Dependencies** Changes in the metadata, such as changes in the user’s profile settings, can cause tests to fail or execute different code paths. Make sure that the metadata in sandbox and production match, or ensure that the metadata changes aren’t the cause of different test execution behavior. **Managed and Unlocked Package Tests** Code coverage that is computed after you run all Apex tests in the user interface, such as the Developer Console, can differ from code coverage obtained in a deployment. If you run all tests, including package-related tests, in the user interface, the overall code coverage in your organization doesn’t include coverage for packaging code. Although package-related tests cover lines of code in managed or unlocked packages, this coverage isn’t part of the organization’s code coverage calculation as total lines and covered lines. In contrast, the code coverage computed in a deployment after running all tests through the `RunAllTestsInOrg` test level includes coverage of package-related code. If you’re running package tests in a deployment through the `RunAllTestsInOrg` test level, we recommend that you run this deployment in a sandbox first or perform a validation deployment to verify code coverage. **Deployment Resulting in Overall Coverage Lower Than 75%** When deploying new components that have 100% coverage to production, the deployment fails if the average coverage between the new and existing code doesn’t meet the 75% threshold. If a test run in the destination organization returns a coverage result of less than 75%, modify the existing test methods or write additional test methods to raise the code coverage over 75%. Deploy the modified or new test methods separately or with your new code that has 100% coverage. **Code Coverage in Production Dropping Below 75%** Sometimes the overall coverage in production drops below 75%, even though it was at least 75% when the components were deployed from sandbox. Test methods that have dependencies on the organization’s data and metadata can cause a drop in code coverage. If the data and metadata have changed sufficiently to alter the result of dependent test methods, some methods can fail or behave differently. In that case, certain lines are no longer covered.

#### Recommended Process for Matching Code Coverage Numbers for Production

Use a Full Sandbox as the staging sandbox environment for production deployments. A Full Sandbox mimics the metadata and data in production and helps reduce differences in code coverage numbers between the two environments. To reduce dependencies on data in sandbox and production organizations, use test data in your Apex tests. If a deployment to production fails due to insufficient code coverage, write more tests to raise the overall code coverage to the highest possible coverage or 100%. Retry the deployment. If a deployment to production fails even after you raise code coverage numbers in sandbox, run local tests from your production organization. Identify the classes with less than 75% coverage. Write additional tests for these classes in sandbox to raise the code coverage.

### Build a Mocking Framework with the Stub API

Apex provides a stub API for implementing a mocking framework. A mocking framework has many benefits. It can streamline and improve testing and help you create faster, more reliable tests. You can use it to test classes in isolation, which is important for unit testing. Building your mocking framework with the stub API can also be beneficial because stub objects are generated at runtime. Because these objects are generated dynamically, you don’t have to package and deploy test classes. You can build your own mocking framework, or you can use one built by someone else. You can define the behavior of stub objects, which are created at runtime as anonymous subclasses of Apex classes. The stub API comprises the `System.StubProvider` interface and the `System.Test.createStub()` method. This feature is intended for advanced Apex developers. Using it requires a thorough understanding of unit testing and mocking frameworks. Let’s look at an example to illustrate how the stub API works. This example isn’t meant to demonstrate the wide range of possible uses for mocking frameworks. It’s intentionally simple to focus on the mechanics of using the Apex stub API. Let’s say we want to test the formatting method in the following class.

```apex
public class DateFormatter {
```

```apex
// Method to test
public String getFormattedDate(DateHelper helper) {
```

```apex
return 'Today\'s date is ' + helper.getTodaysDate();
}
}
```

Usually, when we invoke this method, we pass in a helper class that has a method that returns today’s date.

```apex
public class DateHelper {
```

```apex
// Method to stub
public String getTodaysDate() {
```

```apex
return Date.today().format();
}
}
```

The following code invokes the method.

```apex
DateFormatter df = new DateFormatter();
DateHelper dh = new DateHelper();
String dateStr = df.getFormattedDate(dh);
```

For testing, we want to isolate the `getFormattedDate()` method to make sure that the formatting is working properly. The return value of the `getTodaysDate()` method normally varies based on the day. However, in this case, we want to return a constant, predictable value to isolate our testing to the formatting. Rather than writing a “fake” version of the class, where the method returns a constant value, we create a stub version of the class. The stub object is created dynamically at runtime, and we can specify the “stubbed” behavior of its method. To use a stub version of an Apex class: **1.** Define the behavior of the stub class by implementing the `System.StubProvider` interface. **2.** Instantiate a stub object by using the `System.Test.createStub()` method. **3.** Invoke the relevant method of the stub object from within a test class.

#### Implement the StubProvider Interface

Here’s an implementation of the `StubProvider` interface.

```apex
@isTest
public class MockProvider implements System.StubProvider {
```

```apex
public Object handleMethodCall(Object stubbedObject, String stubbedMethodName,
Type returnType, List<Type> listOfParamTypes, List<String> listOfParamNames,
List<Object> listOfArgs) {
```

```apex
// The following debug statements show an example of logging
// the invocation of a mocked method.
```

```apex
// You can use the method name and return type to determine which method was called.
```

```apex
System.debug('Name of stubbed method: ' + stubbedMethodName);
System.debug('Return type of stubbed method: ' + returnType.getName());
```

```apex
// You can also use the parameter names and types to determine which method
// was called.
for (integer i =0; i < listOfParamNames.size(); i++) {
System.debug('parameter name: ' + listOfParamNames.get(i));
System.debug('
parameter type: ' + listOfParamTypes.get(i).getName());
}
```

```apex
// This shows the actual parameter values passed into the stubbed method at runtime.
```

```apex
System.debug('number of parameters passed into the mocked call: ' +
listOfArgs.size());
System.debug('parameter(s) sent into the mocked call: ' + listOfArgs);
```

```apex
// This is a very simple mock provider that returns a hard-coded value
// based on the return type of the invoked.
if (returnType.getName() == 'String')
```

```apex
return '8/8/2016';
else
return null;
}
}
```

`StubProvider` is a callback interface. It specifies a single method that requires implementing: `handleMethodCall()` . When a stubbed method is called, `handleMethodCall()` is called. You define the behavior of the stubbed class in this method. The method has the following parameters. `stubbedObject` : The stubbed object `stubbedMethodName` : The name of the invoked method `returnType` : The return type of the invoked method `listOfParamTypes` : A list of the parameter types of the invoked method `listOfParamNames` : A list of the parameter names of the invoked method `listOfArgs` : The actual argument values passed into this method at runtime You can use these parameters to determine which method of your class was called, and then you can define the behavior for each method. In this case, we check the return type of the method to identify it and return a hard-coded value.

#### Instantiate a Stub Version of the Class

The next step is to instantiate a stub version of the class. The following utility class returns a stub object that you can use as a mock.

```apex
public class MockUtil {
```

```apex
private MockUtil(){}
```

```apex
public static MockProvider getInstance() {
```

```apex
return new MockProvider();
}
```

```apex
public static Object createMock(Type typeToMock) {
```

```apex
// Invoke the stub API and pass it our mock provider to create a
// mock class of typeToMock.
return Test.createStub(typeToMock, MockUtil.getInstance());
}
}
```

This class contains the method `createMock()` , which invokes the `Test.createStub()` method. The `createStub()` method takes an Apex class type and an instance of the `StubProvider` interface that we created previously. It returns a stub object that we can use in testing.

#### Invoke the Stub Method

Finally, we invoke the relevant method of the stub class from within a test class.

```apex
@isTest
public class DateFormatterTest {
```

```apex
@isTest
public static void testGetFormattedDate() {
```

```apex
// Create a mock version of the DateHelper class.
DateHelper mockDH = (DateHelper)MockUtil.createMock(DateHelper.class);
DateFormatter df = new DateFormatter();
```

```apex
// Use the mocked object in the test.
System.assertEquals('Today\'s date is 8/8/2016', df.getFormattedDate(mockDH));
}
}
```

In this test, we call the `createMock()` method to create a stub version of the `DateHelper` class. We can then invoke the `getTodaysDate()` method on the stub object, which returns our hard-coded date. Using the hard-coded date allows us to test the behavior of the `getFormattedDate()` method in isolation.

#### Apex Stub API Limitations

Keep the following limitations in mind when working with the Apex stub API. The object being mocked must be in the same namespace as the call to the `Test.createStub()` method. However, the implementation of the `StubProvider` interface can be in another namespace. You can’t mock the following Apex elements. Static methods (including future methods) Private methods Properties (getters and setters) Triggers Inner classes System types Classes that implement the `Batchable` interface Classes that have only private constructors Iterators can’t be used as return types or parameter types. StubProvider Interface Test.createStub()

### Apex Integration Tests for Agentforce and Data 360 Services (Developer Preview)

Use Apex integration tests to write end-to-end tests that exercise real interactions between your Salesforce org and services such as Agentforce and Data 360. Unlike standard Apex unit tests, integration tests relax callout restrictions and transaction rollback semantics, so your tests can make real service calls, commit data mid-transaction, and make assertions on expected outcomes. As a developer preview feature, integration tests are available only in scratch orgs. You can’t run them in production orgs or during metadata deployments. The Apex Integration Tests feature is available as a developer preview in scratch orgs in Summer ’26 (API version 67.0). The feature isn’t generally available unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement functionality developed with these commands or tools in your production package.

#### How Integration Tests Compare to Unit Tests

Integration tests complement, rather than replace, existing Apex unit tests. Unit tests remain the right choice for testing isolated business logic, triggers, and flows. Integration tests are for scenarios that require real service interactions across transaction boundaries. Use integration tests used in these ways. Test Agentforce callouts and verify their side effects on org data. Run real SOQL queries against Data 360 data model objects (DMOs) without stub mocks. Test behavior that depends on committed data, such as field history tracking across updates. This table shows the key differences between standard Apex unit tests(@IsTest) and integration tests (@IntegrationTest). Allowed Blocked; require mocks Agentforce and Data 360 callouts Data committed. Use `@TearDown` for cleanup Auto-rollback Transaction behavior `SeeAllData=` `true` by default Test data silo by default Data visibility Doesn’t count toward deployment code coverage requirements Counts toward deployment code coverage requirements Code coverage Excluded Included. Unit tests are xecuted in metadata deployment. Metadata deployments Asynchronous only. Allowed only 1 concurrent execution per org. Synchronous or asynchronous Execution 10 minutes Standard limits Maximum runtime

#### Enable Integration Tests in a Scratch Org Definition File

Before you can run Apex integration tests, you must have a scratch org with the `ApexIntegrationTests` feature enabled. To enable the feature, add `ApexIntegrationTests` to the features array in the `config/project-scratch-def.json` of your Salesforce DX project.

```apex
{
```

```apex
"orgName": "Company",
"edition": "Developer",
"features": ["ApexIntegrationTests"]
}
```

To create a scratch org with this definition, use the `org` `create` `scratch` Salesforce CLI command. For more information about scratch org development, see Scratch Orgs in the Salesforce DX Developer Guide .

#### Create an Integration Test Class

To create an Apex integration test class, use these annotations and methods. `@IntegrationTest` : This annotation marks a class and its test methods as integration tests. A class annotated with `@IntegrationTest` can only contain integration test methods and `@TearDown` methods. You can’t annotate a class with both `@IntegrationTest` and `@IsTest` annotations. You can’t call integration test methods from non-test contexts or from `@IsTest` test methods. However, integration tests can call methods in `@IsTest` utility classes such as shared test data factories. `@TearDown` : This annotation marks a static cleanup method that runs after the test completes, regardless of whether the test passes or fails. Use this method to clean up committed test data. The teardown transaction auto-commits at the end of the execution. `IntegrationTest.commitTestOnly()` : This method commits data to the database mid-transaction so that it’s visible to other threads and services. It resets the uncommitted work checkpoint, so subsequent callouts don’t fail. The method also resets tracking for mixed DML operations, so you can perform setup sObject and non-setup sObject DML in separate commit windows. The method can only be called from an `@IntegrationTest` method. Calling it from outside an integration test context results in a runtime error: `Test.commitTestOnly()` `can` `only` `be` `called` `from` `integration` `testMethods` . This basic integration test verifies that the service can insert an account.

```apex
@IntegrationTest
public class MyServiceIntegrationTest {
```

```apex
@IntegrationTest
public static void testServiceInteraction() {
Account a = new Account(Name = 'Integration Test Account');
insert as user a;
IntegrationTest.commitTestOnly();
```

```apex
Account result = [SELECT Id, Name FROM Account WHERE Id = :a.Id WITH USER_MODE];
Assert.areEqual('Integration Test Account', result.Name);
}
```

```apex
@TearDown
public static void tearDown() {
```

```apex
delete as user [SELECT Id FROM Account WHERE Name = 'Integration Test Account'];
}
}
```

An integration test can invoke an agent with an invocable action and assert on the response. The `commitTestOnly()` call before the agent invocation is critical. Without it, the record you created exists only in your pending transaction and is invisible to the Agentforce planner service.

```apex
@IntegrationTest
public with sharing class AgentforceIntegrationTest {
```

```apex
@IntegrationTest
public static void testAgentSummarizesAccount() {
```

```apex
Account a = new Account(Name = 'AgentDemoAccount', AnnualRevenue = 1000000);
insert as user a;
IntegrationTest.commitTestOnly();
```

```apex
Invocable.Action action = Invocable.Action.createCustomAction(
```

```apex
'generateAiAgentResponse',
'Demo_Action'
);
action.setInvocationParameter('userMessage', 'Summarize my Account ' + a.Id);
```

```apex
List<Invocable.Action.Result> results = action.invoke();
String response =
results[0].getOutputParameters().get('agentResponse').toString();
```

```apex
Assert.isNotNull(response, 'Agent should return a response');
Assert.isTrue(response.contains('AgentDemoAccount'),
```

```apex
'Response should reference the account name');
}
```

```apex
@TearDown
public static void tearDown() {
```

```apex
delete as user [SELECT Id FROM Account WHERE Name = 'AgentDemoAccount'];
}
}
```

This example uses the AdvancedInputBindings agent script recipe and generates a sales report for Q2 2026.

```apex
@IntegrationTest
public with sharing class AdvancedInputBindingsIntegrationTest {
```

```apex
@IntegrationTest
public static void testAgentUpdate() {
```

```apex
// Invoke Agentforce service (callout allowed in integration tests)
Invocable.Action action = Invocable.Action.createCustomAction(
```

```apex
'generateAiAgentResponse',
'AdvancedInputBindings'
);
```

```apex
String prompt = 'Generate a sales report for Q2 2026';
action.setInvocationParameter('userMessage', prompt);
List<Invocable.Action.Result> results = action.invoke();
```

```apex
String response =
results[0].getOutputParameters().get('agentResponse').toString();
Assert.isTrue(response.contains('a0'), 'Expected agent response to create an
sobject');
```

```apex
// query and assert the report was created
List<ASR_Report_Log__c> logs = [
SELECT Id, Report_Type__c, User_ID__c, Format__c
FROM ASR_Report_Log__c
WHERE Start_Date__c = 2026-04-01
];
Assert.areEqual(1, logs.size(), 'Report log should be created');
}
```

```apex
@tearDown
public static void destroyTestRecords() {
List<ASR_Report_Log__c> testRecords = [
SELECT Id, Report_Type__c, User_ID__c, Format__c
FROM ASR_Report_Log__c
WHERE Start_Date__c = 2026-04-01
];
```

```apex
if (testRecords.size() > 0) {
```

```apex
delete testRecords;
}
}
}
```

Query Data 360 data model objects (DMOs) directly in integration tests without using `SoqlStubProvider` or `Test.createSoqlStub` . In standard unit tests, SOQL queries against DMO objects require stub mocks. Integration tests bypass this restriction for Data 360 entities.

```apex
@IntegrationTest
public with sharing class DataCloudQueryIntegrationTest {
```

```apex
@IntegrationTest
public static void testDMOQuery() {
List<SObject> rows = Database.query('SELECT Id FROM Account__dlm WITH USER_MODE
LIMIT 1');
Assert.areEqual(1, rows.size(), 'Data 360 query should return 1 row');
}
}
```

Use `System.runAs()` to run integration test logic as a specific user, including setting up the necessary permission set assignments.

```apex
@IntegrationTest
public with sharing class RunAsIntegrationTest {
```

```apex
@IntegrationTest
public static void testAgentResponseAsStandardUser() {
User u = [SELECT Id FROM User WHERE Alias = 'tstUsr' LIMIT 1];
```

```apex
System.runAs(u) {
Account a = new Account(Name = 'AgentDemoAccount');
insert as user a;
IntegrationTest.commitTestOnly();
```

```apex
Invocable.Action action = Invocable.Action.createCustomAction(
```

```apex
'generateAiAgentResponse',
'Demo_Action'
);
String prompt = 'Summarize my Account ' + a.Id;
action.setInvocationParameter('userMessage', prompt);
List<Invocable.Action.Result> results = action.invoke();
```

```apex
String response = results[0].getOutputParameters()
.get('agentResponse').toString();
Assert.isTrue(response.contains('AgentDemoAccount'));
}
}
```

```apex
@TearDown
public static void tearDown() {
```

```apex
delete as user [SELECT Id FROM Account WHERE Name = 'AgentDemoAccount'];
}
}
```

Regular HTTP callouts to external endpoints other than Agentforce and Data 360 still require mocks in integration tests.

```apex
@IntegrationTest
public with sharing class HttpCalloutMockIntegrationTest implements HttpCalloutMock {
```

```apex
public HTTPResponse respond(HTTPRequest req) {
HttpResponse res = new HttpResponse();
```

```apex
res.setHeader('Content-Type', 'application/json');
res.setBody('{"status":"success"}');
res.setStatusCode(200);
return res;
}
```

```apex
@IntegrationTest
public static void testExternalApiWithMock() {
Test.setMock(HttpCalloutMock.class, new HttpCalloutMockIntegrationTest());
```

```apex
Account a = new Account(Name = 'Callout Test Account');
insert as user a;
IntegrationTest.commitTestOnly();
```

```apex
Http h = new Http();
HttpRequest req = new HttpRequest();
req.setEndpoint('https://external-api.example.com/api');
req.setMethod('POST');
req.setBody('{"accountId":"' + a.Id + '"}');
```

```apex
HttpResponse res = h.send(req);
```

```apex
Assert.areEqual(200, res.getStatusCode());
Assert.isTrue(res.getBody().contains('success'));
}
```

```apex
@TearDown
public static void tearDown() {
```

```apex
delete as user [SELECT Id FROM Account WHERE Name = 'Callout Test Account'];
}
}
```

Asynchronous Apex operations enqueued in integration tests can be dequeued synchronously using the `Test.startTest()` and `Test.stopTest()` pattern.

```apex
@IntegrationTest
public with sharing class AsyncIntegrationTest {
```

```apex
public with sharing class AccountProcessorQueueable implements Queueable {
```

```apex
private Id accountId;
```

```apex
public AccountProcessorQueueable(Id accountId) {
```

```apex
this.accountId = accountId;
}
```

```apex
public void execute(QueueableContext context) {
Account a = [SELECT Id, Name FROM Account WHERE Id = :accountId WITH
USER_MODE];
a.Industry = 'Technology';
update as user a;
}
}
```

```apex
@IntegrationTest
public static void testQueueableExecution() {
Account a = new Account(Name = 'Async Test Account');
insert as user a;
IntegrationTest.commitTestOnly();
```

```apex
Test.startTest();
Id jobId = System.enqueueJob(new AccountProcessorQueueable(a.Id));
Test.stopTest();
```

```apex
Account updated = [SELECT Industry FROM Account WHERE Id = :a.Id WITH USER_MODE];
```

```apex
Assert.areEqual('Technology', updated.Industry,
```

```apex
'Queueable should have updated the industry');
```

```apex
AsyncApexJob job = [
SELECT Status, NumberOfErrors
FROM AsyncApexJob WHERE Id = :jobId
WITH USER_MODE
];
Assert.areEqual('Completed', job.Status);
Assert.areEqual(0, job.NumberOfErrors);
}
@TearDown
public static void tearDown() {
```

```apex
delete as user [SELECT Id FROM Account WHERE Name = 'Async Test Account'];
}
}
```

Use `IntegrationTest.commitTestOnly()` multiple times with a test method to commit data progressively, which is useful when later operations depend on previously committed records.

```apex
@IntegrationTest
public with sharing class MultiCommitIntegrationTest {
```

```apex
@IntegrationTest
public static void testMultipleCommits() {
Account a = new Account(Name = 'Commit Test Account');
insert as user a;
IntegrationTest.commitTestOnly();
```

```apex
a.Website = 'example.com';
update as user a;
IntegrationTest.commitTestOnly();
```

```apex
Contact c = new Contact(
FirstName = 'Test',
LastName = 'Contact',
AccountId = a.Id
);
insert as user c;
```

```apex
IntegrationTest.commitTestOnly();
```

```apex
Assert.areEqual(1,
[SELECT COUNT() FROM Account WHERE Name = 'Commit Test Account' WITH
USER_MODE]);
Assert.areEqual(1,
[SELECT COUNT() FROM Contact WHERE AccountId = :a.Id WITH USER_MODE]);
}
```

```apex
@TearDown
public static void tearDown() {
```

```apex
delete as user [SELECT Id FROM Contact WHERE LastName = 'Contact'];
delete as user [SELECT Id FROM Account WHERE Name = 'Commit Test Account'];
}
}
```

Standard unit tests roll back all data, so field history records are never created. Integration tests commit data, which makes it possible to assert on field history.

```apex
@IntegrationTest
public with sharing class FieldHistoryIntegrationTest {
```

```apex
@IntegrationTest
public static void testFieldHistoryIsTracked() {
Account a = new Account(Name = 'HistoryTestAccount', Website = 'example.com');
```

```apex
insert as user a;
IntegrationTest.commitTestOnly();
```

```apex
a.Website = 'salesforce.com';
update as user a;
IntegrationTest.commitTestOnly();
```

```apex
List<AccountHistory> history = [
SELECT Id FROM AccountHistory WHERE AccountId = :a.Id
WITH USER_MODE
];
Assert.isTrue(history.size() > 0, 'Expected field history to be tracked');
}
```

```apex
@TearDown
public static void tearDown() {
```

```apex
delete as user [SELECT Id FROM Account WHERE Name = 'HistoryTestAccount'];
}
}
```

#### Run an Integration Test

Both the test method and the teardown method commit their transactions automatically at the end of execution. Data created during the test persists unless explicitly deleted in the teardown. `@TestSetup` methods also run before integration tests. Integration tests are considered a distinct “IntegrationTest” category that’s separate from Apex unit tests, flow tests, and Agentforce tests. You can discover and run them using the Salesforce CLI or the Tooling API, either a single test class synchronously or multiple test classes asynchronously. Integration tests are excluded from `RunAllTests` during metadata deployments.

#### Integration Testing Best Practices

Always implement `@TearDown` methods. Because integration tests commit data to the database, test data that is not torn down after the test run can impact subsequent runs. Delete records in the correct order in `@TearDown` . When you create related records, delete child records before parent records to avoid foreign key constraint issues. Use `commitTestOnly()` before callouts to Agentforce and Data 360. These services operate on separate threads that can’t see uncommitted data in your test’s pending transaction. Keep integration tests focused on integration concerns. Test isolated business logic with standard `@IsTest` unit tests. Reserve integration tests for scenarios that require real service interactions. Be aware of concurrency limits. Only one integration test can run per org at a time. Design your test suite accordingly, and prefer shorter, more focused tests over long monolithic ones. Integration tests have access to and can commit data to your org ( `seeAllData=` `true` ). Be mindful of other requests that may be trying to write to the same data rows in your org if you use existing data from your org. Create setup data and avoid reusing org data to avoid row lock contention. Plan for the 10-minute runtime limit. If a test involves multiple slow service calls, consider splitting it into separate test methods. Mock external HTTP endpoints. Even in integration tests, regular HTTP callouts to non-Salesforce endpoints require `HttpCalloutMock` . Only Agentforce and Data 360 services are exempt from the mock requirement.

#### Integration Testing Limitations and Considerations

During developer preview, integration testing can only run in scratch orgs. Integration tests aren’t available in production orgs, sandboxes, or during metadata deployments. Integration tests don’t count toward code coverage requirements. There is no `@TestVisible` access. Unlike `@IsTest` classes, `@IntegrationTest` classes can’t access private members annotated with `@TestVisible` in the test classes. Only asynchronous execution is supported. Only one test runs per org at a time. Asynchronous Apex governor limits (for SOQL, DML, CPU and heap limits) apply to integration testing. See Execution Governors and Limits on page 348. Integration tests share the same 24-hour limit on asynchronous Apex test runs with flow tests and unit tests. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing.htm https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_stub_api.htm https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_unit_tests.htm https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/MockSOQLTestsForDMOs.htm https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Invocable_Action.htm https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_best_practices.htm

## Deploying Apex

You can't develop Apex in your Salesforce production org. Your development work is done in a sandbox, in a scratch org, or in a Developer Edition org.

### Compile On Deploy

Each org’s Apex code is automatically recompiled before completing a metadata deploy, package install, or package upgrade. Compile on deploy is enabled automatically for production orgs and full sandboxes to ensure that users don’t experience reduced performance immediately following a deployment. You can’t disable the compile on deploy option in production orgs. For developer sandbox, developer pro sandbox, partial copy sandbox, developer, trial, and scratch orgs, this feature is disabled by default. To enable, select the **Perform Synchronous Compile on Deploy** option under Apex Settings in Setup. Deselect this option if you want to disable the feature in full sandboxes. With the Compile on Deploy feature, deployments to the org invoke the Apex compiler and save the resulting bytecode as part of the deployment. For example, if you deploy a custom field, all the classes that use that custom field are recompiled. A minimal increase in deployment times can occur, but Apex doesn’t need to be recompiled to process subsequent requests. The slight increase in deployment time can, in fact, mitigate performance issues for currently active users or processes. Consider enabling this feature in sandboxes or scratch orgs shared by multiple users for functional testing or used by continuous integration processes. 1. Deploy Apex Using Change Sets Use change sets to deploy Apex classes and triggers between connected organizations, for example, from a sandbox org to your production org. 2. Deploy Apex Using Salesforce Extensions for Visual Studio Code and Code Builder Salesforce Extensions for VS Code and Code Builder are powered by Salesforce CLI and the Salesforce APIs. 3. Deploy Apex Using Metadata API Use Metadata API to deploy customization information, such as custom object definitions for your org. 4. Deploy Apex Using Tooling API Use Tooling API to deploy Apex classes or Apex triggers. Because Tooling API allows you to change just one element within a complex type, it is easy to deploy using Tooling API. 5. Deploy Apex Using DevOps Center Salesforce DevOps Center provides an improved experience around change and release management. Build a pipeline when you configure DevOps Center and use the pipeline to promote work items through the release lifecycle from development to production.

### Deploy Apex Using Change Sets

Use change sets to deploy Apex classes and triggers between connected organizations, for example, from a sandbox org to your production org. You can create an outbound change set in the Salesforce user interface and add the Apex components that you want to upload and deploy to the target organization. Sandboxes: Staging Environments for Customizing and Testing : Change Sets

### Deploy Apex Using Salesforce Extensions for Visual Studio Code and Code Builder

Salesforce Extensions for VS Code and Code Builder are powered by Salesforce CLI and the Salesforce APIs. Salesforce Extensions for Visual Studio Code support different deployment options based on your role and needs as a customer, system integrator, or independent software vendor (ISV) partner. Salesforce DX supports Org Development and Package Development models to authorize, create, and deploy code in your project. For information on how to deploy to a Salesforce org with Visual Studio Code, see Salesforce Development Models . Salesforce Code Builder is a web-based integrated development environment that has all the power and flexibility of Visual Studio Code in your web browser. For information on how to connect an org to your Code Builder environment and deploy your code, see Code Builder : Quick Start . Salesforce Extensions for Visual Studio Code : Deploy and Retrieve Code Salesforce DX Developer Guide : Develop Against Any Org Salesforce CLI Command Reference : project deploy start

### Deploy Apex Using Metadata API

Use Metadata API to deploy customization information, such as custom object definitions for your org. To deploy custom metadata, use the `Metadata.Operations.enqueueDeployment()` method to asynchronously deploy metadata to the current org. For more information, see Operations Class . If a single deployment has over 2,000 Apex classes, ApexCodeCoverage objects for the deployed classes are deleted even if the deployment fails or is rolled back. ApexCodeCoverageAggregate objects aren’t affected. Metadata API Developer Guide : deploy() Using Salesforce Features with Apex : Metadata

### Deploy Apex Using Tooling API

Use Tooling API to deploy Apex classes or Apex triggers. Because Tooling API allows you to change just one element within a complex type, it is easy to deploy using Tooling API. Use ContainerAsyncRequest to compile and deploy the changes with ApexTriggerMember, ApexComponentMember, and ApexPageMember. Tooling API : When to Use Tooling API

### Deploy Apex Using DevOps Center

Salesforce DevOps Center provides an improved experience around change and release management. Build a pipeline when you configure DevOps Center and use the pipeline to promote work items through the release lifecycle from development to production. For information, see Manage and Release Changes Easily and Collaboratively with DevOps Center : Promote Work Items Through Your Pipeline .

## Apex in Managed Packages

Learn how to develop, distribute, and use managed Apex. Apex in managed packages can behave differently than Apex in unmanaged packages or Apex deployed directly to an org. Managed package developers and subscribers must understand these differences so that they can safely evolve their packages and integrations. Managed Package Types Salesforce supports the creation and distribution of Apex through different types of packages. Understand the distinctions between package types, and recognize that Apex behavior can vary across them. Develop and Distribute Apex for Managed Packages As an independent software vendor (ISV) or Salesforce partner, you can distribute Apex code to customer orgs by using managed packages. For first-generation managed packages (1GP) and migrated second-generation managed packages (2GP), use versioning to evolve components of your managed package gracefully without breaking existing customer integrations. Understand how global Apex in managed packages behaves and learn how to develop global Apex in managed packages specifically for agents. Use Apex Referenced by Managed Packages Learn how to use managed Apex effectively as a managed package subscriber. Safely Upgrade Packages from Developer and Subscriber Perspectives Learn how to upgrade a managed package safely through this extended example. See the actions that package developers and subscribers can take to ensure a smooth transition and safeguard the backwards compatibility of existing integrations.

### Managed Package Types

Salesforce supports the creation and distribution of Apex through different types of packages. Understand the distinctions between package types, and recognize that Apex behavior can vary across them. A package is a container that can be as small as an individual component or as large as a set of related apps. After creating a package, you can distribute it to other Salesforce users and orgs, including orgs outside of your company. Developers can create unmanaged packages and managed packages. These package types have different use cases and characteristics. Unmanaged packages are best suited for one-time drops of apps that require customization after installation. After the components are installed from an unmanaged package, the components can be edited in the org that they’re installed in. The developer who created and uploaded the unmanaged package has no control over the installed components, and can’t change or upgrade them. Managed packages are ideal for commercial distribution through the AppExchange . Unlike unmanaged packages, package developers can upgrade managed packages and push these changes to subscriber orgs. Preserving the backwards-compatibility of managed packages is the package developer’s responsibility. However, Salesforce provides significant guardrails and tools that help package developers safely upgrade managed packages while minimizing the risk of introducing changes that may break existing code. Salesforce supports first-generation managed packages (1GP) and second-generation managed packages (2GP) . Salesforce also supports the conversion and migration of 1GP managed packages to 2GP managed packages . For new apps, we recommend using 2GP managed packages, as they allow for source-driven development and flexible versioning. See Why Switch to Second-Generation Managed Packaging and Comparison of First- and Second-Generation Managed Packages . Apex classes and triggers from 1GP, 2GP, and migrated 2GP managed packages can behave differently depending on the managed package type. If a section of the Apex Developer Guide or the Apex Reference Guide doesn’t specify whether a behavior applies to only 1GP or 2GP, then it applies to all managed package types. ISVforce Guide First-Generation Managed Packaging Developer Guide : Move to 2GP Second-Generation Managed Packaging Developer Guide : Components Available in Second-Generation Managed Packages–Apex Class

### Develop and Distribute Apex for Managed Packages

As an independent software vendor (ISV) or Salesforce partner, you can distribute Apex code to customer orgs by using managed packages. For first-generation managed packages (1GP) and migrated second-generation managed packages (2GP), use versioning to evolve components of your managed package gracefully without breaking existing customer integrations. Understand how global Apex in managed packages behaves and learn how to develop global Apex in managed packages specifically for agents. As you develop managed Apex, keep these points in mind. The code contained in an Apex class, trigger, or Visualforce component that’s part of a managed package is obfuscated. You generally can’t view this code in an installing org. The only exceptions are methods declared as `global` . You can view global method signatures in an installing org. In addition, license management organization users with the View and Debug Managed Apex permission can view their packages’ obfuscated Apex classes when logged in to subscriber orgs via the Subscriber Support Console. 1GP managed packages each have a unique namespace. 2GP managed packages can have the same namespace as other 2GP managed packages. However, you can’t associate a single 2GP managed package with more than one namespace. The namespace is prepended to your class’s names, methods, variables, and so on, which helps prevent duplicate names in a subscriber’s org. You can use the `@NamespaceAccessible` on page 112 annotation to make public Apex in a 2GP managed package available to other 2GP managed packages that use the same namespace. In a single transaction, you can reference only 10 unique namespaces. For example, suppose that you have an object that executes a class in a managed package when the object is updated. Then that class updates a second object, which in turn executes a different class in a different package. Even though the first package didn’t access the second package directly, the access occurs in the same transaction. It’s therefore included in the number of namespaces accessed in a single transaction. You can use the `@Deprecated` on page 94 annotation to identify methods, classes, exceptions, enums, interfaces, and variables that can no longer be referenced in subsequent releases of the managed package in which they reside. This annotation is useful when you’re refactoring code in managed packages as the requirements evolve. See Deprecate Apex in Managed Packages on page 769. For 1GP and migrated 2GP managed packages, you can write test methods that change the package version context to a different package version by using the `System.runAs()` method. See Testing Behavior in Package Versions on page 770. You can’t add a method to a global interface or an abstract method to a global class after you upload that interface or class in a Managed - Released package version. If the class in the Managed - Released package is virtual, the method that you can add to it must also be virtual and must have an implementation. If the class in the Managed - Release package extends another class, you can’t remove the existing class’s contract. See Best Practices for Using Global Apex in Managed Packages on page 772. Salesforce blocks managed package session IDs from authenticating anonymous Apex via Tooling API or SOAP API. Managed packages can’t use `UserInfo.getSessionId()` to obtain a session ID and then use the session ID to execute anonymous Apex. This update is available to package subscribers starting in Summer ’26 and is enforced in Summer ’27. See Block Execute Anonymous from Managed Packages (Release Update) . Instead, we recommend that managed packages interact with subscriber org code through standard mechanisms, such as a shared `global` interface and `Type.forName()` . If a `ConnectApi` class has a dependency on Chatter, the code can be compiled and installed in orgs that don’t have Chatter enabled. However, if Chatter isn’t enabled, the code throws an error at run time. See Packaging `ConnectApi` Classes on page 462. Apex Versioning in Managed Packages A managed package component can exhibit different behavior in different package versions. By versioning managed Apex, you can add and refine components in the managed package, while maintaining backwards compatibility for existing subscribers. Version Apex Code Behavior Package developers can use conditional logic in Apex classes and triggers to exhibit different behavior for different versions. With this conditional logic, you can support existing behavior in classes and triggers in previous package versions while evolving the code. Apex Code Items That Aren’t Versioned Some Apex items in managed packages can’t be versioned. The changes that you make to these items are reflected across all package versions. Additionally, there are limitations to the changes that you can make to some of these items when they are used in Apex code in managed packages. Deprecate Managed Apex Use the `@Deprecated` annotation to specify Apex identifiers that can subscribers can no longer reference in subsequent releases of the managed package. Deprecation is useful when you’re refactoring code in managed packages as the requirements evolve. Testing Versioned Behavior in Apex Code When you change the behavior in an Apex class or trigger for different package versions, it’s important to test that your code runs as expected in the different package versions. You can write test methods that change the package version context to a different package version by using the `System.runAs` method. You can only use `System.runAs` in a test method. Best Practices for Using Global Apex in Managed Packages As an independent software vendor (ISV) developer, understand when and how to use `global` Apex in managed packages. Learn design patterns that maximize flexibility and comply with the strict manageability rules applied to `global` Apex after your managed package’s release. By following these best practices, you can improve the stability and maintainability of your API. Design Managed Apex for Agentforce As an independent software vendor (ISV) developer, you can build custom agent actions using Apex and distribute them in managed packages. To ensure that subscriber admins can declaratively configure your Apex agent actions and that Agentforce can invoke the actions at run time, follow these requirements and recommendations.

#### Apex Versioning in Managed Packages

A managed package component can exhibit different behavior in different package versions. By versioning managed Apex, you can add and refine components in the managed package, while maintaining backwards compatibility for existing subscribers. A package version is a number that identifies the set of components uploaded in a package. The version number has the format `majorNumber.minorNumber.patchNumber` (for example, 2.1.3). The major and minor numbers increase to a chosen value during every major release. The `patchNumber` is generated and updated only for a patch release. Unmanaged packages aren’t upgradeable, so each package version is simply a set of components for distribution. A package version has more significance for managed packages. With managed packages, you can specify different component behavior based on the package version. This practice allows you to evolve the components in your managed package without breaking existing subscriber integrations. When an existing subscriber installs a new package version, there’s still only one instance of each component in the package. However, the components can emulate older versions. For example, a subscriber can use a managed package that contains an Apex class. If the publisher decides to deprecate a method in the Apex class and release a new package version, the subscriber still sees only one instance of the Apex class after installing the new version. However, this Apex class can still emulate the previous version for any code that references the deprecated method in the older version. Version Apex Code Behavior Apex Code Items That Aren’t Versioned Deprecate Managed Apex Testing Versioned Behavior in Apex Code Set Package Versions for Apex Classes and Triggers (for package subscribers)

#### Version Apex Code Behavior

Package developers can use conditional logic in Apex classes and triggers to exhibit different behavior for different versions. With this conditional logic, you can support existing behavior in classes and triggers in previous package versions while evolving the code. Starting in Summer ’25, package subscribers can use Version Settings to specify the version of a migrated second-generation managed package (2GP) that an Apex class depends on. This functionality is already available to first-generation managed packages (1GP), but isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings in Migrated Second-Generation Managed Packages (2GP) . When subscribers install multiple versions of your package and write code that references Apex classes or triggers in your package, they must select the version that they’re referencing. Within the Apex code that is being referenced in your package, you can conditionally execute different code paths based on the version setting of the calling Apex code that is making the reference. The package version setting of the calling code can be determined within the package code by calling the `System.requestVersion` method. In this way, package developers can determine the request context and specify different behavior for different versions of the package. This example uses the `System.requestVersion` method and instantiates the `System.Version` class to define different behaviors in an Apex trigger for different package versions.

```apex
trigger oppValidation on Opportunity (before insert, before update) {
```

```apex
for (Opportunity opp : Trigger.new){
```

```apex
// Add a new validation to the package
// Applies to versions of the managed package greater than 1.0
if (System.requestVersion().compareTo(new Version(1,0)) > 0) {
```

```apex
if (opp.Probability >= 50 && opp.Description == null) {
opp.addError('All deals over 50% require a description');
}
}
```

```apex
// Validation applies to all versions of the managed package.
if (opp.IsWon == true && opp.LeadSource == null) {
opp.addError('A lead source must be provided for all Closed Won deals');
}
}
}
```

For a full list of methods that work with package versions, see Version Class and the `System.requestVersion` method in System Class . The request context persists if a class in an installed package invokes a method of another class in the package. For example, imagine that a subscriber installs a GeoReports package that contains CountryUtil and ContinentUtil classes. The subscriber creates a GeoReportsEx class and associates it with version 2.3 of the GeoReports package. If GeoReportsEx invokes a ContinentUtil method that internally invokes a CountryUtil method, the request context propagates from ContinentUtil to CountryUtil. Therefore, the `System.requestVersion` method in CountryUtil returns version 2.3 of the GeoReports package. Set Package Versions for Apex Classes and Triggers (for package subscribers) Safely Upgrade Packages from Developer and Subscriber Perspectives

#### Apex Code Items That Aren’t Versioned

Some Apex items in managed packages can’t be versioned. The changes that you make to these items are reflected across all package versions. Additionally, there are limitations to the changes that you can make to some of these items when they are used in Apex code in managed packages. As a package developer, you can add or remove these items from Apex in manage packages. `@Future` `@IsTest`

```apex
•
with sharing
```

```apex
•
without sharing
```

```apex
•
transient
```

You can make limited changes to these Apex items in managed packages. `private` —can be changed to `global` `protected` —can be changed to `global` `public` —can be changed to `global` `abstract` —can be changed to `virtual` but can’t be removed `final` —can be removed but can’t be added You can’t remove or change these Apex items in managed packages. `global` `virtual` You can add the `webservice` keyword, but once it has been added, it can’t be removed. You can’t deprecate `webservice` methods or variables in managed package code. If a package upgrade includes an explicit global constructor for a released global class that previously only had an implicit constructor, then the new, explicit constructor will be called from the subscriber. Also, you can’t reduce the access modifier on the default constructor on a released global class in a package. See Best Practices for Using Global Apex in Managed Packages on page 772.

#### Deprecate Managed Apex

Use the `@Deprecated` annotation to specify Apex identifiers that can subscribers can no longer reference in subsequent releases of the managed package. Deprecation is useful when you’re refactoring code in managed packages as the requirements evolve. Apex identifiers include methods, classes, exceptions, enums, interfaces, and variables. After you upload another package version as Managed — Released, new subscribers that install the latest package version can’t see the deprecated identifiers. However, the identifiers still function for existing subscribers and API integrations. As the package developer, you can still reference deprecated identifiers internally. You can’t use the `@Deprecated` annotation in Apex classes or triggers in unmanaged packages. You can use Managed — Beta package versions for evaluation and feedback with a pilot set of users in different Salesforce orgs. If you deprecate an Apex identifier, and then upload a version of the package as Managed — Beta, subscribers that install the package version still see the deprecated identifier in that package version. If the package developer then uploads a Managed — Released package version, subscribers will no longer see the deprecated identifier in the package version after they install it. Best Practices for Using Global Apex in Managed Packages

#### Testing Versioned Behavior in Apex Code

When you change the behavior in an Apex class or trigger for different package versions, it’s important to test that your code runs as expected in the different package versions. You can write test methods that change the package version context to a different package version by using the `System.runAs` method. You can only use `System.runAs` in a test method. This sample shows a trigger with different behavior for different package versions. For more information about defining different behavior for package versions, see Version Apex Behavior on page 768.

```apex
trigger oppValidation on Opportunity (before insert, before update) {
```

```apex
for (Opportunity opp : Trigger.new){
```

```apex
// Add a new validation to the package
// Applies to versions of the managed package greater than 1.0
if (System.requestVersion().compareTo(new Version(1,0)) > 0) {
```

```apex
if (opp.Probability >= 50 && opp.Description == null) {
opp.addError('All deals over 50% require a description');
}
}
```

```apex
// Validation applies to all versions of the managed package.
if (opp.IsWon == true && opp.LeadSource == null) {
opp.addError('A lead source must be provided for all Closed Won deals');
}
}
}
```

The following test class uses the `runAs` method to verify the trigger’s behavior with and without a specific version:

```apex
@IsTest
private class OppTriggerTests{
```

```apex
static testMethod void testOppValidation(){
```

```apex
// Set up 50% opportunity with no description
Opportunity opp = new Opportunity();
opp.Name = 'Test Job';
opp.Probability = 50;
opp.StageName = 'Prospect';
opp.CloseDate = System.today();
```

```apex
// Test running as latest package version
try{
```

```apex
insert opp;
}
catch(DMLException e){
Assert.isTrue(
e.getMessage().contains(
```

```apex
'All deals over 50% require a description'),
e.getMessage());
}
```

```apex
// Run test as managed package version 1.0
System.runAs(new Version(1,0)){
```

```apex
try{
```

```apex
insert opp;
}
catch(DMLException e){
Assert.isFalse(false, e.getMessage());
}
}
```

```apex
// Set up a closed won opportunity with no lead source
opp = new Opportunity();
opp.Name = 'Test Job';
opp.Probability = 50;
opp.StageName = 'Prospect';
opp.CloseDate = System.today();
opp.StageName = 'Closed Won';
```

```apex
// Test running as latest package version
try{
```

```apex
insert opp;
}
catch(DMLException e){
Assert.isTrue(
e.getMessage().contains(
```

```apex
'A lead source must be provided for all Closed Won deals'),
e.getMessage());
}
```

```apex
// Run test as managed package version 1.0
System.runAs(new Version(1,0)){
```

```apex
try{
```

```apex
insert opp;
}
catch(DMLException e){
Assert.isTrue(
e.getMessage().contains(
```

```apex
'A lead source must be provided for all Closed Won deals'),
e.getMessage());
}
}
}
}
```

#### Best Practices for Using Global Apex in Managed Packages

As an independent software vendor (ISV) developer, understand when and how to use `global` Apex in managed packages. Learn design patterns that maximize flexibility and comply with the strict manageability rules applied to `global` Apex after your managed package’s release. By following these best practices, you can improve the stability and maintainability of your API. We recommend using the `global` access modifier only when necessary. The API shape of `global` Apex, such as the name, parameters, and return type of `global` methods, is subject to strict manageability rules. You generally can’t change the API shape of `global` Apex after it’s released in a managed package. The `global` modifier on page 69 provides the widest level of access. It makes your Apex classes, methods, interfaces, and variables accessible and callable from any Apex code outside of your package namespace, including code written by subscribers or other installed packages. A key benefit of Apex in managed packages is Intellectual Property (IP) protection. Although `global` Apex signatures, such as `global` class and method names, parameters, and return types, are visible so subscribers can use your API, the underlying implementation logic within your methods is encapsulated and hidden. This allows you to provide powerful functionality without exposing your proprietary source code. Use `global` Apex when: Exposing a global API. You intend for subscribers to use your package’s core services by directly calling your Apex methods or instantiating your classes from their own Apex code, such as from their triggers, batch classes, or other custom logic. Providing extensibility points. You’re designing `global` interfaces or `global` `abstract` base classes that subscribers must implement or extend to customize or enhance specific behaviors within your app. Creating web service endpoints. You’re exposing Apex classes to handle incoming REST API requests or SOAP web service calls from external systems. These endpoint classes and their methods must be declared `global` to receive calls from external systems. Avoid `global` Apex for: Internal package functionality, meaning any Apex code, such as business logic, helper classes, or utility methods, that’s designed exclusively for use within your managed packages. For these internal components, access modifiers on page 69 such as `public` , `protected` , or `private` avoid the manageability constraints of `global` . You can even combine the `public` access modifier with the `@NamespaceAccessible` annotation to allow access throughout your package namespace. Controller methods, or methods within your package that are called by your Lightning web components (LWC) and aren’t used by your subscribers directly. Make these methods `public` and annotate them with `@AuraEnabled` on page 94. Method signatures with external `global` types. Avoid using `global` Apex types from another managed package as parameters or return types in your own `global` methods. This practice locks your package into a rigid dependency. If the other package later changes or deprecates the types that your `global` signature relies on, it can become difficult or impossible for your package to adopt newer versions of the dependency package. The decision to use `global` is significant because it subjects your code to strict manageability rules after your package is released. Manageability rules protect subscribers against package upgrades that break existing functionality. These rules make your initial `global` Apex design critical, as changes in later versions are heavily restricted. After your managed package is released, these restrictions apply to the `global` Apex in the package. You can’t delete a `global` class, interface, method, variable, or enum. You can’t change the name of a `global` class, interface, method, variable, or enum. You can’t change the access modifier of a `global` class, interface, method, variable, or enum from `global` to another access modifier. You can’t change a `global` method’s signature, including the order, number, and types of parameters, as well as the method’s return type. You can add new methods that overload existing `global` methods. You can’t change the value of a `global` `static` `final` variable. You can’t change the data type of a `global` variable to an incompatible one. You can’t change most annotations or modifiers on `global` members. For example, you can’t add or remove the `@AuraEnabled` annotation or any Apex REST annotation on page 329 from a `global` method. Similarly, you can’t add or remove the `static` or `final` keyword from a `global` method. You can’t remove a zero-argument constructor from a `global` class. This restriction applies both to explicitly deleting a constructor you wrote, and to implicitly removing the default constructor by adding a new constructor that requires arguments. You can’t remove a `global` interface from a `global` class. You can’t extend a `global` interface with a new interface. You can’t change a `global` class to an interface, or vice versa. You can’t add `abstract` methods to `global` interfaces or `abstract` classes. You can’t add `final` methods to `global` `virtual` or `global` `abstract` classes. You can’t remove or reorder `global` enum values, although you can add new enum values. You can't add, remove or change that a global class extends another global class. Given the strict manageability rules, a thoughtful design of your package’s global API is crucial. These best practices for defining and managing `global` Apex promote flexibility, reduce maintenance, and help create a stable, evolvable API. When designing `global` Apex, expose the fewest `global` members possible. Every `global` part of your package is a contract with your subscribers. Fewer `global` members mean fewer restrictions and more freedom for you to update your package later. Before making something `global` , consider these questions. Is it truly necessary? Can you use `public` instead? For example, use `public` for access only by other Apex within the same package, or `public` and `@NamespaceAccessible` for access only by other Apex in packages that have the same namespace. Are there other designs? Can you achieve the same result without making methods or classes `global` ? Make your `global` classes and methods act only as thin entry points. Place any business logic or complex processes in `public` classes and methods within your package. The `global` method then calls these `public` methods. Delegating logic to `public` classes and methods promotes: Flexibility. You can freely add new features or completely change the internal public implementation of your service in future versions without altering the `global` method signature. Maintainability. Fixing bugs and refactoring your existing business logic is now safer and lower-risk because the work is decoupled from the stable global API contract that your subscribers depend on. Testability. Your `public` business logic classes can be unit tested thoroughly and independently of their `global` entry point. In this example, `MyPackageApi.greetUsers` is the stable `global` contract. The actual work happens in `createGreetings` , which is `public` and can be easily modified in future package versions as long as the `greetUsers` signature in `MyPackageApi` remains unchanged. For example, the ISV developer can later optimize `createGreetings` or add new helper methods without violating `global` Apex manageability rules.

```apex
// --- ISV's Managed Package Code ---
// Global Entry Point
global with sharing class MyPackageApi {
```

```apex
// Note: This is a simplified example using a primitive data type. For a
// more flexible and future-proof design, we recommend using parameter
// objects for global method signatures, as explained in the next section.
global static List<String> greetUsers(List<String> userNames) {
```

```apex
// Delegate directly to a public class to do the actual work.
// GreetingService is a 'public' class within your package.
GreetingService service = new GreetingService();
```

```apex
return service.createGreetings(userNames);
}
}
```

```apex
// Public Class (Lives inside your package)
// This class can be updated easily in future package versions.
public with sharing class GreetingService {
```

```apex
// This public method contains all the business logic to process a list of names.
```

```apex
public List<String> createGreetings(List<String> names) {
List<String> greetings = new List<String>();
// Input validation and error handling, e.g. Return an empty list if input is
null or empty.
// Process each name in the list.
for (String name : names) {
greetings.add('Hello, ' + name + '!');
}
return greetings;
}
```

```apex
// If needed, you can freely add private methods here
private void someHelperMethod() {
```

```apex
// ...
}
}
```

```apex
// --- Subscriber Code ---
// Subscriber creates a list and calls the global method
List<String> welcomeMessages = TheIsvNamespace.MyPackageApi.greetUsers(
```

```apex
new List<String>{'Jane Doe', 'Rose Gonzalez'});
// The output is a corresponding list of greetings.
// welcomeMessages will be: ['Hello, Jane Doe!', 'Hello, Rose Gonzalez!']
```

Using primitive data types, such as String or ID, directly in `global` method signatures creates a rigid contract that you can’t change. To avoid this restriction, we recommend using custom `global` Apex classes as parameter objects for both inputs and outputs. This pattern provides a stable API contract that’s evolvable, safer, and readable for subscribers. Benefits of using parameter objects include: Evolvability. You can add new parameters to your API by adding new properties to your input or output classes. The `global` method signature itself never changes, which avoids breaking changes. Safety and discoverability. Subscribers get compile-time safety and code completion while constructing the request object, which reduces the risk of run-time errors from typos or incorrect data types. Readability. Grouping related parameters into a dedicated class makes your method signature clean and its purpose clear. For example, `getCoordinates(Address` `location)` is easier for your subscribers to understand and use than `getCoordinates(` `String` `street,` `String` `city,` `String` `state,` `String` `zip,` `...).` Despite the benefits of using parameter objects, consider these costs. Increased upfront complexity. This pattern requires more initial code, such as multiple classes, and can be excessive for simple actions that aren’t expected to change. Expanded global surface area. Although the primary method signature remains stable, each global property added to the input object becomes a new, permanent part of your package’s API. In this example, the `GeocodingService.getCoordinates` method is the global contract. It uses the custom `global` `AddressRequest` class as its input, and the custom `global` `GeolocationResponse` class as its output.

```apex
// --- ISV's Managed Package Code ---
// The global entry point class contains the global method and input & output wrapper
```

```apex
inner classes.
global with sharing class GeocodingService {
```

```apex
// 1. The Global Method
// The signature is clean, using the inner classes for its input parameter and
return type.
```

```apex
global static GeolocationResponse getCoordinates(AddressRequest location) {
```

```apex
// --- Internal logic to process the request ---
// We recommend calling a public method to delegate all business logic. Skipping
this for brevity in this example
// This could involve callouts to an external geocoding service.
// For this example, we will return mock data.
if (location.postalCode == '94105') {
```

```apex
return new GeolocationResponse(37.7749, -122.4194);
} else {
return new GeolocationResponse(0, 0);
}
}
```

```apex
// 2. The Input Parameter Object (as an inner class)
// A simple inner class with global properties to bundle input parameters.
global with sharing class AddressRequest {
```

```apex
global String street;
global String city;
global String state;
global String postalCode;
```

```apex
// A constructor helps ensure required fields are provided.
global AddressRequest(String street, String city, String state, String
postalCode) {
```

```apex
this.street = street;
this.city = city;
this.state = state;
this.postalCode = postalCode;
}
```

```apex
}
```

```apex
// 3. The Output Parameter Object (as an inner class)
// A simple inner class to provide a structured result.
global with sharing class GeolocationResponse {
```

```apex
// Using 'private set' makes these properties read-only for subscribers.
// @AuraEnabled makes these properties visible to Lightning web components,
if necessary.
```

```apex
@AuraEnabled global Decimal latitude { get; private set; }
@AuraEnabled global Decimal longitude { get; private set; }
```

```apex
// This constructor is public, not global, so subscribers can't create their
own response objects.
```

```apex
public GeolocationResponse(Decimal lat, Decimal lon) {
```

```apex
this.latitude = lat;
this.longitude = lon;
}
}
}
```

```apex
// --- Subscriber Code ---
// The subscriber's experience is clean and type-safe.
// 1. Create an instance of the input object, referencing it via the outer class.
TheIsvNamespace.GeocodingService.AddressRequest sfAddress = new
TheIsvNamespace.GeocodingService.AddressRequest(
```

```apex
'415 Mission St',
'San Francisco',
'CA',
'94105'
);
```

```apex
// 2. Call the global method with the single parameter object.
TheIsvNamespace.GeocodingService.GeolocationResponse coordinates =
TheIsvNamespace.GeocodingService.getCoordinates(sfAddress);
```

```apex
// 3. Process the structured, strongly-typed result.
// For this example we will just log the results.
```

```apex
System.debug('Coordinates found: ' + coordinates.latitude + ', ' +
coordinates.longitude);
```

For scenarios where the inputs aren’t known at compile time, you can use a Map for your method’s input parameters. An example signature with this pattern is `global` `static` `GeolocationResponse` `processUnstructuredRequest(Map<` `String` `,` `Object` `>` `inputs)` . Use this pattern with caution. This pattern isn’t recommended for return types. Accepting a Map allows the subscriber to construct the Map and populate the keys and values themselves. Although this pattern provides maximum flexibility, returning a Map forces the subscriber to guess key names and data types, which leads to fragile code. Additionally, using a Map for inputs sacrifices compile-time safety and discoverability. Subscribers must rely entirely on documentation to know the required keys and their data types. Simple typos in map keys can result in hard-to-debug run-time errors instead of compile-time errors. The standard Callable interface uses the Map pattern through its `call(` `String` `action,` `Map<` `String` `,` `Object` `>` `args)` method. However, this method returns a generic Object, which forces subscribers to cast the response and risk run-time errors. It creates a single, generic entry point that can perform many different functions based on the action string. For a single-purpose action that accepts unstructured inputs, a custom method such as `processUnstructuredRequest` is clearer and safer. Instead of using the Map pattern, prefer strongly-typed parameter objects as shown in the Use Parameter Objects for Global Method Inputs and Return Types on page 774 section. Reserve the Map pattern for advanced use cases where the inputs are truly unpredictable and its risks are acceptable, but always return a strongly-typed object. The facade pattern is effective if you want to define a capability and then provide one or more ways to use it. In this pattern, a global interface defines the capability, and the public classes that implement the interface define how to use the capability. A global factory method gives the subscriber the specific implementation of the interface. Benefits of using the facade pattern include: You can change the public class that does the work as long as it still follows the global interface rules. You can offer new implementations of the interface later. In this example, `Notifier` is the `global` contract, and the `public` class `EmailNotifierImpl` does the work. Because the factory class is `global` but the classes that implement the `Notifier` interface are `public` , the ISV developer can later change or add to these classes. For example, if the ISV developer later wants to offer an SMS notifier, they can add `getSmsNotifier()` to the factory class and implement a new `public` `SmsNotifierImpl` class.

```apex
// --- ISV's Managed Package Code ---
// Global Interface - Defines a capability
global interface Notifier {
```

```apex
global void send(String message);
}
```

```apex
// Global Factory Class - Provides instances
global with sharing class NotificationFactory {
```

```apex
global static Notifier getEmailNotifier() {
```

```apex
return new EmailNotifierImpl(); // EmailNotifierImpl is public
}
}
```

```apex
// Public Implementation (Lives inside your package)
public with sharing class EmailNotifierImpl implements Notifier {
```

```apex
public void send(String message) {
```

```apex
// Logic to send an email (simplified here)
System.debug('Emailing: ' + message);
}
}
```

```apex
// --- Subscriber Code ---
// Subscriber gets an instance of a Notifier
Notifier myEmailer = NotificationFactory.getEmailNotifier();
```

```apex
// Subscriber uses the interface method
myEmailer.send('Welcome to our service!'); // Outputs: Emailing: Welcome to our service!
```

Even though deprecating Apex on page 769 only affects future versions of your package, phasing out a `global` Apex member requires careful planning and clear communication to prevent subscriber disruption. Here’s some recommendations for effectively retiring a `global` Apex member. Communicate early and clearly. Inform subscribers well in advance—ideally, multiple release cycles—of any deprecation. Explain reasons, timelines, and migration paths. Update the documentation, and share it prominently. Provide alternatives. Release well-documented and robust alternatives before or concurrent with the deprecation announcement. Implement soft deprecation with non-breaking warnings. Add the `@Deprecated` annotation to the `global` member. This annotation generates compile-time warnings in developer tools, but doesn’t alter run-time behavior. Consider run-time logging when the deprecated member is invoked, guiding subscribers to the new alternative. You can’t remove the `@Deprecated` annotation to undeprecate something in Apex after you’ve released a package version where that item in Apex is deprecated. You also can’t add new `global` access modifiers to a `@Deprecated` type. Enforce non-operation with exceptions. Change the code to throw an informative exception, such as `FeatureDeprecatedException(` `'` `Method` `X` `is` `retired.` `Use` `Method` `Y.` `')` . This breaking change at run time stops the old logic from running and forces attention to the deprecation. However, any breaking change requires extensive prior communication. Retire code for obsolete `global` Apex. After ample time and communication, confirm that subscribers are no longer using the deprecated `global` member. Then minimize the member’s internal code. Although the `global` signature must remain, its logic can become non-operational (no-op), return a safe default, or throw a specific `Feature` `Retired` exception. Implementing these changes reduces the risk and effort of maintaining the old code. Always thoroughly test changes related to deprecating `global` Apex, including testing your package’s behavior if a subscriber attempts to call the deprecated member. The goal is a graceful transition for your subscribers. Access Modifiers Apex Class Definition Exposing Apex Classes as REST Web Services Exposing Apex Methods as SOAP Web Services NamespaceAccessible Annotation Deprecate Managed Apex Apex Reference Guide : Callable Interface Second-Generation Managed Packaging Developer Guide : Components Available in Second-Generation Managed Packages–Apex Class

#### Design Managed Apex for Agentforce

As an independent software vendor (ISV) developer, you can build custom agent actions using Apex and distribute them in managed packages. To ensure that subscriber admins can declaratively configure your Apex agent actions and that Agentforce can invoke the actions at run time, follow these requirements and recommendations. For Agentforce to use Apex agent actions in managed packages, these Apex members must have the `global` access modifier on page 69. The Apex class containing the `@InvocableMethod` on page 96 that defines the agent action. The input wrapper class that defines the parameters an admin can configure for the action, and the output wrapper class that defines the structured result returned to Agentforce. All `@InvocableVariable` on page 102 members within these input and output wrapper classes. Any custom Apex data types used as properties in your wrapper classes. If any of these Apex members aren’t `global` , then the Apex agent action can’t be invoked by Agentforce at run time. These Apex members must be `global` because Agentforce agents currently can’t be packaged directly, and therefore can’t have a namespace. By definition, this means that Apex agent actions don’t have access to non- `global` Apex, such as `public` Apex, that’s part of a managed package and does have a namespace. Importantly, managed `global` Apex is subject to stricter manageability rules than managed non- `global` Apex. See the Global Apex Manageability Rules on page 772 section of Best Practices for Using Global Apex in Managed Packages on page 772. Although `global` Apex is required for any direct entry point to an agent action, delegate any business logic or heavy lifting to `public` classes and methods. See the Delegate from Thin Global Entry Points on page 773 section of Best Practices for Using Global Apex in Managed Packages on page 772. To define an Apex agent action, use the `@InvocableMethod` on page 96 annotation and follow these requirements. Your Apex method must be `global` `static` . Your Apex method must be annotated with `@InvocableMethod` `(label='` `Your` `Action` `Name` `'` `description='` `Clear,` `concise` `description` `of` `what` `the` `action` `does` `'` `category='` `Your` `ISV` `App` `Name` `')` . Use clear and descriptive `label` and `description` modifiers. The Agentforce reasoning engine uses them to determine when to invoke the action. Subscriber admins configuring Agentforce also use them to help decide which agent topics to add the action to. Use the `category` modifier to help organize actions. We recommend using your ISV app name. Only one method in a class can have the `@InvocableMethod` annotation. Create a separate `global` Apex class for each agent action in your managed package. In addition to the requirements of using `global` Apex and the `@InvocableMethod` annotation, we also recommend using custom `global` classes to structure input and output parameters. By using parameter objects, you avoid changing the `global` method signature when you modify the parameters of the agent action. To learn how to use this pattern, see the Use Parameter Objects for Global Method Inputs and Return Types on page 774 section of Best Practices for Using Global Apex in Managed Packages on page 772. Then review these targeted guidelines to implement Apex agent actions using this pattern. Because you can’t change managed `global` method signatures, make signatures flexible. Define `global` inner Apex classes to serve as containers for input and output parameters. These classes can be in the same top-level class as the invocable method. Annotate both input and output classes with `@JsonAccess(serializable=` `'always'` `deserializable=` `'always'` `)` . The @JsonAccess annotation on page 111 governs the serialization and deserialization of managed Apex. Because Agentforce serializes and deserializes complex Apex types from an unmanaged context at run time, both `@JsonAccess` parameters must be set to `'always'` . Within these input and output classes, declare `global` member variables annotated with `@InvocableVariable(label=` `'` `User-Friendly` `Name` `'` `description='` `Description` `of` `this` `parameter` `'` `required=true/false)` . Use clear and descriptive `label` and `description` modifiers, so that subscribers can configure the inputs declaratively, and Agentforce can understand the output. Set the `required` modifier as `true` or `false` to specify whether the input is required for the agent action to run. This modifier also helps subscriber admins configure your actions. Define the invocable method to accept a `List` of its input class type, for example `List<MyInputAction>` `requests` . Define the invocable method to return a `List` of its output class type, for example `List<MyOutputAction>` `results` . In this example, the `getCoordinates` method is defined as an `@InvocableMethod` so it can be invoked by Agentforce. The method accepts a list of `GeocodingRequest` objects and returns a corresponding list of `GeocodingResponse` objects. The input and output wrapper classes are both annotated with `@JsonAccess(serializable=` `'always'` `deserializable=` `'always'` `)` so Agentforce can serialize and deserialize the objects from an unmanaged context. The properties of both wrapper classes are defined as `@InvocableVariable` so an admin can configure them declaratively. The `label` and `description` modifiers in both `@InvocableMethod` and `@InvocableVariable` are important because they help the Agentforce reasoning engine to understand how to use the action.

```apex
// --- ISV's Managed Package Code ---
// --- 1. The Global Entrypoint Class ---
// This class contains the @InvocableMethod and the input/output wrapper classes.
global with sharing class GeocodingAction {
```

```apex
// This method is the thin, global entry point that delegates any business logic to a
separate public class.
```

```apex
@InvocableMethod(
label='Get Coordinates for Address'
description='Retrieves the latitude and longitude for a given street address.'
```

```apex
category='My ISV App Name'
)
global static List<GeocodingResponse> getCoordinates(List<GeocodingRequest> requests)
{
```

```apex
// Delegate the entire list to the internal logic class to ensure
// any callouts or DML can be performed in bulk.
```

```apex
GeocodingLogic logic = new GeocodingLogic();
return logic.performGeocoding(requests);
}
```

```apex
// --- Input Wrapper Inner Class ---
// Defines the parameters an admin can configure for this action.
@JsonAccess(serializable='always' deserializable='always')
global with sharing class GeocodingRequest {
@InvocableVariable(label='Street' required=true)
global String street;
```

```apex
@InvocableVariable(label='City' required=true)
global String city;
```

```apex
@InvocableVariable(label='State/Province' required=true)
global String state;
```

```apex
@InvocableVariable(label='Postal Code' required=true)
global String postalCode;
}
```

```apex
// --- Output Wrapper Inner Class ---
// Defines the structured result returned to Agentforce.
@JsonAccess(serializable='always' deserializable='always')
global with sharing class GeocodingResponse {
@InvocableVariable(label='Was Successful')
global Boolean isSuccess;
```

```apex
@InvocableVariable(label='Latitude')
global Decimal latitude;
```

```apex
@InvocableVariable(label='Longitude')
global Decimal longitude;
```

```apex
@InvocableVariable(label='Error Message')
global String errorMessage;
}
```

```apex
// Static factory methods for creating consistent results.
```

```apex
public static GeocodingResponse success(Decimal lat, Decimal lon) {
GeocodingResponse result = new GeocodingResponse();
result.isSuccess = true;
result.latitude = lat;
result.longitude = lon;
return result;
}
```

```apex
public static GeocodingResponse error(String message) {
GeocodingResponse result = new GeocodingResponse();
result.isSuccess = false;
result.errorMessage = message;
return result;
}
}
```

```apex
// --- 2. The Internal Logic Class (Public, not Global) ---
// This is where the actual business logic lives.
// It's separate from the global entry point class for better organization and testing.
public with sharing class GeocodingLogic {
```

```apex
// Since we defined the inputs and outputs as inner classes, we use dot notation to
reference them.
```

```apex
public List<GeocodingAction.GeocodingResponse>
performGeocoding(List<GeocodingAction.GeocodingRequest> requests) {
```

```apex
List<GeocodingAction.GeocodingResponse> results = new
List<GeocodingAction.GeocodingResponse>();
```

```apex
// This method would contain your complex, bulkified business logic.
// For example, you can aggregate all requests into a single callout
// to an external geocoding service.
```

```apex
// For this simplified example, we loop and return mock results.
for (GeocodingAction.GeocodingRequest req : requests) {
```

```apex
// In a real implementation, you would perform a callout and handle errors.
if (req.postalCode == '94105') {
results.add(GeocodingAction.success(37.7749, -122.4194));
} else {
results.add(GeocodingAction.error('Address could not be found.'));
}
}
return results;
}
}
```

Best Practices for Using Global Apex in Managed Packages Access Modifiers InvocableMethod Annotation InvocableVariable Annotation Use the with sharing, without sharing, and inherited sharing Keywords Set an Access Mode for Database Operations Salesforce Developers Blog : Build Custom Agent Actions Using Apex

### Use Apex Referenced by Managed Packages

Learn how to use managed Apex effectively as a managed package subscriber. Set Package Versions for Apex Classes and Triggers As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use. Set the package version in Setup, through metadata deployments, or with API requests. Managed Apex Considerations for Package Subscribers As you use managed Apex, keep these considerations in mind.

#### Set Package Versions for Apex Classes and Triggers

As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use. Set the package version in Setup, through metadata deployments, or with API requests. In Summer ’25 and later, package subscribers can use version settings to specify the version of a migrated second-generation managed package (2GP) that an Apex class or trigger depends on. This functionality is already available to first-generation managed packages (1GP), but isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings in Migrated Second-Generation Managed Packages (2GP) . A package version is a number that identifies the set of components uploaded in a package. The version number has the format majorNumber.minorNumber.patchNumber (for example, 2.1.3). The major and minor numbers increase to a chosen value during every major release. The patchNumber is generated and updated only for a patch release. If you install a new package version, only one instance of each component exists in the package, but the components can emulate older versions. Say that you use a managed package that contains an Apex class. If the publisher decides to deprecate a method in the Apex class and release a new package version, you still see only one instance of the Apex class after installing the new version. However, this Apex class can still emulate the previous version for any code that references the deprecated method in the older version. By default, an Apex class or trigger that references a managed package is associated with the package version installed when that class or trigger was last saved or deployed. For example, say that you install version 1.0 of Package A, and then create and deploy an Apex class that references that managed package. If you upgrade to version 2.0 of Package A but don’t redeploy the class, then the class remains associated with version 1.0. However, if you upgrade Package A to version 2.0 and then redeploy the class, then the class is now associated with version 2.0. You can override the default package version settings for an Apex class or trigger. When set to a specific package version, the class or trigger views the package’s global Apex as if that version was installed. Explicitly setting a package version is useful if your class or trigger relies on an older shape of a packaged component. For an example where overriding the default package version is vital to maintain backwards compatibility, see Safely Upgrade Packages from Developer and Subscriber Perspectives on page 785. Version Apex in Managed Packages (for package developers) Safely Upgrade Packages from Developer and Subscriber Perspectives Associate an Apex class or trigger with a specific package version in Setup. To configure the package version settings for an Apex class or trigger: **1.** From Setup, enter `Apex` `Classes` or `Apex` `Triggers` in the Quick Find box, and then select **Apex Classes** or **Apex Triggers** . **2.** From the list, click **Edit** for the Apex class or trigger that you want to configure. **3.** Click the **Version Settings** tab. **4.** From the Version dropdown for the managed package, select the desired version referenced by the class or trigger. The class or trigger continues to use this version even if your install later versions of the managed package, unless you manually update the version setting. **5.** Click **Save** . If the package is referenced in the class or trigger, you can’t remove a class or trigger’s version setting for a managed package. To find where the class or trigger references a managed package, on the class or trigger’s Detail page, click **Show** **Dependencies** . Associate an Apex class or trigger with a specific package version by using Metadata API. With the PackageVersion field, you specify a managed package version in an Apex class or trigger’s metadata. **1.** Identify the managed package’s reference ID. This ID is either the subscriber package ID for migrated 2GP managed packages or the package namespace for 1GP managed packages. **a.** From Setup, in the Quick Find box, enter `Installed` `Packages` , and select **Installed Packages** . **b.** Locate the installed package that you want to reference and click the Package Name. **c.** On the Installed Package Detail page, locate the Version Setting field. The field identifies the type of reference ID. **2.** In the Apex class or trigger’s metadata file, add a `<packageVersions` `>` element. If your Apex class or trigger references multiple managed packages, include a separate `<packageVersions` `>` element for each package. **3.** Within the `<packageVersions` `>` element, add the required fields and the desired values. For migrated 2GP managed packages, add the `packageId` field. For 1GP managed packages, use the `namespace` field instead. Here’s an example declarative metadata definition of an Apex class that references a migrated 2GP managed package.

```apex
<?xml version="1.0" encoding="UTF-8"?>
<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">
```

```apex
<apiVersion>66.0</apiVersion>
<packageVersions>
```

```apex
<majorNumber>3</majorNumber>
<minorNumber>0</minorNumber>
<packageId>033xx0000000001</packageId>
</packageVersions>
<status>Active</status>
</ApexClass>
```

Here’s an example declarative metadata definition of an Apex class that references a 1GP managed package.

```apex
<?xml version="1.0" encoding="UTF-8"?>
<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">
```

```apex
<apiVersion>66.0</apiVersion>
<packageVersions>
```

```apex
<majorNumber>3</majorNumber>
<minorNumber>0</minorNumber>
<namespace>pkg1</namespace>
</packageVersions>
<status>Active</status>
</ApexClass>
```

**Metadata Usage Note for Migrated 2GP Packages** If you set a package version for an Apex class or trigger that references a 1GP managed package before Summer ’25, your existing version settings remain valid when the developer migrates the package to 2GP. If you retrieve metadata using Salesforce API version 61.0 and earlier, `<namespace` `>` is still used in the `<packageVersions` `>` section of the `meta.xml` file to identify the referenced migrated 2GP package. If you retrieve metadata using API version 62.0 and later, `<packageId` `>` is used in the `<packageVersions>` section instead. An error can occur if you deploy metadata using `<packageId` `>` to an org that still has the 1GP or 2GP pre-migrated version of the package installed. To resolve this issue, either upgrade the target org to the migrated package, or edit the `<packageVersions` `>` section to use `<namespace` `>` instead. Specify a managed package version by using the package version header in your API request. **1.** Identify the managed package’s reference ID. This ID is either the subscriber package ID for migrated 2GP managed packages or the package namespace for 1GP managed packages. **a.** From Setup, in the Quick Find box, enter `Installed` `Packages` , and select **Installed Packages** . **b.** Locate the installed package that you want to reference and click the Package Name. **c.** On the Installed Package Detail page, locate the Version Setting field. The field identifies the type of reference ID. If the Version Setting field is set to `packageID` , then the value of the Package field is the package’s reference ID. If the Version Setting field is set to `namespace` , then the value of the Namespace field is the package’s reference ID. **2.** Set the package version header according to the managed package’s reference ID and the desired package version. For REST API calls, use the `x-sfdc-packageversion-[packageId/namespace]` header. See Package Version Header in the REST API Developer Guide . For SOAP API calls, use the `PackageVersionHeader` header. See PackageVersionHeader in the SOAP API Developer Guide . If a package version isn’t specified in a request header, the API client uses the version of the package specified in Setup. To set this value, from Setup, enter `API` in the Quick Find box and select **API** . Then click **Configure Enterprise Package Version** **Settings** under Enterprise Package Version Settings.

#### Managed Apex Considerations for Package Subscribers

As you use managed Apex, keep these considerations in mind. If a package developer deprecates a global Apex identifier in a managed package, you can only reference that identifier if you specify a package version between the creation and the deprecation of the identifier. Identifiers include global Apex methods, classes, exceptions, enums, interfaces, properties, and class variables. This behavior applies to both static and dynamic references, such as identifiers accessed with the `Type.forName()` method, the `instanceof` on page 86 keyword, and the ApexTypeImplementor object. Similarly, if a package developer deletes a schema from a managed package, you can only reference the schema in Apex if you specify a package version before the deletion of the schema. This behavior applies to both static and dynamic references, such as objects and fields accessed with `Schema.describe()` methods.

### Safely Upgrade Packages from Developer and Subscriber Perspectives

Learn how to upgrade a managed package safely through this extended example. See the actions that package developers and subscribers can take to ensure a smooth transition and safeguard the backwards compatibility of existing integrations. These sections follow an example package developer and package subscriber as they move through a managed package upgrade process.

#### 1. Package Developer: Publishes Version 1.0

The package developer publishes version 1.0 of a 1GP managed package in the `eshop` namespace. The package contains Apex `CustomCart` and `CartCalculator` classes.

```apex
/**
* CustomCart
* Simple container for item prices used in a managed package context.
* @version 1.0
* @since 1.0
*/
global with sharing class CustomCart {
```

```apex
global List<Decimal> itemPrices;
```

```apex
global CustomCart() {
```

```apex
this.itemPrices = new List<Decimal>{0.0};
}
}
```

```apex
/**
* CartCalculator
* Handles tasks about calculating items and prices in customer carts.
* @version 1.0
* @since 1.0
*/
global virtual class CartCalculator {
```

```apex
/**
* Adds item prices in a custom cart.
* @param c A CustomCart object that represents a list of items that the customer
* wants to buy
* @return A Decimal object that represents the total price of items in the
* cart
* @version 1.0
* @since 1.0
*/
global virtual Decimal getTotalPrice(CustomCart c) {
```

```apex
Decimal price = 0.0;
// Add up items in cart
for (Decimal itemPrice : c.itemPrices) {
price += itemPrice;
}
return price;
}
}
```

#### 2. Package Subscriber: Adds Functionality by Overriding a Method

The package subscriber installs version 1.0 of the managed package, but they find that the existing `CartCalculator` class is inadequate. They want the ability to factor shipping costs into the total cart price. So, the subscriber extends the `CartCalculator` class in the managed package with a custom `CartCalculatorWithShipping` class. They override the `getTotalPrice()` method so that the total price includes the shipping cost.

```apex
// Package Subscriber - CartCalculatorWithShipping.cls
```

```apex
/**
* Handles tasks about calculating items and prices in customer carts,
* including shipping costs.
*/
public with sharing class CartCalculatorWithShipping extends eshop.CartCalculator {
```

```apex
/**
* Adds item prices in a cart and adds the shipping cost to the total price.
* @param c A CustomCart object that represents a list of items that the customer
* wants to buy
* @return A Decimal object that represents the total price of items in the
```

```apex
* cart, including the shipping cost
*/
public override Decimal getTotalPrice(eshop.CustomCart c) {
```

```apex
return super.getTotalPrice(c) + getShippingCost(c);
}
```

```apex
/**
* Get the shipping cost based on the items in a customer's cart
* @param c A CustomCart object that represents a list of items that the customer
* wants to buy
* @return A Decimal object that represents the total shipping cost
* for the cart
*/
public Decimal getShippingCost(eshop.CustomCart c) {
```

```apex
// Flat rate shipping
return 20.0;
}
```

```apex
}
```

#### 3. Package Developer: Releases Version 2.0 and Implements the Subscriber’s Custom Functionality

The package developer releases version 2.0 of the managed package. In this version, the `CartCalculator` class now includes a native shipping cost calculator. The updated `getTotalPrice()` method calls the new `getShippingCost()` method. Notice that the package developer uses the same method name for `getShippingCost()` as the subscriber does for their custom override method.

```apex
// Package Developer - CartCalculator.cls
```

```apex
/**
* Handles tasks about calculating items and prices in customer carts.
* @version 2.0
* @since 1.0
*/
global virtual class CartCalculator {
/**
* Adds item prices in a cart, including the shipping cost
* @param c A CustomCart object that represents a list of items that the customer
* wants to buy
* @return A Decimal object that represents the total price of items in the
* cart, including the total shipping cost
* @version 2.0
* @since 1.0
*/
global virtual Decimal getTotalPrice(CustomCart c) {
Decimal price = 0.0;
// Add up items in cart
for (Decimal itemPrice : c.itemPrices) {
price += itemPrice;
}
return price + getShippingCost(c);
}
```

```apex
/**
```

```apex
* Get the shipping cost based on the items in a customer's cart
* @param c A CustomCart object that represents a list of items that the customer
* wants to buy
* @return A Decimal object that represents the total shipping cost
* for the cart
* @version 2.0
* @since 2.0
*/
global virtual Decimal getShippingCost(CustomCart c) {
// Flat rate shipping
return 20.0;
}
}
```

#### 4. Package Subscriber: Upgrades to Version 2.0 Without Specifying a Package Version for the Apex

#### Class

By default, an Apex class or trigger is associated with the version of the managed package installed when the class or trigger was most recently deployed. In this example, the package subscriber created and saved the `CartCalculatorWithShipping` class when the `eshop` managed package was on version 1.0. If the package subscriber upgrades their `eshop` managed package to version 2.0, and doesn’t redeploy the `CartCalculatorWithShipping` class, then that class is still associated with version 1.0 of the managed package. Let’s say that the package subscriber upgrades their `eshop` managed package to version 2.0, but does try to redeploy `CartCalculatorWithShipping` . In this case, the subscriber encounters this compilation error: `Method` `must` `use` `the` `override` `keyword:` `public` `Decimal` `getShippingCost(CustomCart` `c)` . This error occurs because there’s a mismatch in the shape of the API. The subscriber’s original `CartCalculatorWithShipping` class has a `getShippingCost()` method, and the `CartCalculator` class in version 2.0 of the managed package now also includes a `getShippingCost()` method. The subscriber didn’t specify a package version for the `CartCalculatorWithShipping` class, so upon redeployment, the class is now associated with version 2.0 of the managed package. Therefore, the subscriber’s `getShippingCost()` method technically overrides the `getShippingCost()` method in `CartCalculator` , and so the Apex compiler requires an `override` keyword for the method.

#### 5. Package Subscriber: Sets Apex Class to Package Version 1.0

To avoid this compilation error, the package subscriber explicitly sets a package version for the `CartCalculatorWithShipping` class. When is set to a specific package version, the class views the package’s global Apex as if that version was installed. In this case, setting `CartCalculatorWithShipping` to version 1.0 of the managed package avoids a compilation error because the package’s `CartCalculator` class doesn’t define a `getShippingCost()` method until version 2.0. As long as the `CartCalculatorWithShipping` class is set to an earlier package version, the package’s `CartCalculator` class doesn’t expose the `getShippingCost()` method to the subscriber. Therefore, the Apex compiler doesn’t flag the subscriber’s own `getShippingCost()` method as needing to override the method in the managed package. To override the default package version for an Apex class or trigger, use the Salesforce Setup UI or the `packageVersions` field of the class’s ApexClass metadata type. See Set Package Versions for Apex Classes and Triggers on page 782. In Spring ’25 and earlier, setting Apex classes and triggers to a package version was available for only first-generation managed packages (1GP). In Summer ’25 and later, package version setting is also available for migrated 2GP managed packages. Package version setting isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings in Migrated Second-Generation Managed Packages (2GP) . For migrated 2GP managed packages, the `packageVersions` field of the ApexClass metadata type is different from that of 1GP managed packages. 2GP managed packages are identified by their package ID, whereas 1GP managed packages are identified by their namespace. This difference occurs because multiple 2GP managed packages can have the same namespace, whereas 1GP managed packages each require a unique namespace. For example, here’s the metadata file for the subscriber’s `CartCalculatorWithShipping` class, where the class is set to version 1.0 of the managed package. Because the package is a 1GP managed package, the namespace is specified instead of the package ID.

```apex
<!-- CartCalculatorWithShipping.cls-meta.xml -->
<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">
```

```apex
<apiVersion>66.0</apiVersion>
<status>Active</status>
<packageVersions>
```

```apex
<namespace>eshop</namespace> <!-- For only 1GP
-->
<majorNumber>1</majorNumber>
<minorNumber>0</minorNumber>
</packageVersions>
</ApexClass>
```

#### 6. Package Subscriber: getTotalPrice() Returns an Incorrect Value

The subscriber sets the `CartCalculatorWithShipping` class to version 1.0 of the managed package and successfully recompiles the class. However, the subscriber now encounters a new issue at run time: the `getTotalPrice()` method in the `CartCalculatorWithShipping` class returns the wrong total price. Recall that specifying an earlier package version for an Apex class or trigger hides globals that are defined in later versions during compilation. In other words, setting a package version preserves the shape of the API. However, it doesn’t necessarily preserve the behavior of the API at run time. In version 1.0, the `getTotalPrice()` method in the `CartCalculator` class returns only the base price. But in version 2.0, the `getTotalPrice()` method now returns the price plus the result of `getTotalShippingCost()` . The `getTotalPrice()` method exists in both versions of the managed package, even though its behavior differs. Therefore, even if the subscriber sets the `CartCalculatorWithShipping` class to version 1.0, the `getTotalPrice()` executes with its version 2.0 behavior at run time. Remember that the subscriber’s `getTotalPrice()` method in their `CartCalculatorWithShipping` class overrides the native `getTotalPrice()` method in the managed package. The subscriber’s override method adds the `getShippingCost()` result to the result of the native `getTotalPrice()` method. In version 2.0 of the managed package, the native `getTotalPrice()` method already adds the shipping cost, so the shipping cost is erroneously added twice.

```apex
// Package Developer - CartCalculator.cls (v2.0) (code unchanged)
global virtual class CartCalculator {
```

```apex
global virtual Decimal getTotalPrice(CustomCart c) {
Decimal price = 0.0;
// Add up items in cart
for (Decimal itemPrice : c.itemPrices) {
price += itemPrice;
}
return price + getShippingCost(c);
}
```

```apex
global virtual Decimal getShippingCost(CustomCart c) {
// Flat rate shipping
```

```apex
return 20.0;
}
```

```apex
}
```

```apex
// Package Subscriber - CartCalculatorWithShipping.cls (code unchanged)
public with sharing class CartCalculatorWithShipping extends eshop.CartCalculator {
```

```apex
// Now returns the wrong price because getShippingCost is added twice
public override Decimal getTotalPrice(eshop.CustomCart c) {
return super.getTotalPrice(c) + getShippingCost(c);
}
```

```apex
public Decimal getShippingCost(eshop.CustomCart c) {
// Flat rate shipping
return 20.0;
}
}
```

To resolve this problem without requiring the subscriber to change their code, the package developer must version the behavior of Apex classes and triggers in the package.

#### 7. Package Developer: Implements Backward Compatibility with System.requestVersion()

After the package subscriber informs the package developer about the unexpected `getTotalPrice()` behavior, the package developer releases a patch update. Version 2.1 of the package allows the subscriber to keep their original `CartCalculatorWithShipping` class by implementing backwards compatibility with `System.requestVersion()` . Here’s version 2.1 of the `CartCalculator` class that contains an updated `getTotalPrice()` method. In the method, a `callerVersion` variable is set to `System.requestVersion()` , which returns a `Version` object that represents the managed package version of the calling class. A `minVersionWithShippingCost` variable is set to the managed package version that introduced the changed `getTotalPrice()` behavior. Then, the `Version.compareTo()` method compares `callerVersion` and `minVersionWithShippingCost` . If the caller version is earlier than the version that the shipping cost feature was introduced in, then `getTotalPrice()` returns the price. This value aligns with the original behavior in version 1.0 of the managed package. If the caller version matches or is later than the version that the shipping cost feature was introduced in, then `getTotalPrice()` returns the price addition to the shipping cost.

```apex
// Package Developer - CartCalculator.cls
```

```apex
/**
* Handles tasks about calculating items and prices in customer carts.
* @version 2.1
* @since 1.0
*/
global virtual class CartCalculator {
```

```apex
/**
* Adds item prices in a cart.
* @param c A CustomCart object that represents a list of items that the customer
* wants to buy
* @return A Decimal object that represents the total price of items in the
```

```apex
* cart. Total price includes the shipping cost for v2.0 and later.
* @version 2.1
* @since 1.0
*/
global virtual Decimal getTotalPrice (CustomCart c) {
```

```apex
Decimal price = 0.00;
// Add up items in cart
Version callerVersion = System.requestVersion();
Version minVersionWithShippingCost = new Version(2, 0);
if (callerVersion.compareTo(minVersionWithShippingCost) < 0) {
// callVer < minVer that you introduced the shipping cost feature in
```

```apex
return price;
} else {
return price + getShippingCost(c);
}
}
```

```apex
/**
* Get the shipping cost based on the items in a customer's cart
* @param c A CustomCart object that represents a list of items that the customer
* wants to buy
* @return A Decimal object that represents the total shipping cost
* for the cart
* @version 2.1
* @since 2.0
*/
global virtual Decimal getShippingCost(CustomCart c) {
```

```apex
return 20.00;
}
}
```

By versioning the behavior of `getTotalPrice()` , the package developer has implemented basic backward compatibility for the class. Now, as long as package subscribers set Apex classes to the desired managed package version, then their existing implementations won’t break when they upgrade from version 1.0 to version 2.1 of the package.

#### 8: Package Developer: Tests Backward Compatibility with System.runAs()

To ensure that `getTotalPrice()` now behaves differently based on the package version of the calling code, the package developer can use `System.runAs()` in their unit tests. This method, which can only be used in test methods, changes the current package version to the package version specified in the argument Here’s a basic unit test that the package developer implements for `getTotalPrice()` .

```apex
// Package Developer - CartCalculatorTest.cls
@isTest
private class CartCalculatorTest {
```

```apex
private static final List<Decimal> prices = new List<Decimal>{
10.0,
20.0,
30.0
};
```

```apex
@isTest
```

```apex
static void testGetTotalPrice_WithShippingCost() {
CustomCart cart = new CustomCart();
cart.itemPrices = prices;
```

```apex
CartCalculator calculator = new CartCalculator();
```

```apex
//Version 2.0 includes the shipping cost calculation
System.runAs(new Version(2, 0)) {
Decimal totalPrice = calculator.getTotalPrice(cart);
// The expected total is sum of item prices (60.0) plus the shipping cost
(20.0)
Assert.areEqual(80.0, totalPrice, 'The total price should be 80.0');
}
}
```

```apex
@isTest
static void testGetTotalPrice_WithoutShippingCost() {
CustomCart cart = new CustomCart();
cart.itemPrices = prices;
CartCalculator calculator = new CartCalculator();
// Version 1.0 doesn't include the shipping cost calculation
System.runAs(new Version(1, 0)) {
Decimal totalPrice = calculator.getTotalPrice(cart);
// The expected total is the sum of item prices (60.0)
Assert.areEqual(60.0, totalPrice, 'The total price should be 60.0');
}
}
}
```

#### Summary: Shared Responsibilities for Safe Package Upgrades

The extended example demonstrates that the package developer and package subscriber both play a role in ensuring safe package upgrades. Here’s a table that summarizes the recommended actions that each actor can take so that the package can evolve without compromising subscriber implementations. **Table 11: Safe Package Upgrade Responsibilities** Be aware of the default versioned behavior: an Apex class or trigger is associated with Package Subscriber Version API Shape the version of a managed package installed when that class or trigger was most recently deployed or saved. If necessary, override the default by explicitly setting dependent Apex classes and triggers to a specific package version. See Set Package Versions for Apex Classes and Triggers on page 782. Version changed behavior with `System.requestVersion()` , and Package Developer Version API Behavior
