
# Getting Started with Apex

## APEX DEVELOPER GUIDE

Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control statements on the Salesforce Platform server, in conjunction with calls to the API. This guide introduces you to the Apex development process and provides valuable information on learning, writing, deploying and testing Apex. For reference information on Apex classes, interfaces, exceptions and so on, see Apex Reference Guide . Apex Release Notes Use the Salesforce Release Notes to learn about the most recent updates and changes to Apex. Getting Started with Apex Learn about the Apex development lifecycle. Follow a step-by-step tutorial to create an Apex class and trigger, and deploy them to a production organization. Writing Apex Apex is like Java for Salesforce. It enables you to add and interact with data in the Lightning Platform persistence layer. It uses classes, data types, variables, and if-else statements. You can make it execute based on a condition, or have a block of code execute repeatedly. Running Apex You can access many features of the Salesforce user interface programmatically in Apex, and you can integrate with external SOAP and REST Web services. You can run Apex code using a variety of mechanisms. Apex code runs in atomic transactions. Debugging, Testing, and Deploying Apex Develop your Apex code in a sandbox and debug it with the Developer Console and debug logs. Unit-test your code, then distribute it to customers using packages. Apex Reference In Summer ’21 and later versions, Apex reference content is moved to a separate guide called the Apex Reference Guide. Appendices

## Apex Release Notes

Use the Salesforce Release Notes to learn about the most recent updates and changes to Apex. For Apex updates and changes that impact the Salesforce Platform, see the Apex Release Notes . For new and changed Apex classes, methods, exceptions and interfaces, see Apex: New and Changed Items in the Salesforce Release Notes.

## Getting Started with Apex

Learn about the Apex development lifecycle. Follow a step-by-step tutorial to create an Apex class and trigger, and deploy them to a production organization. Introducing Apex Apex code is the first multitenant, on-demand programming language for developers interested in building the next generation of business applications. Apex revolutionizes the way developers create on-demand applications. Apex Development Process In this chapter, you’ll learn about the Apex development lifecycle, and which organization and tools to use to develop Apex. You’ll also learn about testing and deploying Apex code. Apex Quick Start This step-by-step tutorial shows how to create a simple Apex class and trigger, and how to deploy these components to a production organization.

## Introducing Apex

Apex code is the first multitenant, on-demand programming language for developers interested in building the next generation of business applications. Apex revolutionizes the way developers create on-demand applications. While many customization options are available through the Salesforce user interface, such as the ability to define new fields, objects, workflow, and approval processes, developers can also use the SOAP API to issue data manipulation commands such as `delete()` , `update()` or `upsert()` , from client-side programs. These client-side programs, typically written in Java, JavaScript, .NET, or other programming languages, grant organizations more flexibility in their customizations. However, because the controlling logic for these client-side programs is not located on Salesforce servers, they are restricted by the performance costs of making multiple round-trips to the Salesforce site to accomplish common business transactions, and by the cost and complexity of hosting server code, such as Java or .NET, in a secure and robust environment. 1. What is Apex? Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control statements on Salesforce servers in conjunction with calls to the API. Using syntax that looks like Java and acts like database stored procedures, Apex enables developers to add business logic to most system events, including button clicks, related record updates, and Visualforce pages. Apex code can be initiated by Web service requests and from triggers on objects. 2. Understanding Apex Core Concepts Apex code typically contains many things that you're familiar with from other programming languages. 3. When Should I Use Apex? Salesforce provides the ability to customize prebuilt apps to fit your organization. For complex business processes, you can implement custom functionality and user interfaces with a variety of tools, including Apex and Lightning Components. 4. How Does Apex Work? All Apex runs entirely on-demand on the Lightning Platform. Developers write and save Apex code to the platform, and end users trigger the execution of the Apex code via the user interface. 5. Developing Code in the Cloud The Apex programming language is saved and runs in the cloud—the multitenant platform. Apex is tailored for data access and data manipulation on the platform, and it enables you to add custom business logic to system events. While it provides many benefits for automating business processes on the platform, it is not a general purpose programming language.

### What is Apex?

