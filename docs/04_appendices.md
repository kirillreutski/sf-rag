
# Appendices

test it with `System.runAs()` . See Version Apex in Managed Packages on page 767. Develop and Distribute Apex for Managed Packages Use Apex Referenced by Managed Packages

## Apex Reference

In Summer ’21 and later versions, Apex reference content is moved to a separate guide called the Apex Reference Guide. For reference information on Apex classes, interfaces, exceptions and so on, see Apex Reference Guide .

## Appendices

Apex Versioned Behavior Changes This document includes major Apex behavior changes across API versions, organized by version number for easy lookup. It isn’t an exhaustive list of all versioned Apex behavior. For example, this compilation excludes versioned changes to Connect in Apex and classes in the ConnectApi namespace. Shipping Invoice Example Reserved Keywords These words can be used only as keywords. Documentation Typographical Conventions Apex and Visualforce documentation uses these typographical conventions.

## Apex Versioned Behavior Changes

This document includes major Apex behavior changes across API versions, organized by version number for easy lookup. It isn’t an exhaustive list of all versioned Apex behavior. For example, this compilation excludes versioned changes to Connect in Apex and classes in the ConnectApi namespace. Keep these guidelines in mind regarding API version usage: Salesforce strongly recommends that you use the latest available API version. If you can't upgrade to the latest version yet, use API versions released in the past three years for improved performance, security, and compatibility. To reduce complexity, consolidate your Apex codebase to use the minimal number of API versions, ideally, just one API version.

### Version 67.0

**Database Operations in User Mode by Default** In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default. See Set an Access Mode for Database Operations . **Apex Classes Enforce Sharing by Default** In API version 67.0 and later, classes without an explicit sharing declaration are run in the current user context. In API version 66.0 and earlier, for classes without an explicit sharing declaration, the current sharing rule remains in effect. See Use the with sharing, without sharing, and inherited sharing Keywords . **WITH_SECURITY_ENFORCED Not Supported in SOQL Queries** With API version 67.0 and later, you cannot use the `WITH` `SECURITY_ENFORCED` clause in SOQL SELECT queries in Apex code. Instead, to run a SOQL or SOSL query in user mode, use the `WITH` `USER_MODE` clause.

### Version 65.0

**Access Modifiers with Abstract and Override Methods** In API version 65.0 and later, an abstract or override method requires a `protected` , `public` , or `global` access modifier. If one of these access modifiers isn't explicitly included in the method declaration, then method access defaults to private. Private access is invalid for these method types because the implementing class can't access the abstract method. Therefore, if you attempt to declare an abstract or override method without an allowed access modifier, you get the compilation error: Abstract methods require at least one of these modifiers: `global` , `public` , `protected` . See Extending a Class .

### Version 63.0

**DataWeave Version** API version 63.0 and later support DataWeave 2.9 script syntax. API version 62.0 supports DataWeave 2.8, and API version 61.0 and earlier support DataWeave 2.5. See Implementing DataWeave in Apex . **JSON Serialization of Exceptions** In API version 63.0 and later, JSON serialization of custom exceptions and most built-in exceptions isn't supported. Attempting to serialize an exception throws an error: Type unsupported in JSON: MyException. See JSON Support .

### Version 62.0

**DataWeave Version** API version 62.0 supports DataWeave 2.8 script syntax. API version 61.0 and earlier versions support DataWeave 2.5. See Implementing DataWeave in Apex .

### Version 61.0

**Private Method Override** In API version 61.0 and later, private methods are no longer overridden by an instance method with the same signature in a subclass. In API version 60.0 and earlier, if a subclass declares an instance method with the same signature as a private method in one of its superclasses, the subclass method overrides the private method. See Interfaces . **DMO Information** In API version 61.0 and later, you can get information on a specific DMO by using `SObjectType.getDescribe()` . Field-level security isn't enforced because all fields on DMOs that are accessed by field describes and security model checks are read-only. See Data Cloud In Apex .

### Version 60.0

`instanceof` **Operator with** `List` **and** `Iterable` In API version 60.0 and later, if a `List` data type implements the Iterable data type, compilation fails. See Using the instanceof Keyword . **Transaction Control: Savepoints** In API version 60.0 and later, all Apex test savepoints are released when `Test.startTest()` and `Test.stopTest()` are called. If any savepoints are reset, a SAVEPOINT_RESET event is logged. In API version 59.0 and earlier, making a callout after creating savepoints throws a CalloutException regardless of whether there was uncommitted DML or the changes were rolled back to a savepoint. In API version 60.0 and later, `Database.rollback(databaseSavepoint)` and `Database.setSavepoint()` calls don't increment the DML row usage limit. In API version 59.0 and earlier, these methods increment the DML row usage limit. See Transaction Control .

### API Reference Changes

API version 60.0 and later: `Database.rollback(databaseSavepoint)` and Database System `Database.setSavepoint()` calls don't increment the DML row usage limit. In API version 59.0 and earlier, these methods increment the DML row usage limit. See Database.rollBack() . API version 60.0 and later: Apex test savepoints are released when `Test.startTest()` and `Test.stopTest()` are called. If any Test System savepoints are reset, a SAVEPOINT_RESET event is logged. In API version 59.0 and earlier, making a callout after creating savepoints throws a CalloutException regardless of whether there was uncommitted DML or the changes were rolled back to a savepoint. See Database.rollBack() . API version 60.0 and later: Using an invalid namespace while calling this method returns null. Previously, Apex allowed you to specify an invalid Type System namespace such as `Type.forName(` `'InvalidNamespace'` `,` `'OuterClass.InnerClass'` `)` or use an outer class as a namespace such as `Type.forName(` `'OuterClass'` `,` `'InnerClass'` `)` with indeterminate results. See Type.forName() .

### Version 57.0

### API Reference Changes

API version 57.0 and later: The `toString()` method only includes member variables of Apex objects that are visible in the current Object System namespace. Non-global properties are suppressed from output when you invoke `toString()` on managed Apex types. To keep the non-global state of the object visible in debug output, you can explicitly override the `toString()` method. See Object.toString() .

### Version 55.0

**@AuraEnabled Annotation** In API version 55.0 and later, overloads aren't allowed on methods annotated with @AuraEnabled. See AuraEnabled Annotation .

### Version 54.0

### API Reference Changes

API version 54.0 and later: If you call `Date` `.valueOf` with a Datetime object, the method converts the object to a valid Date without the time information. See Date.valueOf() . Date System API version 54.0 and later: Assignment of an invalid 15 or 18 character ID to a variable results in a System.StringException exception. See Id.valueOf() . Id System API version 54.0 and later: For custom settings and custom metadata type objects, `DescribeSObjectResult.isAccessible()` DescribeSObjectResult Schema returns false if the user doesn't have permissions to access the queried objects. In API version 53.0 and earlier, the method returns true even if the user doesn't have the required permissions. See DescribeSObjectResult.isAccessible() . API version 54.0 and later: A null `emailMessageIds` parameter results in a System.IllegalArgumentException exception. In API version Messaging System 53.0 and earlier, a null `emailMessageIds` parameter results in an error. See Messaging.sendEmailMessage() .

### Version 53.0

**DataWeave Integration** Apex classes must be at API version 53.0 or later to access DataWeave integration methods. See Implementing DataWeave in Apex . **JSON DateTime Format** In API version 53.0 and later, DateTime format and processing has been updated. The API correctly handles DateTime values in JSON requests that use more than 3 digits after the decimal point. Requests that use an unsupported DateTime format (such as 123456000) result in an error. Salesforce recommends that you strictly adhere to DateTime formats specified in Valid Date and DateTime Formats. See Valid Date and DateTime Formats . **Trigger Order of Execution** In API version 53.0 and earlier, after-save record-triggered flows run after entitlements are executed. See Triggers and Order of Execution .

### API Reference Changes

API version 53.0 and later: The `getId()` method returns the sObject ID. However, if record locking fails during the update operation, the SaveResult Database method returns a null value. In API version 52.0 and earlier, the `getId()` method returns a null value if the record isn't updated successfully. See SaveResult.getId() . API version 53.0 and later: The `getId()` method returns the sObject ID. However, if record locking fails during the update operation, the UpsertResult Database method returns a null value. In API version 52.0 and earlier, the `getId()` method returns a null value if the record isn't updated successfully. See UpsertResult.getId() .

### Version 52.0

**CardPaymentMethods and DigitalWallets** In API version 52.0 and later, CardPaymentMethods and DigitalWallets can’t store values for GatewayTokenEncryption and GatewayToken at the same time on the same record. If you try to assign one while the other exists, Salesforce throws an error. See Tokenization Service Apex Class Implementation .

### API Reference Changes

API version 52.0 and later: If the `executeBatch` call fails to acquire an Apex flex queue lock, the call throws a System.AsyncException. In API Database System version 51.0 and earlier, if the executeBatch call fails to acquire an Apex flex queue lock, the call returns an empty ID, "000000000000000", instead of throwing an exception. See Database.executeBatch() .

### Version 51.0

### API Reference Changes

API version 51.0 and later: The `getReferenceTo()` method returns referenced objects that aren't accessible to the context user. If the context DescribeFieldResult Schema user has access to an object's field that references another object, irrespective of the context user's access to the cross-referenced object, the method returns references. In API version 50.0 and earlier, if the context user doesn't have access to the cross-referenced object, the method returns an empty list. See DescribeFieldResult.getReferenceTo() . API version 51.0 and later: The `format()` method supports single quotes in the stringToFormat parameter and returns a formatted string String System using the formattingArguments parameter. In version 50.0 and earlier, single quotes aren't supported. See String.format() . API version 51.0 and later: The `hashCode()` method returns the same hashCode for identical Id values. In API version 50.0 and earlier, identical System System Id values don't always generate the same hashCode value. See System.hashCode() .

### Version 50.0

**@NamespaceAccessible Annotation** In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are annotated with @NamespaceAccessible. See NamespaceAccessible Annotation and Class Variables .

### Version 49.0

**@JsonAccess Annotation** In API version 49.0 and later, the default access for both serialization and deserialization is `sameNamespace` . In API version 48.0 and earlier, the default access for deserialization is `always` and the default access for serialization is `sameNamespace` to preserve the existing behavior. See JsonAccess Annotation . **@ReadOnly Annotation on REST Methods** In API version 49.0 and later, you can annotate Apex REST methods with just @ReadOnly. In API version 49.0 and earlier, Apex REST methods with the @ReadOnly annotation also require the @RemoteAction annotation. See ReadOnly Annotation .

### Version 47.0

**@NamespaceAccessible Annotation** In API version 47.0 and later, @NamespaceAccessible isn't allowed on an entity marked with @AuraEnabled. Therefore, an Aura or Lightning web component installed from a package can't call an Apex method from another package, even if both packages are in the same namespace. However, an @AuraEnabled public method from one package can call a @NamespaceAccessible public method from another package in the same namespace. See NamespaceAccessible Annotation .

### API Reference Changes

