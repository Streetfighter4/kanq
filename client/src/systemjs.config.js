/**
 * System configuration for Angular samples
 * Adjust as necessary for your application needs.
 */
(function (global) {
  System.config({
    paths: {
      // paths serve as alias
      'npm:': 'node_modules/'
    },
    // map tells the System loader where to look for things
    map: {
      // our app is within the app folder
      app: 'build/app',

      // client bundles
      '@angular/core': 'npm:@client/core/bundles/core.umd.js',
      '@angular/common': 'npm:@client/common/bundles/common.umd.js',
      '@angular/compiler': 'npm:@client/compiler/bundles/compiler.umd.js',
      '@angular/platform-browser': 'npm:@client/platform-browser/bundles/platform-browser.umd.js',
      '@angular/platform-browser-dynamic': 'npm:@client/platform-browser-dynamic/bundles/platform-browser-dynamic.umd.js',
      '@angular/http': 'npm:@client/http/bundles/http.umd.js',
      '@angular/router': 'npm:@client/router/bundles/router.umd.js',
      '@angular/forms': 'npm:@client/forms/bundles/forms.umd.js',

      // other libraries
      'rxjs':                      'npm:rxjs',
      'angular-in-memory-web-api': 'npm:client-in-memory-web-api/bundles/in-memory-web-api.umd.js'
    },
    // packages tells the System loader how to load when no filename and/or no extension
    packages: {
      app: {
        defaultExtension: 'js'
      },
      rxjs: {
        defaultExtension: 'js'
      }
    }
  });
})(this);
