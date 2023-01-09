# Summary 

This page contains the main steps required to develop an *extension for a browser*. 
Concretely, an extension for Mozilla Firefox

# Steps

1. Create the 'manifest.json'
   2. It contains metadata
   3. The desciption
   4. The icon: 48 x 48 pixels or 96 x 96
   5. The 'content_scripts': indicates the patterns that has to match and the script to run
6. Open the debug page (web page):  about:debugging
   7. Click the Load Temporary Add-on button, then select any file in your extension's directory

# Sources
1. (official) First steps to built a web extension: 
   https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension