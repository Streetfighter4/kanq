import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {AppRoutingModule} from './app-routing.module';
import {FacebookAuthenticatorComponent} from './oauth/facebook/facebook_authenticator.component';

@NgModule({
  imports:      [
    BrowserModule,
    AppRoutingModule
  ],
  declarations: [
    AppComponent,
    FacebookAuthorizerComponent,
    FacebookAuthenticatorComponent
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
