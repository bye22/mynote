var printer = require("printer");

console.log('default printer name: ' + (printer.getDefaultPrinterName() || 'is not defined on your computer'));

