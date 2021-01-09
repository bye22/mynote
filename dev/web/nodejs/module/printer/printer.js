var printer=require('printer');
utils = require('util');
console.log("installed printers:\n"+utils.inspect(printer.getPrinters(), {colors:true, depth:10}));