`changedfields` Properties in `EventBus.ChangeEventHeader` : A list of the fields that were changed in an update operation, including the LastModifiedDate system field. This field is empty for other operations, including record creation. This property is available in Apex saved using API version 47.0 or later. See ChangeEventHeader Properties .

### Version 45.0

**WITH SECURITY_ENFORCED Clause in SOQL** The WITH SECURITY_ENFORCED clause is only available in Apex. We don’t recommend using WITH SECURITY_ENFORCED in Apex classes or triggers with an API version earlier than 45.0. See Filter SOQL Queries Using WITH SECURITY_ENFORCED .

### API Reference Changes

API version 45.0 and later: `getDisplayName()` displays Daylight Savings Time appropriately when daylight savings is in effect. For example, TimeZone System British Summer Time is displayed for Europe/London and Pacific Daylight Time for America/Los_Angeles. See TimeZone.getdisplayName() .

### Version 44.0

**BatchApexErrorEvent** The BatchApexErrorEvent object represents a platform event associated with a batch Apex class. This object is available in API version 44.0 and later. If the `start` , `execute` , or `finish` method of a batch Apex job encounters an unhandled exception, a `BatchApexErrorEvent` platform event is fired. For more details, see BatchApexErrorEvent **AuraEnabled Annotation** In API version 44.0 and later, you can improve runtime performance by caching method results on the client by using the annotation `@AuraEnabled(cacheable=` `true` `)` . You can cache method results only for methods that retrieve data but don’t modify it. Using this annotation eliminates the need to call `setStorable()` in JavaScript code on every action that calls the Apex method. See AuraEnabled Annotation .

### Version 42.0

**Hierarchy Custom Settings** In API version 42.0 and later, if a hierarchy custom setting is inserted in a `testSetup` method, inserting a hierarchy custom setting record with the same SetupOwnerId in a test method throws a DUPLICATE_VALUE exception. In API version 41.0 and earlier, each method in an Apex test class, including `testSetup` methods, is able to insert hierarchy custom setting values. This behavior is true even when the methods have the same SetupOwnerId value as a hierarchy custom setting record inserted in a different test method. See Hierarchy Custom Setting Methods . **Apex Properties** In API version 42.0 and later, unless a variable value is set in a set accessor, you can’t update its value in a get accessor. See Apex Properties .

### Version 41.0

**Exception Handling** In API version 41.0 and later, unreachable statements in your code cause compilation errors. See Exception Statements .

### API Reference Changes

API version 41.0 and later: Apex URL objects are represented by the java.net.URI type, not the java.net.URL type. The API version in which the URL System URL object was instantiated determines the behavior of subsequent method calls to the specific instance. Salesforce strongly encourages you to use API version 41.0 and later for fully RFC-compliant URL parsing that includes proper handling of edge cases of complex URL structures. In API version 41.0 and later, inputs must be valid, RFC-compliant URL or URI strings. See URL Class .

### Version 39.0

### API Reference Changes

API version 39.0 and later: `getPopulatedFieldsAsMap()` returns all values set on the SObject, even if values were set after the record was SObject System queried. This behavior is dependent on the version of the Apex class calling this method and not on the version of the class that generated the SObject. If you query an SObject at API version 20.0, and then call this method in a class with API version 40.0, you will get the full set of fields. See SObject.getPopulatedFieldsAsMap() .

### Version 35.0

**Serialization of IDs** In API version 35.0 and later, ID comparison using `==` does not fail for IDs that have been through roundtrip JSON serialization and deserialization. See Roundtrip Serialization and Deserialization .

### API Reference Changes

When deserializing JSON content into an Apex class in any API version, or into an object in API version 35.0 or later, no exception is thrown. When JSON System deserializing JSON content into a custom object or an sObject using Salesforce API version 34.0 or earlier, the `deserialize(jsonString,` `apexType)` and `readValueAs(apexType)` methods throw a runtime exception when passed extraneous attributes. See JSON.deserialize(jsonString, apexType) and JSONParser.readValueAs() . In API version 34.0 and later, `getContent()` and `getContentAsPDF()` are treated as callouts. If you use PageReference System `getContent()` or `getContentAsPDF()` in a test method, the test method fails. See PageReference.getContent() . In API version 35.0 and later, the `split()` method works correctly if you use a zero-width regExp parameter. In API version 34.0 and earlier, Pattern System a zero-width regExp value produces an empty list item at the beginning of the `split()` method output. See Pattern.split() .

### Version 34.0

**Schema Namespace Prefixes** In API version 34.0 and later, `Schema.DescribeSObjectResult` on a custom SObjectType includes map keys prefixed with the namespace, even if the namespace is that of currently executing code. If you work with multiple namespaces and generate run-time describe data, make sure that your code accesses keys correctly by using the namespace prefix. See Namespace Prefix .

### API Reference Changes

API version 34.0 to 53.0: If you call `Date` `.valueOf` with a `Datetime` object, the method converts `Datetime` to a valid `Date` without the Date System time information, but the result depends on the manner in which the `Datetime` object was initialized. For example, if the `Datetime` object was initialized using `Datetime` `.valueOf(stringDate)` , the returned `Date` value contains time (hours) information. If the `Datetime` object is initialized by using `Datetime` `.newInstance(year,` `month,` `day,` `hour,` `minute,` `second)` , the returned Date value doesn't contain time information. See Date.valueOf() . In API version 34.0 and later, you must include the namespace name to retrieve a field from a field Map using the `get(fieldName)` method. SObject System For example, to get the account__c field in the MyNamespace namespace from field Map called "fields", use: `fields.get(` `'MyNamespace__account__c'` `)` . See SObject.get(fieldName) .