Apex is a strongly typed, object-oriented programming language that allows developers to execute flow and transaction control statements on Salesforce servers in conjunction with calls to the API. Using syntax that looks like Java and acts like database stored procedures, Apex enables developers to add business logic to most system events, including button clicks, related record updates, and Visualforce pages. Apex code can be initiated by Web service requests and from triggers on objects. **You can add Apex to most system events.** As a language, Apex is: **Integrated** Apex provides built-in support for common Lightning Platform idioms, including: Data manipulation language (DML) calls, such as `INSERT` , `UPDATE` , and `DELETE` , that include built-in `DmlException` handling Inline Salesforce Object Query Language (SOQL) and Salesforce Object Search Language (SOSL) queries that return lists of sObject records Looping that allows for bulk processing of multiple records at a time Locking syntax that prevents record update conflicts Custom public API calls that can be built from stored Apex methods Warnings and errors issued when a user tries to edit or delete a custom object or field that is referenced by Apex **Easy to use** Apex is based on familiar Java idioms, such as variable and expression syntax, block and conditional statement syntax, loop syntax, object and array notation. Where Apex introduces new elements, it uses syntax and semantics that are easy to understand and encourage efficient use of the Lightning Platform. Therefore, Apex produces code that is both succinct and easy to write. **Data focused** Apex is designed to thread together multiple query and DML statements into a single unit of work on the Salesforce server. Developers use database stored procedures to thread together multiple transaction statements on a database server in a similar way. Like other database stored procedures, Apex does not attempt to provide general support for rendering elements in the user interface. **Rigorous** Apex is a strongly typed language that uses direct references to schema objects such as object and field names. It fails quickly at compile time if any references are invalid. It stores all custom field, object, and class dependencies in metadata to ensure that they are not deleted while required by active Apex code. **Hosted** Apex is interpreted, executed, and controlled entirely by the Lightning Platform. **Multitenant aware** Like the rest of the Lightning Platform, Apex runs in a multitenant environment. So, the Apex runtime engine is designed to guard closely against runaway code, preventing it from monopolizing shared resources. Any code that violates limits fails with easy-to-understand error messages. **Easy to test** Apex provides built-in support for unit test creation and execution. It includes test results that indicate how much code is covered, and which parts of your code could be more efficient. Salesforce ensures that all custom Apex code works as expected by executing all unit tests prior to any platform upgrades. **Versioned** You can save your Apex code against different versions of the API. This enables you to maintain behavior. Apex is included in Performance Edition, Unlimited Edition, Developer Edition, Enterprise Edition, and Database.com.

### Understanding Apex Core Concepts

Apex code typically contains many things that you're familiar with from other programming languages. **Programming elements in Apex** The section describes the basic functionality of Apex, as well as some of the core concepts.

#### Using Version Settings

In the Salesforce user interface you can specify a version of the Salesforce API against which to save your Apex class or trigger. This setting indicates not only the version of SOAP API to use, but which version of Apex as well. You can change the version after saving. Every class or trigger name must be unique. You can’t save the same class or trigger against different versions. You can also use version settings to associate a class or trigger with a particular version of a managed package that is installed in your organization from AppExchange. This version of the managed package continues to be used by the class or trigger if later versions of the managed package are installed, unless you manually update the version setting. To add an installed managed package to the settings list, select a package from the list of available packages. The list is only displayed if you have an installed managed package that is not already associated with the class or trigger. For more information about using version settings with managed packages, see About Package Versions in Salesforce Help.

#### Naming Variables, Methods and Classes

You can’t use any of the Apex reserved keywords when naming variables, methods, or classes. These include words that are part of Apex and the Lightning Platform, such as `list` , `test` , or `account` , as well as reserved keywords .

#### Using Variables and Expressions

Apex is a strongly-typed language, that is, you must declare the data type of a variable when you first refer to it. Apex data types include basic types such as Integer, Date, and Boolean, as well as more advanced types such as lists, maps, objects, and sObjects. Variables are declared with a name and a data type. You can assign a value to a variable when you declare it. You can also assign values later. Use the following syntax when declaring variables:

```apex
datatype variable_name [ = value];
```

The semi-colon at the end of preceding codeblock is not optional. You must end all statements with a semi-colon. The following are examples of variable declarations:

```apex
// The following variable has the data type of Integer with the name Count,
// and has the value of 0.
Integer Count = 0;
// The following variable has the data type of Decimal with the name Total. Note
// that no value has been assigned to it.
Decimal Total;
// The following variable is an account, which is also referred to as an sObject.
Account MyAcct = new Account();
```

In Apex, all primitive data type arguments, such as Integer or String, are passed into methods by value. This fact means that any changes to the arguments exist only within the scope of the method. When the method returns, the changes to the arguments are lost. Non-primitive data type arguments, such as sObjects, are passed into methods by reference. Therefore, when the method returns, the passed-in argument still references the same object as before the method call. Within the method, the reference can't be changed to point to another object, but the values of the object's fields can be changed.

#### Using Statements

A statement is any coded instruction that performs an action. In Apex, statements must end with a semicolon and can be one of these types: Assignment, such as assigning a value to a variable Conditional (if-else) Loops: Do-while While For Locking Data Manipulation Language (DML) Transaction Control Method Invoking Exception Handling A block is a series of statements that are grouped with curly braces and can be used in any place where a single statement is allowed. For example:

```apex
if (true) {
System.debug(1);
System.debug(2);
} else {
System.debug(3);
System.debug(4);
}
```

In cases where a block consists of only one statement, the curly braces can be left off. For example:

```apex
if (true)
System.debug(1);
else
```

```apex
System.debug(2);
```

#### Using Collections

Apex has the following types of collections: Lists (arrays) Maps Sets A list is a collection of elements, such as Integers, Strings, objects, or other collections. Use a list when the sequence of elements is important. You can have duplicate elements in a list. The first index position in a list is always 0. To create a list: Use the `new` keyword Use the `List` keyword followed by the element type contained within `<>` characters. Use the following syntax for creating a list:

```apex
List <datatype> list_name
[= new List<datatype>();] |
[=new List<datatype>{value [, value2. . .]};] |
;
```

The following example creates a list of Integer, and assigns it to the variable `My_List` . Remember, because Apex is strongly typed, you must declare the data type of `My_List` as a list of Integer.

```apex
List<Integer> My_List = new List<Integer>();
```

For more information, see Lists on page 29. A set is a collection of unique, unordered elements. It can contain primitive data types, such as String, Integer, Date, and so on. It can also contain more complex data types, such as sObjects. To create a set: Use the `new` keyword Use the `Set` keyword followed by the primitive data type contained within `<>` characters Use the following syntax for creating a set:

```apex
Set<datatype> set_name
[= new Set<datatype>();] |
[= new Set<datatype>{value [, value2. . .] };] |
;
```

The following example creates a set of String. The values for the set are passed in using the curly braces `{}` .

```apex
Set<String> My_String = new Set<String>{'a', 'b', 'c'};
```

For more information, see Sets on page 31. A map is a collection of key-value pairs. Keys can be any primitive data type. Values can include primitive data types, as well as objects and other collections. Use a map when finding something by key matters. You can have duplicate values in a map, but each key must be unique. To create a map: Use the `new` keyword Use the `Map` keyword followed by a key-value pair, delimited by a comma and enclosed in `<>` characters. Use the following syntax for creating a map:

```apex
Map<key_datatype, value_datatype> map_name
[=new Map<key_datatype, value_datatype>();] |
[=new Map<key_datatype, value_datatype>
{key1_value => value1_value
[, key2_value => value2_value. . .]};] |
;
```

The following example creates a map that has a data type of Integer for the key and String for the value. In this example, the values for the map are being passed in between the curly braces `{}` as the map is being created.

```apex
Map<Integer, String> My_Map = new Map<Integer, String>{1 => 'a', 2 => 'b', 3 => 'c'};
```

For more information, see Maps on page 32.

#### Using Branching

An `if` statement is a true-false test that enables your application to do different things based on a condition. The basic syntax is as follows:

```apex
if (Condition){
// Do this if the condition is true
} else {
// Do this if the condition is not true
}
```

For more information, see Conditional (If-Else) Statements on page 54.

#### Using Loops

While the `if` statement enables your application to do things based on a condition, loops tell your application to do the same thing again and again based on a condition. Apex supports the following types of loops: Do-while While For A Do-while loop checks the condition after the code has executed. A While loop checks the condition at the start, before the code executes. A For loop enables you to more finely control the condition used with the loop. In addition, Apex supports traditional For loops where you set the conditions, as well as For loops that use lists and SOQL queries as part of the condition. For more information, see Loops on page 58.

### When Should I Use Apex?

Salesforce provides the ability to customize prebuilt apps to fit your organization. For complex business processes, you can implement custom functionality and user interfaces with a variety of tools, including Apex and Lightning Components.

#### Apex

Use Apex if you want to: Create Web services. Create email services. Perform complex validation over multiple objects. Create complex business processes that aren’t supported by Flow Builder. Create custom transactional logic (logic that occurs over the entire transaction, not just with a single record or object). Attach custom logic to another operation, such as saving a record, so that it occurs whenever the operation is executed, regardless of whether it originates in the user interface, a Visualforce page, or from SOAP API.

#### Lightning Components

Develop Lightning components to customize Lightning Experience, the Salesforce mobile app, or to build your own standalone apps. You can also use out-of-the-box components to speed up development. As of Spring ’19 (API version 45.0), you can build Lightning components using two programming models: the Lightning Web Components model, and the original Aura Components model. Lightning web components are custom HTML elements built using HTML and modern JavaScript. Lightning web components and Aura components can coexist and interoperate on a page. Configure Lightning web components and Aura components to work in Lightning App Builder and Experience Builder. Admins and end users don’t know which programming model was used to develop the components. To them, they’re simply Lightning components. We recommend using the Lightning Web Components (LWC) model to create custom user interfaces. LWC follows W3C web standards, and you can build and package components using standard JavaScript syntax. With LWC, you can work easily with Salesforce data using Apex and Lightning Data Service. For more information, see the LWC Dev Guide .

#### Visualforce

Visualforce consists of a tag-based markup language that gives developers a more powerful way of building applications and customizing the Salesforce user interface. With Visualforce you can: Build wizards and other multistep processes. Create your own custom flow control through an application. Define navigation patterns and data-specific rules for optimal, efficient application interaction. For more information, see the Visualforce Developer's Guide .

#### SOAP API

Use standard SOAP API calls when you want to add functionality to a composite application that processes only one type of record at a time and does not require any transactional control (such as setting a Savepoint or rolling back changes). For more information, see the SOAP API Developer Guide .

### How Does Apex Work?

All Apex runs entirely on-demand on the Lightning Platform. Developers write and save Apex code to the platform, and end users trigger the execution of the Apex code via the user interface. **Apex is compiled, stored, and run entirely on the Lightning Platform** When a developer writes and saves Apex code to the platform, the platform application server first compiles the code into an abstract set of instructions that can be understood by the Apex runtime interpreter, and then saves those instructions as metadata. When an end user triggers the execution of Apex, perhaps by clicking a button or accessing a Visualforce page, the platform application server retrieves the compiled instructions from the metadata and sends them through the runtime interpreter before returning the result. The end user observes no differences in execution time from standard platform requests.

### Developing Code in the Cloud

