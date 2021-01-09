# Setting the JDK

```
"java.configuration.runtimes": [
  {
    "name": "JavaSE-1.8",
    "path": "/path/to/jdk-8",
  },
  {
    "name": "JavaSE-11",
    "path": "/path/to/jdk-11",
  },
  {
    "name": "JavaSE-14",
    "path": "/path/to/jdk-14",
    "default": true
  },
]
```
# Available commands
    Java:Update Project configuration (Shift+Alt+U): is available when the editor is focused on a Maven pom.xml or a Gradle file. It forces project configuration / classpath updates (eg. dependency changes or Java compilation level), according to the project build descriptor.
    Java:Open Java language server log file: opens the Java Language Server log file, useful for troubleshooting problems.
    Java:Open Java extension log file: opens the Java extension log file, useful for troubleshooting problems.
    Java:Force Java compilation (Shift+Alt+B): manually triggers compilation of the workspace.
    Java:Open Java formatter settings: Open the Eclipse formatter settings. Creates a new settings file if none exists.
    Java:Clean the Java language server workspace: Clean the Java language server workspace.
    Java:Attach Source: Attach a jar/zip source to the currently opened binary class file. This command is only available in the editor context menu.

# Supported VS Code settings
```


java.home : Absolute path to JDK home folder used to launch the Java Language Server. Requires VS Code restart.

java.jdt.ls.vmargs : Extra VM arguments used to launch the Java Language Server. Requires VS Code restart.

java.errors.incompleteClasspath.severity : 指定当Java文件的类路径不完整时消息的严重性。支持的值包括忽略，信息，警告，错误。

java.trace.server : Traces the communication between VS Code and the Java language server.

java.configuration.updateBuildConfiguration : Specifies how modifications on build files update the Java classpath/configuration. Supported values are disabled (nothing happens), interactive (asks about updating on every modification), automatic (updating is automatically triggered).

java.configuration.maven.userSettings : Path to Maven's settings.xml.

java.configuration.checkProjectSettingsExclusions: Checks if the extension-generated project settings files (.project, .classpath, .factorypath, .settings/) should be excluded from the file explorer. Defaults to true.

java.referencesCodeLens.enabled : Enable/disable the references code lenses.

java.implementationsCodeLens.enabled : Enable/disable the implementations code lenses.

java.signatureHelp.enabled : Enable/disable signature help support (triggered on ().

java.contentProvider.preferred : Preferred content provider (see 3rd party decompilers available in vscode-java-decompiler).

java.import.exclusions : Exclude folders from import via glob patterns. Use ! to negate patterns to allow subfolders imports. You have to include a parent directory. The order is important.

java.import.gradle.enabled : Enable/disable the Gradle importer.

java.import.gradle.home: setting for GRADLE_HOME.

java.import.gradle.arguments: Arguments to pass to Gradle.

java.import.gradle.jvmArguments: JVM arguments to pass to Gradle.

java.import.gradle.wrapper.enabled: Enable/disable the Gradle wrapper.

java.import.gradle.version: Gradle version, used if the gradle wrapper is missing or disabled.

java.import.maven.enabled : Enable/disable the Maven importer.

java.autobuild.enabled : Enable/disable the 'auto build'.

java.maxConcurrentBuilds: Set max simultaneous project builds.

java.completion.enabled : Enable/disable code completion support.

java.completion.overwrite : When set to true, code completion overwrites the current text. When set to false, code is simply added instead.

java.completion.guessMethodArguments : When set to true, method arguments are guessed when a method is selected from as list of code assist proposals.

java.completion.filteredTypes: Defines the type filters. All types whose fully qualified name matches the selected filter strings will be ignored in content assist or quick fix proposals and when organizing imports. For example 'java.awt.*' will hide all types from the awt packages.

java.completion.favoriteStaticMembers : Defines a list of static members or types with static members.

java.completion.importOrder : Defines the sorting order of import statements.

java.progressReports.enabled : [Experimental] Enable/disable progress reports from background processes on the server.

java.format.enabled : Enable/disable the default Java formatter.

java.format.settings.url : Specifies the url or file path to the Eclipse formatter xml settings.

java.format.settings.profile : Optional formatter profile name from the Eclipse formatter settings.

java.format.comments.enabled : Includes the comments during code formatting.

java.format.onType.enabled : Enable/disable on-type formatting (triggered on ;, } or <return>).

java.foldingRange.enabled: Enable/disable smart folding range support. If disabled, it will use the default indentation-based folding range provided by VS Code.

java.maven.downloadSources: Enable/disable eager download of Maven source artifacts.

java.maven.updateSnapshots: Force update of Snapshots/Releases. Defaults to false.

java.codeGeneration.hashCodeEquals.useInstanceof: Use 'instanceof' to compare types when generating the hashCode and equals methods. Defaults to false.

java.codeGeneration.hashCodeEquals.useJava7Objects: Use Objects.hash and Objects.equals when generating the hashCode and equals methods. This setting only applies to Java 7 and higher. Defaults to false.

java.codeGeneration.useBlocks: Use blocks in 'if' statements when generating the methods. Defaults to false.

java.codeGeneration.generateComments: Generate method comments when generating the methods. Defaults to false.

java.codeGeneration.toString.template: The template for generating the toString method. Defaults to ${object.className} [${member.name()}=${member.value}, ${otherMembers}].

java.codeGeneration.toString.codeStyle: The code style for generating the toString method. Defaults to STRING_CONCATENATION.

java.codeGeneration.toString.skipNullValues: Skip null values when generating the toString method. Defaults to false.

java.codeGeneration.toString.listArrayContents: List contents of arrays instead of using native toString(). Defaults to true.

java.codeGeneration.toString.limitElements: Limit number of items in arrays/collections/maps to list, if 0 then list all. Defaults to 0.

java.selectionRange.enabled: Enable/disable Smart Selection support for Java. Disabling this option will not affect the VS Code built-in word-based and bracket-based smart selection.

java.showBuildStatusOnStart.enabled: Automatically show build status on startup. Defaults to false.

java.project.referencedLibraries: Configure glob patterns for referencing local libraries to a Java project.

java.completion.maxResults: Maximum number of completion results (not including snippets). 0 (the default value) disables the limit, all results are returned. In case of performance problems, consider setting a sensible limit..

java.import.gradle.offline.enabled: Enable/disable the Gradle offline mode. Defaults to false.

java.configuration.runtimes: Map Java Execution Environments to local JDKs.

java.import.gradle.user.home: setting for GRADLE_USER_HOME.

java.server.launchMode:

Standard: Provides full features such as intellisense, refactoring, building, Maven/Gradle support etc...
LightWeight: Starts a syntax server with lower start-up cost. Only provides syntax features such as outline, navigation, javadoc, syntax errors. The lightweight mode won't load thirdparty extensions, such as java test runner, java debugger, etc.
Hybrid: Provides full features with better responsiveness. It starts a standard language server and a secondary syntax server. The syntax server provides syntax features until the standard server is ready. And the syntax server will be shutdown automatically after the standard server is fully ready.
Default launch mode is Hybrid. Legacy mode is Standard

java.sources.organizeImports.starThreshold: Specifies the number of imports added before a star-import declaration is used, default is 99.

java.sources.organizeImports.staticStarThreshold: Specifies the number of static imports added before a star-import declaration is used, default is 99.

java.semanticHighlighting.enabled: Enable/disable Semantic Highlighting for Java files. Defaults to false.

java.requirements.JDK11Warning: Enable/disable a warning about the impending requirement of Java 11. Defaults to true.

java.refactor.renameFromFileExplorer: Specifies whether to update imports and package declarations when renaming files from File Explorer. Defaults to prompt.

never: Don't enable refactoring for rename operations on File Explorer.
autoApply: Always automatically update the imports and package declarations.
preview: Always preview the changes before applying.
prompt: Ask user to confirm whether to bypass refactor preview.
java.imports.gradle.wrapper.checksums: Defines allowed/disallowed SHA-256 checksums of Gradle Wrappers.

New in 0.64.0:

java.project.importOnFirstTimeStartup: Specifies whether to import the Java projects, when opening the folder in Hybrid mode for the first time. Supported values are disabled (never imports), interactive (asks to import or not), automatic (always imports). Default to interactive.
java.project.importHint: Enable/disable the server-mode switch information, when Java projects import is skipped on startup. Defaults to true.

```