### Version 33.0

### API Reference Changes

In API version 33.0 and earlier, if you call `Date` `.valueOf` with a Datetime object, the method returns a Date value that contains the hours, minutes, seconds, and milliseconds set. See Date.valueOf() . Date System

### Version 32.0

`instanceof` **Operator** In API version 32.0 and later, `instanceof` returns `false` if the left operand is a null object. In API version 31.0 and earlier, `instanceof` returns `true` in this case. See Using the Instance of Keyword .

### Version 28.0

**Null Fields in JSON Serialization** In API version 28.0 and later, null fields aren’t serialized and aren’t included in the JSON string, unlike in earlier versions. This change doesn’t affect deserializing JSON strings with JSON methods, such as Json.deserialize() . This change is noticeable when you inspect the JSON string. **VLOOKUP Validation Rule Function** In API version 28.0 and later, the VLOOKUP validation rule function no longer accesses organization data from a running Apex test. The function looks up only data created by the test, unless the test class or method is annotated with `IsTest(SeeAllData=` `true` `)` . In API version 27.0 and earlier, the VLOOKUP validation rule function always looks up org data in addition to test data when fired by a running Apex test. See Isolation of Test Data from Organization Data in Unit Tests .

### Version 26.0

**Chaining Batch Jobs** In API version 26.0 and later, you can start another batch job from an existing batch job to chain jobs together, enforcing strict sequential execution. See Use Batch Apex . **Calling** `Database.executeBatch` **and** `System.scheduleBatch` **Methods** In API version 26.0 and later, you can call `Database.executeBatch` and `System.scheduleBatch` from any batch Apex method. See Use Batch Apex .

### Version 24.0

**Apex Test Methods** In API version 24.0 and later, Apex test methods can’t access pre-existing org data by default, such as standard objects, custom objects, and custom settings data. They can only access data that they create. However, objects that are used to manage your organization or metadata objects can still be accessed in your tests. In API version 23.0 and earlier, test code continues to have access to all data in the organization and its data access is unchanged. See Isolation of Test Data from Organization Data in Unit Tests .

### Version 22.0

**Batch Apex Exceptions with Test Methods** In API version 22.0 and later, exceptions that occur during the execution of a batch Apex job invoked by a test method are passed to the calling test method. As a result, these exceptions cause the test method to fail. See Use Batch Apex .

### Version 21.0

**Bulk API Requests** In API version 21.0 and later, if a Bulk API request causes a trigger to fire, each chunk of 200 records for the trigger to process is no longer split into smaller chunks. If a Bulk API request causes a trigger to fire multiple times for chunks of 200 records, governor limits are reset between these trigger invocations for the same HTTP request. Static variables aren’t reset within the multiple trigger invocations for the same Bulk API request. In API version 20.0 and earlier, if a Bulk API request causes a trigger to fire, each chunk of 200 records for the trigger to process is split into chunks of 100 records. `FeedPost` **Objects** In API version 21.0, insert and delete triggers on FeedPost objects are supported. In API version 20.0 and earlier, these trigger operations on FeedPost aren't supported. See Triggers for Chatter Objects . The `FeedPost` object is discontinued in API version 22.0 and later. Use `FeedItem` instead. See FeedItem

### Version 17.0

**HTTP Response Decoding** In API version 17.0 and later, HTTP responses are decoded using the encoding specified in the Content-Type header. In API versions 16.0 and earlier, HTTP responses for callouts are always decoded using UTF-8, regardless of the Content-Type header. See SOAP Services: Defining a Class from a WSDL Document .

### Version 16.0

**Decimal Data Type** In API version 16.0 and later, Apex uses the higher-precision `Decimal` data type in certain types such as currency. See Primitive Data Types .

### Version 15.0

`anyType` **datatype** The Salesforce datatype `anyType` is not supported in WSDLs used to generate Apex code that is saved by using API version 15.0 and later. In API version 14.0 and earlier, `anyType` is mapped to String. See SOAP Services: Defining a Class from a WSDL Document . **DMLOptions Settings** DMLOptions settings are only available for Apex saved against API versions 15.0 and higher. DMLOptions settings take effect only for record operations performed by using Apex DML and not through the Salesforce user interface. In API version 15.0 and later, the Database.DMLOptions `emailHeader` property enables you to specify information about the email sent when an event occurs because of Apex DML code execution. See Setting DML Options . **String values** In API version 15.0 and higher, assigning a `String` value that is too long for the field produces a run-time error.

## Shipping Invoice Example

This appendix provides an example of an Apex application. This is a more complex example than the Hello World example. Shipping Invoice Walk-Through Shipping Invoice Example Code 1. Shipping Invoice Example Walk-Through 2. Shipping Invoice Example Code

### Shipping Invoice Example Walk-Through

The sample application in this section includes traditional Salesforce functionality blended with Apex. Many of the syntactic and semantic features of Apex, along with common idioms, are illustrated in this application. The Shipping Invoice sample requires custom objects. You can either create these on your own, or download the objects and Apex code as an unmanaged package from the Salesforce AppExchange. To obtain the sample assets in your org, install the Apex Tutorials Package . This package also contains sample code and objects for the Apex Quick Start .

#### Scenario

In this sample application, the user creates a new shipping invoice, or order, and then adds items to the invoice. The total amount for the order, including shipping cost, is automatically calculated and updated based on the items added or deleted from the invoice.

#### Data and Code Models

This sample application uses two new objects: Item and Shipping_invoice. The following assumptions are made: Item A cannot be in both orders shipping_invoice1 and shipping_invoice2. Two customers cannot obtain the same (physical) product. The tax rate is 9.25%. The shipping rate is 75 cents per pound. Once an order is over $100, the shipping discount is applied (shipping becomes free). The fields in the Item custom object include: The name of the item String Name The price of the item Currency Price The number of items in the order Number Quantity The weight of the item, used to calculate shipping costs Number Weight The order this item is associated with Master-Detail (shipping_invoice) Shipping_invoice The fields in the Shipping_invoice custom object include: The name of the shipping invoice/order String Name The subtotal Currency Subtotal The total amount, including tax and shipping Currency GrandTotal The amount charged for shipping (assumes $0.75 per pound) Currency Shipping Only applied once when subtotal amount reaches $100 Currency ShippingDiscount The amount of tax (assumes 9.25%) Currency Tax The total weight of all items Number TotalWeight All of the Apex for this application is contained in triggers. This application has the following triggers: Updates the shipping invoice, calculates the totals and shipping after insert, after update, after delete Calculate Item Updates the shipping invoice, calculating if there is a shipping discount after update ShippingDiscount Shipping_invoice The following is the general flow of user actions and when triggers run: **Flow of user action and triggers for the shopping cart application** **1.** User clicks **Orders** > **New** , names the shipping invoice and clicks **Save** . **2.** User clicks **New Item** , fills out information, and clicks **Save** . **3.** Calculate trigger runs. Part of the Calculate trigger updates the shipping invoice. **4.** ShippingDiscount trigger runs. **5.** User can then add, delete or change items in the invoice. In Shipping Invoice Example Code both of the triggers and the test class are listed. The comments in the code explain the functionality.

#### Testing the Shipping Invoice Application

Before an application can be included as part of a package, 75% of the code must be covered by unit tests. Therefore, one piece of the shipping invoice application is a class used for testing the triggers. The test class verifies the following actions are completed successfully: Inserting items Updating items Deleting items Applying shipping discount Negative test for bad input

### Shipping Invoice Example Code

The following triggers and test class make up the shipping invoice example application: Calculate trigger ShippingDiscount trigger Test class

#### Calculate Trigger

```apex
trigger calculate on Item__c (after insert, after update, after delete) {
```

```apex
// Use a map because it doesn't allow duplicate values
```

```apex
Map<ID, Shipping_Invoice__C> updateMap = new Map<ID, Shipping_Invoice__C>();
```

```apex
// Set this integer to -1 if we are deleting
Integer subtract ;
```

```apex
// Populate the list of items based on trigger type
List<Item__c> itemList;
```

```apex
if(trigger.isInsert || trigger.isUpdate){
itemList = Trigger.new;
subtract = 1;
}
else if(trigger.isDelete)
{
```

```apex
// Note -- there is no trigger.new in delete
itemList = trigger.old;
subtract = -1;
}
```

```apex
// Access all the information we need in a single query
// rather than querying when we need it.
// This is a best practice for bulkifying requests
```

```apex
set<Id> AllItems = new set<id>();
```

```apex
for(item__c i :itemList){
// Assert numbers are not negative.
// None of the fields would make sense with a negative value
```

```apex
System.assert(i.quantity__c > 0, 'Quantity must be positive');
System.assert(i.weight__c >= 0, 'Weight must be non-negative');
System.assert(i.price__c >= 0, 'Price must be non-negative');
```

```apex
// If there is a duplicate Id, it won't get added to a set
AllItems.add(i.Shipping_Invoice__C);
}
```

```apex
// Accessing all shipping invoices associated with the items in the trigger
List<Shipping_Invoice__C> AllShippingInvoices = [SELECT Id, ShippingDiscount__c,
SubTotal__c, TotalWeight__c, Tax__c, GrandTotal__c
FROM Shipping_Invoice__C WHERE Id IN :AllItems];
```

```apex
// Take the list we just populated and put it into a Map.
// This will make it easier to look up a shipping invoice
```

```apex
// because you must iterate a list, but you can use lookup for a map,
Map<ID, Shipping_Invoice__C> SIMap = new Map<ID, Shipping_Invoice__C>();
```

```apex
for(Shipping_Invoice__C sc : AllShippingInvoices)
{
SIMap.put(sc.id, sc);
}
```

```apex
// Process the list of items
```

```apex
if(Trigger.isUpdate)
{
```

```apex
// Treat updates like a removal of the old item and addition of the
// revised item rather than figuring out the differences of each field
// and acting accordingly.
// Note updates have both trigger.new and trigger.old
for(Integer x = 0; x < Trigger.old.size(); x++)
{
Shipping_Invoice__C myOrder;
myOrder = SIMap.get(trigger.old[x].Shipping_Invoice__C);
```

```apex
// Decrement the previous value from the subtotal and weight.
myOrder.SubTotal__c -= (trigger.old[x].price__c *
```

```apex
trigger.old[x].quantity__c);
myOrder.TotalWeight__c -= (trigger.old[x].weight__c *
```

```apex
trigger.old[x].quantity__c);
```

```apex
// Increment the new subtotal and weight.
myOrder.SubTotal__c += (trigger.new[x].price__c *
```

```apex
trigger.new[x].quantity__c);
myOrder.TotalWeight__c += (trigger.new[x].weight__c *
```

```apex
trigger.new[x].quantity__c);
}
```

```apex
for(Shipping_Invoice__C myOrder : AllShippingInvoices)
{
```