The Apex programming language is saved and runs in the cloud—the multitenant platform. Apex is tailored for data access and data manipulation on the platform, and it enables you to add custom business logic to system events. While it provides many benefits for automating business processes on the platform, it is not a general purpose programming language. Apex cannot be used to: Render elements in the user interface other than error messages Change standard functionality—Apex can only prevent the functionality from happening, or add additional functionality Create temporary files Spawn threads All Apex code runs on the Lightning Platform, which is a shared resource used by all other organizations. To guarantee consistent performance and scalability, the execution of Apex is bound by governor limits that ensure no single Apex execution impacts the overall service of Salesforce. This means all Apex code is limited by the number of operations (such as DML or SOQL) that it can perform within one process. All Apex requests return a collection that contains from 1 to 50,000 records. You cannot assume that your code only works on a single record at a time. Therefore, you must implement programming patterns that take bulk processing into account. If you don’t, you may run into the governor limits. Trigger and Bulk Request Best Practices

## Apex Development Process

In this chapter, you’ll learn about the Apex development lifecycle, and which organization and tools to use to develop Apex. You’ll also learn about testing and deploying Apex code. What is the Apex Development Process? To develop Apex, get a Developer Edition account, write and test your code, then deploy your code. Choose a Salesforce Org for Apex Development You can develop Apex in a sandbox, scratch org, or Developer Edition org, but not directly in a production org. With so many choices, here’s some help to determine which org type is right for you and how to create it. Choose a Development Environment for Writing Apex There are several development environments for developing Apex code. Choose the environment that meets your needs. Learning Apex After you have your developer account, there are many resources available to you for learning about Apex Writing Tests Testing is the key to successful long-term development and is a critical component of the development process. We strongly recommend that you use a test-driven development process, that is, test development that occurs at the same time as code development. Deploying Apex to a Sandbox Organization Sandboxes create copies of your Salesforce org in separate environments. Use them for development, testing, and training without compromising the data and applications in your production org. Sandboxes are isolated from your production org, so operations that you perform in your sandboxes don’t affect your production org. Deploy Apex to a Salesforce Production Organization After you’ve finished all of your unit tests and verified that your Apex code is executing properly, the final step is deploying Apex to your Salesforce production organization. Adding Apex Code to a AppExchange App You can include an Apex class or trigger in an app that you’re creating for AppExchange.

### What is the Apex Development Process?

To develop Apex, get a Developer Edition account, write and test your code, then deploy your code. We recommend the following process for developing Apex: **1.** Choose a Salesforce Org for Apex development. **2.** Learn more about Apex . **3.** Write your Apex. **4.** While writing Apex, you should also be writing tests . **5.** Optionally deploy your Apex to a sandbox organization and do final unit tests. **6.** Deploy your Apex to your Salesforce production organization. In addition to deploying your Apex, once it is written and tested, you can also add your classes and triggers to a AppExchange App package .

### Choose a Salesforce Org for Apex Development

You can develop Apex in a sandbox, scratch org, or Developer Edition org, but not directly in a production org. With so many choices, here’s some help to determine which org type is right for you and how to create it.

#### Sandboxes (Recommended)

A sandbox is a copy of your production org’s metadata in a separate environment, with varying amounts of data depending on the sandbox type. A sandbox provides a safe space for developers and admins to experiment with new features and validate changes before deploying code to production. Developer and Developer Pro sandboxes with source tracking enabled can take advantage of many of the features of our Salesforce DX source-driven development tools, including Salesforce CLI, Code Builder, and DevOps Center. See Create a Sandbox in Salesforce Help.

#### Scratch Orgs (Recommended)

A scratch org is a source-driven and temporary deployment of Salesforce code and metadata. A scratch org is fully configurable, allowing you to emulate different Salesforce editions with different features and settings. Scratch orgs have a maximum 30-day lifespan, with the default set at 7 days. For information on using and creating scratch orgs, see Scratch Orgs in the Salesforce DX Developer Guide .

#### Developer Edition (DE) Orgs

A DE org is a free org that provides access to many of the features available in an Enterprise Edition org. Developer Edition orgs can become out-of-date over time and have limited storage. Developer Edition orgs don’t have source tracking enabled and can’t be used as development environments in DevOps Center. Developer Edition orgs expire if they aren't logged into regularly. You can sign up for as many Developer Edition orgs as you like on the Developer Edition Signup page.

#### Trial Edition Orgs

Trial editions usually expire after 30 days, so they’re great for evaluating Salesforce functionality but aren’t intended for use as a permanent development environment. Although Apex triggers are available in trial editions, they’re disabled when you convert to any other edition. Deploy your code to another org before conversion to retain your Apex triggers. Salesforce offers several product- and industry-specific free trial orgs .

#### Production Orgs (Not Supported)

A production org is the final destination for your code and applications, and has live users accessing your data. You can't develop Apex in your Salesforce production org, and we recommend that you avoid directly modifying any code or metadata directly in production. Live users accessing the system while you're developing can destabilize your data or corrupt your application.

### Choose a Development Environment for Writing Apex

There are several development environments for developing Apex code. Choose the environment that meets your needs.

#### Agentforce for Developers

Agentforce for Developers is an AI-powered developer tool that generates Apex code from natural language prompts and automatically suggests code completions as you type. Use Agentforce for Developers to easily create unit test cases for your Apex code and get to the required Apex test coverage. Agentforce for Developers extension (salesforcedx-einstein-gpt) is a part of the Salesforce Expanded Pack . Agentforce for Developers is enabled by default in VS Code. For more information, see Set Up Agentforce for Developers . To access Agentforce for Developers from inside an Apex file in the VS Code editor, see Generate Apex Code . To use AI-based autocomplete to accept suggestions for Apex code as you write it, see Inline Auto Completion . To use Agentforce for Developers to quickly generate unit tests, see Test Case Generation .