```apex
// Set tax rate to 9.25%
Please note, this is a simple example.
// Generally, you would never hard code values.
// Leveraging Custom Settings for tax rates is a best practice.
// See Custom Settings in the Apex Developer Guide
// for more information.
myOrder.Tax__c = myOrder.Subtotal__c * .0925;
```

```apex
// Reset the shipping discount
myOrder.ShippingDiscount__c = 0;
```

```apex
// Set shipping rate to 75 cents per pound.
// Generally, you would never hard code values.
// Leveraging Custom Settings for the shipping rate is a best practice.
// See Custom Settings in the Apex Developer Guide
// for more information.
myOrder.Shipping__c = (myOrder.totalWeight__c * .75);
myOrder.GrandTotal__c = myOrder.SubTotal__c + myOrder.tax__c +
myOrder.Shipping__c;
```

```apex
updateMap.put(myOrder.id, myOrder);
}
}
else
{
```

```apex
for(Item__c itemToProcess : itemList)
{
Shipping_Invoice__C myOrder;
```

```apex
// Look up the correct shipping invoice from the ones we got earlier
myOrder = SIMap.get(itemToProcess.Shipping_Invoice__C);
myOrder.SubTotal__c += (itemToProcess.price__c *
itemToProcess.quantity__c * subtract);
myOrder.TotalWeight__c += (itemToProcess.weight__c *
itemToProcess.quantity__c * subtract);
}
```

```apex
for(Shipping_Invoice__C myOrder : AllShippingInvoices)
{
```

```apex
// Set tax rate to 9.25%
Please note, this is a simple example.
// Generally, you would never hard code values.
// Leveraging Custom Settings for tax rates is a best practice.
// See Custom Settings in the Apex Developer Guide
// for more information.
myOrder.Tax__c = myOrder.Subtotal__c * .0925;
```

```apex
// Reset shipping discount
myOrder.ShippingDiscount__c = 0;
```

```apex
// Set shipping rate to 75 cents per pound.
// Generally, you would never hard code values.
// Leveraging Custom Settings for the shipping rate is a best practice.
// See Custom Settings in the Apex Developer Guide
// for more information.
myOrder.Shipping__c = (myOrder.totalWeight__c * .75);
myOrder.GrandTotal__c = myOrder.SubTotal__c + myOrder.tax__c +
myOrder.Shipping__c;
```

```apex
updateMap.put(myOrder.id, myOrder);
```

```apex
}
}
```

```apex
// Only use one DML update at the end.
// This minimizes the number of DML requests generated from this trigger.
update updateMap.values();
}
```

#### ShippingDiscount Trigger

```apex
trigger ShippingDiscount on Shipping_Invoice__C (before update) {
```

```apex
// Free shipping on all orders greater than $100
```

```apex
for(Shipping_Invoice__C myShippingInvoice : Trigger.new)
{
```

```apex
if((myShippingInvoice.subtotal__c >= 100.00) &&
(myShippingInvoice.ShippingDiscount__c == 0))
{
myShippingInvoice.ShippingDiscount__c =
myShippingInvoice.Shipping__c * -1;
myShippingInvoice.GrandTotal__c += myShippingInvoice.ShippingDiscount__c;
}
}
}
```

#### Shipping Invoice Test

```apex
@IsTest
private class TestShippingInvoice{
```

```apex
// Test for inserting three items at once
public static testmethod void testBulkItemInsert(){
```

```apex
// Create the shipping invoice. It's a best practice to either use defaults
// or to explicitly set all values to zero so as to avoid having
// extraneous data in your test.
Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,
totalweight__c = 0, grandtotal__c = 0,
ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);
```

```apex
// Insert the order and populate with items
insert Order1;
List<Item__c> list1 = new List<Item__c>();
Item__c item1 = new Item__C(Price__c = 10, weight__c = 1, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item2 = new Item__C(Price__c = 25, weight__c = 2, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 1,
Shipping_Invoice__C = order1.id);
list1.add(item1);
list1.add(item2);
list1.add(item3);
insert list1;
```

```apex
// Retrieve the order, then do assertions
order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,
grandtotal__c, shippingdiscount__c
FROM Shipping_Invoice__C
WHERE id = :order1.id];
```

```apex
System.assert(order1.subtotal__c == 75,
```

```apex
'Order subtotal was not $75, but was '+ order1.subtotal__c);
System.assert(order1.tax__c == 6.9375,
```

```apex
'Order tax was not $6.9375, but was ' + order1.tax__c);
System.assert(order1.shipping__c == 4.50,
```

```apex
'Order shipping was not $4.50, but was ' + order1.shipping__c);
```

```apex
System.assert(order1.totalweight__c == 6.00,
```

```apex
'Order weight was not 6 but was ' + order1.totalweight__c);
System.assert(order1.grandtotal__c == 86.4375,
```

```apex
'Order grand total was not $86.4375 but was '
```

```apex
+ order1.grandtotal__c);
System.assert(order1.shippingdiscount__c == 0,
```

```apex
'Order shipping discount was not $0 but was '
+ order1.shippingdiscount__c);
}
```

```apex
// Test for updating three items at once
public static testmethod void testBulkItemUpdate(){
```

```apex
// Create the shipping invoice. It's a best practice to either use defaults
// or to explicitly set all values to zero so as to avoid having
// extraneous data in your test.
Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,
totalweight__c = 0, grandtotal__c = 0,
ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);
```

```apex
// Insert the order and populate with items.
insert Order1;
List<Item__c> list1 = new List<Item__c>();
Item__c item1 = new Item__C(Price__c = 1, weight__c = 1, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item2 = new Item__C(Price__c = 2, weight__c = 2, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item3 = new Item__C(Price__c = 4, weight__c = 3, quantity__c = 1,
Shipping_Invoice__C = order1.id);
list1.add(item1);
list1.add(item2);
list1.add(item3);
insert as system list1;
```