#### Salesforce Extensions for Visual Studio Code and Code Builder

The Salesforce Extensions for Visual Studio Code and Code Builder are tools for developing on the Salesforce platform in the lightweight, extensible VS Code editor. These tools provide features for working with development orgs (scratch orgs, sandboxes, and developer edition orgs), Apex, Lightning components, and Visualforce. Code Builder is a browser-based version of the desktop experience, with everything installed and configured. It provides all the goodness of the desktop experience, but provides you with the flexibility to work anywhere, from any computer.

#### Developer Console

The Developer Console is an integrated development environment (IDE) built into Salesforce. Use it to create, debug, and test Apex classes and triggers. To open the Developer Console from Lightning Experience: Click the quick access menu ( ), then click **Developer Console** . To open the Developer Console from Salesforce Classic: Click `Your` `Name` > **Developer Console** . The Developer Console supports these tasks: Writing code—You can add code using the source code editor. Also, you can browse packages in your organization. Compiling code—When you save a trigger or class, the code is automatically compiled. Any compilation errors are reported. Debugging—You can view debug logs and set checkpoints that aid in debugging. Testing—You can execute tests of specific test classes or all tests in your organization, and you can view test results. Also, you can inspect code coverage. Checking performance—You can inspect debug logs to locate performance bottlenecks. SOQL queries—You can query data in your organization and view the results using the Query Editor. Color coding and autocomplete—The source code editor uses a color scheme for easier readability of code elements and provides autocompletion for class and method names.

#### Salesforce Setup Code Editors

In Salesforce Setup, you can view and edit Apex classes and triggers. All classes and triggers are compiled when they’re saved, and any syntax errors are flagged. You can’t save your code until it compiles without errors. The Salesforce user interface also numbers the lines in the code, and uses color coding to distinguish different elements, such as comments, keywords, literal strings, and so on. From Setup in the Quick Find box, enter `Apex` , and select an Apex class or trigger. To edit it, click **Edit** beside the class or trigger name. To create a trigger on an object, from Setup in the Quick Find box, enter `Object` and click **Object Manager** . Click the object name and click **Triggers** . Click **New** and enter your code. You can’t use the Salesforce Setup code editors to modify Apex in a Salesforce production org.

#### Additional Editors

Alternatively, you can use any text editor, such as Notepad, to write Apex code. Then either copy and paste the code into your application, or use one of the API calls to deploy it. To develop an Apex IDE of your own, use SOAP API methods for compiling triggers and classes, and executing test methods. Use Metadata API methods for deploying code to production environments. For more information, see Deploying Apex on page 763. Salesforce Help : Find Object Management Settings

### Learning Apex

After you have your developer account, there are many resources available to you for learning about Apex

#### Apex Trailhead Content

Beginning and intermediate programmers Several Trailhead modules provide tutorials on learning Apex. Use these modules to learn the fundamentals of Apex and how you can use it on the Salesforce Platform. Use Apex to add custom business logic through triggers, unit tests, asynchronous Apex, REST Web services, and Lightning components. Quick Start: Apex Apex Basics & Database Apex Triggers Apex Integration Services Apex Testing Asynchronous Apex

#### Salesforce Developers Apex Developer Center

Beginning and advanced programmers The Apex Developer Center has links to several resources including articles about the Apex programming language. These resources provide a quick introduction to Apex and include best practices for Apex development.

#### Code Samples and SDKs

Beginning and advanced programmers Open-source code samples and SDKs, reference code, and best practices can be found at Code samples and SDKs . A library of concise, meaningful examples of Apex code for common use cases, following best practices, can be found at Apex-recipes .

#### Training Courses

Training classes are also available from Salesforce Trailhead Academy . Grow and validate your skills with Salesforce Credentials .

#### In This Guide (Apex Developer Guide)

Beginning programmers can look at the following: Introducing Apex , and in particular: Documentation Conventions Core Concepts Quick Start Tutorial Classes, Objects, and Interfaces Testing Apex Execution Governors and Limits In addition, advanced programmers can look at: Trigger and Bulk Request Best Practices Advanced Apex Programming Example Understanding Apex Describe Information Asynchronous Execution ( `@future` Annotation) Batch Apex and Apex Scheduler

### Writing Tests

Testing is the key to successful long-term development and is a critical component of the development process. We strongly recommend that you use a test-driven development process, that is, test development that occurs at the same time as code development. To facilitate the development of robust, error-free code, Apex supports the creation and execution of unit tests . Unit tests are class methods that verify whether a particular piece of code is working properly. Unit test methods take no arguments, commit no data to the database, and send no emails. Such methods are flagged with the `@IsTest` annotation in the method definition. Unit test methods must be defined in test classes, that is, classes annotated with `@IsTest` . The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a future release. In addition, before you deploy Apex or package it for the AppExchange, the following must be true. Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully. Note the following. When deploying Apex to a production organization, each unit test in your organization namespace is executed by default. Calls to `System.debug` aren’t counted as part of Apex code coverage. Test methods and test classes aren’t counted as part of Apex code coverage. While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead, make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and single records. This approach ensures that 75% or more of your code is covered by unit tests. Every trigger must have some test coverage. All classes and triggers must compile successfully. For more information on writing tests, see Testing Apex on page 719.

### Deploying Apex to a Sandbox Organization

Sandboxes create copies of your Salesforce org in separate environments. Use them for development, testing, and training without compromising the data and applications in your production org. Sandboxes are isolated from your production org, so operations that you perform in your sandboxes don’t affect your production org. To deploy Apex from a local project in the Salesforce extension for Visual Studio Code to a Salesforce organization, see Salesforce Extensions for Visual Studio Code . You can also use the `deploy()` Metadata API call to deploy your Apex from a developer organization to a sandbox organization. A useful API call is `runTests()` . In a development or sandbox organization, you can run the unit tests for a specific class, a list of classes, or a namespace. You can also use Salesforce CLI. See Develop Against Any Org for details. For more information, see Deploying Apex .

### Deploy Apex to a Salesforce Production Organization

After you’ve finished all of your unit tests and verified that your Apex code is executing properly, the final step is deploying Apex to your Salesforce production organization. **1.** To deploy Apex from a local project in Visual Studio Code editor to a Salesforce organization, see Salesforce Extensions for Visual Studio Code and Code Builder . Also, you can deploy Apex through change sets in the Salesforce user interface. For more information and for additional deployment options, see Deploying Apex on page 763, and Build and Release Your App .

### Adding Apex Code to a AppExchange App

You can include an Apex class or trigger in an app that you’re creating for AppExchange. Any Apex that is included as part of a package must have at least 75% cumulative test coverage. Each trigger must also have some test coverage. When you upload your package to AppExchange, all tests are run to ensure that they run without errors. In addition, tests with the `@isTest(OnInstall=true)` annotation run when the package is installed in the installer's organization. You can specify which tests should run during package install by annotating them with `@isTest(OnInstall=true)` . This subset of tests must pass for the package install to succeed. For more information, see the Second-Generation Managed Packaging Developer Guide .

## Apex Quick Start

This step-by-step tutorial shows how to create a simple Apex class and trigger, and how to deploy these components to a production organization. When you have a Developer Edition or sandbox organization, you can learn some of the core concepts of Apex. After reviewing the basics, you’re ready to write your first Apex program—a simple class, trigger, and unit test. Because Apex is similar to Java, you can recognize much of the functionality. This tutorial is based on a custom object called Book that is created in the first step. This custom object is updated through a trigger. This Hello World sample requires custom objects. You can either create these objects on your own, or download the objects and Apex code as an unmanaged package from AppExchange. To obtain the sample assets in your org, install the Apex Tutorials Package . This package also contains sample code and objects for the Shipping Invoice example. There’s a more complex Shipping Invoice example that you can also walk through. That example illustrates many more features of the language. 1. Create a Custom Object In this step, you create a custom object called Book with one custom field called Price. 2. Add an Apex Class In this step, you add an Apex class that contains a method for updating the book price. This method is called by the trigger that you’ll be adding in the next step. 3. Add an Apex Trigger In this step, you create a trigger for the `Book__c` custom object that calls the `applyDiscount` method of the `MyHelloWorld` class that you created in the previous step. 4. Add a Test Class In this step, you add a test class with one test method. You also run the test and verify code coverage. The test method exercises and validates the code in the trigger and class. Also, it enables you to reach 100% code coverage for the trigger and class. 5. Deploy Components to Production In this step, you deploy the Apex code and the custom object you created previously to your production organization using change sets.

### Create a Custom Object

In this step, you create a custom object called Book with one custom field called Price. Prerequisites: A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org. For more information about creating a sandbox org, see “Sandbox Types and Templates” in Salesforce Help. To sign up for a free Developer org, see the Developer Edition Environment Sign Up Page . **1.** Log in to your sandbox or Developer org. **2.** From your management settings for custom objects, if you’re using Salesforce Classic, click **New Custom Object** , or if you’re using Lightning Experience, select **Create** > **Custom Object** . **3.** Enter `Book` for the label. **4.** Enter `Books` for the plural label. **5.** Click **Save** . Ta dah! You’ve now created your first custom object. Now let’s create a custom field. **6.** In the **Custom Fields & Relationships** section of the Book detail page, click **New** . **7.** Select Number for the data type and click **Next** . **8.** Enter `Price` for the field label. **9.** Enter 16 in the length text box. **10.** Enter 2 in the decimal places text box, and click **Next** . **11.** Click **Next** to accept the default values for field-level security. **12.** Click **Save** . You've created a custom object called Book, and added a custom field to that custom object. Custom objects already have some standard fields, like Name and CreatedBy, and allow you to add other fields that are more specific to your implementation. For this tutorial, the Price field is part of our Book object, and the Apex class you’ll write in the next step accesses it. Salesforce Help : Find Object Management Settings

### Add an Apex Class

In this step, you add an Apex class that contains a method for updating the book price. This method is called by the trigger that you’ll be adding in the next step. Prerequisites: A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org. The Book custom object . **1.** From Setup, enter “Apex Classes” in the `Quick` `Find` box, then select **Apex Classes** and click **New** . **2.** In the class editor, enter this class definition:

```apex
public class MyHelloWorld {
```

```apex
}
```