```apex
// Update the prices on the 3 items
list1[0].price__c = 10;
list1[1].price__c = 25;
list1[2].price__c = 40;
update as system list1;
```

```apex
// Access the order and assert items updated
order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,
grandtotal__c, shippingdiscount__c
FROM Shipping_Invoice__C
WHERE Id = :order1.Id];
```

```apex
System.assert(order1.subtotal__c == 75,
```

```apex
'Order subtotal was not $75, but was '+ order1.subtotal__c);
System.assert(order1.tax__c == 6.9375,
```

```apex
'Order tax was not $6.9375, but was ' + order1.tax__c);
System.assert(order1.shipping__c == 4.50,
```

```apex
'Order shipping was not $4.50, but was '
+ order1.shipping__c);
System.assert(order1.totalweight__c == 6.00,
```

```apex
'Order weight was not 6 but was ' + order1.totalweight__c);
System.assert(order1.grandtotal__c == 86.4375,
```

```apex
'Order grand total was not $86.4375 but was '
+ order1.grandtotal__c);
System.assert(order1.shippingdiscount__c == 0,
```

```apex
'Order shipping discount was not $0 but was '
+ order1.shippingdiscount__c);
```

```apex
}
```

```apex
// Test for deleting items
public static testmethod void testBulkItemDelete(){
```

```apex
// Create the shipping invoice. It's a best practice to either use defaults
// or to explicitly set all values to zero so as to avoid having
// extraneous data in your test.
Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,
totalweight__c = 0, grandtotal__c = 0,
ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);
```

```apex
// Insert the order and populate with items
insert Order1;
List<Item__c> list1 = new List<Item__c>();
Item__c item1 = new Item__C(Price__c = 10, weight__c = 1, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item2 = new Item__C(Price__c = 25, weight__c = 2, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c itemA = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c itemB = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c itemC = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c itemD = new Item__C(Price__c = 1, weight__c = 3, quantity__c = 1,
Shipping_Invoice__C = order1.id);
list1.add(item1);
list1.add(item2);
list1.add(item3);
list1.add(itemA);
list1.add(itemB);
list1.add(itemC);
list1.add(itemD);
insert list1;
```

```apex
// Seven items are now in the shipping invoice.
// The following deletes four of them.
```

```apex
List<Item__c> list2 = new List<Item__c>();
list2.add(itemA);
list2.add(itemB);
list2.add(itemC);
list2.add(itemD);
delete list2;
```

```apex
// Retrieve the order and verify the deletion
order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,
grandtotal__c, shippingdiscount__c
FROM Shipping_Invoice__C
WHERE Id = :order1.Id];
```

```apex
System.assert(order1.subtotal__c == 75,
```

```apex
'Order subtotal was not $75, but was '+ order1.subtotal__c);
System.assert(order1.tax__c == 6.9375,
```

```apex
'Order tax was not $6.9375, but was ' + order1.tax__c);
System.assert(order1.shipping__c == 4.50,
```

```apex
'Order shipping was not $4.50, but was ' + order1.shipping__c);
System.assert(order1.totalweight__c == 6.00,
```

```apex
'Order weight was not 6 but was ' + order1.totalweight__c);
System.assert(order1.grandtotal__c == 86.4375,
```

```apex
'Order grand total was not $86.4375 but was '
+ order1.grandtotal__c);
System.assert(order1.shippingdiscount__c == 0,
```

```apex
'Order shipping discount was not $0 but was '
+ order1.shippingdiscount__c);
}
// Testing free shipping
public static testmethod void testFreeShipping(){
```

```apex
// Create the shipping invoice. It's a best practice to either use defaults
// or to explicitly set all values to zero so as to avoid having
// extraneous data in your test.
Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,
totalweight__c = 0, grandtotal__c = 0,
ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);
```

```apex
// Insert the order and populate with items.
insert Order1;
List<Item__c> list1 = new List<Item__c>();
Item__c item1 = new Item__C(Price__c = 10, weight__c = 1,
quantity__c = 1, Shipping_Invoice__C = order1.id);
Item__c item2 = new Item__C(Price__c = 25, weight__c = 2,
quantity__c = 1, Shipping_Invoice__C = order1.id);
Item__c item3 = new Item__C(Price__c = 40, weight__c = 3,
quantity__c = 1, Shipping_Invoice__C = order1.id);
list1.add(item1);
list1.add(item2);
list1.add(item3);
insert list1;
```

```apex
// Retrieve the order and verify free shipping not applicable
order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,
grandtotal__c, shippingdiscount__c
FROM Shipping_Invoice__C
WHERE Id = :order1.Id];
```

```apex
// Free shipping not available on $75 orders
System.assert(order1.subtotal__c == 75,
```

```apex
'Order subtotal was not $75, but was '+ order1.subtotal__c);
System.assert(order1.tax__c == 6.9375,
```

```apex
'Order tax was not $6.9375, but was ' + order1.tax__c);
System.assert(order1.shipping__c == 4.50,
```

```apex
'Order shipping was not $4.50, but was ' + order1.shipping__c);
System.assert(order1.totalweight__c == 6.00,
```

```apex
'Order weight was not 6 but was ' + order1.totalweight__c);
System.assert(order1.grandtotal__c == 86.4375,
```

```apex
'Order grand total was not $86.4375 but was '
+ order1.grandtotal__c);
System.assert(order1.shippingdiscount__c == 0,
```