The previous code is the class definition to which you’ll be adding one method in the next step. Apex code is contained in classes. This class is defined as `public` , which means the class is available to other Apex classes and triggers. For more information, see Classes, Objects, and Interfaces on page 61. **3.** Add this method definition between the class opening and closing brackets.

```apex
public static void applyDiscount(Book__c[] books) {
```

```apex
for (Book__c b :books){
b.Price__c *= 0.9;
}
}
```

This method is called `applyDiscount` , and it’s both public and static. Because it’s a static method, you don't need to create an instance of the class to access the method—you can use the name of the class followed by a dot (.) and the name of the method. For more information, see Static and Instance Methods, Variables, and Initialization Code on page 70. This method takes one parameter, a list of Book records, which is assigned to the variable `books` . Notice the `__c` in the object name `Book__c` . This indicates that it’s a custom object that you created. Standard objects that are provided in the Salesforce application, such as Account, don't end with this postfix. The next section of code contains the rest of the method definition:

```apex
for (Book__c b :books){
b.Price__c *= 0.9;
}
```

Notice the `__c` after the field name `Price__c` . This indicates that it’s a custom field that you created. Standard fields that are provided by default in Salesforce are accessed using the same type of dot notation but without the `__c` , for example, `Name` doesn't end with `__c` in `Book__c.Name` . The statement `b.Price__c` `*=` `0.9;` takes the old value of `b.Price__c` , multiplies it by 0.9, which means its value is discounted by 10%, and then stores the new value into the `b.Price__c` field. The `*=` operator is a shortcut. Another way to write this statement is `b.Price__c` `=` `b.Price__c` `*` `0.9;` . See Expression Operators on page 40. **4.** Click **Save** to save the new class. You now have this full class definition.

```apex
public class MyHelloWorld {
```

```apex
public static void applyDiscount(Book__c[] books) {
```

```apex
for (Book__c b :books){
b.Price__c *= 0.9;
}
}
}
```

You now have a class that contains some code that iterates over a list of books and updates the Price field for each book. This code is part of the `applyDiscount` static method called by the trigger that you’ll create in the next step.

### Add an Apex Trigger

In this step, you create a trigger for the `Book__c` custom object that calls the `applyDiscount` method of the `MyHelloWorld` class that you created in the previous step. Prerequisites: A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org. The MyHelloWorld Apex class. A trigger is a piece of code that executes before or after records of a particular type are inserted, updated, or deleted from the Lightning Platform database. Every trigger runs with a set of context variables that provide access to the records that caused the trigger to fire. All triggers run in bulk; that is, they process several records at once. **1.** From the object management settings for books, go to Triggers, and then click **New** . **2.** In the trigger editor, delete the default template code and enter this trigger definition:

```apex
trigger HelloWorldTrigger on Book__c (before insert) {
```

```apex
Book__c[] books = Trigger.new;
```

```apex
MyHelloWorld.applyDiscount(books);
}
```

The first line of code defines the trigger:

```apex
trigger HelloWorldTrigger on Book__c (before insert) {
```

It gives the trigger a name, specifies the object on which it operates, and defines the events that cause it to fire. For example, this trigger is called HelloWorldTrigger, it operates on the `Book__c` object, and runs before new books are inserted into the database. The next line in the trigger creates a list of book records named `books` and assigns it the contents of a trigger context variable called `Trigger.` `new` . Trigger context variables such as `Trigger.` `new` are implicitly defined in all triggers and provide access to the records that caused the trigger to fire. In this case, `Trigger.` `new` contains all the new books that are about to be inserted.

```apex
Book__c[] books = Trigger.new;
```

The next line in the code calls the method `applyDiscount` in the `MyHelloWorld` class. It passes in the array of new books.

```apex
MyHelloWorld.applyDiscount(books);
```

You now have all the code that is needed to update the price of all books that get inserted. However, there’s still one piece of the puzzle missing. Unit tests are an important part of writing code and are required. In the next step, you'll see why this is so and will be able to add a test class. Salesforce Help : Find Object Management Settings

### Add a Test Class

In this step, you add a test class with one test method. You also run the test and verify code coverage. The test method exercises and validates the code in the trigger and class. Also, it enables you to reach 100% code coverage for the trigger and class. Prerequisites: A Salesforce account in a sandbox Professional, Enterprise, Performance, or Unlimited Edition org, or an account in a Developer org. The HelloWorldTrigger Apex trigger. Testing is an important part of the development process. Before you can deploy Apex or package it for AppExchange, the following must be true. Unit tests must cover at least 75% of your Apex code, and all of those tests must complete successfully. Note the following. When deploying Apex to a production organization, each unit test in your organization namespace is executed by default. Calls to `System.debug` aren’t counted as part of Apex code coverage. Test methods and test classes aren’t counted as part of Apex code coverage. While only 75% of your Apex code must be covered by tests, don’t focus on the percentage of code that is covered. Instead, make sure that every use case of your application is covered, including positive and negative cases, as well as bulk and single records. This approach ensures that 75% or more of your code is covered by unit tests. Every trigger must have some test coverage. All classes and triggers must compile successfully. **1.** From Setup, enter `Apex` `Classes` in the `Quick` `Find` box, then select **Apex Classes** and click **New** . **2.** In the class editor, add this test class definition, and then click **Save** .

```apex
@IsTest
private class HelloWorldTestClass {
```

```apex
@IsTest
static void validateHelloWorld() {
Book__c b = new Book__c(Name='Behind the Cloud', Price__c=100);
System.debug('Price before inserting new book: ' + b.Price__c);
```

```apex
// Insert book
insert b;
```

```apex
// Retrieve the new book
b = [SELECT Price__c FROM Book__c WHERE Id =:b.Id];
System.debug('Price after trigger fired: ' + b.Price__c);
```

```apex
// Test that the trigger correctly updated the price
System.assertEquals(90, b.Price__c);
```

```apex
}
}
```

This class is defined using the `@IsTest` annotation. Classes defined this way should only contain test methods and any methods required to support those test methods. One advantage to creating a separate class for testing is that classes defined with `@IsTest` don’t count against your org’s limit of 6 MB of Apex code. You can also add the `@IsTest` annotation to individual methods. For more information, see `@IsTest` Annotation on page 106 and Execution Governors and Limits . The method `validateHelloWorld` is defined using the `@IsTest` annotation. This annotation means that if changes are made to the database, they’re rolled back when execution completes. You don’t have to delete any test data created in the test method. The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a future release. First, the test method creates a book and inserts it into the database temporarily. The `System.debug` statement writes the value of the price in the debug log.

```apex
Book__c b = new Book__c(Name='Behind the Cloud', Price__c=100);
System.debug('Price before inserting new book: ' + b.Price__c);
```

```apex
// Insert book
insert b;
```

After the book is inserted, the code retrieves the newly inserted book, using the ID that was initially assigned to the book when it was inserted. The `System.debug` statement then logs the new price that the trigger modified.

```apex
// Retrieve the new book
b = [SELECT Price__c FROM Book__c WHERE Id =:b.Id];
System.debug('Price after trigger fired: ' + b.Price__c);
```

When the `MyHelloWorld` class runs, it updates the `Price__c` field and reduces its value by 10%. The following test verifies that the method `applyDiscount` ran and produced the expected result.

```apex
// Test that the trigger correctly updated the price
System.assertEquals(90, b.Price__c);
```

**3.** To run this test and view code coverage information, switch to the Developer Console. **4.** In the Developer Console, click **Test** > **New Run** . **5.** To select your test class, click **HelloWorldTestClass** . **6.** To add all methods in the `HelloWorldTestClass` class to the test run, click **Add Selected** . **7.** Click **Run** . The test result displays in the Tests tab. Optionally, you can expand the test class in the Tests tab to view which methods were run. In this case, the class contains only one test method. **8.** The Overall Code Coverage pane shows the code coverage of this test class. To view the percentage of lines of code in the trigger covered by this test, which is 100%, double-click the code coverage line for **HelloWorldTrigger** . Because the trigger calls a method from the `MyHelloWorld` class, this class also has coverage (100%). To view the class coverage, double-click **MyHelloWorld** . **9.** To open the log file, in the Logs tab, double-click the most recent log line in the list of logs. The execution log displays, including logging information about the trigger event, the call to the `applyDiscount` method, and the price before and after the trigger. By now, you’ve completed all the steps necessary for writing some Apex code with a test that runs in your development environment. In the real world, after you tested your code and are satisfied with it, you want to deploy the code and any prerequisite components to a production org. The next step shows you how to do this deployment for the code and custom object you created. Salesforce Help : Open the Developer Console

### Deploy Components to Production

In this step, you deploy the Apex code and the custom object you created previously to your production organization using change sets. Prerequisites: A Salesforce account in a sandbox Performance, Unlimited, or Enterprise Edition organization. The HelloWorldTestClass Apex test class. A deployment connection between the sandbox and production organizations that allows inbound change sets to be received by the production organization. See “Change Sets” in Salesforce Help. “Create and Upload Change Sets” user permission to create, edit, or upload outbound change sets. This procedure doesn't apply to Developer organizations since change sets are available only in Performance, Unlimited, Enterprise, or Database.com Edition organizations. If you have a Developer Edition account, you can use other deployment methods. For more information, see Deploying Apex . **1.** From Setup, enter `Outbound` `Changesets` in the `Quick` `Find` box, then select **Outbound Changesets** . **2.** If a splash page appears, click **Continue** . **3.** In the Change Sets list, click **New** . **4.** Enter a name for your change set, for example, `HelloWorldChangeSet` , and optionally a description. Click **Save** . **5.** In the Change Set Components section, click **Add** . **6.** Select Apex Class from the component type dropdown list, then select the MyHelloWorld and the HelloWorldTestClass classes from the list and click **Add to Change Set** . **7.** To add the dependent components, click **View/Add Dependencies** . **8.** To select all components, select the top checkbox. Click **Add To Change Set** . **9.** In the Change Set Detail section of the change set page, click **Upload** . **10.** Select the target organization, in this case production, and click **Upload** . **11.** After the change set upload completes, deploy it in your production organization. **a.** Log in to your production organization. **b.** From Setup, enter `Inbound` `Change` `Sets` in the `Quick` `Find` box, then select **Inbound Change Sets** . **c.** If a splash page appears, click **Continue** . **d.** In the change sets awaiting deployment list, click your change set's name. **e.** Click **Deploy** . In this tutorial, you learned how to create a custom object, how to add an Apex trigger, class, and test class. Finally, you also learned how to test your code, and how to upload the code and the custom object using Change Sets.