```apex
'Order shipping discount was not $0 but was '
+ order1.shippingdiscount__c);
```

```apex
// Add items to increase subtotal
item1 = new Item__C(Price__c = 25, weight__c = 20, quantity__c = 1,
Shipping_Invoice__C = order1.id);
insert item1;
```

```apex
// Retrieve the order and verify free shipping is applicable
order1 = [SELECT id, subtotal__c, tax__c, shipping__c, totalweight__c,
grandtotal__c, shippingdiscount__c
FROM Shipping_Invoice__C
WHERE Id = :order1.Id];
```

```apex
// Order total is now at $100, so free shipping should be enabled
System.assert(order1.subtotal__c == 100,
```

```apex
'Order subtotal was not $100, but was '+ order1.subtotal__c);
System.assert(order1.tax__c == 9.25,
```

```apex
'Order tax was not $9.25, but was ' + order1.tax__c);
System.assert(order1.shipping__c == 19.50,
```

```apex
'Order shipping was not $19.50, but was '
+ order1.shipping__c);
System.assert(order1.totalweight__c == 26.00,
```

```apex
'Order weight was not 26 but was ' + order1.totalweight__c);
System.assert(order1.grandtotal__c == 109.25,
```

```apex
'Order grand total was not $86.4375 but was '
+ order1.grandtotal__c);
System.assert(order1.shippingdiscount__c == -19.50,
```

```apex
'Order shipping discount was not -$19.50 but was '
+ order1.shippingdiscount__c);
}
```

```apex
// Negative testing for inserting bad input
public static testmethod void testNegativeTests(){
```

```apex
// Create the shipping invoice. It's a best practice to either use defaults
// or to explicitly set all values to zero so as to avoid having
// extraneous data in your test.
Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,
totalweight__c = 0, grandtotal__c = 0,
ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);
```

```apex
// Insert the order and populate with items.
```

```apex
insert Order1;
Item__c item1 = new Item__C(Price__c = -10, weight__c = 1, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item2 = new Item__C(Price__c = 25, weight__c = -2, quantity__c = 1,
Shipping_Invoice__C = order1.id);
Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = -1,
Shipping_Invoice__C = order1.id);
Item__c item4 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 0,
Shipping_Invoice__C = order1.id);
```

```apex
try{
```

```apex
insert item1;
}
catch(Exception e)
{
system.assert(e.getMessage().contains('Price must be non-negative'),
```

```apex
'Price was negative but was not caught');
}
```

```apex
try{
```

```apex
insert item2;
}
catch(Exception e)
{
system.assert(e.getMessage().contains('Weight must be non-negative'),
```

```apex
'Weight was negative but was not caught');
}
```

```apex
try{
```

```apex
insert item3;
}
catch(Exception e)
{
system.assert(e.getMessage().contains('Quantity must be positive'),
```

```apex
'Quantity was negative but was not caught');
}
```

```apex
try{
```

```apex
insert item4;
}
catch(Exception e)
{
system.assert(e.getMessage().contains('Quantity must be positive'),
```

```apex
'Quantity was zero but was not caught');
}
}
}
```

## Reserved Keywords

These words can be used only as keywords. **Table 12: Reserved Keywords** package false abstract parallel final activate pragma finally and private float any protected for array public from as retrieve global asc return goto autonomous rollback group begin select having bigdecimal set hint blob short if boolean sObject implements break sort import bulk static in by string inner byte super insert case switch instanceof cast synchronized int catch system integer char testmethod interface class then into collect this join commit throw like const time limit continue transaction list currency trigger long date true loop datetime try map decimal undelete merge default update new delete upsert not desc using null do virtual nulls double void number else webservice object end when of enum where on exception or exit while outer export override extends These words are special types of keywords that aren't reserved words and can be used as identifiers. after before count excludes first includes last order sharing with

## Documentation Typographical Conventions

Apex and Visualforce documentation uses these typographical conventions. In descriptions of syntax, a monospace font indicates items that you should type as shown, except for brackets. For example:

```apex
Public class HelloWorld
```

```apex
Courier font
```

In descriptions of syntax, italics represent variables. You supply the actual value. In the following example, three values must be supplied: `datatype` `variable_name` [ = `value` ]; If the syntax is bold and italic, the text represents a code element that needs a value supplied by you, such as a class name or variable value:

```apex
public static class YourClassHere { ... }
```

```apex
Italics
```

In code samples and syntax descriptions, a bold courier font emphasizes a portion of the code or syntax. `Bold` `Courier` `font` In descriptions of syntax, less-than and greater-than symbols (< >) are typed exactly as shown.

```apex
<apex:pageBlockTable value="{!account.Contacts}" var="contact">
```

< >

```apex
<apex:column value="{!contact.Name}"/>
<apex:column value="{!contact.MailingCity}"/>
<apex:column value="{!contact.Phone}"/>
</apex:pageBlockTable>
```

In descriptions of syntax, braces ({ }) are typed exactly as shown.

```apex
<apex:page>
Hello {!$User.FirstName}!
</apex:page>
```

{ } In descriptions of syntax, anything included in brackets is optional. In the following example, specifying `value` is optional:

```apex
data_type variable_name [ = value];
```

[ ] In descriptions of syntax, the pipe sign means “or”. You can do one of the following (not all). In the following example, you can create a new unpopulated set in one of two ways, or you can populate the set:

```apex
Set<data_type> set_name
[= new Set<data_type>();] |
```

|

```apex
[= new Set<data_type{value [, value2. . .] };] |
;
```
